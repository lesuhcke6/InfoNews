from datetime import timedelta
from redis import Redis

# 将配置信息封装在config类中  统一管理
class Config:
    DEBUG = True   # 开启调试模式
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info23"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪数据库变化
    REDIS_HOST = "127.0.0.1"  # redis绑定的ip 可以自定义配置key封装到Config类中
    REDIS_POST = 6379  # redis监听的端口
    SESSION_TYPE = "redis"  # 设置session的存储方式
    SESSION_REDIS = Redis(host=REDIS_HOST,port=REDIS_POST) # 设置redis操作对象
    SESSION_USE_SIGNER = True
    SECRET_KEY = "qbzXNNbe0MDRxcgBb2LjzwNjkyP+S2NKV/XyfescggXqcxCD2ba1GPXRFUpVBY4+"  # 设置应用秘钥,对 sessionID进行加密
    PERMANENT_SESSION_LIFETIME = timedelta(days=7) # 设置session过期时间

# 不同的代码环境应该使用不同的配置信息(配置子类化)
# 开发环境:项目开发阶段需要的代码环境
class DevelopementConfig(Config):
    DEBUG = True
    REDIS_HOST = "127.0.0.1"

# 生产环境:项目上线后需要的代码环境(用户可以外网访问)
class ProductionConfig(Config):
    DEBUG = False
    # REDIS_HOST = "222.xx.xx.xx"