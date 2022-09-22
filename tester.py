import json
import requests

data={"hello":"world"}

res=requests.post("http://localhost:5000/apis/partners")
print(res.status_code)
