import csv
import logging
import os
import time
from collections import Counter
from pprint import pprint
from queue import Queue

import jieba
import matplotlib.pyplot as plt
import pymysql
import requests
from bs4 import BeautifulSoup
from gevent import monkey
from gevent.pool import Pool
from wordcloud import WordCloud

monkey.patch_all()

#日志内容处理
def get_logger():
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    logger = logging.getLogger("monitor")
    logger.setLevel(LOG_LEVEL)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

START_URL = (
    "http://search.51job.com/list/010000%252C020000%252C030200%252C040000"
    ",000000,0000,00,9,99,Python,2,{}.html? lang=c&stype=1&postchannel=00"
    "00&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lon"
    "lat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&"
    "address=&line=&specialarea=00&from=&welfare="
)

LOG_LEVEL = logging.INFO    # 日志等级
POOL_MAXSIZE = 8  # 线程池最大容量

logger = get_logger()

#51 job 网站爬虫类
class JobSpider:

    def __init__(self):
        self.count = 1  # 记录当前爬第几条数据
        self.company = []
        self.desc_url_queue = Queue()  # 线程池队列
        self.pool = Pool(POOL_MAXSIZE)  # 协程池管理线程,最大协程数

    #爬虫入口
    def job_spider(self):
        urls = [START_URL.format(p) for p in range(1, 16)]
        for url in urls:
            logger.info("爬取第 {} 页".format(urls.index(url) + 1))
            html = requests.get(url, headers=HEADERS).content.decode("gbk")
            bs = BeautifulSoup(html, "lxml").find("div", class_="dw_table").find_all(
                "div", class_="el"
            )
            for b in bs:
                try:
                    href, post = b.find("a")["href"], b.find("a")["title"]
                    locate = b.find("span", class_="t3").text
                    salary = b.find("span", class_="t4").text
                    item = {
                        "href": href, "post": post, "locate": locate, "salary": salary
                    }
                    self.desc_url_queue.put(href)  # 岗位详情链接加入队列
                    self.company.append(item)
                except Exception:
                    pass
        # 打印队列长度,即多少条岗位详情 url
        logger.info("队列长度为 {} ".format(self.desc_url_queue.qsize()))

    #爬取职位描述
    def post_require(self):
        while True:
            # 从队列中取 url
            url = self.desc_url_queue.get()
            resp = requests.get(url, headers=HEADERS)
            if resp.status_code == 200:
                logger.info("爬取第 {} 条岗位详情".format(self.count))
                html = resp.content.decode("gbk")
                self.desc_url_queue.task_done()
                self.count += 1
            else:
                self.desc_url_queue.put(url)
                continue
            try:
                bs = BeautifulSoup(html, "lxml").find(
                    "div", class_="bmsg job_msg inbox"
                ).text
                s = bs.replace("微信", "").replace("分享", "").replace("邮件", "").replace(
                    "\t", ""
                ).strip()
                with open(
                    os.path.join("data", "post_require_new.txt"), "a", encoding="utf-8"
                ) as f:
                    f.write(s)
            except Exception as e:
                logger.error(e)
                logger.warning(url)

    #职位描述统计
    @staticmethod
    def post_desc_counter():
        post = open(
            os.path.join("data", "post_require.txt"), "r", encoding="utf-8"
        ).read()

        # 使用 jieba 分词
        file_path = os.path.join("data", "user_dict.txt")
        jieba.load_userdict(file_path)
        seg_list = jieba.cut(post, cut_all=False)
        counter = dict()
        for seg in seg_list:
            counter[seg] = counter.get(seg, 1) + 1
        counter_sort = sorted(counter.items(), key=lambda value: value[1], reverse=True)
        pprint(counter_sort)
        with open(
            os.path.join("data", "post_pre_desc_counter.csv"), "w+", encoding="utf-8"
        ) as f:
            f_csv = csv.writer(f)
            f_csv.writerows(counter_sort)

    #职位统计
    def post_counter(self):
        lst = [c.get("post") for c in self.company]
        counter = Counter(lst)
        counter_most = counter.most_common()
        pprint(counter_most)
        with open(
            os.path.join("data", "post_pre_counter.csv"), "w+", encoding="utf-8"
        ) as f:
            f_csv = csv.writer(f)
            f_csv.writerows(counter_most)

    #工资，薪酬，上班地点
    def post_salary_locate(self):
        lst = []
        for c in self.company:
            lst.append((c.get("salary"), c.get("post"), c.get("locate")))
        pprint(lst)
        with open(
            os.path.join("data", "post_salary_locate.csv"), "w+", encoding="utf-8"
        ) as f:
            f_csv = csv.writer(f)
            f_csv.writerows(lst)

    #薪资统一处理
    @staticmethod
    def post_salary():
        mouth = []
        year = []
        thousand = []
        with open(
            os.path.join("data", "post_salary_locate.csv"), "r", encoding="utf-8"
        ) as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                if "万/月" in row[0]:
                    mouth.append((row[0][:-3], row[2], row[1]))
                elif "万/年" in row[0]:
                    year.append((row[0][:-3], row[2], row[1]))
                elif "千/月" in row[0]:
                    thousand.append((row[0][:-3], row[2], row[1]))
        pprint(mouth)

        calc = []
        for m in mouth:
            s = m[0].split("-")
            calc.append(
                (round((float(s[1]) - float(s[0])) * 0.4 + float(s[0]), 1), m[1], m[2])
            )
        for y in year:
            s = y[0].split("-")
            calc.append(
                (
                    round(((float(s[1]) - float(s[0])) * 0.4 + float(s[0])) / 12, 1),
                    y[1],
                    y[2],
                )
            )
        for t in thousand:
            s = t[0].split("-")
            calc.append(
                (
                    round(((float(s[1]) - float(s[0])) * 0.4 + float(s[0])) / 10, 1),
                    t[1],
                    t[2],
                )
            )
        pprint(calc)
        with open(os.path.join("data", "post_salary.csv"), "w+", encoding="utf-8") as f:
            f_csv = csv.writer(f)
            f_csv.writerows(calc)

    #薪资统计
    @staticmethod
    def post_salary_counter():
        with open(os.path.join("data", "post_salary.csv"), "r", encoding="utf-8") as f:
            f_csv = csv.reader(f)
            lst = [row[0] for row in f_csv]
        counter = Counter(lst).most_common()
        pprint(counter)
        with open(
            os.path.join("data", "post_salary_counter1.csv"), "w+", encoding="utf-8"
        ) as f:
            f_csv = csv.writer(f)
            f_csv.writerows(counter)

    #生成词云
    @staticmethod
    def world_cloud():
        counter = {}
        with open(
            os.path.join("data", "post_pre_desc_counter.csv"), "r", encoding="utf-8"
        ) as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                counter[row[0]] = counter.get(row[0], int(row[1]))
            pprint(counter)
        file_path = os.path.join("font", "msyh.ttf")
        wc = WordCloud(
            font_path=file_path, max_words=100, height=600, width=1200
        ).generate_from_frequencies(
            counter
        )
        plt.imshow(wc)
        plt.axis("off")
        plt.show()
        wc.to_file(os.path.join("images", "wc.jpg"))

    #插入数据到数据库
    @staticmethod
    def insert_into_db():
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="0303",
            db="chenx",
            charset="utf8",
        )
        cur = conn.cursor()
        with open(os.path.join("data", "post_salary.csv"), "r", encoding="utf-8") as f:
            f_csv = csv.reader(f)
            sql = "insert into jobpost(j_salary, j_locate, j_post) values(%s, %s, %s)"
            for row in f_csv:
                value = (row[0], row[1], row[2])
                try:
                    cur.execute(sql, value)
                    conn.commit()
                except Exception as e:
                    logger.error(e)
        cur.close()

    '''
    协程池接收请求任务,可以扩展把解析,存储耗时操作加入各自队列,效率最大化
    :param target: 任务函数
    :param count: 启动线程数量
    '''
    def execute_more_tasks(self, target):
        for i in range(POOL_MAXSIZE):
            self.pool.apply_async(target)

    #多线程爬数据
    def run(self):
        self.job_spider()
        self.execute_more_tasks(self.post_require)
        self.desc_url_queue.join()  # 主线程阻塞,等待队列清空


if __name__ == "__main__":
    spider = JobSpider()

    start = time.time()
    spider.run()
    logger.info("总耗时 {} 秒".format(time.time() - start))

    # 按需启动
    # spider.post_salary_locate()
    # spider.post_salary()
    # spider.insert_into_db()
    # spider.post_salary_counter()
    # spider.post_counter()
    # spider.world_cloud()
