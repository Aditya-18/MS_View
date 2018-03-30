from threading import Thread
from Queue import Queue
import malespeaker
import pythoncom
import textwrap
import win32com.client as wincl
MAX_WORDS = 5

def break_the_line(iterable, n = 1):
    current_batch = []
    print "inside iterable"
    for item in iterable:
        current_batch.append(item)
        if len(current_batch) == n:
            yield current_batch
            current_batch = []
    if current_batch:
        yield current_batch

class Speaker():
    def __init__(self):
        self.queue = Queue(maxsize=100)
        self.speaker = wincl.Dispatch("SAPI.SpVoice")
        self.thread = Thread(target=self.run)
        self.thread.start()

    def speak(self, text):
        words = text.split()
        self.stop()

        for line in break_the_line(words, MAX_WORDS):
            print "putting to queue", (' '.join(line))
            self.queue.put(' '.join(line))

    def stop(self):
        self.queue.queue.clear()

    def run(self):
        pythoncom.CoInitialize()
        while True:
            if self.queue.empty():
                continue

            text = self.queue.get()
            if len(text) > 0:
                self.speaker.speak(text)

            self.queue.task_done()

def tests():
    # This should interrupt the speaker in between speaking the first line
    lines = ["hi there, this is a long line to speak I am speaking to myself", "I hate interruptions"]
    speaker = Speaker()

    for line in lines:
        print "Speaking"
        speaker.speak(line)

speaker = Speaker()

if __name__ == "__main__":
    tests()
