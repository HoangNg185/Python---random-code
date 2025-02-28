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


# -----------------------------------------------------------------------
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
