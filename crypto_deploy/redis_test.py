import redis as _redis
import time


def wtf():

    r = _redis.StrictRedis(host='0.0.0.0', port=6379, db=0)
    ts = int(round(time.time() * 1000))
    r.set('nonce', str(ts))

wtf()