import os

from gtts import gTTS

lang = 'en'
text = 'harry do u have that $100 that i can borrow'

speech = gTTS(text=text, lang=lang, slow=False, tld='com.au')

speech.save('speechfile.mp3')
os.system('start speechfile.mp3')
