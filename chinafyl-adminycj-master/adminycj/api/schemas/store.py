from datetime import datetime, date
from decimal import Decimal

from voluptuous import Schema, Required, All, Length, Optional, Boolean, In, Datetime, Date


add_store_schema = Schema({
    Required('store_name'): str,
    Required('department_id'): int,
    Required('person_id'): int,
    Optional('picture'): str,
    Optional('business_number'): str,
    Optional('is_bigillegal'): Boolean(),
    Optional('business_start'): Date(),
    Optional('business_termi'): Date(),
    Required('longitude'): str,
    Required('latitude'): str,
    Optional('address'): str,
    Optional('state'): In(('NARMAL', 'CLOSE', 'REST', 'ORDERCLOSE')),
    Optional('store_category'): str,
    Optional('is_chain'): Boolean(),
    Optional('is_suspension'): Boolean(),
    Optional('business_format'): In(('SHIZA', 'WULEYE', 'CHAOSHI', 'BIANLI', 'YANJIU', 'SHANGCHANG', 'OTHER')),
    Optional('administrative'): In(('BENJI','WUCHENG', 'JINDONG', 'LANXI', 'PUJIANG', 'YIWU', 'DONGYANG', 'PANAN', 'YONGKANG', 'WUYI')),
    Optional('market_type'): In(('COUNTRYSIDE', 'TOWNSHIP', 'COUNTRYTOWN', 'URBAN')),
    Optional('phone'): str,
    Optional('settlement_account'): str,
    Optional('circle'): In(('ZHENGWU', 'XUEQU', 'JUMINQU', 'SHANGYEQU', 'GONGYEQU', 'LVKEZHONGZHUAN', 'JIMAOSHICHANG', 'WULEQU')),
    Optional('is_downgrade'): Boolean(),
    Optional('car_1'): str,
    Optional('car_2'): str,
    Optional('car_3'): str,
    Optional('car_photo1'): str,
    Optional('car_photo2'): str,
    Optional('car_photo3'): str,
    Optional('operators1'): str,
    Optional('license_ship1'): In(('EMPLOY', 'RELATION', 'SELF', 'OTHER')),
    Optional('operators2'): str,
    Optional('license_ship2'): In(('EMPLOY', 'RELATION', 'SELF', 'OTHER')),
    Optional('operators3'): str,
    Optional('license_ship3'): In(('EMPLOY', 'RELATION', 'SELF', 'OTHER')),
    Optional('special_category'): In(('NORMAL', 'DEMOLITION', 'DISABILITY', 'UNEMPLOY','LOWLIVE', 'ARMY', 'POVERTY', 'OTHER')),
    Optional('special_History'): In(('VIOLENCE', 'PSYCHOSIS', 'IMPORTUNE', 'COMPLAINT','COMPLEX','NOSPECIAL')),
})

