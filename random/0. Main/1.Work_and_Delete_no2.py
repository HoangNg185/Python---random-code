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

'''
<span class="ryNqvb"
jsname="W297wb"
jsaction="click:PDNqTc,GFf3ac,qlVvte;contextmenu:Nqw7Te,QP7LD;
mouseout:Nqw7Te;
mouseover:PDNqTc,c2aHje">
pas maintenant et</span>
'''
# if the word has space, replace it with '%20'
# https://translate.google.ca/?sl=en&tl=fr-CA&text=not%20now%20%26amp%3B&op=translate       :eng to francais
# https://translate.google.ca/?sl=fr-CA&tl=en&text=pas%20maintenant%20et&op=translate       :francais to eng
# ---------------->
# https://www.google.com/search?sca_esv=1a2a07081c7891bb&rlz=1C1CHBF_enCA967CA967&sxsrf=AHTn8zqamyzpZJZ8iFkouYZJQMYqyRe4rQ:1741158915743&q=lentilles&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBsxayPSIAqObp_AgjkUGqengxVrJ7hrmYmz7X2OZp_NIYfhIAjPnSJLO3GH6L0gKvsMx863yWAECACzcq28K_xbJJoPcSEvdLSYBoilrVRznyvhgudvug19AweeEbrCGkt1-WOOEb9EGKHZMjwGgxB85lVM932Nv9pb4lgel1ps0RGcIKA&sa=X&ved=2ahUKEwiPnK61svKLAxVyvokEHTjYFOIQtKgLegQIERAB&biw=1920&bih=953&dpr=1
# https://www.google.com/search?sca_esv=1a2a07081c7891bb&rlz=1C1CHBF_enCA967CA967&sxsrf=AHTn8zrOQXwrDpH7yLXhmp7KGMOHHz4cgg:1741158847691&q=broccoli&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBsxayPSIAqObp_AgjkUGqekYoUzDaOcDDjQfK4KpR2OIJg0p8GjEafhVsU6UZNT2tUhHTA_XMhcunRVhbh9fJ-E_NpOwc0V4M-pxQ-VRkNVBLtVA39i8pg8uW6jlEtLtrbdNHgWLD-vHAmoqmNrKak2sYhiqpsjYUvt_8vhjtkMNrZWABg&sa=X&ved=2ahUKEwjkzvSUsvKLAxVDkokEHZqEKRUQtKgLegQIExAB&biw=1920&bih=953&dpr=1
import speech_recognition as sr


def compare_spoken_word(target_word):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(f"🎙️ Please say: {target_word}")
        audio = recognizer.listen(source)

        try:
            # Convert speech to text (language='fr-FR' for French recognition)
            spoken_word = recognizer.recognize_google(audio, language='fr-FR')
            print(f"✅ You said: {spoken_word}")

            if spoken_word.lower() == target_word.lower():
                print("🎉 Correct!")
            else:
                print(f"❌ Incorrect! Expected: {target_word}, but you said: {spoken_word}")

        except sr.UnknownValueError:
            print("❓ Couldn't understand your voice.")
        except sr.RequestError as e:
            print(f"🚨 Could not request results; {e}")


# Example usage

'''
href='https://www.wsj.com/business/autos/tesla-elon-musk-consumer-backlash-19326a57?mod=hp_lead_pos7'
data outplay style: visual-eleven
class: css-1h3cyqz

first: .css-qkw8fy
second: .css-11tsx9c
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Cut off first half
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next  # Store next pointers
            first.next = second  # Merge node from second half
            second.next = temp1  # Connect back to first half
            first, second = temp1, temp2  # Move to next pair


# Example Usage
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(head)
sol = Solution()
sol.reorderList(head)
print_list(head)  # Output: 1 -> 5 -> 2 -> 4 -> 3 -> None
