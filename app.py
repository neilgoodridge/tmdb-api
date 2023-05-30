from flask import Flask, render_template, request
from api_key import API_KEY
from datetime import datetime
import requests

base_url = 'https://api.themoviedb.org/3'
api_key = API_KEY
app = Flask(__name__)

# print(f'\nYour API key is {api_key}. Please comment out this line once confirmed\n')

@app.route('/')
def top_films():
    page = request.args.get('page', 1, type=int)
    endpoint = '/movie/top_rated'
    url = f'{base_url}{endpoint}?api_key={api_key}&page={page}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        top_films = data['results']

        total_pages = data['total_pages']
        current_page = data['page']

        film_details = []
        for film in top_films:
            movie_id = film['id']
            movie_info = get_movie_details(movie_id)
            film_details.append(movie_info)

        return render_template('top.html', films=film_details, total_pages=total_pages, current_page=current_page)
    else:
        print('Error')
        return render_template('top.html', films=[])

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

def get_movie_credits(movie_id):
    endpoint = f'/movie/{movie_id}/credits'
    url = f'{base_url}{endpoint}?api_key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        credits_data = response.json()
        cast = credits_data['cast']
        crew = credits_data['crew']
        return cast, crew
    else:
        return [], []

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    cast, crew = get_movie_credits(movie_id)
    movie = get_movie_details(movie_id)

    cast_details = []
    for actor in cast:
        person_id = actor['id']
        person_info = get_person_details(person_id)
        if person_info:
            cast_details.append(person_info)

    return render_template('details.html', film=movie, cast=cast, crew=crew, cast_details=cast_details, get_initials=get_initials)


@app.route('/popular')
def popular_films():
    page = request.args.get('page', 1, type=int)
    endpoint = '/movie/popular'
    url = f'{base_url}{endpoint}?api_key={api_key}&page={page}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        popular_films = data['results']

        total_pages = data['total_pages']
        current_page = data['page']

        film_details = []
        for film in popular_films:
            movie_id = film['id']
            movie_info = get_movie_details(movie_id)
            film_details.append(movie_info)

        return render_template('popular.html', films=film_details, total_pages=total_pages, current_page=current_page)
    else:
        print('Error')
        return render_template('popular.html', films=[])

@app.route('/search')
def search_films():
    query = request.args.get('query', '')
    endpoint = '/search/movie'
    url = f'{base_url}{endpoint}?api_key={api_key}&query={query}&sort_by=relevance'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        search_results = data['results']
        total_pages = data['total_pages']

        return render_template('search.html', results=search_results, query=query, current_page=None, total_pages=total_pages)
    else:
        print('Error')
        return render_template('search.html', results=[], query=query)


@app.route('/person/<int:person_id>')
def cast_details(person_id):
    person_info = get_person_details(person_id)
    combined_credits = get_combined_credits(person_id)
    if person_info:
        return render_template('cast.html', person=person_info, combined_credits=combined_credits)
    else:
        return render_template('cast.html', person=None)

def get_person_details(person_id):
    endpoint = f'/person/{person_id}'
    url = f'{base_url}{endpoint}?api_key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        person_data = response.json()
        return person_data
    else:
        return None

def get_combined_credits(person_id):
    endpoint = f'/person/{person_id}/movie_credits'
    url = f'{base_url}{endpoint}?api_key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        credits_data = response.json()
        combined_credits = credits_data['cast']
        return combined_credits
    else:
        return []

def get_initials(name):
    initials = ""
    name_parts = name.split()
    for part in name_parts:
        initials += part[0].upper()
    return initials

@app.route('/tv')
def top_tv_shows():
    page = request.args.get('page', 1, type=int)
    endpoint = '/tv/top_rated'
    url = f'{base_url}{endpoint}?api_key={api_key}&page={page}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        top_shows = data['results']

        total_pages = data['total_pages']
        current_page = data['page']

        show_details = []
        for show in top_shows:
            show_id = show['id']
            show_info = get_show_details(show_id)
            show_details.append(show_info)

        return render_template('top_tv.html', shows=show_details, total_pages=total_pages, current_page=current_page)
    else:
        print('Error')
        return render_template('top_tv.html', shows=[])


def get_show_details(show_id):
    endpoint = f'/tv/{show_id}'
    url = f'{base_url}{endpoint}?api_key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        show_data = response.json()
        first_air_date = show_data['first_air_date']
        formatted_first_air_date = datetime.strptime(first_air_date, '%Y-%m-%d').strftime('%-d %B %Y')

        show_details = {
            'name': show_data['name'],
            'overview': show_data['overview'],
            'poster_path': show_data['poster_path'],
            'id': show_data['id'],
            'backdrop_path': show_data['backdrop_path'],
            'episode_runtime': show_data['episode_run_time'],
            'first_air_date': formatted_first_air_date
        }
        return show_details
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
