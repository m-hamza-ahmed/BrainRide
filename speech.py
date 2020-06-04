#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
'''
import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
mic=sr.Microphone(device_index=1)
PA_ALSA_PLUGHW=1
with mic as source:
    audio=r.listen(source)


def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('Google says {}'.format(message))
    engine.runAndWait()


print(r.recognize_google(audio))
speak(r.recognize_google(audio))
'''
import speech_recognition as sr
 
 
 
def main():
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
 
 
        # recognize speech using google
 
        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")
 
 
        except Exception as e:
            print("Error :  " + str(e))
 
 
 
 
        # write audio
 
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
 
 
if __name__ == "__main__":
    main()