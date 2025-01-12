from gtts import gTTS


def text_to_speech(txt_file_path, output_audio_file):
    try:
        # Read the text from the file
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Convert text to speech
        tts = gTTS(text, lang='en')

        # Save the audio file
        tts.save(output_audio_file)
        print(f"Audio file saved as {output_audio_file}")

    except FileNotFoundError:
        print(f"Error: The file {txt_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# File paths
txt_file_path = 'example.txt'  # Replace with your .txt file path
output_audio_file = 'output.mp3'  # Output audio file name

# Convert text to speech
text_to_speech('Outputs/PDF_output_gambler_3.txt', 'Outputs/output_voice_gambler_3.mp3')
