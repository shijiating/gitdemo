#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import os
from flask import Flask, request
from werkzeug.utils import secure_filename  # 获取上传文件的文件名
from flask import Blueprint
import xlrd
from xlrd import xldate_as_tuple
import simplejson
from api.extensions import allowed_file
from api.models.case_Info import ExcelInAndOut,Purchase
from api.models.store_Info import Store,PersonInfo
from api import db
from api.settings import UPLOAD_FOLDER
# from api.views.base import common_response, SysStatus

blue_print = Blueprint('uploadfile', __name__, url_prefix='/api/uploadfile')


# 案件违法信息excel上传
@blue_print.route('/uploadfilecaseinfo', methods=['POST'])
def upload_file_caseinfo():
    """
            @api {post} api/uploadfile/uploadfilecaseinfo  案件违法信息excel上传
            @apiVersion 0.0.1
            @apiName uploadfilecaseinfo
            @apiGroup uploadfile
            @apiDescription 案件违法信息excel上传
            @apiParamExample {json} Request-Example:
            {
                注意 本接口将上传和解析到数据库两个接口写在一起，必须遵从以下规则
                1.文件名必须是全英文或者全数字，不得混用，混用虽然会导入成功，但是系统会改变文件名
                2.必须保证excel导入时sheet表名是 Sheet0
                3.数据必须按照群里发的卷烟案件数据导入模板的样式，数据列不得调整，否则会导致导入失败
                4.本接口只支持导入xls、 xlsx格式导入
            }
            ,encoding_override="utf-8"
    """
    if request.method == 'POST':  # 如果是 POST 请求方式
        file = request.files['file']  # 获取上传的文件
        if file and allowed_file(file.filename):  # 如果文件存在并且符合要求则为 true
            filename = secure_filename(file.filename)  # 获取上传文件的文件名
            file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + filename
            file.save(os.path.join(UPLOAD_FOLDER, file_name))  # 保存文件
            book = xlrd.open_workbook(os.path.join(UPLOAD_FOLDER, file_name))
            sheet = book.sheet_by_name("Sheet0")
            session_list = []

            for r in range(1, sheet.nrows):
                single_brand_id = sheet.cell(r, 0).value
                single_brand_name = sheet.cell(r, 1).value
                code_front = sheet.cell(r, 2).value
                code_behind = sheet.cell(r, 3).value
                count = sheet.cell(r, 4).value
                input_case_id = sheet.cell(r, 5).value
                values = ExcelInAndOut(singlebrand_id=single_brand_id, singlebrand_name=single_brand_name,
                                       code_front=code_front, code_behind=code_behind, count=count,
                                       input_caseid=input_case_id)
                session_list.append(values)
            db.session.add_all(session_list)
            db.session.commit()
            # columns = str(sheet.ncols)
            # rows = str(sheet.nrows)
            # return ('{} upload successed!'.format(filename),"导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")
            # return '{} upload successed!'.format(filename)  # 返回保存成功的信息
            data = {
                "code":0,
                "msg":"上传成功",
                "data":None
            }
            return simplejson.dumps(data)
        else:
            data = {
                "code": 0,
                "msg": "文件名不符合条件，上传失败",
                "data": None
            }
            return simplejson.dumps(data)

