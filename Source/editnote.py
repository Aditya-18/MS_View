import pyautogui
import subprocess
import malespeaker
import transcribe
from time import sleep
from docx import Document
import os

def worddown(q):
	malespeaker.speak("Please tell me which document to edit")
	tobenoted = transcribe.transcribe_file()
	os.system('start "" winword.exe C:\\Users\\"Aditya Goel"\\Documents\\' + tobenoted + '.docx')
	doc= Document('C:\\Users\\Aditya Goel\\Documents\\hello.docx')
	wholedoc=""
	for para in doc.paragraphs:
		wholedoc = para.text
		malespeaker.speak(wholedoc)
	sleep(2)

if __name__ == '__main__':
	worddown("hello")
