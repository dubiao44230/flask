from redis import Redis


class FlaskSet(object):
    DEBUG = True
    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis(db=5)
