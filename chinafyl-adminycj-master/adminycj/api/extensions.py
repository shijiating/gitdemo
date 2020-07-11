import hashlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from api.settings import REDIS_HOST, REDIS_POST, ALLOWED_EXTENSIONS

db = SQLAlchemy()


def validate_picture():
    total = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789'
    # 图片大小130 x 50
    width = 130
    heighth = 50
    # 先生成一个新图片对象
    im = Image.new('RGB', (width, heighth), 'green')
    # 设置字体
    font = ImageFont.truetype('DejaVuSans', 40)
    # 创建draw对象
    draw = ImageDraw.Draw(im)
    str = ''
    # 输出每一个文字
    for item in range(5):
        text = random.choice(total)
        str += text
        draw.text((5 + random.randint(4, 7) + 20 * item, 5 + random.randint(3, 7)), text=text, fill='black', font=font)

    # 划几根干扰线
    for num in range(8):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, heighth / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(heighth / 2, heighth)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    # 模糊下,加个帅帅的滤镜～
    im = im.filter(ImageFilter.FIND_EDGES)
    return im, str


def gen_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()


def allowed_file(filename):  # 验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，两者都满足则返回 true
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def like_filter(keyword, column):
    if keyword:
        return column.like("%{}%".format(keyword))
    else:
        return None


redis_store = StrictRedis(host=REDIS_HOST, port=REDIS_POST, decode_responses=True)
