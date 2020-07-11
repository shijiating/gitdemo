from api.models.user import User

user_info_ser = [
    User.id,
    User.account,
    User.user_name,
    User.department_id,
    User.role_id,
    User.station_id
]
