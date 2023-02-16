import speech_recognition as sr

class AudioToText: 

    def __init__(self, audio):      
        r = sr.Recognizer()
        with sr.AudioFile(audio) as source:  
            audio_text = r.listen(source)        
            try:           
                text = r.recognize_google(audio_text, language = "pt-BR")
                print('convertendo audio para texto ...')
                print(text)            
            except:
                print('Desculpe.. execute novamente...')
# tem que ser wav
i = 1
while (i <=1):
  audio = AudioToText("audio"+str(i)+".wav")
  i = i  + 1