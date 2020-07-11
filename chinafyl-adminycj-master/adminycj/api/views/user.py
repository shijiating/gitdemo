from flask import Blueprint, request, flash, session, make_response
from sqlalchemy import desc,or_
from io import BytesIO
import base64
from werkzeug.security import generate_password_hash, check_password_hash
from api.extensions import gen_md5, db,validate_picture
from api.models.user import User, RoleEnum,Station,Department
from api.schemas.user import user_login_schema, register_schema, user_info_schema, add_user_schema, \
    del_user_schema,user_info_by_id_schema,departboss_by_roleid_schema,user_by_someroleid_schema,\
    userinfo_by_roleid_searchlike_schema,user_info_by_name_schema,user_info_by_multiple_id_schema,reset_pass_schema
from api.serializer.user import user_info_ser
from api.views.base import common_response, SysStatus, login_user_data, need_permission

blue_print = Blueprint('user', __name__, url_prefix='/api/user')

#生成验证码接口
@blue_print.route('/getcode', methods=['GET'])
def get_code():
    """
             @api {GET} api/user/getcode 生成验证码接口
             @apiVersion 0.0.1
             @apiName getcode
             @apiGroup User
             @apiDescription 生成验证码接口,配合用户登录接口使用，使用get直接可以获取到动态验证码
             @apiSuccessExample {json} Success-Response:
                 {
                    示例:http://39.96.52.170:5000/api/user/getcode
                 }
     """
    image, code = validate_picture()
    # 将验证码图片以二进制形式写入在内存中，防止将图片都放在文件夹中，占用大量磁盘
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = code
    return response

# 用户登录
@blue_print.route('/login', methods=['POST'])
def ycj_login():
    """
        @api {post} api/user/login  用户登录
        @apiVersion 0.0.1
        @apiName login
        @apiGroup User
        @apiDescription 用户登录,添加了验证码
        @apiParam {String}  account      (必须)    账号名(手机号11位)
        @apiParam {String}  password    (必须)    账户密码
        @apiParam {String}  verify_code    (必须)    验证码
        @apiParamExample {json} Request-Example:
            {
                "account": "10010001000",
                "password": "123456"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": {
                    "id": 2,
                    "account": "10010001000",
                    "user_name": "金华市专卖局局长",
                    "department_id": null,
                    "role_id": 2,
                    "station_id": 1
                },
                "message": "成功"
            }

        @apiErrorExample {json} Error-Response:
            {
                "sys_status": "FAIL",
                "data": null,
                "message": "用户名密码不匹配"
            }

    """
    params = user_login_schema(request.json or '')
    account = params.get('account')
    password = params.get('password')
    # verify_code = params.get('verify_code').lower()
    # user = db.session.query(User).filter(User.account == account,User.is_delete == 0).with_entities(
    #     *user_info_ser).first()
    user = db.session.query(User).filter(User.account == account, User.is_delete == 0).first()
    # if verify_code == session['image'].lower():
    if user and user.check_password(password):
        session['user_id'] = user.id  # 设置session，记录用户id（登陆状态保持）
        user = db.session.query(User).filter(User.account == account,User.is_delete == 0).with_entities(
            *user_info_ser).first()
        return common_response(SysStatus.SUCCESS, user, '成功')

    else:
        return common_response(SysStatus.FAIL, None, '用户名密码不匹配')
    # else:
    #     return common_response(SysStatus.FAIL, None, '验证码不正确')



# # 用户登录
# @blue_print.route('/login', methods=['POST'])
# def ycj_login():
#     params = user_login_schema(request.json)
#     account = params.get('account')
#     password = params.get('password')
#     # verify_code = params.get('verify_code')
#     user_data = User.query.filter(User.account == account, User.password == password,User.is_delete == 0).with_entities(
#         *user_info_ser).first()
#     if not user_data:
#         return common_response(SysStatus.FAIL, None, '用户名密码不匹配')
#     else:
#         session['user_id'] = user_data.id  # 设置session，记录用户id（登陆状态保持）
#         return common_response(SysStatus.SUCCESS, user_data, '成功')


