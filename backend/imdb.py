from bs4 import BeautifulSoup
import requests
import re
#import requests as HTTP
import paramiko
from paramiko.client import SSHClient
from flask import Flask, request
import json

# Mapping emotions to relevant movies

def detect_emotion(emotion):
    # IMDb URLs for Drama genre of movie against emotion Anger
    if(emotion == "angry"):
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

    # IMDb URLs for Drama genre of movie against emotion Disgust
    elif(emotion == "disgust"):
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

    # IMDb URLs for Drama genre of movie against emotion Fear
    elif(emotion == "fear"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

    # IMDb URLs for Drama genre of movie against emotion Happy
    elif(emotion == "happy"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    # IMDb URLs for Drama genre of movie against emotion Neutral
    elif(emotion == "neutral"):
         urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

    # IMDb URLs for Drama genre of movie against emotion Sad
    elif(emotion == "sad"):
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

    #IMDb URLs for Drama genre of movie against emotion Surprise
    elif(emotion == "surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'


    page = requests.get(urlhere)
    soup = BeautifulSoup(page.content, 'html.parser')

    movie_info_list = []
    movie_list = soup.find_all(class_='lister-item mode-advanced')

    for movie in movie_list:
            title = movie.find(class_='lister-item-header').a.text
            genre = re.findall(r'(\w+)', movie.find(class_='genre').text)
            image_url = movie.find('img')['loadlate']

            movie_info = {"title": title, "genre": genre, "image_url": image_url}
            movie_info_list.append(movie_info)

    return movie_info_list

app = Flask(__name__)

path = '/'
@app.route(path, methods=['POST'])

def connect():
    data = request.json
    data = json.dumps(data)
    data = json.loads(data)
    sentiment_type = data["sentiment"]
    #a dictionary obj that contains relevent info about movies.
    res = detect_emotion(sentiment_type)

    #TODO : to get values separately for future implementation
    for i in res:
        titles = i.get("title")
        print(titles)
        genres = i.get("genre")
        img_urls = i.get("image_url")


    return{
        "response ": res  #TODO: this should be optimized to return a status.
    }

if __name__ == "__main__":
    app.run(debug=True)


'''
curl req to pass :
curl -X POST http://127.0.0.1:5000/ -H 'Content-Type: application/json' -d '{"sentiment": "<mood>"}'

Example :
curl -X POST http://127.0.0.1:5000/ -H 'Content-Type: application/json' -d '{"sentiment": "angry"}'

'''
