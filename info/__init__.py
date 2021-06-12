from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from config import config_dict

# 将数据库链接对象定义为全局变量 以便其他文件导入使用
db = None   # type: SQLAlchemy
rs = None   # type: Redis

# 工厂函数: 由 外界 提供物料,函数内部封装对象的创建过程
def creat_app(config_type):  # 封装web应用创建过程
    # 根据类型取出对应的配置子类
    config_class = config_dict[config_type]
    app = Flask(__name__)
    # 数据库设置
    app.config.from_object(config_class)

    # 声明全局变量
    global db,rs

    # 创建数据库链接
    db = SQLAlchemy(app)
    # 创建redis链接
    rs = Redis(host=config_class.REDIS_HOST,port=config_class.REDIS_POST)
    # 初始化session存储器
    Session(app)
    # 初始化数据迁移器
    Migrate(app, db)

    # 注册蓝图对象  如果内容只在文件中使用一次,最好在使用前才导入,可以有效避免导入错误
    from info.modules.home import home_blu
    app.register_blueprint(home_blu)

    return app

