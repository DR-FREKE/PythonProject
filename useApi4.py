import requests
# Make the same request we did two screens ago.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
# print(type(json_data))
# first_pass_duration = json_data['duration'];
print(json_data['response'])