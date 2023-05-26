from api_key import API_KEY
import requests

url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer {API_KEY}"
}

response = requests.get(url, headers=headers)

print(response.text)
