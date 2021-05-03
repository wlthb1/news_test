from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

class Config(object):
    """ 项目的配置 """
    DEBUG = True

    SECRET_KEY = "aEtF9gvwHXsV/iSpUOTZ/f1prCzkgF6EvMIefanhRCEBZKoHGDxJS0qYfOkx9c/1"


    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # Session保存位置
    SESSION_TYPE = 'redis'
    # 开启session签名
    SESSION_USE_SIGNER = True

    # 指定session保存到redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    # 取消永久保存session时效并设置时间
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启当前项目CSRF保护
CSRFProtect(app)

# 设置session指定保存位置
Session(app)

@app.route("/")
def index():
    return 'hello world!!'


if __name__ == "__main__":

    app.run(debug=True)