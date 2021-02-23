import requests

try:
    response = requests.get("http://api.open-notify.org/iss-now.json");

    if(response.status_code == 200):
        print(response.status_code);
    else:
        print("invalid URL");
except IOError:
    print("an error occured");
