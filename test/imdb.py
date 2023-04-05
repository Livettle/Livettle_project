from bs4 import BeautifulSoup
import requests
import re
#import requests as HTTP
import paramiko
from paramiko.client import SSHClient
from flask import Flask, request
import json

# Mapping emotions to relevant movies
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def detect_emotion():

    emotion = request.json['emotion']

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

    url = "https://online-movie-database.p.rapidapi.com/auto-complete"
    headers = {
        "X-RapidAPI-Key": "18de6d8512msh6ecfefddc049adcp17758bjsn8cec6d306dd5",
        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }

    content = [[] for i in range(5)]

    for title in range(0,5):
        i = res[title]
        titles = i.get("title")

        querystring = {"q":titles}
        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = json.loads(response.text)
        content[title].append(json_data["d"][0]['i']['imageUrl'])
        content[title].append(json_data["d"][0]['l'])
        content[title].append(json_data["d"][0]['y'])
        content[title].append(json_data["d"][0]['qid'])

    for i in content:
        print(i)
    return{
        "response ": response.text
    }

detect_emotion(request.form['emotion'])

if __name__ == "__main__":
    app.run(debug=True)

'''
curl req to pass :
curl -X POST http://127.0.0.1:5000/ -H 'Content-Type: application/json' -d '{"sentiment": "<mood>"}'
Example :
curl -X POST http://127.0.0.1:5000/ -H 'Content-Type: application/json' -d '{"sentiment": "angry"}'

'''
