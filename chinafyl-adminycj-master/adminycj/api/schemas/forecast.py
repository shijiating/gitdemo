from voluptuous import Schema, Required, Optional, Date, Boolean, In, Number

forecast_result_schema = Schema({
    Required('forecast_model'): In(("Rule", "Comprehensive"))
})
forecast_warning_params_schema = Schema({
    Required('model_warning_params'): In(("RULE", "BP"))
})
warning_params_schema = Schema({
    Required('model_warning_params'): In(("RULE", "BP")),
    Optional('param1'): Number(2, 2),
    Optional('param2'): Number(2, 2),
    Optional('param3'): Number(2, 2)
})

statistic_schema = Schema({
    Required('start_year'): int,
    Required('start_month'): int,
    Required('end_year'): int,
    Required('end_month'): int
    # Required('mode'): str
})

forecast_store_schema = Schema({
    Required('role_id'): int,
    Required('station_id'): int,
    Optional('department_id'): int,
    Required('mode'): In(("Rule", "Comprehensive"))
})
