from flask import Flask, render_template
from api_key import API_KEY
from datetime import datetime
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
            background = film['backdrop_path']
            movie_info = {
                'title': title,
                'id': id,
                'overview': overview,
                'poster_path': image,
                'backdrop_path': background
            }
            film_details.append(movie_info)

        return render_template('index.html', films=film_details)
    else:
        print('Error')
        return render_template('index.html', films=[])

def get_movie_details(movie_id):
    endpoint = f'/movie/{movie_id}'
    url = f'{base_url}{endpoint}?api_key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()
        release_date = movie_data['release_date']
        formatted_release_date = datetime.strptime(release_date, '%Y-%m-%d').strftime('%-d %B %Y')

        movie_details = {
            'title': movie_data['title'],
            'overview': movie_data['overview'],
            'poster_path': movie_data['poster_path'],
            'id': movie_data['id'],
            'backdrop_path': movie_data['backdrop_path'],
            'runtime': movie_data['runtime'],
            'tagline': movie_data['tagline'],
            'release_date': formatted_release_date


        }
        return movie_details
    else:
        return None

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie = get_movie_details(movie_id)
    return render_template('details.html', film=movie)

if __name__ == '__main__':
    app.run()
