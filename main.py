import  speech_recognition as siri
import pyttsx3

listener = siri.Recognizer()
engine = pyttsx3.init()
engine.say(" i am your alexa")
engine.say(" fuck me up")
engine.runAndWait()


def take_command():
  try:
    with siri.Microphone() as source:
        print("listening....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
           print(command)
  except:
    pass
  return command


def run():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        print(song)