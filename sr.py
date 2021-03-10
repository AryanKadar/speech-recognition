import speech_recognition as sr
import webbrowser as wy
global l2
from tkinter import *
root=Tk()
root.title("SRecognition")
root.geometry("500x300")
root.resizable(width=False, height=False)
p=PhotoImage(file="mic.png")
l2=Label(root,text="",fg="black")
l2.place(x=215,y=200)
l1=Label(root,image=p,bg="white",width=235,height=167)
l1.place(x=140,y=0)
def spr():
	r1=sr.Recognizer()
	url='https://www.google.com/search?q='
	url2='&rlz=1C1SQJL_enIN857IN857&oq=python&aqs=chrome..69i57j35i39l2j69i60l5.4395j0j7&sourceid=chrome&ie=UTF-8'
	with sr.Microphone() as jj:
		r1.adjust_for_ambient_noise(jj,duration=0.5)
		au=r1.listen(jj)
	l1=Label(root,image=p,bg="white",width=235,height=167).place(x=140,y=0)
	try:
		at=r1.recognize_google(au)
		l2=Label(root,text=at,fg="black",width=70,height=1)
		l2.place(x=0,y=200)
		wy.get().open_new(url+at+url2)
	
	
	except sr.UnknownValueError:
		l2=Label(root,text="Unable to recognize",fg="red",width=70,height=1)
		l2.place(x=0,y=200)
		root.mainloop()
	except sr.RequestError as e:
		l2=Label(root,text="FAILED",fg="red",width=70,height=1)
		l2.place(x=0,y=200)
		root.mainloop()

def create(l1):
	l1.pack_forget()
	l1=Label(root,image=p,bg="red",width=235,height=167).place(x=140,y=0)
	l2=Label(root,text="SPEAK",fg="red",width=70,height=1)
	l2.place(x=0,y=200)
	root.after(100,spr)
	root.mainloop()
from PIL import Image
img = Image.open("mic1.png")
new_width  = 40
new_height = 40
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save("mic2.png")	
p1=PhotoImage(file="mic2.png")
Button(root,image=p1,command=lambda: [create(l1)]).place(x=220,y=230)
root.mainloop()