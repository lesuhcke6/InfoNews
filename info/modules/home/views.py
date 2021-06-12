from info.modules.home import home_blu
from info import rs

# 使用蓝图对象注册路由
@home_blu.route("/")
def index():
    rs.set("age",20)

    return "index"