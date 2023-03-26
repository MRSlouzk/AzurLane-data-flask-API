from flask import Flask, jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return '''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Serverless Devs - Powered By Serverless Devs</title>
    <link href="https://example-static.oss-cn-beijing.aliyuncs.com/web-framework/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div class="website">
    <div class="ri-t">
        <h1>AzurLane Data</h1>
        <h2>这是一个使用 Flask 部署的项目</h2>
        <br/>
        <p>
            交流群：757739422
        </p>
    </div>
</div>
</body>
</html>
'''

@app.route('/pool')
def pool_t():
    cot = json.load(open("./nonebot-plugin-azurlane-assistant-data/azurlane/pool.json", "r", encoding="utf-8"))
    return jsonify(cot)

@app.route('/pool/<pool_type>')
def pool(pool_type):
    cot = json.load(open("./nonebot-plugin-azurlane-assistant-data/azurlane/pool.json", "r", encoding="utf-8"))
    if(cot.get(pool_type) == None):
        return jsonify({"error": "pool type not found"})
    return jsonify(cot[pool_type])

@app.route('/pool/<pool_type>/<rarity>')
def pool_2(pool_type, rarity):
    cot = json.load(open("./nonebot-plugin-azurlane-assistant-data/azurlane/pool.json", "r", encoding="utf-8"))
    if(cot.get(pool_type) == None):
        return jsonify({"error": "pool type not found"})
    if(cot[pool_type].get(rarity) == None):
        return jsonify({"error": "rarity not found"})
    return jsonify(cot[pool_type][rarity])


@app.route('/ship')
def ship_a():
    cot = json.load(open("./nonebot-plugin-azurlane-assistant-data/azurlane/ship.json", "r", encoding="utf-8"))
    return jsonify(cot["data"])

@app.route('/ship/t')
def ship_t():
    cot = json.load(open("./nonebot-plugin-azurlane-assistant-data/azurlane/ship.json", "r", encoding="utf-8"))
    return jsonify(cot["total_num"])

@app.route('/ship/<ship_name>')
def ship(ship_name):
    cot = json.load(open("./nonebot-plugin-azurlane-assistant-data/azurlane/ship.json", "r", encoding="utf-8"))
    for k in cot["data"]:
        if(k["name"] == ship_name):
            return jsonify(k)
        elif(ship_name in k["alias"]):
            return jsonify(k)
        else:
            continue
    return jsonify({"error": "未找到船只"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
