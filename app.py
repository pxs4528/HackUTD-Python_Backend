import time

import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.taapi.io/macd?secret=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjM3MGJkZWJmYzVhOGFkZmVjYWMzZTFmIiwiaWF0IjoxNjY4MzMzMDU1LCJleHAiOjMzMTcyNzk3MDU1fQ.2aS4jcjhQ6UQGLfJnk3DCJBEpc-wixKemrJ5FXMh5as&exchange=binance&symbol=BTC/USDT&interval=30m&backtrack=40"
    response = requests.get(url)
    values = response.json()
    print(type(values))
    BTC = response.json()
    time.sleep(15)

    url = "https://api.taapi.io/macd?secret=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjM3MGJkZWJmYzVhOGFkZmVjYWMzZTFmIiwiaWF0IjoxNjY4MzMzMDU1LCJleHAiOjMzMTcyNzk3MDU1fQ.2aS4jcjhQ6UQGLfJnk3DCJBEpc-wixKemrJ5FXMh5as&exchange=binance&symbol=ETH/USDT&interval=30m&backtrack=40"
    response = requests.get(url)
    values = response.json()
    print(type(values))
    ETC = response.json()
    time.sleep(15)

    url = "https://api.taapi.io/macd?secret=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjM3MGJkZWJmYzVhOGFkZmVjYWMzZTFmIiwiaWF0IjoxNjY4MzMzMDU1LCJleHAiOjMzMTcyNzk3MDU1fQ.2aS4jcjhQ6UQGLfJnk3DCJBEpc-wixKemrJ5FXMh5as&exchange=binance&symbol=LTC/USDT&interval=30m&backtrack=40"
    response = requests.get(url)
    values = response.json()
    print(type(values))
    LTC = response.json()
    time.sleep(15)

    url = "https://api.taapi.io/macd?secret=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjM3MGJkZWJmYzVhOGFkZmVjYWMzZTFmIiwiaWF0IjoxNjY4MzMzMDU1LCJleHAiOjMzMTcyNzk3MDU1fQ.2aS4jcjhQ6UQGLfJnk3DCJBEpc-wixKemrJ5FXMh5as&exchange=binance&symbol=XRP/USDT&interval=30m&backtrack=40"
    response = requests.get(url)
    values = response.json()
    print(type(values))
    XRP = response.json()
    time.sleep(15)
    url = "https://api.taapi.io/macd?secret=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjM3MGJkZWJmYzVhOGFkZmVjYWMzZTFmIiwiaWF0IjoxNjY4MzMzMDU1LCJleHAiOjMzMTcyNzk3MDU1fQ.2aS4jcjhQ6UQGLfJnk3DCJBEpc-wixKemrJ5FXMh5as&exchange=binance&symbol=XMR/USDT&interval=30m&backtrack=40"
    response = requests.get(url)
    values = response.json()
    print(type(values))
    XMR = response.json()
    x = BTC['valueMACD']
    y = ETC['valueMACD']
    z = LTC['valueMACD']
    a = XRP['valueMACD']
    b = XMR['valueMACD']

    dict = {"BTC" : x}
    dict.update({"ETC" : y})
    dict.update({"LTC" : z})
    dict.update({"XRP" : a})
    dict.update({"XMR" : b})
    a = sorted(dict.items(), key=lambda x: x[1], reverse = True)    
    print(type(a))

    return dict
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4552, debug=True)
    
    #Darth Parth rulez
