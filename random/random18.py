import speech_recognition
from datetime import datetime

recog = speech_recognition.Recognizer()

# Open file in 'a+' mode to append to existing content or create a new file if it doesn't exist
f = open('VoiceRecognition.txt', 'a+', encoding='utf-8')

try:
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recog.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recog.listen(mic)
                text = recog.recognize_google(audio)
                text = text.lower()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f'[{timestamp}] Computer heard as: {text}')
                # Write timestamp and recognized text to file
                f.write(f'[{timestamp}] {text}\n')
        except speech_recognition.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except KeyboardInterrupt:
            print("Exiting program.")
            break
finally:
    f.close()  # Make sure to close the file when done
