import requests

try:
    parameters = {"lat":40.71, "lon":-74};
    urlConnection = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters);
    if(urlConnection.status_code == 200):
        # what this returns is a string in json format i.e json data but coted to resemble a string hence is a string
        # what we can do is convert the string to dictionary or any python object
        # print(urlConnection.content);

        # the server returns not just data and status code but also return metadata like the header
        # the header is also a dictionary
        print(urlConnection.headers)

        # printing the content type of the response. this is always stored in the header
        print(urlConnection.headers['Content-Type']);
        print(urlConnection.json())
    else:
        print("invalid URL entered");
except:
    print("no connection");