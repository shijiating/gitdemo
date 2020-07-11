from voluptuous import Schema, Required, All, Length, Optional

user_login_schema = Schema({
    Required('account'): All(str, Length(max=11)),
    Required('password'): str,
    Optional('verify_code'): str,
})

register_schema = Schema({
    Required('user_id'): int,
    Required('password_old'): str,
    Required('password'): str,
})

reset_pass_schema = Schema({
    Required('user_id'): int,
    Required('role_id'): int,
    Optional('department_id'): int,
    Optional('station_id'): int,
})

user_info_schema = Schema({
    Required('user_id'): int,
    Required('account'): All(str, Length(max=11)),
    Required('user_name'): str,
    Required('password'): str,
    Optional('department_id'): int,
    Required('role_id'): int,
    Required('station_id'): int,
})

user_info_by_id_schema = Schema({
    Required('user_id'):int,
    Required('role_id'): int,
})

user_info_by_multiple_id_schema = Schema({
    Required('user_id'):str,
})

user_info_by_name_schema = Schema({
    Required('user_name'):str,
    Required('page'): int,
    Required('per_page'): int,
    Required('role_id'): int,
    Required('query_role_id'): int,
    Optional('station_id'): int,
    Optional('department_id'): int,
})

add_user_schema = Schema({
    Required('account'): All(str, Length(max=11)),
    Required('password'): str,
    Required('user_name'): str,
    Required('station_id'): int,
    Optional('department_id'): int,
    Required('role_id'): int,
})

del_user_schema = Schema({
    Required('user_id'): int,
    Required('account'): All(str, Length(max=11)),
})

departboss_by_roleid_schema = Schema({
    Required('station_id'): int,
    Required('role_id'): int,
    Required('page'): int,
    Required('per_page'): int,
})

user_by_someroleid_schema = Schema({
    Optional('station_id'): int,
    Optional('department_id'): int,
    Required('role_id'): int,
    Required('page'): int,
    Required('per_page'): int,
})

userinfo_by_roleid_searchlike_schema = Schema({
    Optional('station_id'): int,
    Required('role_id'): int,
    Required('page'): int,
    Required('per_page'): int,
    Optional('department_id'): int,
    Required('key'): str,
})