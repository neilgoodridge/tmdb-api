from flask import Flask, render_template
from api_key import API_KEY
import requests

base_url = 'https://api.themoviedb.org/3'
api_key = API_KEY
app = Flask(__name__)

@app.route('/')
def top_films():
    endpoint = '/movie/top_rated'
    url = f'{base_url}{endpoint}?api_key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        top_films = data['results']

        film_details = []
        for film in top_films:
            title = film['title']
            overview = film['overview']
            image = film['poster_path']
            id = film['id']
            movie_info = {
                'title': title,
                'id': id,
                'overview': overview,
                'poster_path': image
            }
            film_details.append(movie_info)

        return render_template('index.html', films=film_details)
    else:
        print('Error')
        return render_template('index.html', films=[])

if __name__ == '__main__':
    app.run()
