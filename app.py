from flask import Flask, render_template
from api_key import API_KEY
import requests

base_url = 'https://api.themoviedb.org/3'
app = Flask(__name__)

def get_top_films(api_key):
    endpoint = '/movie/top_rated'

    url = f'{base_url}{endpoint}?api_key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        top_films = data['results']
        return top_films
    else:
        print('Error')


@app.route('/')
def top_films():
    films = get_top_films(API_KEY)
    return render_template('index.html', films=films)

if __name__ == '__main__':
    app.run()
