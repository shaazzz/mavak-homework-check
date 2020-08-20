import json
import time

from ReqHandler import ReqHandler

req = ReqHandler()
with open("keys.txt", "r") as f:
    keys = json.loads(f.read())
api_key = keys["apiKey"]
apiSecret = keys["apiSecret"]

params = {"apiKey": api_key, "time": time.time()}
req.request("https://mavak.shaazzz.ir/")
