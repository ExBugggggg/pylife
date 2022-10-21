from django_redis import get_redis_connection

class RedisConnection:

    __connection = None

    def connect(self):
        self.__connection = get_redis_connection('default')
        return self.__connection

