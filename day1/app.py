from flask import Flask, jsonify
import random

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由：当访问根路径时返回欢迎信息
@app.route('/')
def home():
    return "欢迎使用随机数API！访问 /random 获取随机数"


# 定义核心路由：返回随机数的API
@app.route('/random/<int:max_value>', methods=['GET'])
def get_random_number(max_value):
    # 生成0-100之间的随机整数
    random_num = random.randint(0, max_value)

    # 构建JSON响应
    response = {
        "random_number": random_num,
        "message": "成功生成随机数",
        "range": "0-100"
    }
    return jsonify(response)


if __name__ == '__main__':

    # 启动Flask开发服务器（0.0.0.0表示可外部访问）
    app.run(host='0.0.0.0', port=5000, debug=True)