# 拒绝隐式引入，如果celery.py和celery模块名字一样，避免冲突，需要加上这条语句
# 该代码中，名字是不一样的，最好也要不一样
from __future__ import absolute_import
from celery import Celery
app = Celery('tasks')
app.config_from_object('celery_periodic.celeryconfig')
