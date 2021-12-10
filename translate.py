import speech_recognition as sr 
from google_trans_new import google_translator
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print('Listening...')
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source, timeout=1)
try:
    print('Recognizing...')
    result = r.recognize_google(audio, language='id')
except Exception as ex:
    print(ex)
    
def trans():
    langinput = input('Type the language code you want to translate:')
    translator = google_translator()
    translate_text = translator.translate(str(result), lang_tgt=str(langinput))
    print(translate_text)
    engine.say(str(translate_text))
    engine.runAndWait()
trans()