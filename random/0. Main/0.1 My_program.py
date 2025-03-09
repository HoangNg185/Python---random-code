def program_1_Français():
    import wave
    import pyaudio
    import speech_recognition as sr
    # Audio settings
    FORMAT = pyaudio.paInt16  # 16-bit audio format
    CHANNELS = 1  # Mono
    RATE = 44100  # 44.1 kHz sample rate
    CHUNK = 1024  # Buffer size
    RECORD_SECONDS = 5  # Length of recording

    AUDIO_FILENAME = "enregistrement.wav"  # Recorded file
    TEXT_FILENAME = "transcription.txt"  # Transcribed text file

    # 1️⃣ RECORD VOICE
    def record_voice():
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)

        print("🎤 Enregistrement... Parlez maintenant !")

        frames = []
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("✅ Enregistrement terminé.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        with wave.open(AUDIO_FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

    # 2️⃣ TRANSCRIBE VOICE TO TEXT
    def transcribe_voice():
        recognizer = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILENAME) as source:
            print("📝 Transcription en cours...")
            audio_data = recognizer.record(source)

            try:
                # Use Google Speech Recognition (set to French)
                text = recognizer.recognize_google(audio_data, language="fr-FR")
                print(f"🗣️ Transcription : {text}")

                # Save text to file
                with open(TEXT_FILENAME, 'w', encoding='utf-8') as file:
                    file.write(text)

                print(f"✅ Transcription enregistrée dans '{TEXT_FILENAME}'")

            except sr.UnknownValueError:
                print("❌ Impossible de comprendre l'audio.")
            except sr.RequestError as e:
                print(f"❌ Erreur de service : {e}")

    # Run the whole process
    record_voice()
    transcribe_voice()
def program_2_english():
    from datetime import datetime
    import speech_recognition
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
def generate_QR_code(link):
    from tkinter import Tk, Text, Button, filedialog, Label
    import qrcode
    from PIL import ImageTk

    def SaveFile():
        file = filedialog.asksaveasfile(defaultextension='.png', filetypes=[('PNG file', '*.png')])
        if file is not None:
            img.save(file.name)

    def generate_qr_code(link):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img

    window = Tk()
    window.title("QR Code Generator")

    # link = 'https://www.wsj.com/us-news/law/jim-justice-debt-west-virginia-senate-3668d28b?mod=hp_lead_pos8'
    img = generate_qr_code(link)
    img = ImageTk.PhotoImage(img)

    text = Text(window)
    text.pack()
    button = Button(window, text='Save QR Code', command=SaveFile)
    button.pack()
    qr_label = Label(window, image=img)
    qr_label.pack()

    window.mainloop()
def WSJ_to_My_profile(message=''):
    import pandas as pd
    df = pd.read_csv('WSJ.csv')
    print(f'    <p class="date">{message}</p>')
    print(f'    <ul class="link">')
    for i in df.index:
        title = df.loc[i, 'title']
        link = df.loc[i, 'link']

        print(f'        <li><a href="{link}" target="_blank">{title}</a></li>')
    print(f'    </ul>')
def consider_1():
    import calendar

    # Mapping month names in French to numbers
    mois_francais = {
        "janvier": 1,
        "février": 2,
        "mars": 3,
        "avril": 4,
        "mai": 5,
        "juin": 6,
        "juillet": 7,
        "août": 8,
        "septembre": 9,
        "octobre": 10,
        "novembre": 11,
        "décembre": 12
    }

    # Mapping days of the week to numbers (Monday = 1)
    jours_semaine = {
        "lundi": 1,
        "mardi": 2,
        "mercredi": 3,
        "jeudi": 4,
        "vendredi": 5,
        "samedi": 6,
        "dimanche": 7
    }

    # Function to ask for a valid date in French
    def demander_date():
        while True:
            date_str = input("Entrez une date complète en français (ex: 01 mars 2025) : ").strip().lower()

            # Split into parts
            try:
                jour, mois, annee = date_str.split()
                jour = int(jour)
                annee = int(annee)

                if mois not in mois_francais:
                    raise ValueError("Mois invalide.")

                mois_num = mois_francais[mois]

                # Check if the date is valid (e.g., no 31 février)
                calendar.monthrange(annee, mois_num)  # This will raise an error if month/year combo is invalid

                return jour, mois, annee, mois_num

            except (ValueError, KeyError):
                print("❌ Date invalide. Essayez encore avec le format '26 février 2025'.")

    # Function to find day of the week (in French)
    def trouver_jour_semaine(jour, mois_num, annee):
        jour_semaine_index = calendar.weekday(annee, mois_num, jour)  # 0 = Monday, 6 = Sunday
        jours_ordre = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
        jour_semaine_nom = jours_ordre[jour_semaine_index]
        return jour_semaine_nom, jours_semaine[jour_semaine_nom]

    # Main program
    jour, mois, annee, mois_num = demander_date()

    # Find day of the week
    jour_semaine_nom, jour_semaine_num = trouver_jour_semaine(jour, mois_num, annee)

    # Output result
    print(f"✅ Date saisie : {jour} {mois} {annee}")
    print(f"📆 Ce jour est : {jour_semaine_nom.capitalize()} (jour numéro {jour_semaine_num})")
    print(f"📅 Mois numéro : {mois_num}")
    print(f"📅 Année : {annee}")
