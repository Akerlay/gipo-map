import redis


class Cache:
    def __init__(self, expire_sec):
        self.red_client = redis.StrictRedis(host='redis', port=6379, db=1)
        self.expire_sec = expire_sec

    def set(self, key: str, value):
        self.red_client.set(key, value, ex=self.expire_sec)

    def get(self, key: str):
        return self.red_client.get(key)
