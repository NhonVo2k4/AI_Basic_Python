import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

	
robot_brain = ""
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()

while True :
	with speech_recognition.Microphone() as mic:
		print("Robot: Trợ lý xinh đẹp nghe ^.^")
		audio = robot_ear.listen(mic)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	print("You: " + you)

	if you == "":
		robot_brain = "I don't known"
	elif "hello" in you :
		robot_brain = "Hello DarkDream"
	elif "date" in you :
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now() 
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you :
		robot_brain = "Bye"
		print("Robot_brain: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else :
		robot_brain = "I'm fine thank you and you"

	print("Robot_brain: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()