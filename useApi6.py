import requests

headers = {
    'x-rapidapi-host': "bing-image-search1.p.rapidapi.com",
    'x-rapidapi-key': "df694f93e2msh0d689dc2772e188p10a83ajsnf463614893dc"
}

response = requests.request("GET", "https://bing-image-search1.p.rapidapi.com/images/trending", headers=headers);
print(response.text)