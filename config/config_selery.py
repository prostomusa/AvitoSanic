REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'
#CELERY_BROKER_URL = 'redis://redis:6379'  # Docker
#CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
#CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
#CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
SELERY_RESULT_SERIALIZER = 'json'