storeinfo_by_depart_id_schema = Schema({
    Required('department_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

storeinfo_by_departboss_id_schema = Schema({
    Optional('department_id'):int,
    Optional('station_id'):int,
    Required('page'):int,
    Required('per_page'):int,
    Required('role_id'):int,
})

storeinfo_by_role_id_schema = Schema({
    Optional('department_id'):int,
    Required('page'):int,
    Required('per_page'):int,
    Required('role_id'):int,
    Optional('station_id'):int,
})

storeinfo_by_store_name_schema = Schema({
    Required('store_name'):str,
    Required('page'): int,
    Required('per_page'): int,
    Required('role_id'):int,
    Optional('station_id'):int,
    Optional('department_id'):int,
})

storeinfo_by_store_nameandpersonname_schema = Schema({
    Required('name'):str,
    Required('role_id'):int,
    Optional('station_id'):int,
    Optional('department_id'):int,
})

storeinfo_by_store_multiplequery_schema = Schema({
    Required('name'):str,
    Required('role_id'):int,
    Optional('station_id'):int,
    Optional('department_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

storeinfo_by_storeid_schema = Schema({
    Required('store_id'):int,
})

store_info_schema = Schema({
    Required('store_id'):int,
    Optional('store_name'): str,
    Optional('department_id'): int,
    Optional('person_id'): int,
    Optional('picture'): str,
    Optional('business_number'): str,
    Optional('is_bigillegal'): Boolean(),
    Optional('business_start'): Date(),
    Optional('business_termi'): Date(),
    Optional('longitude'): str,
    Optional('latitude'): str,
    Optional('address'): str,
    Optional('state'): In(('NARMAL', 'CLOSE', 'REST', 'ORDERCLOSE')),
    Optional('store_category'): str,
    Optional('is_chain'): Boolean(),
    Optional('is_suspension'): Boolean(),
    Optional('business_format'): In(('SHIZA', 'WULEYE', 'CHAOSHI', 'BIANLI', 'YANJIU', 'SHANGCHANG', 'OTHER')),
    Optional('administrative'): In(('BENJI', 'WUCHENG', 'JINDONG', 'LANXI', 'PUJIANG', 'YIWU', 'DONGYANG', 'PANAN', 'YONGKANG', 'WUYI')),
    Optional('market_type'): In(('COUNTRYSIDE', 'TOWNSHIP', 'COUNTRYTOWN', 'URBAN')),
    Optional('phone'): str,
    Optional('settlement_account'): str,
    Optional('circle'): In(('ZHENGWU', 'XUEQU', 'JUMINQU', 'SHANGYEQU', 'GONGYEQU', 'LVKEZHONGZHUAN', 'JIMAOSHICHANG', 'WULEQU')),
    Optional('is_downgrade'): Boolean(),
    Optional('car_1'): str,
    Optional('car_2'): str,
    Optional('car_3'): str,
    Optional('car_photo1'): str,
    Optional('car_photo2'): str,
    Optional('car_photo3'): str,
    Optional('operators1'): str,
    Optional('license_ship1'): In(('EMPLOY', 'RELATION', 'SELF', 'OTHER')),
    Optional('operators2'): str,
    Optional('license_ship2'): In(('EMPLOY', 'RELATION', 'SELF', 'OTHER')),
    Optional('operators3'): str,
    Optional('license_ship3'): In(('EMPLOY', 'RELATION', 'SELF', 'OTHER')),
    Optional('special_category'): In(('NORMAL', 'DEMOLITION', 'DISABILITY', 'UNEMPLOY', 'LOWLIVE', 'ARMY', 'POVERTY', 'OTHER')),
    Optional('special_History'): In(('VIOLENCE', 'PSYCHOSIS', 'IMPORTUNE', 'COMPLAINT', 'COMPLEX','NOSPECIAL')),
})

del_store_schema = Schema({
    Required('store_name'):str,
    Required('store_id'):int,
})

add_personinfo_schema = Schema({
    Required('name'):str,
    Required('sex'):str,
    Required('id_card'):str,
    Optional('id_address'):str,
    Optional('birthday'):Date(),
    Optional('nation'):str,
    Optional('census_register'):str,
    Optional('phone'):str,
    Optional('address'):str,
})

personinfo_by_name_schema = Schema({
    Required('name'):str,
    Required('page'): int,
    Required('per_page'): int,
    Optional('department_id'):int,
    Required('role_id'):int,
    Optional('station_id'):int,
})

personinfo_by_name_notid_schema = Schema({
    Required('name'):str,
    Required('page'): int,
    Required('per_page'): int,
})

personinfo_by_id_schema = Schema({
    Required('person_id'):int,
})

person_info_schema = Schema({
    Required('person_id'):int,
    Optional('name'):str,
    Optional('sex'):str,
    Optional('id_card'):str,
    Optional('id_address'):str,
    Optional('birthday'):Date(),
    Optional('nation'):str,
    Optional('census_register'):str,
    Optional('phone'):str,
    Optional('address'):str,
})

del_personinfo_schema = Schema({
    Required('name'):str,
    Required('person_id'):int,
})

personinfo_by_store_id_schema = Schema({
    Required('store_id'):int,
})

storeinfo_by_personid_schema = Schema({
    Required('person_id'):int,
})

personinfo_by_storeandpersoninfo_id_schema = Schema({
    Required('store_id'):int,
})

paginate_test_schema = Schema({
    Required('page'):int,
})

personinfo_by_role_id_schema = Schema({
    Optional('department_id'):int,
    Required('page'):int,
    Required('per_page'):int,
    Required('role_id'):int,
    Optional('station_id'):int,
})