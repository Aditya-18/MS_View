from threading import Thread
import malespeaker
import pythoncom
import textwrap
import win32com.client as wincl
MAX_WORDS = 5

def break_the_line(iterable, n = 1):
    current_batch = []
    for item in iterable:
        current_batch.append(item)
        if len(current_batch) == n:
            yield current_batch
            current_batch = []
    if current_batch:
        yield current_batch

class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0,item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Speaker():
    def __init__(self):
        self.queue = Queue()
        self.speaker = wincl.Dispatch("SAPI.SpVoice")
        self.thread = Thread(target=self.run)
        self.thread.start()

    def speak(self, text):
        words = text.split()

        self.stop()
        for line in break_the_line(words, MAX_WORDS):
            #print("putting", ' '.join(line))
            self.queue.put(' '.join(line))

    def stop(self):
        self.queue = Queue()

    def run(self):
        pythoncom.CoInitialize()
        while True:
            if self.queue.empty():
                continue

            text = self.queue.get()
            #print("speaking", text)
            if len(text) > 0:
                self.speaker.speak(text)

def tests():
    # This should interrupt the speaker in between speaking the first line
    lines = ["hi there, this is a long line to speak I am speaking to myself", "I hate interruptions"]
    speaker = Speaker()

    for line in lines:
        speaker.speak(line)

speaker = Speaker()

if __name__ == "__main__":
    tests()
