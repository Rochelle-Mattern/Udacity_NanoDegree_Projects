import media
import urllib
import json
import P1_python_movies

#Create a function that will pull data from the omdb api
def pull_api_data(movie_title):
    movie_title_formatted = movie_title.replace(" ", "+")
    connection = urllib.urlopen("http://www.omdbapi.com/?t="
                                + movie_title_formatted+"&y=2016&plot=short&tomatoes=true")
    output = connection.read()
    output_json = json.loads(output)
    return {'Title': output_json['Title'],
            'Storyline': output_json['Plot'],
            'poster_image': output_json['Poster'],
            'rating': output_json['tomatoMeter']}
    connection.close()

#Create instances of Movies for each golden globe winer
moonlight = media.Movies(
    pull_api_data("Moonlight")['Title'],
    pull_api_data("Moonlight")['Storyline'],
    pull_api_data("Moonlight")['poster_image'],
    "https://www.youtube.com/watch?v=9NJj12tJzqc",
    pull_api_data("Moonlight")['rating'])


la_la_land = media.Movies(
    pull_api_data("La La Land")['Title'],
    pull_api_data("La La Land")['Storyline'],
    pull_api_data("La La Land")['poster_image'],
    "https://www.youtube.com/watch?v=0pdqf4P9MB8",
    pull_api_data("La La Land")['rating'])

elle = media.Movies(pull_api_data("Elle")['Title'],
    pull_api_data("Elle")['Storyline'],
    pull_api_data("Elle")['poster_image'],
    "https://www.youtube.com/watch?v=H-iBBgcp7PY",
    pull_api_data("Elle")['rating'])

manchester_by_the_sea = media.Movies(
    pull_api_data("Manchester by the Sea")['Title'],
    pull_api_data("Manchester by the Sea")['Storyline'],
    pull_api_data("Manchester by the Sea")['poster_image'],
    "https://www.youtube.com/watch?v=gsVoD0pTge0",
    pull_api_data("Manchester by the Sea")['rating'])

fences = media.Movies(pull_api_data("Fences")['Title'],
    pull_api_data("Fences")['Storyline'],
    pull_api_data("Fences")['poster_image'],
    "https://www.youtube.com/watch?v=a2m6Jvp0bUw",
    pull_api_data("Fences")['rating'])

nocturnal_animals = media.Movies(pull_api_data("Nocturnal Animals")['Title'],
    pull_api_data("Nocturnal Animals")['Storyline'],
    pull_api_data("Nocturnal Animals")['poster_image'],
    "https://www.youtube.com/watch?v=-H1Ii1LjyFU",
    pull_api_data("Nocturnal Animals")['rating'])

zootopia = media.Movies(pull_api_data("Zootopia")['Title'], 
    pull_api_data("Zootopia")['Storyline'], 
    pull_api_data("Zootopia")['poster_image'],
    "https://www.youtube.com/watch?v=jWM0ct-OLsM", 
    pull_api_data("Zootopia")['rating'])

#Create a list of movies to use in the open movies page function
movies = [la_la_land, elle, manchester_by_the_sea,
          fences, nocturnal_animals, zootopia]

P1_python_movies.open_movies_page(movies)
