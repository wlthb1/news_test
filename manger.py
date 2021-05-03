from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db

manager = Manager(app)

# 将 app 与 db关联
Migrate(app, db)

# 将迁移命令添加到manager中
manager.add_command('db',MigrateCommand)

@app.route("/")
def index():
    return 'hello world!!'


if __name__ == "__main__":
    manager.run()