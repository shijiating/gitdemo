from voluptuous import Schema, Required, Optional, Boolean, Date, In

#本表是关于任务表部分接口
#audit表部分
add_audit_schema = Schema({
    Required('store_id'): int,
    Required('inspector_id'): int,
    Required('audit_date'): Date(),
    Optional('audit_pic1'): str,
    Optional('audit_pic2'): str,
    Optional('audit_pic3'): str,
    Optional('audit_pic4'): str,
    Optional('audit_pic5'): str,
    Optional('audit_pic6'): str,
    Optional('audit_result'): Boolean(),
    Optional('audit_note'): str,
    Optional('is_opensale'): Boolean(),
    Optional('measures'): In(('ORAL', 'ORDER', 'COMMON', 'CORRECTION')),
    Optional('is_holdcertificate'): Boolean(),
    Optional('is_opencertificate'): Boolean(),
    Optional('is_saleticket'): Boolean(),
    Optional('is_saleskyprice'): Boolean(),
    Optional('is_potentially_illegal'): Boolean(),
    Optional('score'): str,
})

# storeinfo_by_depart_id_schema = Schema({
#     Required('department_id'):int,
# })
#
# auditinfo_by_store_name_schema = Schema({
#     Required('store_name'):str,
# })
#
auditinfo_by_id_schema = Schema({
    Required('audit_id'):int,
})
#
audit_info_schema = Schema({
    Required('audit_id'):int,
    Optional('store_id'): int,
    Optional('inspector_id'): int,
    # Optional('task_id'): int, 这个应该是不可以修改的
    Optional('audit_date'): Date(),
    Optional('audit_pic1'): str,
    Optional('audit_pic2'): str,
    Optional('audit_pic3'): str,
    Optional('audit_pic4'): str,
    Optional('audit_pic5'): str,
    Optional('audit_pic6'): str,
    Optional('audit_result'): Boolean(),
    Optional('audit_note'): str,
    Optional('is_opensale'): Boolean(),
    Optional('measures'): In(('ORAL', 'ORDER', 'COMMON', 'CORRECTION')),
    Optional('is_holdcertificate'): Boolean(),
    Optional('is_opencertificate'): Boolean(),
    Optional('is_saleticket'): Boolean(),
    Optional('is_saleskyprice'): Boolean(),
    Optional('is_potentially_illegal'): Boolean(),
    Optional('score'): str,
})

del_audit_schema = Schema({
    Required('audit_id'):int,
})

auditinfo_by_store_id_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

auditinfo_by_store_id_with_hidepicture_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})

auditinfo_by_task_id_schema = Schema({
    Required('task_id'):int,
})


#藏匿图表部分
add_hidepicture_schema = Schema({
    Required('store_id'): int,
    Required('audit_id'): int,
    Required('picture'): str,
    Required('graffiti'): str,
    Optional('note'): str,
})

hidepicureinfo_by_auditid_schema = Schema({
    Required('audit_id'):int,
})

hidepicureinfo_by_storeid_schema = Schema({
    Required('store_id'):int,
    Required('page'):int,
    Required('per_page'):int,
})
#
hidepicure_info_schema = Schema({
    Required('hidepicture_id'):int,
    Optional('store_id'): int,
    Optional('audit_id'): int,
    Optional('picture'): str,
    Optional('graffiti'): str,
    Optional('note'): str,
})
#
del_hidepicure_schema = Schema({
    Required('hidepicture_id'):int,
})

