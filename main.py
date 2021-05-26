from datetime import timedelta

from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)

# 将配置信息封装到config类中  统一管理
class Config:
    DEBUG = True   # 开启调试模式
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info23"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪数据库变化
    REDIS_HOST = "127.0.0.1"  # redis绑定的ip 可以自定义配置key封装到Config类中
    REDIS_POST = 6379  # redis监听的端口
    SESSION_TYPE = "redis"  # 设置session的存储方式
    SESSION_REDIS = Redis(host=REDIS_HOST,port=REDIS_POST) # 设置redis操作对象
    SESSION_USE_SIGNER = True
    app.secret_key = "qbzXNNbe0MDRxcgBb2LjzwNjkyP+S2NKV/XyfescggXqcxCD2ba1GPXRFUpVBY4+"  # 设置应用秘钥,对 sessionID进行加密
    PERMANENT_SESSION_LIFETIME = timedelta(days=7) # 设置session过期时间



# 数据库设置
app.config.from_object(Config)

# 创建数据库链接
db = SQLAlchemy(app)
# 创建redis链接
rs = Redis(host=Config.REDIS_HOST,port=Config.REDIS_POST)
# 初始化session存储器
Session(app)

# 创建管理器
mgr = Manager(app)

# 初始化数据迁移器
Migrate(app,db)
# 使用管理器生成迁移命令
mgr.add_command("mc",MigrateCommand)

@app.route("/")
def index():
    # 和之前一样使用session进行存取操作
    session["name"] = "zs"
    return "index"


if __name__ == '__main__':
    mgr.run()
