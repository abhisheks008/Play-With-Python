from tkinter import *
import speech_recognition as aa
import pyttsx3

root = Tk()
root.title('Speech to Text')
root.geometry('500x500')

def action():
    status['text'] = "Listening..."
    listener = aa.Recognizer()
    
    # check microphone is working or not
    try : 
        #using microphone
        with aa.Microphone() as origin:
            # speech_output['text'] = "Listening"
            print("Listening...")
            speech = listener.listen(origin)
            #recognise the voice and convert into text
            instruction = listener.recognize_google(speech)
    except :
        pass
    
    status['text'] = " "
    speech_output['text'] = instruction

label = Label(root, text="Speech to Text Converter",font=("Arial", 20) )
label.pack()
status = Label(root, text=" ", font=("Arial", 10))
status.pack()
button = Button(root, text="Talk", command=action, font=("Arial", 12))
button.pack()
speech_output = Label(text="", font=("Arial", 16))
speech_output.pack()


root.mainloop()
