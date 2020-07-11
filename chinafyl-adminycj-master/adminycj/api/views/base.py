import calendar
import datetime
import functools
from decimal import Decimal

from enum import Enum

from flask import Response, render_template, session, current_app
import simplejson

from api.models.user import Role
from api.settings import origin


class SysStatus(Enum):
    SUCCESS = '成功'
    FAIL = '失败'
    NOT_FOUND = '页面未找到'
    PARAMETER_CHECK_ERROR = '参数校验失败'


class StatusCode(Enum):
    SUCCESS = 2000
    FAIL = 2001
    NOT_FOUND = 4004
    PARAMETER_CHECK_ERROR = 3001


class DatatimeEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Enum):
            return {obj.name: obj.value}
        elif isinstance(obj, Decimal):
            return str(obj.quantize(Decimal('0.00')))
        return simplejson.JSONEncoder.default(self, obj)


def common_response(sys_status, data, message=None):
    if not message:
        message = sys_status.value
    res = simplejson.dumps({'sys_status': sys_status.name, 'data': data, 'message': message}, ensure_ascii=False,
                           use_decimal=False,
                           cls=DatatimeEncoder)
    response = Response(res, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', origin)

    return response


# 将视图函数添加上该装饰器，就能获取到用户对象
def login_user_data(view_func):
    # 防止内层装饰器修改被装饰的函数的名字
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):

        # 获取session里面uers_id
        user = None
        user_id = session.get("user_id")
        if not user_id:
            user_id = 1  # TODO:方便测试，未登陆用户id为1，登陆状态为是True

        # 根据user_id查询用户数据
        try:
            # 延迟导入 解决循环导入问题
            from api.models.user import User
            if user_id:
                user = User.query.get(user_id)
                if not user:
                    return common_response(SysStatus.FAIL, None, '请先登陆')
        except Exception as e:
            current_app.logger.error(e)
        # 3.保存数据后在view_func函数中能够获取到用户数据(*******)
        # g.user = user
        # 在进入实现函数里面由于是处于同一个request请求，里面就能够获取g对象中的临时变量
        result = view_func(user, **kwargs)
        return result

    return wrapper


# 获取本周一的日期
def get_this_monday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    m1 = calendar.MONDAY
    while today.weekday() != m1:
        today -= oneday
    this_monday = today.strftime('%Y-%m-%d')
    # print(this_monday)
    return this_monday


# 权限装饰器
def need_permission(role_name):
    """在需要权限访问的接口加上这个装饰器，如 @need_permission(RoleEnum.STATION_ADMIN)，这样访问的权限就是 已登陆+是局管理人"""

    def decorate(func):
        @functools.wraps(func)
        @login_user_data  # 这里是上面的要求登陆的装饰器
        def wrapper(*args, **kwargs):
            user = kwargs.get('user')
            role_id = user.role_id
            # 查出用户的权限名称
            role = Role.query.filter(Role.id == role_id).first()
            if role.role_name != role_name:
                return common_response(SysStatus.FAIL, data=None, message='没有权限')
            return func(*args, **kwargs)

        return wrapper

    return decorate
