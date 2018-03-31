from selenium import webdriver, common
from speaker import speaker
from form import get_forms
import os
import pickle
from time import sleep
from helper_functions import get_child_by_class, extract_notification
from apptool import startSpeak, getUserChoice, getUserSpeech

browser = None
TWITTER_BASE = "https://twitter.com"
LOGIN_PAGE = TWITTER_BASE + "/login"
HOME_PAGE = TWITTER_BASE + "/"
NOTIFICATION_PAGE = TWITTER_BASE + "/i/notifications"
inited = False
signed_in = False
tweets = []
notifications = []
current_tweet_index = -1
current_notification_index = -1

def init():
    global browser
    global inited
    if(inited):
        return False
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(chrome_options=options)
    inited = True

def close():
    if browser:
        browser.close()

def get_credentials():
    username = ''
    password = ''
    file_path = os.path.join(os.environ['HOMEPATH'], 'Desktop/Details.txt')
    with open(file_path, "r") as details:
        lines = details.readlines()
        username = lines[3].rstrip('\n')
        password = lines[4].rstrip('\n')

    return username, password

def login():
    global signed_in

    if signed_in:
        return True
    init()
    startSpeak("logging in to twitter, please hold on")
    browser.get(LOGIN_PAGE)
    form = get_forms(browser)[0]
    username, password = get_credentials()
    form["input_boxes"][0].send_keys(username)
    form["input_boxes"][1].send_keys(password)
    form["form"].submit()
    signed_in = True


def post_tweet():
    login()
    browser.get(TWITTER_BASE)
    tweet_box = browser.find_element_by_id('tweet-box-home-timeline')
    tweet_box.click()

    confirmation = 2
    while(confirmation == 2):
        startSpeak("Please speak what you would like to tweet")
        text = getUserSpeech()
        startSpeak("I am going to tweet this: " + text)
        confirmation = getUserChoice(['confirm', 'speak again', 'discard'])
        if(confirmation == 1):
            tweet_box.send_keys(text)
            browser.find_element_by_class_name('js-tweet-btn').click()
            return startSpeak("Tweeted successfully")
        elif(confirmation == 3):
            return startSpeak("Discarding the tweet")

def read_tweets():
    global tweets
    login()
    if(browser.current_url != TWITTER_BASE):
        browser.get(TWITTER_BASE)
        sleep(2)

    tweet_items = browser.find_elements_by_class_name('js-stream-item')

    for tweet_item in tweet_items:
        from_user = ""
        time = ""
        tweet_text = ""
        lang = ""
        try:
            from_user = get_child_by_class(tweet_item, 'fullname').text
            if(from_user is None):
                continue
            time = get_child_by_class(tweet_item, 'time').text.split('\n')[0]
            tweet_text_container = get_child_by_class(tweet_item, 'tweet-text')
            lang = tweet_text_container.get_attribute("lang").encode('utf-8')
            tweet_text = tweet_text_container.text

        except common.exceptions.NoSuchElementException:
            print("No such exception")
        except AttributeError:
            print("Attribute error")
        finally:
            if(lang == b'en' and len(from_user) > 0):
                tweets.append({
                    "from_user": str(from_user),
                    "time": str(time),
                    "text": str(tweet_text)
                })
    read_next_tweet()

def read_notifications():
    global notifications
    login()
    startSpeak("Loading notifications")
    if(browser.current_url != NOTIFICATION_PAGE):
        browser.get(NOTIFICATION_PAGE)
    browser.get(NOTIFICATION_PAGE)
    noti_wrapper = browser.find_element_by_class_name("stream-items")
    noti_li_items = []
    try:
        noti_li_items = noti_wrapper.find_elements_by_class_name("highlighted")
    except:
        pass

    notifications = [ item for item in [ extract_notification(elem) for elem in noti_li_items ] if len(item["heading"]) > 0 ]
    if(len(notifications) > 0):
        startSpeak("Here are the notifications: ")
        read_next_notification()
    else:
        startSpeak("There are no new notifications")

def read_next_notification():
    global notifications
    global current_notification_index
    current_notification_index += 1
    if(current_notification_index >= len(notifications)):
        return startSpeak("There are no more unread notifications")

    noti = notifications[current_notification_index]
    startSpeak(noti["heading"])
    input = take_input('notification')
    if(input == 1):
        read_next_notification

def read_next_tweet():
    global tweets
    global current_tweet_index

    current_tweet_index += 1
    if(current_tweet_index >= len(tweets)):
        return startSpeak("Read all the tweets, would you like to fetch new ones?")

    tweet = tweets[current_tweet_index]
    startSpeak(tweet["from_user"] + " tweeted " + tweet["time"] + " ago")
    startSpeak(tweet["text"])

    input = take_input("tweet")
    if(input == 1):
        read_next_tweet()

def take_input(type):
    type = 'next ' + type
    speaker.speak(question, True)
    choices = [type, 'close']
    return getUserChoice(choices)

if(__name__ == "__main__"):
    read_tweets()
