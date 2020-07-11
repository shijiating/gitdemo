#!/usr/bin/evn python
# coding=utf-8
from datetime import timedelta
from celery.schedules import crontab, schedule

# Broker and Backend
BROKER_URL = "redis://localhost:6379/2"  # 指定 Broker
# CELERY_RESULT_BACKEND = "redis://localhost:6379/3"  # 指定 Backend
# Timezone
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，不指定默认为 'UTC'
# CELERY_TIMEZONE='UTC'
# import
CELERY_IMPORTS = (
    'celery_periodic.tasks.bpdata_insert',
    'celery_periodic.tasks.bp_forecast',
    'celery_periodic.tasks.rule_forecast',
    'celery_periodic.tasks.svmdata_insert',
    'celery_periodic.tasks.svm_forecast'
)
# schedules
CELERYBEAT_SCHEDULE = {
    'bp-add-every-7-days': {
        'task': 'celery_periodic.tasks.bpdata_insert.store_query',
        'schedule': schedule.every().monday.at("01:00"),  # BP数据插入每周一凌晨一点
        'args': ()
    },
    'svm-add-every-7-days': {
        'task': 'celery_periodic.tasks.svmdata_insert.store_query',
        'schedule': schedule.every().monday.at("01:20"),  # SVM数据插入每周一凌晨一点二十
        'args': ()
    },
    'bp-fore-every-7-days': {
        'task': 'celery_periodic.tasks.bp_forecast.bp_fore',
        'schedule': schedule.every().monday.at("01:40"),  # BP预测
        'args': ()
    },
    'svm-fore-every-7-days': {
        'task': 'celery_periodic.tasks.svm_insert.svm_fore',
        'schedule': schedule.every().monday.at("01:50"),  # SVM预测
        'args': ()
    },
    'rule-fore-every-7-days': {
        'task': 'celery_periodic.tasks.rule_forecast.rule_fore',
        'schedule': schedule.every().monday.at("02:00"),  # 规则预测
        'args': ()
    }
}
