from voluptuous import MultipleInvalid
from api import create_app, DevConfig, db
from api.views.base import common_response, SysStatus
from flask_cors import CORS

# 解决跨域问题
app = create_app(DevConfig)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


@app.errorhandler(MultipleInvalid)
def handle_exception(error):
    return common_response(SysStatus.PARAMETER_CHECK_ERROR, None, str(error))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001")
