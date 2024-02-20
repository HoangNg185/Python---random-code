import speech_recognition
import pyttsx3

recog = speech_recognition.Recognizer()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recog.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recog.listen(mic)
            text = recog.recognize_google(audio,language='vi-VN')
            text = text.lower()
            print(f'Computer heard as: {text}')
    except speech_recognition.UnknownValueError:
        recog = speech_recognition.Recognizer()
        continue


