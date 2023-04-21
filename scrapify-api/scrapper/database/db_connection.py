import redis as redis_modules

redis_client = redis_modules.Redis(host="cache", port=6379, db=0)
