# pip install gtts(google text-to-speach)

from gtts import gTTS

import os

print("This is a ROBO SPEAKER...")

mytext=input("Enter your text here which you want to listen\n")

language='en'
output=gTTS(text=mytext,lang=language,slow=False)

output.save("myaudio.mp3")

os.system("start myaudio.mp3")

