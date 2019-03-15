# -*- coding: utf-8 -*-
# 使用celery
from celery import Celery
from django.core.mail import send_mail
from django.conf import settings

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ttsx.settings")
django.setup()

# 创建你一个Celery类 的实例对象
app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/8')
# 定义函数任务
@app.task
def sender_register_active_email(to_email, username, token):
    '''发送激活邮件'''
    subject = 'django_test'
    message = ''
    html_message = '<h1>%s，欢迎您成为我们的注册会员</h1>请点击下面链接激活用户<br/>' \
                   '<a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/' \
                   'user/active/%s</a>' % (username, token, token)
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    send_mail(subject, message, sender, receiver, html_message=html_message)