# 重置个人密码
@blue_print.route('/reset_password', methods=['POST'])
def reset_pass():
    """
        @api {post} api/user/reset_password  重置用户密码
        @apiVersion 0.0.1
        @apiName reset_pass
        @apiGroup User
        @apiDescription 重置用户密码为123456
        @apiParam {int}  user_id      (必须)    需要重置密码的用户id
        @apiParam {int}  role_id    (必须)    用户角色
        @apiParam {int}  station_id      (可选)    所属专卖局id
        @apiParam {int}  department_id     (可选)   所属稽查所id
        @apiParamExample {json} Request-Example:
        {

                "user_id":4,
                "role_id":1

            }
        @apiSuccessExample {json} Success-Response:
           {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "重置密码成功"
            }
    """
    params = reset_pass_schema(request.json or '')
    user_id = params.get('user_id')
    role_id = params.get('role_id')
    # department_id = params.get('department_id')
    # station_id = params.get('station_id')
    rest_passwrd = "123456"
    if role_id == 1:
        user = User.query.filter(User.id == user_id,User.is_delete == 0).first()
        if user:
            user.password = generate_password_hash(rest_passwrd)
            user.save()
            return common_response(SysStatus.SUCCESS, None, '重置密码成功')
        else:
            return common_response(SysStatus.FAIL, None, '没有查询到这个用户')
    # if role_id == 2:
    #     user = User.query.filter(User.id == user_id, User.station_id == station_id, User.is_delete == 0).first()
    #     if user:
    #         user.password = generate_password_hash(rest_passwrd)
    #         user.save()
    #         return common_response(SysStatus.SUCCESS, None, '重置密码成功')
    #     else:
    #         return common_response(SysStatus.FAIL, None, '没有查询到这个用户')
    # if role_id == 3:
    #     user = User.query.filter(User.id == user_id, User.station_id == station_id, User.department_id == department_id, User.is_delete == 0).first()
    #     if user:
    #         user.password = generate_password_hash(rest_passwrd)
    #         user.save()
    #         return common_response(SysStatus.SUCCESS, None, '重置密码成功')
    #     else:
    #         return common_response(SysStatus.FAIL, None, '没有查询到这个用户')
    else:
        return common_response(SysStatus.FAIL, None, '您无权重置密码')


# 修改个人密码
@blue_print.route('/modify_password', methods=['POST'])
def modify_pass():
    """
        @api {post} api/user/modify_password  用户修改密码
        @apiVersion 0.0.1
        @apiName modify_pass
        @apiGroup User
        @apiDescription 用户修改密码
        @apiParam {int}  user_id      (必须)    用户id
        @apiParam {String}  password_old    (必须)    旧密码
        @apiParam {String}  password    (必须)    新密码
        @apiParamExample {json} Request-Example:
            {
                "user_id":2,
                "password_old": "125689",
                "password":"123456"
            }
        @apiSuccessExample {json} Success-Response:
           {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "修改密码成功"
            }

        @apiErrorExample {json} Error-Response:
           {
                "sys_status": "FAIL",
                "data": null,
                "message": "原密码错误"
            }

    """
    params = register_schema(request.json or '')
    user_id = params.get('user_id')
    password_old = params.get('password_old')
    password = params.get('password')
    user = User.query.filter(User.id == user_id,User.is_delete == 0).first()
    if user.check_password(password_old):
        user.password = generate_password_hash(password)
        user.save()
        return common_response(SysStatus.SUCCESS, None, '修改密码成功')
    else:
        return common_response(SysStatus.FAIL, None, '原密码错误')

#通过用户id获取用户详细信息
@blue_print.route('/getUserInfoByid',methods = ['POST'])
def get_userinfo_by_id():
    """
            @api {POST} api/user/getUserInfoByid 通过用户id获取用户详细信息
            @apiVersion 0.0.1
            @apiName getUserInfoByid
            @apiGroup User
            @apiDescription 通过用户id获取用户详细信息
            @apiParam {int}  user_id     (必须)    用户id
            @apiParam {int}  role_id     (必须)    角色id
            @apiParamExample {json} Request-Example:
                {
                    "user_id":2,
                    "role_id":2
                }
            @apiSuccessExample {json} Success-Response:
                 {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 2,
                            "account": "10010001000",
                            "role_id": 2,
                            "department_id": null,
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）",
                            "user_name": "金华市专卖局局长"
                        }
                    ],
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                {
                    "user_id":3,
                    "role_id":3
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": [
                        {
                            "id": 3,
                            "account": "10010011000",
                            "role_id": 3,
                            "department_id": 1,
                            "depart_name": "专卖城区二所",
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）",
                            "user_name": "专卖城区二所所长"
                        }
                    ],
                    "message": " "
                }
    """
    params = user_info_by_id_schema(request.json or '')
    user_id = params.get('user_id')
    role_id = params.get('role_id')
    if role_id == 1 or role_id == 2:
        data = db.session.query(User).join(Station).filter(User.id == user_id,User.is_delete == 0).with_entities(
            User.id,
            User.account,
            User.role_id,
            User.department_id,
            User.station_id,
            Station.station_name,
            User.user_name
        ).order_by(User.id).all()
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 3 or role_id == 4 or role_id == 5:
        data = db.session.query(Department).join(User,Station).filter(User.id == user_id,User.is_delete == 0).with_entities(
            User.id,
            User.account,
            User.role_id,
            User.department_id,
            Department.depart_name,
            User.station_id,
            Station.station_name,
            User.user_name
        ).order_by(User.id).all()
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')

