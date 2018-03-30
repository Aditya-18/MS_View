from selenium import webdriver, common
import malespeaker
from form import get_forms
import os
import pickle
from time import sleep
from helper_functions import get_child_by_class, extract_notification

browser = None
TWITTER_BASE = "https://twitter.com"
LOGIN_PAGE = TWITTER_BASE + "/login"
HOME_PAGE = TWITTER_BASE + "/"
NOTIFICATION_PAGE = TWITTER_BASE + "/i/notifications"

def init():
    global browser
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(chrome_options=options)

def close():
    if browser:
        browser.close()

init()
signed_in = False
browser.get(LOGIN_PAGE)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
#browser.refresh()

'''
if browser.current_url != LOGIN_PAGE:
    signed_in = True

if not signed_in:

    form = get_forms(browser)[0]
    malespeaker.speak("You need to log into twitter")
    malespeaker.speak("What's your twitter handle?")
    malespeaker.speak("Password?")
    twitter_username = 'iamanshulmalik'
    twitter_pass = os.environ["TWITTER_PASSWORD"]
    form["input_boxes"][0].send_keys(twitter_username)
    form["input_boxes"][1].send_keys(twitter_pass)
    form["form"].submit()
'''

def save_session():
    cookies = browser.get_cookies()
    pickle.dump(cookies, open("cookies.pkl", "wb"))

#malespeaker.speak("You are successfully signed in to twitter")
save_session()


def post_tweet(text):
    browser.get(TWITTER_BASE)
    tweet_box = browser.find_element_by_id('tweet-box-home-timeline')
    tweet_box.click()
    tweet_box.send_keys(text)
    browser.find_element_by_class_name('js-tweet-btn').click()

def get_tweets():
    tweet_items = browser.find_elements_by_class_name('js-stream-item')
    print(len(tweet_items))

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
                print(type(from_user), from_user)
                print(type(time))
                malespeaker.speak(str(from_user) + " tweeted " + str(time) + " ago")
                malespeaker.speak(str(tweet_text))
#sleep(4)
#get_tweets()

'''
malespeaker.speak("Loading notifications")
browser.get(NOTIFICATION_PAGE)
noti_wrapper = browser.find_element_by_class_name("stream-items")
noti_li_items = []
try:
    noti_li_items = noti_wrapper.find_elements_by_class_name("highlighted")
except:
    pass

noti_list = [ item for item in [ extract_notification(elem) for elem in noti_li_items ] if len(item["heading"]) > 0 ]
if(len(noti_list) > 0):
    malespeaker.speak("Here are the notifications: ")
else:
    malespeaker.speak("There are no new notifications")

for noti in noti_list:
    malespeaker.speak(noti["heading"])
'''
