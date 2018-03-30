from selenium import webdriver
import malespeaker

browser = None

def init():
    global browser
    browser = webdriver.Chrome()
    browser.maximize_window()

def close():
    if browser:
        browser.close()

init()

browser.get("http://google.com")
form = browser.find_element_by_tag_name('form')

url = "https://www.google.co.in/search?q=how+not+to+go+crazy"

if(form):
    role = form.get_attribute('role')
    malespeaker.speak("I have found a form on this page")
    if(role):
        malespeaker.speak("The role the form is " + role)

    malespeaker.speak("would you like to fill this form?")


all_input_boxes = form.find_elements_by_tag_name('input')
input_boxes = []
for input_box in all_input_boxes:
    if(input_box.get_attribute('type') == 'text' and input_box.get_attribute('name')):
        input_boxes.append(input_box)

if(len(input_boxes)):
    malespeaker.speak("The form requires some text information to be filled")
    for input_box in input_boxes:
        placeholder = input_box.get_attribute('placeholder')
        if(not placeholder):
            placeholder = input_box.get_attribute('title')

        malespeaker.speak("What should I write in")
        malespeaker.speak(input_box.get_attribute('title'))

        # get input from user
        input_box.send_keys('how not to go crazy')

form.submit()
