import speech_recognition as sr
import os
#pyaudio speechrecognition
r = sr.Recognizer()
def record_audio():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #audio=r.record(source,duration=7)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio,language="tr-tr")
            
        except sr.UnknownValueError:
            print("Üzgünüm ne dediğinizi anlamadım,program baştan başlatılıyor...")
            os.system("python3 main.py")

        except sr.RequestError:
            print("Sistemden kaynaklı bir hata var.")
        return voice_data

def respond(voice_data):
    if "ses" or "söz" or "a" or "seç" in voice_data:
        print("Merhaba :') ")


print("Merhaba,nasıl yardımcı olabilirim? ")
voice_data = record_audio()
#respond(voice_data)
print(voice_data)

