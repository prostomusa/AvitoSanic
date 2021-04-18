from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
import config
# set the default Django settings module for the 'celery' program.
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Avito.settings')

my_celery = Celery('AvitoSanic')

my_celery.config_from_object('config.config_selery', namespace='CELERY')
my_celery.autodiscover_tasks()
my_celery.conf.beat_schedule = {
	'T1': {
		'task': 'tasks.counter',
		'schedule': crontab(minute=0, hour='*/1'),
	},
}