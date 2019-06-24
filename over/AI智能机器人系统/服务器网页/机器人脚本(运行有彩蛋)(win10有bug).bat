rem import  requests
rem import json

rem url = 'http://app360.webservice.mobeye.mob.com/officialWebsite/rank'

rem data = {"ageBin": -99,
        rem "category": "0",
        rem "channelId": 3,
        rem "family": -1,
        rem "gender": -99,
        rem "mobileLevel": -99,
        rem "zone": "cn"}

rem html1 = requests.post(url, json=data)
rem html1.encoding = 'utf-8'
rem response1=html1.json()
rem #print(response)
rem content1=response1['content']
rem '''for sub in  content1:
   rem print(str(sub['icon']))'''


rem url2="http://app360.webservice.mobeye.mob.com/officialWebsite/propertyByApp"

rem for  sub in  content1:
    rem apppkg=sub['app_id']
    rem data2={
    rem "apppkg":apppkg,
    rem "channelId":3,
    rem "family":-1,
    rem "lang":"cn",
    rem "zone":"cn"
    rem }
    

    rem html2=requests.post(url2,json=data2)
    rem response2=html2.json()
    rem #print(response2)
    rem if response2['status']==200:
        rem content2=response2['content']
        rem #print(content1)
        rem appDetail=content2['appDetail']
      
        rem cat_1=sub['app_cat_1']
        rem cat_2=sub['app_cat_2']
        rem APP_Name=sub['appname']
        rem age_list=content2['appProperty']['agebin']
        rem #print(age_list)
        rem value_sum=age_list[0]['value']+age_list[1]['value']+age_list[2]['value']+age_list[3]['value']+age_list[4]['value']

        rem for i  in age_list:
            rem if i['key']=='9':
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'18岁以下用户占比：' + '\t'+str(round(i['value'],4))+'\t2018年11月')
            rem if i['key']=='8':
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'18岁-24岁用户占比：' + '\t'+str(round(i['value'],4))+'\t2018年11月')
            rem if i['key']=='7':
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'25-34岁用户占比：' +  '\t'+str(round(i['value'],4))+'\t2018年11月')
            rem if i['key']=='6' :
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'35-44岁用户占比：' + '\t'+str(round(i['value'],4))+'\t2018年11月')
            rem if i['key']=='5':
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'45岁以上用户占比：' + '\t'+str(round(i['value'],4))+'\t2018年11月')
    
    rem else:
        rem continue

:start
start cmd
goto start
rem import  requests
rem import json

rem url = 'http://app360.webservice.mobeye.mob.com/officialWebsite/rank'

rem data = {"ageBin": -99,
        rem "category": "0",
        rem "channelId": 3,
        rem "family": -1,
        rem "gender": -99,
        rem "mobileLevel": -99,
        rem "zone": "cn"}

rem html1 = requests.post(url, json=data)
rem html1.encoding = 'utf-8'
rem response1=html1.json()
rem #print(response)
rem content1=response1['content']
rem '''for sub in  content1:
   rem print(str(sub['icon']))'''


rem url2="http://app360.webservice.mobeye.mob.com/officialWebsite/propertyByApp"

rem for  sub in  content1:
    rem apppkg=sub['app_id']
    rem data2={
    rem "apppkg":apppkg,
    rem "channelId":3,
    rem "family":-1,
    rem "lang":"cn",
    rem "zone":"cn"
    rem }
    

    rem html2=requests.post(url2,json=data2)
    rem response2=html2.json()
    rem #print(response2)
    rem if response2['status']==200:
        rem content2=response2['content']
        rem #print(content1)
        rem appDetail=content2['appDetail']
      
        rem cat_1=sub['app_cat_1']
        rem cat_2=sub['app_cat_2']
        rem APP_Name=sub['appname']
        rem age_list=content2['appProperty']['agebin']
        rem #print(age_list)
        rem value_sum=age_list[0]['value']+age_list[1]['value']+age_list[2]['value']+age_list[3]['value']+age_list[4]['value']

        rem for i  in age_list:
            rem if i['key']=='9':
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'18岁以下用户占比：' + '\t'+str(round(i['value'],4))+'\t2018年11月')
            rem if i['key']=='8':
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'18岁-24岁用户占比：' + '\t'+str(round(i['value'],4))+'\t2018年11月')
            rem if i['key']=='7':
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'25-34岁用户占比：' +  '\t'+str(round(i['value'],4))+'\t2018年11月')
            rem if i['key']=='6' :
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'35-44岁用户占比：' + '\t'+str(round(i['value'],4))+'\t2018年11月')
            rem if i['key']=='5':
                rem i['value']=i['value']/value_sum
                rem print(str(cat_1)+"\t"+str(cat_2)+'\t'+str(APP_Name)+'\t'+'45岁以上用户占比：' + '\t'+str(round(i['value'],4))+'\t2018年11月')
    
    rem else:
        rem continue
