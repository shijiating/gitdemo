from datetime import datetime, date
from decimal import Decimal

from voluptuous import Schema, Required, All, Length, Optional, Boolean, In, Datetime, Date

# 规则修改
modify_rule_schema = Schema({
    Required('rule_id'):int,
    Optional('rule_name'): str,
    Optional('parameter1'): int,
    Optional('parameter2'): int,
    Optional('parameter3'): int,
    Optional('parameter4'): int,
    Optional('score1'): int,
    Optional('score2'): int,
    Optional('score3'): int,
    Optional('score4'): int,
    Optional('describe_rule'): str,
    Optional('modifydate'): Date(),
})

# 规则停用
del_rule_schema = Schema({
    Required('rule_id'): int,
    Optional('rule_name'): str,
})

# 规则启用
add_rule_schema = Schema({
    Required('rule_id'): int,
    Optional('rule_name'): str,
})

# 查询高危用户的分数构成
highrisk_store = Schema({
    Required('store_id'): int,
})

# 查询规则
search_rule = Schema({
    Required('rule_id'): str,
})



