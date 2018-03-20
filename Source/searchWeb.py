import wikipedia
import os
import subprocess
import webbrowser
import malespeaker
import pyautogui


def fun2(y):
    y = y.replace(" the ", "")
    y = y.replace(" a ", "")
    y = y.replace(" an ", "")
    return y


def remove(s):
    s = s.replace("listen", "")
    return ''.join([i if ord(i) < 128 else '' for i in s])


def fun():
    for i in range(0, 20):
        pyautogui.press('down')
    for i in range(0, 20):
        pyautogui.press('up')


def apiaicall(y):
    if 'who is' in y:
        y = fun2(y)
        y = y.replace("who is", "")
        try:
            x = (wikipedia.summary(y, sentences=1))
            x = remove(x)
        # print(x)
        except:
            x = "Sorry I dont know that sir...My friend Google will help out with this"
        url = "https://www.google.co.in/search?safe=active&source=hp&ei=g44vWrDqGMndvASvrKjYAQ&q=" + y
        webbrowser.open(url)
        malespeaker.speak(x)
        # fun()

        return x
    elif 'where is' in y:
        y = fun2(y)
        y = y.replace("where is", "")
        try:
            x = (wikipedia.summary(y, sentences=1))
            x = remove(x)
        # print(x)
        except:
            x = "Sorry I dont know that sir... My friend Google will help out with this"
        url = "http://www.google.co.in/maps/place/" + y + "/&amp;"
        webbrowser.open(url)
        malespeaker.speak(x)

    elif 'what is' in y:
        y = y.replace("what is", "")
        y = fun2(y)
        try:
            x = (wikipedia.summary(y, sentences=1))
            x = remove(x)
        # print(x)
        except:
            x = "Sorry I dont know that sir, My friend google will help out with this"
        url = "https://www.google.co.in/search?safe=active&source=hp&ei=g44vWrDqGMndvASvrKjYAQ&q=" + y
        webbrowser.open(url)
        malespeaker.speak(x)
        # fun()
    else:
        y = fun2(y)
        try:
            x = (wikipedia.summary(y, sentences=1))
            x = remove(x)
            print(x)
        except:
            x = "I will google out your query sir"
        url = "https://www.google.co.in/search?safe=active&source=hp&ei=g44vWrDqGMndvASvrKjYAQ&q=" + y
        webbrowser.open(url)
        malespeaker.speak(x)
        # fun()


if __name__ == '__main__':
    apiaicall("what's my current location")
