import os
import time
# import faceverify
import malespeaker
def exec(q):
	if ("shut down" in q or "shutdown" in q or "log off" in q or "logoff" in q):
		malespeaker.speak("shutting down for you")
		os.system("shutdown /p")

	elif("restart" in q or "re start" in q):
		os.shutdown("restart /p")

	elif("none" in q):
		print("hello")



if __name__ == '__main__':
	exec("shut down")