from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

app = Flask(__name__)

# 将配置信息封装到config类中  统一管理
class Config:
    DEBUG = True   # 开启调试模式
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info23"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪数据库变化
    REDIS_HOST = "127.0.0.1"  # redis绑定的ip 可以自定义配置key封装到Config类中
    REDIS_POST = 6379  # redis监听的端口

# 数据库设置
app.config.from_object(Config)

# 创建数据库链接
db = SQLAlchemy(app)
# 创建redis链接
rs = Redis(host=Config.REDIS_HOST,port=Config.REDIS_POST)


@app.route("/")
def index():

    return "index"


if __name__ == '__main__':

    app.run()
