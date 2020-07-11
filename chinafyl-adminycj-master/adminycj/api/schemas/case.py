from voluptuous import Schema, Required, Optional, Date, Boolean,All,Length

# 本表是关于违法部分接口
# 违法案件表部分
add_caseinfo_schema = Schema({
    Required('caseId'): str,
    Required('store_id'): int,
    Optional('case_date'): Date(),
    Optional('case_value'): str,
    Optional('count'): str,
    Optional('case_nature'): str,
    Optional('is_criminal'): Boolean(),
    Optional('smoke_property01'): Boolean(),
    Optional('smoke_property02'): Boolean(),
    Optional('smoke_property03'): Boolean(),
})

# storeinfo_by_depart_id_schema = Schema({
#     Required('department_id'):int,
# })
#
# auditinfo_by_store_name_schema = Schema({
#     Required('store_name'):str,
# })
#
caseinfo_by_id_schema = Schema({
    Required('case_id'): int,
})
#
case_info_schema = Schema({
    Required('case_id'): int,
    Required('caseId'): str,
    Required('store_id'): int,
    Optional('case_date'): Date(),
    Optional('case_value'): str,
    Optional('count'): str,
    Optional('case_nature'): str,
    Optional('is_criminal'): Boolean(),
    Optional('smoke_property01'): Boolean(),
    Optional('smoke_property02'): Boolean(),
    Optional('smoke_property03'): Boolean(),
})

del_case_schema = Schema({
    Required('case_id'): int,
})

caseinfo_by_store_id_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

caseinfo_by_select_schema = Schema({
    Optional('caseId'): str,
    Optional('case_date'): Date(),
    # Optional('case_value'): str,
    # Optional('count'): str,
    Optional('case_nature'): str,
    Optional('is_criminal'): Boolean(),
    Optional('smoke_property01'): Boolean(),
    Optional('smoke_property02'): Boolean(),
    Optional('smoke_property03'): Boolean(),
    Optional('page'):int,
})

caseinfo_by_store_name_schema = Schema({
    Required('store_name'):str,
    Required('page'):int,
    Required('per_page'):int,
    Required('role_id'):int,
    Optional('station_id'):int,
    Optional('department_id'):int,
})

# caseinfo_by_storenameandselect_schema = Schema({
#     Required('store_name'):str,
#     Required('page'):int,
#     Required('per_page'):int,
#     Optional('low_case_value'):str,
#     Optional('high_case_value'):str,
#     Optional('low_case_data'):Date(),
#     Optional('high_case_data'):Date(),
# })

caseinfo_by_storenameandselect_schema = Schema({
    Optional('store_name'):str,
    Required('page'):int,
    Required('per_page'):int,
    Optional('low_case_value'):str,
    Optional('high_case_value'):str,
    Optional('low_case_data'):Date(),
    Optional('high_case_data'):Date(),
    Optional('case_nature'):str,
    Required('role_id'):int,
    Optional('station_id'):int,
    Optional('department_id'):int,
})

get_purchaseinfo_by_timeandstore_id_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
    Required('start_date'): Date(),
    Required('end_date'): Date()
})

caseinfo_by_role_id_schema = Schema({
    Optional('department_id'):int,
    Required('page'):int,
    Required('per_page'):int,
    Required('role_id'):int,
    Optional('station_id'):int,
})

#进货记录表相关接口
purchaseinfo_by_id_schema = Schema({
    Required('purchase_id'):int,
})

purchaseinfo_by_store_id_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

#案件涉烟详情表接口
casecigarinfo_by_id_schema = Schema({
    Required('casecigar_id'):int,
})

casecigarinfo_by_store_id_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

casecigarinfo_by_timeandstore_id_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
    Required('start_date'): Date(),
    Required('end_date'): Date()
})

casecigarinfo_by_case_id_schema = Schema({
    Required('case_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

inter_casecigarinfo_schema = Schema({
    Required('role_id'):int,
    Optional('date_start'):Date(),
    Optional('date_end'):Date(),
    Optional('department_id'):int,
    Optional('station_id'):int,
    # Required('page'):int,
    # Required('per_page'):int,
})

inter_casecigarinfo_by_departid_schema = Schema({
    Optional('date_start'):Date(),
    Optional('date_end'):Date(),
    Required('department_id'):int,
})

#进货明细表相关接口
brandinfo_by_id_schema = Schema({
    Required('brand_id'):int,
})

brandinfo_by_purchase_id_schema = Schema({
    Required('purchase_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

brandinfo_by_store_id_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

#excel导入导出表相关schemas
excel_inandout_info_by_caseid_schema = Schema({
    Required('input_caseid'):str,

})

excel_inandout_info_by_caseid_page_schema = Schema({
    Required('input_caseid'):str,
    Required('page'):int,
    Required('per_page'):int,
})

scan_code_upload_info_schema = Schema({
    Required('input_caseid'):str,
    Required('singlebrand_name'):str,
    Required('code_front'):All(str, Length(max=16)),
    Required('code_behind'):All(str, Length(max=16)),
    Required('user_id'):int,
})

del_inandout_caseid_schema = Schema({
    Required('input_caseid'):str,

})

get_all_singlename_by_caseid_schema = Schema({
    Required('input_caseid'):str,

})

get_uncomplish_singlename_by_caseid_schema = Schema({
    Required('input_caseid'):str,

})

get_complish_singlename_by_caseid_schema = Schema({
    Required('input_caseid'):str,

})

get_all_singlenamecount_by_caseid_schema = Schema({
    Required('input_caseid'):str,
    Required('singlebrand_name'):str,
})

get_uncomplish_singlenamecount_by_caseid_schema = Schema({
    Required('input_caseid'):str,
    Required('singlebrand_name'):str,
})

get_complish_singlenamecount_by_caseid_schema = Schema({
    Required('input_caseid'):str,
    Required('singlebrand_name'):str,
})