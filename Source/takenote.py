import pyautogui
import subprocess
import malespeaker
import transcribe
import time

def notedown(q):
	malespeaker.speak("Please tell me note you want to write")
	tobenoted = transcribe.transcribe_file()
	subprocess.Popen("C:\Windows\System32\\notepad.exe", shell=True)
	time.sleep(2)
	pyautogui.click(250, 250);
	pyautogui.typewrite(tobenoted,0.02)
	pyautogui.hotkey('ctrl', 's')
	pyautogui.typewrite('note1.txt')
	time.sleep(1)
	pyautogui.press('enter')
	pyautogui.press('left')
	pyautogui.press('enter')
	malespeaker.speak("Your note has been saved successfully to note1.txt in documents")

if __name__ == '__main__':
	notedown("Hello world")
