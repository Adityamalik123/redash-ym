# Configuration file


class Config():
    def __init__(self):
        pass

    ML_SSO_URL = 'http://node-2:3000'
    ML_MONGO_URL = 'mongodb://mongodb-0:27017,mongodb-1:27017,mongodb-2:27017/?replicaSet=rs0'
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    ADMIN_URL = 'http://node-0:3001'
    ML_URL = 'http://localhost:8000'
    ELASTICSEARCH_URLS=["es-node-0:9200","es-node-1:9200","es-node-2:9200"]
    NEWRELIC_INI = '/home/yellow/.newrelic.ini'
    BOTS_URL='http://node-1:3000'
    REDIS={"host":"10.4.0.50","port":6379}

class DevelopmentConfig(Config):
    def __init__(self):
        Config.__init__(self)

    ML_SSO_URL = 'http://104.211.93.103:3000'
    ML_MONGO_URL = 'mongodb://104.211.93.103:27017'
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    ADMIN_URL = 'http://104.211.93.103:3001'
    ML_URL = 'http://localhost:8000'
    ELASTICSEARCH_URLS=["104.211.93.103:9200"]
    NEWRELIC_INI = '/home/yellow/.newrelic.ini'
    BOTS_URL='http://104.211.93.103/bots/'
    REDIS={"host":"104.211.93.103","port":6379}

class ProductionConfig(Config):
    def __init__(self):
        Config.__init__(self)

    ML_SSO_URL = 'http://sso:3000'
    ML_MONGO_URL = 'mongodb://mongodb-0:27017,mongodb-1:27017,mongodb-2:27017/?replicaSet=rs0'
    CELERY_BROKER_URL = 'amqp://rabbitmq.rabbitmq'
    CELERY_RESULT_BACKEND = 'amqp://rabbitmq.rabbitmq'
    ADMIN_URL = 'http://admin:3000'
    ML_URL = 'http://ml-3:8000'
    NEWRELIC_INI = '/home/yellow/.newrelic.ini'
    ELASTICSEARCH_URLS=["es-node-0:9200","es-node-1:9200","es-node-2:9200"]
    BOTS_URL='http://docker-0:7000'
    REDIS={"host":"10.4.3.10","port":6379,"password":"CyJAKC69ldUtwW95xbw3Idj4kPSeJSym+GHYD+0GvFw="}
    REDIS_CLUSTER=[{"host": "10.4.0.43", "port": "6379"},{"host": "10.4.0.47", "port": "6379"},{"host": "10.4.0.58", "port": "6379"}]
    REDIS_CLUSTER_PASSWORD="GoZifCCeMROKDqT8pH1GXwOf3jHmOBzAoErdzo1YsYQ="
