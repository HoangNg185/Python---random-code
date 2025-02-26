import wave

import pyaudio
import speech_recognition as sr

# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
AUDIO_FILENAME = "enregistrement.wav"
TEXT_FILENAME = "transcription.txt"

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Enregistrement en cours... Parlez maintenant.")
frames = []

# Record audio
for _ in range(int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Enregistrement terminé.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recording as a WAV file
with wave.open(AUDIO_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Fichier audio enregistré sous {AUDIO_FILENAME}")

# Convert speech to text
recognizer = sr.Recognizer()
with sr.AudioFile(AUDIO_FILENAME) as source:
    print("Transcription en cours...")
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        print("Texte transcrit:", text)

        # Save to text file
        with open(TEXT_FILENAME, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)

        print(f"Transcription enregistrée sous {TEXT_FILENAME}")

    except sr.UnknownValueError:
        print("Impossible de reconnaître la parole.")
    except sr.RequestError:
        print("Erreur de connexion à l'API de reconnaissance vocale.")
