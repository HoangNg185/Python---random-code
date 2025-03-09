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
