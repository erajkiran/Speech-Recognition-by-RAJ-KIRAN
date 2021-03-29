import pyttsx3
import speech_recognition as sr
import webbrowser as wb

engine=pyttsx3.init()
engine.say("Good morning Raj, How Can I Help You")
engine.runAndWait()


safari_path='/Applications/Safari.app %s'

r=sr.Recognizer()

print("\t\t\t\t\t\t\t\t\t Raj's Personal ARTIFICIAL INTELLIGENCE Assistant \n")
with sr.Microphone() as source:
	print("Good morning Raj, How Can I Help You\n ")
	audio=r.listen(source)
	print("\t Done..! Processing your Speech")

try:
	text=r.recognize_google(audio)
	print("\n AI thinks you said : "+text)
	print("\n")
	wb.get(safari_path).open(text)

	engine.say(text)


except Exception as e:
	print(e)

