import requests;
import json;

headers = {"Authorization" : "8e5e787c69f486b7e610eb23719a4e656d7aa410"};

response = requests.get("https://api.github.com/users/VikParuchuri/orgs", headers=headers);
orgs = response.json();
print(orgs); 