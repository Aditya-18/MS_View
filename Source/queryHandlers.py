import os
import malespeaker
import news
import datetime
import calendar
import gui
import date_time
import getpass
import fetchMails
import requests
import re
import time
import subprocess
import weatherUpdates
import pyautogui
import takenote
import windowCommands
import searchWeb


def remove(s):
    return ''.join(['' if ord(i) < 123 and ord(i)>96 else i for i in s])

def get(q):
    q = q.lower()
    if ("who are you" in q or "what are you" in q):
        malespeaker.speak("I am Mantis Shrimp. A voice controlled assistant that can control your device according to your commands.")
        return

    elif ("fetch" in q or "get" in q or "tell" in q or "show" in q or "give" in q) and ("news" in q or "updates" in q or "stories" in q) and ("where" not in q or "why" not in q):
        news.allnews()
        return

    # elif (("give" in q or "tell" in q or "show" in q) and ("calendar" in q)) or"calendar" in q:
    #     c = calendar.TextCalendar(calendar.SUNDAY)
    #     if("next month" in q):
    #         str = c.formatmonth(2018+int((datetime.datetime.now().month+1)/12),((datetime.datetime.now().month+1)%12))
    #     elif("previous month" in q):
    #         str = c.formatmonth((2018-int((datetime.datetime.now().month-1)/12)),(datetime.datetime.now().month-1)%12)
    #     else:
    #         str = c.formatmonth(2018,datetime.datetime.now().month)
    #     gui.query_gui(str)
    #     return

    elif ("get" in q or "tell" in q or "show" in q) and ("date" in q or "time" in q or "month" in q or "day" in q or "year" in q or "calendar" in q) or ("today's date" in q) or "what date is today" in q or "which month is this" in q or "what year is this" in q or "which year is this" in q or "what time is it" in q or "what is time" in q or "what time is today" in q or "current time" in q:
        date_time.current_date_time()
        return

    elif ("fetch" in q or "open" in q or "get" in q or "tell" in q or "show" in q or "give" in q or "open" in q) and ("mails" in q or "mail updates" in q or "emails" in q or "gmail" in q or "yahoo" in q or "mail" in q) and ("where" not in q or "who" not in q or "why" not in q or "how" not in q):
        malespeaker.speak("Sir please enter your secure server password to prove your identity")
        passwd = getpass.getpass("Your Password please : ")
        if passwd != "jdq836adi@1997":
            malespeaker.speak("Sorry you are not authorized to see mails")
            return
        fetchMails.mails()
        return

    elif "how is weather" in q or "how is weather today" in q or "weather today" in q or ("fetch" in q or "get" in q or "tell" in q or "show" in q or "give" in q) and ("weather" in q or "weather updates" in q or "temeperature" in q or "hot" in q or "cold " in q or "humidity" in q or "weather condition" in q or "climate" in q) or "how is weather today" in q or "is it hot outside" in q or "is it cold outside" in q:
        weatherUpdates.getWeather(q)
        return


    elif ("calculate" in q or "solve" in q or "solution of" in q or "simplify" in q or "result of" in q) and ("maths" in q or "mathematics" in q or "expression" in q) or "open calc" in q or "open calculator" in q or "/" in q or "*" in q or "+" in q or "-" in q:
        malespeaker.speak("wait while I solve your maths query")
        q = remove(q)
        url = 'http://api.mathjs.org/v1/?expr='+q
        y = requests.get(url)
        gui.query_gui("solution of your query is "+y.text)
        malespeaker.speak("solution of your query is "+y.text)
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        time.sleep(3)
        #pyautogui.hotkey('alt', 'tab')
        pyautogui.typewrite(q,0.04)
        pyautogui.typewrite('=')
        return

    elif ("play" in q or "open" in q or "start" in q or "begin" in q) and ("music" in q or "song" in q ):
        malespeaker.speak("Playing your favourite music")
        os.system('C:\\Users\\"Aditya Goel"\\Music\\hasi.mp3')
        return


    elif ("open" in q or "popup" in q or "show" in q) and ("taskmanager" in q or "Taskmanager" in q or "task manager" in q or "Task manager" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        malespeaker.speak("Opening taskmanager")
        subprocess.Popen("C:\Windows\System32\\Taskmgr.exe", shell=True)
        return

    elif ("open" in q or "popup" in q or "show" in q) and ("notepad" in q or "Notepad" in q or "note taking app" in q or "note keeper" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        malespeaker.speak("Opening notepad")
        subprocess.Popen("C:\Windows\System32\\notepad.exe", shell=True)
        return

    elif ("open" in q or "popup" in q or "show" in q) and ("control panel" in q or "Control panel" in q or "settings" in q or "computer setting" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        malespeaker.speak("Control Panel")
        subprocess.Popen("C:\Windows\System32\\control.exe", shell=True)
        return

    elif ("open" in q or "popup" in q or "show" in q) and ("cmd" in q or "CMD" in q or "command line" in q or "command prompt" in q or "commandline" in q or "commandprompt" in q) or "open windows shell" in q and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        malespeaker.speak("Opening Command Prompt")
        os.system('start "my window" cmd.exe')
        return

    elif ("write a note" in q or "take a note" in q or (("take" in q or "write" in q) and ("note") in q)) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        malespeaker.speak("Wait a moment while I open notepad")
        takenote.notedown(q)
        time.sleep(10)
        return
    elif ("decrease" in q or "reduce" in q or "lower" in q ) and ("volume" in q or "sound" in q or "volumelevel" in q or "soundlevel" in q or "volume level" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        q = re.sub('\D',"",q)
        malespeaker.speak("Decreasing volume of device by" + q+" percents")
        if q != "":
            for i in range(0, int((int(q) + 1) / 2)):
                pyautogui.press('volumedown')
        return
    elif ("increase" in q or "up" in q or "higher" in q ) and ("volume" in q or "sound" in q or "volumelevel" in q or "soundlevel" in q or "volume level" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        q = re.sub('\D',"",q)
        malespeaker.speak("Increasing volume of device by "+q+" percents")
        if q != "":
            for i in range(0, int((int(q) + 1) / 2)):
                pyautogui.press('volumeup')
        return
    elif ("mute" in q or "shut up" in q or "quiet" in q ) and ("volume" in q or "sound" in q or "volumelevel" in q or "soundlevel" in q or "volume level" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        malespeaker.speak("Mute")
        pyautogui.press('volumemute')
        return
    elif ("take" in q or "get" in q or "keep" in q ) and ("screenshot" in q or "screen shot" in q or "snapshot" in  q or "snap shot" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
        pyautogui.hotkey('winleft', 'printscreen')
        malespeaker.speak("Snapshot saved in pictures")
        return
    # elif ("scroll down" in q or "scrolldown" in q or "go down" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
    #     malespeaker.speak("Scrolling down")
    #     pyautogui.scroll(-400)
    #     return
    # elif ("scroll up" in q or "scrollup" in q or "go up" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q):
    #     malespeaker.speak("scrolling up")
    #     pyautogui.scroll(400)
    #     return
    elif ("shut down" in q or "shutdown" in q or "log off" in q or "logoff" in q or "signout" in q or "sign me out" in q or "sign out" in q or "restart" in q or "re start" in q or "sleep this device" in q) and ("what" not in q or "where" not in q or "who" not in q or "why" not in q or "how" not in q)or "good night axis" in q or "get a nap" in q or "shut down computer" in q or "log off computer" in q:
        windowCommands.exec(q)
        return
    else:
        searchWeb.apiaicall(q)
        return
    return
if __name__ == '__main__':
    get("what is Google")
