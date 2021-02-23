import requests;
import json

response = requests.get("http://api.open-notify.org/astros.json");
real_res = response.content;
print(json.loads(real_res)['number']);