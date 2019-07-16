import redis

class Redis_Server(object):
    def __init__(self, host, port):
        self.redis_uri = 'redis://'