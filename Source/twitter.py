from selenium import webdriver, common
import malespeaker
from form import get_forms
import os
import pickle

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
browser.refresh()

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

def extract_notification(elem):
    heading = ''
    try:
        heading = elem.find_element_by_class_name("ActivityItem-textSection").text
    except common.exceptions.NoSuchElementException:
        heading = ''
    return {
        "heading": heading,
        "target": elem
    }

browser.get(NOTIFICATION_PAGE)
noti_wrapper = browser.find_element_by_class_name("stream-items")
noti_li_items = noti_wrapper.find_elements_by_tag_name("li")
noti_list = [ item for item in [ extract_notification(elem) for elem in noti_li_items ] if len(item["heading"]) > 0 ]
malespeaker.speak("Here are the notifications: ")

for noti in noti_list:
    malespeaker.speak(noti["heading"])


malespeaker.speak("You are signed in")

def getTweets():
    tweet_items = browser.find_elements_by_class_name('tweet')

for tweet_item in tweet_items:
    from_user = ""
    time = ""
    tweet_text = ""
    try:
        from_user = tweet_item.find_element_by_class_name('FullNameGroup').text.encode('utf-8')
        time = tweet_item.find_element_by_class_name('time').text.encode('utf-8').split('\n')[0]
        tweet_text = tweet_item.find_element_by_class_name('tweet-text').text.encode('utf-8')
        lang = tweet_text.get_attribute()
    except:
        from_user = ""
        time = ""
        tweet_text = ""

    malespeaker.speak(from_user + " tweeted " + time + " ago")
    malespeaker.speak(tweet_text)


def save_session():
    cookies = browser.get_cookies()
    pickel.dump(cookies, open("cookies.pkl", "wb"))