#批量通过用户id获取用户详细信息
@blue_print.route('/getUserInfoByMultipleid',methods = ['POST'])
def get_userinfo_by_multiple_id():
    """
            @api {POST} api/user/getUserInfoByMultipleid 批量通过用户id获取用户详细信息
            @apiVersion 0.0.1
            @apiName getUserInfoByMultipleid
            @apiGroup User
            @apiDescription 批量通过用户id获取用户详细信息
            @apiParam {str}  user_id     (必须)    用户id,用逗号分割
            @apiParamExample {json} Request-Example:
                {
                    "user_id":"2,3,4"
                }
            @apiSuccessExample {json} Success-Response:
                 {
                    "sys_status": "SUCCESS",
                    "data": [
                        [
                            {
                                "id": 2,
                                "account": "10010001000",
                                "role_id": 2,
                                "department_id": null,
                                "station_id": 1,
                                "station_name": "金华市烟草专卖局（公司）",
                                "user_name": "金华市专卖局局长"
                            }
                        ],
                        [
                            {
                                "id": 3,
                                "account": "10010011000",
                                "role_id": 3,
                                "department_id": 1,
                                "depart_name": "专卖城区二所",
                                "station_id": 1,
                                "station_name": "金华市烟草专卖局（公司）",
                                "user_name": "专卖城区二所所长"
                            }
                        ],
                        [
                            {
                                "id": 4,
                                "account": "10010011001",
                                "role_id": 4,
                                "department_id": 1,
                                "depart_name": "专卖城区二所",
                                "station_id": 1,
                                "station_name": "金华市烟草专卖局（公司）",
                                "user_name": "专卖城区二所稽查员张飞"
                            }
                        ]
                    ],
                    "message": " "
                }
    """
    params = user_info_by_multiple_id_schema(request.json or '')
    user_id = params.get('user_id')
    fenge = user_id.split(',')
    userdata = []
    for i in range(len(fenge)):
        user_id = fenge[i]
        user = User.query.filter(User.id == user_id,User.is_delete == 0).first()
        if user:
            if user.role_id == 1 or user.role_id == 2:
                data = db.session.query(User).join(Station).filter(User.id == user_id,User.is_delete == 0).with_entities(
                    User.id,
                    User.account,
                    User.role_id,
                    User.department_id,
                    User.station_id,
                    Station.station_name,
                    User.user_name
                ).order_by(User.id).all()
                userdata.append(data)
            else:
                data = db.session.query(Department).join(User, Station).filter(User.id == user_id,User.is_delete == 0).with_entities(
                    User.id,
                    User.account,
                    User.role_id,
                    User.department_id,
                    Department.depart_name,
                    User.station_id,
                    Station.station_name,
                    User.user_name
                ).order_by(User.id).all()
                userdata.append(data)
        else:
            userdata.append(None)
    if userdata:
        return common_response(SysStatus.SUCCESS, userdata, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')


# 添加用户账号
@blue_print.route('/addUser', methods=['POST'])
# @login_user_data
# def add_user(user):
def add_user():
    """
        @api {post} api/user/addUser  添加用户账号
        @apiVersion 0.0.1
        @apiName add_user
        @apiGroup User
        @apiDescription 添加用户账号
        @apiParam {String}  account      (必须)    账号名(手机号11位)
        @apiParam {String}  password    (必须)    账户密码
        @apiParam {String}  user_name    (必须)    用户真实姓名
        @apiParam {int}  station_id      (必须)    所属专卖局id
        @apiParam {int}  department_id     (可选)   所属稽查所id
        @apiParam {int}  role_id      (必须)    用户账号等级id
        @apiParamExample {json} Request-Example:
            {  添加局长不需要department_id
                "account":"10010001000",
                "password":"123456",
                "user_name":"金华市专卖局局长",
                "station_id":1,
                "role_id":2
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "用户添加成功"
            }
        @apiParamExample {json} Request-Example:
        { 添加所长或者稽查人员或者队长需要department_id,这里以添加所长为例
                "account":"10010011000",
                "password":"123456",
                "user_name":"专卖城区二所所长",
                "station_id":1,
                "role_id":3,
                "department_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "用户添加成功"
            }
        @apiErrorExample {json} Error-Response:
            {
                "sys_status": "PARAMETER_CHECK_ERROR",
                "data": null,
                "message": "required key not provided @ data['role_id']"
            }

    """
    params = add_user_schema(request.json or '')
    account = params.get('account')
    password = params.get('password')
    user_name = params.get('user_name')
    station_id=params.get('station_id')
    department_id = params.get('department_id')
    role_id = params.get('role_id')
    user = User.query.filter(User.account == account,User.is_delete == 0).first()
    if user:
        return common_response(SysStatus.FAIL, user.account, '该账户已被注册')
    else:
        user = User.query.filter(User.account == account, User.is_delete == 1).first()
        if user:
            if role_id == 2 or role_id == 1:
                user.update(account=account, password=generate_password_hash(password), user_name=user_name,station_id=station_id, department_id=None,
                        role_id=role_id,is_delete = 0)
                db.session.commit()
                return common_response(SysStatus.SUCCESS, None, '用户添加成功')
            else:
                user.update(account=account, password=generate_password_hash(password), user_name=user_name, station_id=station_id,
                            department_id=department_id,is_delete = 0,role_id=role_id)
                db.session.commit()
                return common_response(SysStatus.SUCCESS, None, '用户添加成功')
        else:
            if role_id == 2 or role_id == 1:
                user = User(account=account, password=password, user_name=user_name,station_id=station_id, department_id=None,
                        role_id=role_id)
                db.session.add(user)
                db.session.commit()
                return common_response(SysStatus.SUCCESS, None, '用户添加成功')
            else:
                user = User(account=account, password=password, user_name=user_name, station_id=station_id,
                            department_id=department_id,
                            role_id=role_id)
                db.session.add(user)
                db.session.commit()
                return common_response(SysStatus.SUCCESS, None, '用户添加成功')

# 删除用户账号
@blue_print.route('/delUser', methods=['POST'])
@login_user_data
def delete_user(user):
    """
        @api {post} api/user/delUser  删除用户账号
        @apiVersion 0.0.1
        @apiName delete_user
        @apiGroup User
        @apiDescription 删除用户账号
        @apiParam {String}  account      (必须)    账号名(手机号11位)
        @apiParam {int}  user_id      (必须)    用户id
        @apiParamExample {json} Request-Example:
            {
                "user_id":2,
                "account":"10010001000"
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": true,
                "message": "用户删除成功"
            }
    """
    params = del_user_schema(request.json or '')
    user_id = params.get('user_id')
    account = params.get('account')
    is_delete = 1
    user = User.query.filter(User.id == user_id, User.account == account,User.is_delete == 0).first()
    user.is_delete = is_delete
    user.save()
    return common_response(SysStatus.SUCCESS, user.is_delete, '用户删除成功')


# 修改用户账号信息  这个接口是开放给谁使用，这里没有给出管理局id，如果不限定，局管理的值
#会自动增加
@blue_print.route('/modifyUserInfo', methods=['POST']) #这里使用put和post都可以
# @login_user_data
def user_info_put():
    """
        @api {post} api/user/modifyUserInfo  修改用户信息
        @apiVersion 0.0.1
        @apiName  user_info_put
        @apiGroup User
        @apiDescription 修改用户信息
        @apiParam {int}  user_id      (必须)    用户id
        @apiParam {String}  account      (必须)    账号名(手机号11位)
        @apiParam {String}  user_name    (必须)    用户真实姓名
        @apiParam {String}  password    (必须)    账户密码
        @apiParam {int}  department_id     (可选)   所属稽查所id
        @apiParam {int}  role_id      (必须)    用户账号等级id
        @apiParam {int}  station_id      (必须)    所属专卖局id
        @apiParamExample {json} Request-Example:
            {如果role_id为1或2，不需要传稽查所id
                "user_id":2,
                "account":"10010001000",
                "password":"145362",
                "user_name":"专卖城区二所所长",
                "role_id":2,
                "station_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "用户信息修改成功"
            }
        @apiParamExample {json} Request-Example:
            {如果role_id为3或4或者5，需要传稽查所id
                "user_id":4,
                "account":"10010011001",
                "password":"154286",
                "user_name":"专卖城区二所稽查员张飞",
                "role_id":4,
                "department_id":1
                "station_id":1
            }
        @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": null,
                "message": "用户信息修改成功"
            }

    """
    params = user_info_schema(request.json or '')
    account = params.get('account')
    user_id = params.get('user_id')
    password = params.get('password')
    user_name = params.get('user_name')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    role_id = params.get('role_id')
    user = User.query.filter(User.id == user_id, User.is_delete == 0).first()
    if role_id == 1 or role_id == 2 :
        user.update(account=account, password=generate_password_hash(password), user_name=user_name, station_id=station_id,
                   role_id=role_id)
        db.session.commit()
        return common_response(SysStatus.SUCCESS, None, '用户信息修改成功')
    if role_id == 3 or role_id == 4 or role_id == 5:
        user.update(account=account, password=generate_password_hash(password), user_name=user_name,
                    station_id=station_id,department_id=department_id, role_id=role_id)
        db.session.commit()
        return common_response(SysStatus.SUCCESS, None, '用户信息修改成功')


# 系统管理员查询所有用户
@blue_print.route('/getAllUsers', methods=['GET'])
@need_permission(RoleEnum.ADMIN)
def get_all_users(user):
    role_id = user.role_id
    if role_id == 1:
        data = User.query.filter(User.is_delete == 0).with_entities(User.id,
                                               User.account,
                                               User.password,
                                               User.department_id,
                                               User.station_id,
                                               User.role_id,
                                               User.user_name).order_by(user.id).all()
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无权限查询')


# 局负责人查询所辖局内所有用户
@blue_print.route('/getStationUsers', methods=['GET'])
@need_permission(RoleEnum.STATION_ADMIN)
def get_station_users(user):
    role_id = user.role_id
    station_id = user.station_id
    if role_id == 2:
        data = User.query.filter(User.station_id == station_id,User.is_delete == 0).with_entities(User.id,
                                                                              User.account,
                                                                              User.password,
                                                                              User.department_id,
                                                                              User.role_id,
                                                                              User.user_name).order_by(
            user.id).all()
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无权限查询')


# 稽查所负责人查询所辖所内所有用户
@blue_print.route('/getDepartUsers', methods=['GET'])
@need_permission(RoleEnum.DEPART_ADMIN)
def get_depart_users(user):
    role_id = user.role_id
    department_id = user.department_id
    if role_id == 3:
        data = User.query.filter(User.department_id == department_id,User.is_delete == 0).with_entities(User.id,
                                                                                    User.account,
                                                                                    User.password,
                                                                                    User.role_id,
                                                                                    User.user_name).order_by(
            user.id).all()
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无权限查询')


# 直接通过get查询所有专卖局负责人（专卖局负责人管理）
@blue_print.route('/getAllstationboss', methods=['GET'])
def get_all_station_boss():
    """
            @api {GET} api/user/getAllstationboss 直接通过get查询所有专卖局负责人，使用分页
            @apiVersion 0.0.1
            @apiName getAllstationboss
            @apiGroup User
            @apiDescription 直接通过get查询所有专卖局负责人
            @apiSuccessExample {json} Success-Response:
              {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "id": 2,
                            "role_id": 2,
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）",
                            "account": "10010001000",
                            "user_name": "专卖城区二所所长",
                            "department_id": null
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 1, type=int)
    pagination = db.session.query(Station).join(User).filter(User.role_id == 2,User.is_delete == 0).\
        with_entities(
        User.id,
        User.role_id,
        User.station_id,
        Station.station_name,
        User.account,
        User.user_name,
        User.department_id
    ).order_by(
            Station.id).paginate(page,per_page=per_page,error_out=False)
    userdata = pagination.items
    count = pagination.total
    data = {
        'data': userdata,
        'count': count
    }
    if data:
        return common_response(SysStatus.SUCCESS, data, ' ')
    else:
        return common_response(SysStatus.FAIL, None, '无查询结果')

#做了一点修改
#稽查所负责人管理
@blue_print.route('/getdepartbossByroleid', methods=['POST'])
def get_depart_boss_by_roleid():
    """
            @api {POST} api/user/getdepartbossByroleid 稽查所负责人管理
            @apiVersion 0.0.1
            @apiName getdepartbossByroleid
            @apiGroup User
            @apiDescription 稽查所负责人管理,此处使用了分页功能，page参数指定页数，per_page参数指定每页显示多少内容
            @apiParam {int}  station_id     (必须)    专卖局id
            @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "station_id":1,
                    "role_id":1,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
               {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "id": 3,
                            "role_id": 3,
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）",
                            "depart_name": "专卖城区二所",
                            "account": "10010011000",
                            "user_name": "专卖城区二所所长",
                            "department_id": 1
                        },
                        {
                            "id": 5,
                            "role_id": 5,
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）",
                            "depart_name": "金华市烟草专卖局一大队",
                            "account": "10010021001",
                            "user_name": "金华市烟草专卖局一队队长",
                            "department_id": 32
                        }
                    ],
                    "count": 2
                },
                "message": " "
            }
            @apiParamExample {json} Request-Example:
                {
                    "station_id":1,
                    "role_id":3,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
               {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "id": 3,
                            "role_id": 3,
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）",
                            "depart_name": "专卖城区二所",
                            "account": "10010011000",
                            "user_name": "专卖城区二所所长",
                            "department_id": 1
                        },
                        {
                            "id": 5,
                            "role_id": 5,
                            "station_id": 1,
                            "station_name": "金华市烟草专卖局（公司）",
                            "depart_name": "金华市烟草专卖局一大队",
                            "account": "10010021001",
                            "user_name": "金华市烟草专卖局一队队长",
                            "department_id": 32
                        }
                    ],
                    "count": 2
                },
                "message": " "
            }
    """
    params = departboss_by_roleid_schema(request.json or '')
    role_id = params.get('role_id')
    page = params.get('page')
    per_page = params.get('per_page')
    station_id = params.get('station_id')
    if role_id == 1:
        pagination = db.session.query(Department).join(User,Station).filter(or_(User.role_id == 3,User.role_id == 5), User.is_delete == 0). \
            with_entities(
            User.id,
            User.role_id,
            User.station_id,
            Station.station_name,
            Department.depart_name,
            User.account,
            User.user_name,
            User.department_id
        ).order_by(
            User.id).paginate(page,per_page=per_page,error_out=False)
        userdata = pagination.items
        count = pagination.total
        data = {
            'data':userdata,
            'count':count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2 or role_id == 3 or role_id == 5:
        pagination = db.session.query(Department).join(User,Station).filter(or_(User.role_id == 3,User.role_id == 5),User.station_id == station_id, User.is_delete == 0). \
            with_entities(
            User.id,
            User.role_id,
            User.station_id,
            Station.station_name,
            Department.depart_name,
            User.account,
            User.user_name,
            User.department_id
        ).order_by(
            User.id).paginate(page,per_page=per_page,error_out=False)
        userdata = pagination.items
        count = pagination.total
        data = {
            'data': userdata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')

#做了一些修改
#稽查人员管理--队长只是可以看到本所下的稽查人员
@blue_print.route('/getUserBysomeroleid', methods=['POST'])
def get_User_by_someroleid():
    """
            @api {GET} api/user/getUserBysomeroleid 稽查人员管理
            @apiVersion 0.0.1
            @apiName getUserBysomeroleid
            @apiGroup User
            @apiDescription 稽查人员管理,此处使用了分页功能，page参数指定页数，per_page参数指定每页显示多少内容
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParam {int}  department_id     (可选)    稽查所id
            @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                {
                    "station_id":1,
                    "department_id":1,
                    "role_id":3,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 4,
                                "role_id": 4,
                                "station_id": 1,
                                "station_name": "金华市烟草专卖局（公司）",
                                "depart_name": "专卖城区二所",
                                "account": "10010011001",
                                "user_name": "专卖城区二所稽查员张飞",
                                "department_id": 1
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                {
                    "station_id":1,
                    "department_id":1,
                    "role_id":3,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
               {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 4,
                                "role_id": 4,
                                "station_id": 1,
                                "station_name": "金华市烟草专卖局（公司）",
                                "depart_name": "专卖城区二所",
                                "account": "10010011001",
                                "user_name": "专卖城区二所稽查员张飞",
                                "department_id": 1
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
            @apiParamExample {json} Request-Example:
                {
                    "station_id":1,
                    "department_id":1,
                    "role_id":3,
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 4,
                                "role_id": 4,
                                "station_id": 1,
                                "station_name": "金华市烟草专卖局（公司）",
                                "depart_name": "专卖城区二所",
                                "account": "10010011001",
                                "user_name": "专卖城区二所稽查员张飞",
                                "department_id": 1
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = user_by_someroleid_schema(request.json or '')
    department_id = params.get('department_id')
    role_id = params.get('role_id')
    page = params.get('page')
    per_page = params.get('per_page')
    station_id = params.get('station_id')
    if role_id == 1:
        pagination = db.session.query(Department).join(User,Station).filter(User.role_id == 4, User.is_delete == 0). \
            with_entities(
            User.id,
            User.role_id,
            User.station_id,
            Station.station_name,
            Department.depart_name,
            User.account,
            User.user_name,
            User.department_id
        ).order_by(
            User.id).paginate(page, per_page=per_page, error_out=False)
        userdata = pagination.items
        count = pagination.total
        data = {
            'data': userdata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2:
        pagination = db.session.query(Department).join(User,Station).filter(User.role_id == 4, User.station_id == station_id,
                                                                    User.is_delete == 0). \
            with_entities(
            User.id,
            User.role_id,
            User.station_id,
            Station.station_name,
            Department.depart_name,
            User.account,
            User.user_name,
            User.department_id
        ).order_by(
            User.id).paginate(page, per_page=per_page, error_out=False)
        userdata = pagination.items
        count = pagination.total
        data = {
            'data': userdata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 4 or role_id == 3 or role_id == 5:
        pagination = db.session.query(Department).join(User,Station).filter(User.role_id == 4, User.department_id == department_id,
                                                                    User.is_delete == 0). \
            with_entities(
            User.id,
            User.role_id,
            User.station_id,
            Station.station_name,
            Department.depart_name,
            User.account,
            User.user_name,
            User.department_id
        ).order_by(
            User.id).paginate(page, per_page=per_page, error_out=False)
        userdata = pagination.items
        count = pagination.total
        data = {
            'data': userdata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')


#做了一些修改
#稽查人员模糊查询--吴
@blue_print.route('/getUserinfoByroleidSearchlike', methods=['POST'])
def get_userinfo_by_roleid_searchlike():
    """
            @api {POST} api/user/getUserinfoByroleidSearchlike 稽查人员模糊查询--吴
            @apiVersion 0.0.1
            @apiName getUserinfoByroleidSearchlike
            @apiGroup User
            @apiDescription 稽查人员模糊查询,模糊查询使用分页，角色id为1，可以获取所有符合条件的数据，角色id为2（局长），可以获取本局的数据，角色id为3或者4或者5，可以获取稽查所/队内稽查人员信息数据
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParam {int}  role_id     (必须)    角色id
            @apiParam {int}  department_id     (可选)    稽查所id
            @apiParam {string}  key     (必须)    以姓名或者账号作为搜索条件
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParamExample {json} Request-Example:
                { role_id为1系统管理员，可以查询所有用户
                    "role_id":1,
                    "key":"张",
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
              {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "id": 4,
                            "role_id": 4,
                            "station_id": 1,
                            "depart_name": "专卖城区二所",
                            "account": "10010011001",
                            "user_name": "专卖城区二所稽查员张飞",
                            "department_id": 1
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }
            @apiParamExample {json} Request-Example:
               { role_id为2可以查询本局下所有用户
                    "role_id":2,
                    "station_id":1,
                    "key":"张",
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "id": 4,
                            "role_id": 4,
                            "station_id": 1,
                            "depart_name": "专卖城区二所",
                            "account": "10010011001",
                            "user_name": "专卖城区二所稽查员张飞",
                            "department_id": 1
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }
            @apiParamExample {json} Request-Example:
               { role_id 为3  4  5  可以查询本所或者队下所有用户
                    "role_id":3,
                    "station_id":1,
                    "department_id":1,
                    "key":"张",
                    "page":1,
                    "per_page":8
                }
            @apiSuccessExample {json} Success-Response:
            {
                "sys_status": "SUCCESS",
                "data": {
                    "data": [
                        {
                            "id": 4,
                            "role_id": 4,
                            "station_id": 1,
                            "depart_name": "专卖城区二所",
                            "account": "10010011001",
                            "user_name": "专卖城区二所稽查员张飞",
                            "department_id": 1
                        }
                    ],
                    "count": 1
                },
                "message": " "
            }
    """
    params = userinfo_by_roleid_searchlike_schema(request.json or '')
    role_id = params.get('role_id')
    page = params.get('page')
    per_page = params.get('per_page')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    key = params.get('key')
    if role_id == 1:
        pagination = db.session.query(Department).join(User).filter(User.is_delete == 0,or_(User.user_name.like("%" + key + "%") if key is not None else "",
                                                              User.account.like("%" + key + "%") if key is not None else "")). \
            with_entities(
            User.id,
            User.role_id,
            User.station_id,
            Department.depart_name,
            User.account,
            User.user_name,
            User.department_id
        ).order_by(
            User.id).paginate(page, per_page=per_page, error_out=False)
        userdata = pagination.items
        count = pagination.total
        data = {
            'data': userdata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 2:
        pagination = db.session.query(Department).join(User).filter(User.station_id == station_id, User.is_delete == 0,
                                                                    or_(User.user_name.like("%" + key + "%") if key is not None else "",
                                                              User.account.like("%" + key + "%") if key is not None else "" )). \
            with_entities(
            User.id,
            User.role_id,
            User.station_id,
            Department.depart_name,
            User.account,
            User.user_name,
            User.department_id
        ).order_by(
            User.id).paginate(page, per_page=per_page, error_out=False)
        userdata = pagination.items
        count = pagination.total
        data = {
            'data': userdata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')
    if role_id == 3 or role_id ==4 or role_id == 5:
        pagination = db.session.query(Department).join(User).filter(User.department_id == department_id, User.is_delete == 0,or_(User.user_name.like("%" + key + "%") if key is not None else "",
                                                              User.account.like("%" + key + "%") if key is not None else "")). \
            with_entities(
            User.id,
            User.role_id,
            User.station_id,
            Department.depart_name,
            User.account,
            User.user_name,
            User.department_id
        ).order_by(
            User.id).paginate(page, per_page=per_page, error_out=False)
        userdata = pagination.items
        count = pagination.total
        data = {
            'data': userdata,
            'count': count
        }
        if data:
            return common_response(SysStatus.SUCCESS, data, ' ')
        else:
            return common_response(SysStatus.FAIL, None, '无查询结果')

#做了一些修改
#通过用户姓名获取用户详细信息--分页—--杨--模糊查询
@blue_print.route('/getUserInfoByname',methods = ['POST'])
def get_userinfo_by_name():
    """
            @api {POST} api/user/getUserInfoByname 通过用户姓名获取用户详细信息--分页—--杨--模糊查询
            @apiVersion 0.0.1
            @apiName getUserInfoByname
            @apiGroup User
            @apiDescription 通过用户姓名获取用户详细信息--分页—--杨
            @apiParam {string}  user_name     (必须)    用户名
            @apiParam {int}  page     (必须)    页数
            @apiParam {int}  role_id     (必须)    用户角色id
            @apiParam {int}  query_role_id     (必须)    查询用户用户角色id
            @apiParam {int}  per_page     (必须)    每页的页数
            @apiParam {int}  station_id     (可选)    专卖局id
            @apiParam {int}  department_id     (可选)    稽查所id
            @apiParamExample {json} Request-Example:
                {
                    "user_name":"张",
                    "role_id":2,
                    "query_role_id":4,
                    "page":1,
                    "per_page":8,
                    "station_id":1,
                    "department_id":1
                }
            @apiSuccessExample {json} Success-Response:
                {
                    "sys_status": "SUCCESS",
                    "data": {
                        "data": [
                            {
                                "id": 4,
                                "account": "10010011001",
                                "role_id": 4,
                                "department_id": 1,
                                "depart_name": "专卖城区二所",
                                "station_id": 1,
                                "station_name": "金华市烟草专卖局（公司）",
                                "user_name": "专卖城区二所稽查员张飞"
                            }
                        ],
                        "count": 1
                    },
                    "message": " "
                }
    """
    params = user_info_by_name_schema(request.json or '')
    user_name = params.get('user_name')
    page = params.get('page')
    per_page = params.get('per_page')
    role_id = params.get('role_id')
    query_role_id = params.get('query_role_id')
    station_id = params.get('station_id')
    department_id = params.get('department_id')
    if query_role_id == 3:
        userdata = [User.role_id == 3,User.role_id == 5]
    if role_id == 1:
        if query_role_id == 3:
            pagination = db.session.query(Department).join(User, Station).filter(
                User.user_name.like("%" + user_name + "%") if user_name is not None else "",or_(*userdata), User.is_delete == 0).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                Department.depart_name,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        elif query_role_id == 2 or query_role_id == 1:
            pagination = db.session.query(User).join(Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "", User.role_id == query_role_id, User.is_delete == 0).with_entities(
            User.id,
            User.account,
            User.role_id,
            User.department_id,
            User.station_id,
            Station.station_name,
            User.user_name
            ).order_by(User.id).paginate(page,per_page=per_page,error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            pagination = db.session.query(Department).join(User,Station).filter(
                User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                User.role_id == query_role_id, User.is_delete == 0).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                Department.depart_name,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    elif role_id == 2:
        if query_role_id == 2:
            pagination = db.session.query(User).join(Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                                                                                 User.role_id == query_role_id,
                                                                                 User.is_delete == 0).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        elif query_role_id == 3:
            pagination = db.session.query(Department).join(User, Station).filter(
                User.user_name.like("%" + user_name + "%") if user_name is not None else "",or_(*userdata),
                User.is_delete == 0, User.station_id == station_id).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                Department.depart_name,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            pagination = db.session.query(Department).join(User, Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                                                                                 User.role_id == query_role_id,
                                                                                 User.is_delete == 0,User.station_id == station_id).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                Department.depart_name,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    elif role_id == 3 or role_id == 5:
        if query_role_id == 2:
            pagination = db.session.query(User).join(Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                                                                                     User.role_id == query_role_id,
                                                                                     User.is_delete == 0).with_entities(
                    User.id,
                    User.account,
                    User.role_id,
                    User.department_id,
                    User.station_id,
                    Station.station_name,
                    User.user_name
                ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                    'data': userdata,
                    'count': count
                }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        elif query_role_id == 3:
            pagination = db.session.query(Department).join(User, Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                                                                                 or_(*userdata),
                                                                                 User.is_delete == 0,
                                                                                 User.station_id == station_id).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                Department.depart_name,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        elif query_role_id == 4:
            pagination = db.session.query(Department).join(User, Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                                                                                 User.role_id == query_role_id,
                                                                                 User.is_delete == 0,
                                                                                 User.station_id == station_id,User.department_id == department_id).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                Department.depart_name,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
    elif role_id == 4:
        if query_role_id == 2:
            pagination = db.session.query(User).join(Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                                                                                 User.role_id == query_role_id,
                                                                                 User.is_delete == 0).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        elif query_role_id == 3:
            pagination = db.session.query(Department).join(User, Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                                                                                 or_(*userdata),
                                                                                 User.is_delete == 0,
                                                                                 User.station_id == station_id).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                Department.depart_name,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')
        else:
            pagination = db.session.query(Department).join(User, Station).filter(User.user_name.like("%" + user_name + "%") if user_name is not None else "",
                                                                                 User.role_id == query_role_id,
                                                                                 User.is_delete == 0,
                                                                                 User.station_id == station_id,User.department_id == department_id).with_entities(
                User.id,
                User.account,
                User.role_id,
                User.department_id,
                Department.depart_name,
                User.station_id,
                Station.station_name,
                User.user_name
            ).order_by(User.id).paginate(page, per_page=per_page, error_out=False)
            userdata = pagination.items
            count = pagination.total
            data = {
                'data': userdata,
                'count': count
            }
            if data:
                return common_response(SysStatus.SUCCESS, data, ' ')
            else:
                return common_response(SysStatus.FAIL, None, '无查询结果')

