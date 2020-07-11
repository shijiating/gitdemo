#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from flask import Blueprint
from pandas._libs import json

from api.views.base import SysStatus, common_response

blue_print = Blueprint('data', __name__, url_prefix='/api/pages')


# json数据读取
@blue_print.route('/data', methods=['GET'])
def data_read():
    json_dic = {
        # "success": true,
        "data": {
            "LineA": {
                "categories": ["11月第一周", "第二周", "第三周", "第四周", "12月第一周", "第二周"],
                "series": [{
                    "name": "金华",
                    "data": [35, 8, 25, 37, 4, 20]
                }, {
                    "name": "义乌",
                    "data": [70, 40, 65, 100, 44, 68]
                }, {
                    "name": "兰溪",
                    "data": [100, 80, 95, 150, 112, 132]
                }]
            },
            "Area": {
                "categories": ["11月第一周", "第二周", "第三周", "第四周", "12月第一周", "第二周"],
                "series": [{
                    "name": "无证运输",
                    "data": [100, 80, 95, 150, 112, 132],
                    "color": "#facc14"
                }, {
                    "name": "外流卷烟",
                    "data": [70, 40, 65, 100, 44, 68],
                    "color": "#2fc25b"
                }, {
                    "name": "销售非法生产卷烟",
                    "data": [35, 20, 25, 37, 4, 20],
                    "color": "#1890ff"
                }]
            },
            "Radar": {
                "categories": ["本级", "义乌", "兰溪", "浦江", "武义", "永康"],
                "series": [{
                    "name": "无证运输",
                    "data": [90, 110, 165, 195, 187, 172]
                }, {
                    "name": "外流卷烟",
                    "data": [190, 210, 105, 35, 27, 102]
                }]
            },
            "LineB": {
                "categories": ["2012", "2013", "2014", "2015", "2016", "2017"],
                "series": [{
                    "name": "金华",
                    "data": [35, 8, 25, 37, 4, 20]
                }, {
                    "name": "义乌",
                    "data": [70, 40, 65, 100, 44, 68]
                }, {
                    "name": "兰溪",
                    "data": [100, 80, 95, 150, 112, 132]
                }]
            }
        }
    }
    #json_form = json.dumps(json_dic)
    return common_response(SysStatus.SUCCESS, json_dic, '成功')