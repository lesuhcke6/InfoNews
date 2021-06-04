from flask import Flask,session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from info import creat_app

app = creat_app("dev")
# 创建管理器
mgr = Manager(app)

# 使用管理器生成迁移命令
mgr.add_command("mc",MigrateCommand)

@app.route("/")
def index():
    # 和之前一样使用session进行存取操作
    session["name"] = "zs"
    return "index"


if __name__ == '__main__':
    mgr.run()
