FROM gemingyu/py3flask:latest
ENV PROD=false
WORKDIR /adminycj
COPY ./requirements.txt ./
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install --no-cache-dir -r requirements.txt
CMD ls
CMD pwd
CMD  python manage.py db upgrade; uwsgi uwsgi.ini