def quelle_heuer_est_il():
    import random

    hour = random.randint(0, 24)
    minute = random.randint(0, 60)
    print(f'le temps est {hour:02}:{minute:02}\nil est ___ heures ___')
    for _ in range(0, 3):
        numéro = random.randint(0, 100)
        print(f'Vos chiffres sont: {numéro}')
    print('le (premier/ deuxième/ troisième) numéro est ___')
def change_file_names_to_number(link):
    import os
    num = 0
    for a, _, c in os.walk(link):
        for file in c:
            old_path = os.path.join(a, file)
            extension = os.path.splitext(file)[1]
            num += 1
            new_name = f'{num}{extension}'
            new_path = os.path.join(a, new_name)
            print(f'Changes from {old_path} ------{new_path}')
            os.rename(old_path, new_path)
def open_image_by_number(num):
    folder = 'C:\\Users\\Liam\\OneDrive - Seneca\\Pictures\\Saved Pictures'

    for root, _, files in os.walk(folder):
        for file in files:
            # Check if file starts with the number
            if file.startswith(f"{num}"):
                filepath = os.path.join(root, file)
                img = Image.open(filepath)
                img.show()
                return  # Stop after showing one match (optional)
# Donne-moi du vocabulaire pour les ___?
# -----------------------------------------------------------
from Vocabulaire import *
def download_images(search_query='Cat', num_images=5):
    import requests
    from PIL import Image
    from io import BytesIO
    from duckduckgo_search import DDGS
    with DDGS() as ddgs:
        results = ddgs.images(search_query, max_results=num_images, safesearch='off')

    if not results:
        print(f"No images found for: {search_query}")
        return

    for i, result in enumerate(results):
        url = result['image']
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            image = Image.open(BytesIO(response.content))

            filename = f"downloads\\{search_query.replace(' ', '_')}_{i + 1}.jpg"
            image.save(filename)

            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
def show_images(query='active dog', num_images=1, size="Medium", type_image="Photo", safe="off"):
    import requests
    from PIL import Image
    from io import BytesIO
    from duckduckgo_search import DDGS
    with DDGS() as ddgs:
        results = ddgs.images(
            query,
            max_results=num_images,
            size=size,
            type_image=type_image,
            safesearch=safe
        )

    if not results:
        print(f"No images found for: {query}")
        return

    for i, result in enumerate(results):
        url = result['image']
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            image = Image.open(BytesIO(response.content))

            # Directly display the image (without saving)
            image.show(title=f"{query} - {i + 1}")


        except Exception as e:
            print(f"Failed to fetch {url}: {e}")


def read_french_word(word):
    import os
    import pygame
    from gtts import gTTS
    # Generate the audio file
    tts = gTTS(text=word, lang='fr')
    tts.save("word.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("word.mp3")
    pygame.mixer.music.play()

    # Wait until the sound finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Stop and release the file
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # Now it's safe to delete the file
    os.remove("word.mp3")


# -----------------------------------------------------------
def read_and_image_from_list(your_list=legumes):
    a = -1
    while True:
        a += 1
        # word = random.choice(your_list)
        word = your_list[a]
        print(f'{a}:{your_list[a]}')
        read_french_word(word)
        # show_images(word)


read_and_image_from_list(les_formes)
