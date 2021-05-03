from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """ 项目的配置 """
    DEBUG = True

    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)

@app.route("/")
def index():
    return 'hello world!!'


if __name__ == "__main__":

    app.run(debug=True)