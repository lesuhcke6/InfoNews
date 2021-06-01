from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from config import DevelopementConfig

app = Flask(__name__)
# 数据库设置
app.config.from_object(DevelopementConfig)

# 创建数据库链接
db = SQLAlchemy(app)
# 创建redis链接
rs = Redis(host=DevelopementConfig.REDIS_HOST,port=DevelopementConfig.REDIS_POST)
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