# #任务表部分
# taskinfo_by_id_schema = Schema({
#     Required('task_id'):int,
# })
#
# com_taskinfo_by_role_id_schema = Schema({
#     Required('role_id'):int,
#     Optional('station_id'):int,
#     Optional('department_id'):int,
#     Required('page'):int,
#     Required('per_page'):int,
# })
#
# uncom_taskinfo_by_role_id_schema = Schema({
#     Required('role_id'):int,
#     Optional('station_id'):int,
#     Optional('department_id'):int,
#     Required('page'):int,
#     Required('per_page'):int,
# })
#
# uncomtaskinfo_by_user_id_schema = Schema({
#     Required('user_id'):int,
#     Required('role_id'):int,
#     Optional('station_id'):int,
#     Optional('department_id'):int,
#     Required('page'):int,
#     Required('per_page'):int,
# })
#
# comtaskinfo_by_user_id_schema = Schema({
#     Required('user_id'):int,
#     Required('role_id'):int,
#     Optional('station_id'):int,
#     Optional('department_id'):int,
#     Required('page'):int,
#     Required('per_page'):int,
# })
#
# add_single_task_schema = Schema({
#     Required('role_id'): int,
#     Required('user_id'): int,
#     Required('store_id'): int,
#     Required('inspector1_id'): int,
#     Optional('inspector2_id'): int,
#     Optional('inspector3_id'): int,
#     Optional('inspector4_id'): int,
#     Optional('inspector5_id'): int,
#     Optional('end_date'): Date(),
#     Optional('status'): Boolean(),
# })
#
# add_multiple_task_schema = Schema({
#     Required('role_id'): int,
#     Required('user_id'): int,
#     Required('store_id'): str,
#     Required('inspector1_id'): int,
#     Optional('inspector2_id'): int,
#     Optional('inspector3_id'): int,
#     Optional('inspector4_id'): int,
#     Optional('inspector5_id'): int,
#     Optional('end_date'): Date(),
#     Optional('status'): Boolean(),
# })
#
# task_evaluate_schema = Schema({
#     Required('task_id'): int,
#     Required('task_score'): str,
#     Optional('remark'): str,
#     Required('role_id'): int,
# })

# #预测表部分
# add_forecast_schema = Schema({
#     Optional('store_id'): int,
#     Optional('forecast_date'): Date(),
#     Optional('mode'): In(('SVM','BP','LM','RBF')),
#     Optional('result'): str,
# })
#
# # storeinfo_by_depart_id_schema = Schema({
# #     Required('department_id'):int,
# # })
# #
# # auditinfo_by_store_name_schema = Schema({
# #     Required('store_name'):str,
# # })
# #
# forecastinfo_by_id_schema = Schema({
#     Required('forecast_id'):int,
# })
#
# forecastinfo_by_storeid_schema = Schema({
#     Required('store_id'):int,
# })
# #
# forecast_info_schema = Schema({
#     Required('forecast_id'):int,
#     Optional('store_id'): int,
#     Optional('forecast_date'): Date(),
#     Optional('mode'): In(('SVM', 'BP', 'LM', 'RBF')),
#     Optional('result'): str,
# })
# #
# del_forecast_schema = Schema({
#     Required('forecast_id'):int,
# })
# #
# # add_personinfo_schema = Schema({
# #     Optional('name'):str,
# #     Optional('sex'):str,
# #     Optional('id_card'):str,
# #     Optional('id_address'):str,
# #     Optional('birthday'):Date(),
# #     Optional('nation'):str,
# #     Optional('census_register'):str,
# #     Optional('phone'):str,
# #     Optional('address'):str,
# # })
# #
# # personinfo_by_name_schema = Schema({
# #     Required('name'):str,
# # })
# #
# # personinfo_by_id_schema = Schema({
# #     Required('person_id'):int,
# # })
# #
# # person_info_schema = Schema({
# #     Required('person_id'):int,
# #     Optional('name'):str,
# #     Optional('sex'):str,
# #     Optional('id_card'):str,
# #     Optional('id_address'):str,
# #     Optional('birthday'):Date(),
# #     Optional('nation'):str,
# #     Optional('census_register'):str,
# #     Optional('phone'):str,
# #     Optional('address'):str,
# # })
# #
# # del_personinfo_schema = Schema({
# #     Required('name'):str,
# #     Required('person_id'):int,
# # })
# #
# # auditinfo_by_store_id_schema = Schema({
# #     Required('store_id'):int,
# # })
# #
# # storeinfo_by_personid_schema = Schema({
# #     Required('person_id'):int,
# # })

