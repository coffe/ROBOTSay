#-*-coding:utf-8-*-
import os, time

os.system("clear")
print ("R.O.B.O.T - jag pratar, alltså finns jag!?")

#startar en loop


try:
    def robot(text):
        os.system("espeak -v swedish ' " + text + " ' ")

except:
    print ("Det verkar som om du inte har * espeak * installerat på din dator?")
    quit()

time.sleep(1)

robot("Hallå")
     
time.sleep(1)

while True:

    robot ("Vad vill du att jag ska säga? ")

    text = raw_input ("Vad vill du att jag ska säga? ")
    str(text)

    if text == "quit":
        break

    robot (text)

    time.sleep(1)

print ("Hejdå")