# # 导入违法案件信息
# @blue_print.route('/inputcaseinfo', methods=['POST'])
# def input_file_caseinfo():
#     """
#     """
#     if request.method == 'POST':  # 如果是 POST 请求方式
#         file = request.files['file']  # 获取上传的文件
#         if file and allowed_file(file.filename):  # 如果文件存在并且符合要求则为 true
#             filename = secure_filename(file.filename)  # 获取上传文件的文件名
#             file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + filename
#             file.save(os.path.join(UPLOAD_FOLDER, file_name))  # 保存文件
#             book = xlrd.open_workbook(os.path.join(UPLOAD_FOLDER, file_name))
#             sheet = book.sheet_by_name("Sheet1")
#
#             for r in range(1, sheet.nrows):
#                 caseId = sheet.cell(r, 0).value
#                 business_number = sheet.cell(r, 2).value
#                 datetest = sheet.cell(r, 3).value
#                 datetemp = datetime.datetime.strptime(datetest,'%Y-%m-%d %H:%M:%S')
#                 case_date = datetime.datetime.strftime(datetemp, '%Y-%m-%d %H:%M:%S')
#                 case_value = sheet.cell(r, 4).value
#                 count = sheet.cell(r, 5).value
#                 case_nature = sheet.cell(r, 6).value
#                 cigar_property = sheet.cell(r, 7).value
#                 is_criminal = sheet.cell(r, 8).value
#                 smoke_property01 = False
#                 smoke_property02 = False
#                 smoke_property03 = False
#                 if cigar_property == '真烟':
#                     smoke_property01 = True
#                 if cigar_property == '假烟':
#                     smoke_property02 = True
#                 if cigar_property == '走私烟':
#                     smoke_property03 = True
#                 storedata = db.session.query(Store).filter(Store.business_number == business_number).first()
#                 if storedata:
#                     store_id = storedata.id
#                 else:
#                     store_id = None
#                 casedata = Casetest.query.filter(Casetest.caseId == caseId).first()
#                 if casedata:
#                     if smoke_property01 == True:
#                         casedata.smoke_property01 = True
#                         db.session.commit()
#                     if smoke_property02 == True:
#                         casedata.smoke_property02 = True
#                         db.session.commit()
#                     if smoke_property03 == True:
#                         casedata.smoke_property03 = True
#                         db.session.commit()
#                 else:
#                     values = Casetest(caseId=caseId, store_id=store_id,smoke_property01 = smoke_property01,smoke_property02 = smoke_property02,
#                                            case_value=case_value, count=count,smoke_property03 = smoke_property03,case_date = case_date,
#                                            case_nature=case_nature,is_criminal = is_criminal)
#                     db.session.add(values)
#                     db.session.commit()
#             return '{} upload successed!'.format(filename)  # 返回保存成功的信息
#             # columns = str(sheet.ncols)
#             # rows = str(sheet.nrows)
#             # return ('{} upload successed!'.format(filename),"导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")
#             # return '{} upload successed!'.format(filename)  # 返回保存成功的信息

# 导入违法案件信息
@blue_print.route('/inputpurchase', methods=['POST'])
def input_file_inputpurchase():
    """
    """
    if request.method == 'POST':  # 如果是 POST 请求方式
        file = request.files['file']  # 获取上传的文件
        if file and allowed_file(file.filename):  # 如果文件存在并且符合要求则为 true
            filename = secure_filename(file.filename)  # 获取上传文件的文件名
            file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + filename
            file.save(os.path.join(UPLOAD_FOLDER, file_name))  # 保存文件
            book = xlrd.open_workbook(os.path.join(UPLOAD_FOLDER, file_name))
            sheet = book.sheet_by_name("Sheet4")
            session_list = []

            for r in range(1, sheet.nrows):
                store_name = sheet.cell(r, 0).value
                person_name = sheet.cell(r, 1).value
                datetest = sheet.cell(r, 2).value
                # datetemp = datetime.datetime.strptime(datetest,'%Y-%m-%d')
                datetemp = xlrd.xldate_as_datetime(datetest, 0)
                purchase_date = datetime.datetime.strftime(datetemp, '%Y-%m-%d')
                purchase_week = sheet.cell(r, 3).value
                settlement_account = sheet.cell(r, 4).value
                required_count = sheet.cell(r, 5).value
                average_price = sheet.cell(r, 6).value
                storedata = db.session.query(Store).filter(Store.store_name == store_name).first()
                # person_id = storedata.person_id
                if storedata:
                    store_id = storedata.id
                else:
                    store_id = None
                # persondata = db.session.query(PersonInfo).filter(PersonInfo.id == person_id).first()
                # if persondata.name == person_name:
                values = Purchase(store_id=store_id,purchase_date=purchase_date,purchase_week=purchase_week,settlement_account=settlement_account,
                                        required_count=required_count,average_price=average_price)
                session_list.append(values)
            db.session.add_all(session_list)
            db.session.commit()
            return '{} upload successed!'.format(filename)  # 返回保存成功的信息
            # columns = str(sheet.ncols)
            # rows = str(sheet.nrows)
            # return ('{} upload successed!'.format(filename),"导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")
            # return '{} upload successed!'.format(filename)  # 返回保存成功的信息

