from voluptuous import Schema, Required, All, Optional, Length,Boolean

add_station_schema = Schema({
    Required('station_name'): str,

})

del_station_schema = Schema({
    Required('station_name'): str,
    Required('station_id'): int,

})

station_info_schema = Schema({
    Required('station_id'): int,
    Optional('station_name'): str,

})

get_AllUser_byStationid_schema = Schema({
    Required('station_id'): int,
    Required('page'): int,
    Required('per_page'): int,
    Required('role_id'): int,
})

get_AllDepart_byStation_schema = Schema({
    Required('station_id'): int,
    Required('page'): int,
    Required('per_page'): int,
})

get_AllInfo_byRole_schema = Schema({
    Required('role_id'): int,
    Optional('station_id'): int,
    Optional('department_id'): int,
    Required('page'): int,
    Required('per_page'):int,
})

add_department_schema = Schema({
    Required('depart_name'): str,
    Required('station_id'): int,
    # Optional('is_captain'): Boolean(),

})

del_department_schema = Schema({
    Required('depart_name'): str,
    Required('department_id'): int,

})

department_info_schema = Schema({
    Required('department_id'): int,
    Optional('depart_name'): str,
    Optional('station_id'): int,

})

departname_info_by_departid_schema = Schema({
    Required('department_id'): int,

})

station_info_by_station_name_schema = Schema({
    Required('station_name'):str,
    Required('page'): int,
    Required('per_page'): int,
})