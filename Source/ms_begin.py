import os
import malespeaker
import random
# import time
from datetime import datetime
import transcribe
import queryHandlers

def main():
    """
       Greets the user.
       Checks when the system was last updated.
       Checks if there are reminders.
       Waits for user input.
       If input is "bye" (or similar), quits.
       Else passes the user input to the function msview() stored in msview.py
    """
    # greetings_path = os.path.dirname(os.getcwd()) + "/Text_Files/greetings.txt"
    # f_greetings = open(greetings_path, "r")
    # greetings_list = f_greetings.read().strip().split("\n")
    # f_greetings.close()
    # random_greeting = random.randrange(0, len(greetings_list))
    malespeaker.speak("Hello Sir!")

    # bye_path = os.path.dirname(os.getcwd()) + "/Text_Files/bye.txt"
    # f_bye = open(bye_path, "r")
    # bye_list = f_bye.read().strip().split("\n")
    # f_bye.close()
    # bye_list2 = [''.join(bye_list[i])+" Shrimp" for i in range(0, len(bye_list))]
    # bye_list3 = [''.join(bye_list[i])+" Mantis" for i in range(0, len(bye_list))]
    # bye_list4 = [''.join(bye_list[i]) + " MS" for i in range(0, len(bye_list))]
    while 1:
        malespeaker.speak("How can I help You?")
        voice_query = transcribe.transcribe_file();
        # voice_query = input('\033[1m'+'Username: '+'\033[0m')  # modify
        # print (voice_query)
        if voice_query:
            voice_query = voice_query.lower()
            # if voice_query in bye_list or \
                # voice_query in bye_list2 or \
                # voice_query in bye_list3 or \
                # voice_query in bye_list4:
            if "bye" in voice_query or "nothanks" in voice_query or "no thanks" in voice_query:
                time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if int(time_now[11:13]) > 20 or int(time_now[11:13]) < 4:
                    malespeaker.speak("Goodnight.")
                else:
                    malespeaker.speak('See you later then! Have a good day!')
                return
            queryHandlers.get(voice_query)


if __name__ == '__main__':
    main()