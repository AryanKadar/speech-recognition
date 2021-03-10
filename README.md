# speech-recognition
speech_recognition using python
Hello everyone 
	
	1.Here is my another project about Recognising the words spoken from person and also search for that word 
on google search engine.
	2.Basically it takes audio input from your mic that forms audio file and extract data from that file as Audiodata
and feed that to recognize_google method (API) of instance of Recognizer class where all the magic happens for converting speech 
into readable text.
	3.After converting that into readable text, this program search for that word on google.
	4.The program overcome one major problem of reducing noise of environment so that in loud environment it can still recognize , But
this program has it limitation for detection of human speech from noisy envoirnment,Has this program wait for few seconds after taking input 
from mic so has to confirm that the person is done with his words.
	5.So if there is continuous noise without break then it may or may not recognize.


How to excecute:
	1.Save the file and all image in one folder and then execute in python enviornment 
	by typing "python sr.py",then click on mic button and speak any thing you would like to search on google.
