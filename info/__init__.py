from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import config

app = Flask(__name__)

# 加载配置
app.config.from_object(config["development"])

# 初始化数据库
db = SQLAlchemy(app)

redis_store = StrictRedis(host=config["development"].REDIS_HOST, port=config["development"].REDIS_PORT)

# 开启当前项目CSRF保护
CSRFProtect(app)

# 设置session指定保存位置
Session(app)