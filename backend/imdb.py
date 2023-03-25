from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP
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

    # IMDb URLs for Drama genre of movie against emotion Surprise
    elif(emotion == "surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

# Scraping part
# HTTP request to get the data of
    # the whole page
    response = HTTP.get(urlhere)
    data = response.text

    # Parsing the data using
    # BeautifulSoup
    soup = SOUP(data, "lxml")

    # Extract movie titles from the
    # data using regex
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    return title

app = Flask(__name__)

path = '/'
@app.route(path, methods=['POST','GET'])

def connect():
    data = request.json
    data = json.dumps(data)
    data = json.loads(data)
    sentiment_type = data["sentiment"]

    res = detect_emotion(sentiment_type)

    return{
        "Movies to recommend ": str(res)
    }

if __name__ == "__main__":
    app.run(debug=True)


'''
curl req to pass :
curl -X POST http://127.0.0.1:5000/ -H 'Content-Type: application/json' -d '{"sentiment": "<mood>"}'

Example :
curl -X POST http://127.0.0.1:5000/ -H 'Content-Type: application/json' -d '{"sentiment": "angry"}'

'''
