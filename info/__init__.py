from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from config import config_dict

# 工厂函数: 由 外界 提供物料,函数内部封装对象的创建过程
def creat_app(config_type):  # 封装web应用创建过程
    # 根据类型取出对应的配置子类
    config_class = config_dict[config_type]
    app = Flask(__name__)
    # 数据库设置
    app.config.from_object(config_class)

    # 创建数据库链接
    db = SQLAlchemy(app)
    # 创建redis链接
    rs = Redis(host=config_class.REDIS_HOST,port=config_class.REDIS_POST)
    # 初始化session存储器
    Session(app)
    # 初始化数据迁移器
    Migrate(app, db)

    return app

