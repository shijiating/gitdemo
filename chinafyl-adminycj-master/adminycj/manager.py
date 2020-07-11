from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from voluptuous import MultipleInvalid
from api import create_app, DevConfig, db
from api.views.base import common_response, SysStatus
from flask_cors import CORS
from api.models import user, store_Info, forecast, case_Info, base, rule, svm_bp, task

# 解决跨域问题
app = create_app(DevConfig)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
# db = SQLAlchemy(app)
manager = Manager(app)


@app.errorhandler(MultipleInvalid)
def handle_exception(error):
    return common_response(SysStatus.PARAMETER_CHECK_ERROR, None, str(error))


Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
