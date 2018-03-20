import requests
import json
import urllib
import gui
import malespeaker
import time

def allnews():
    url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=5cab5d5971064472bb501bd1d73a7a2d'
    response = requests.get(url)
    r = response.json()
    k = json.dumps(r, indent=4)
    res = json.loads(k)
    malespeaker.speak("Here are top news updates from BBC:")
    print()
    i=0
    x="NEWS\n"
    y=""
    while i<5:
        image = str(i)+'.jpg'
        #urllib.request.urlretrieve(res['articles'][i]['urlToImage'],image)
        x =""
        x+=(res['articles'][i]['title'])+"\n"
        x+=(res['articles'][i]['description'])+"\n\n"
        print(x)
        malespeaker.speak(x)
        i=i+1

def newstopic(topic):
    url = 'https://newsapi.org/v2/everything?q='+topic+'&sortBy=popularity&apiKey=5cab5d5971064472bb501bd1d73a7a2d'
    response = requests.get(url)
    r = response.json()
    k = json.dumps(r, indent=4)
    res = json.loads(k)
    print("Here are top news updates about "+topic)
    print()
    i=0
    while i<5:
        image = str(i)+'.jpg'
        #urllib.request.urlretrieve(res['articles'][i]['urlToImage'],image)
        print(res['articles'][i]['title'])
        print(res['articles'][i]['description'])
        print(res['articles'][i]['url'])
        malespeaker.speak(res['articles'][i]['title'])
        time.sleep(4)
        print()
        i=i+1

if __name__ == '__main__':
    allnews()
