from tkinter import *
from transliteration import transliterate
from mlmorph import Analyser


def stem(word):
    try:
        return Analyser().analyse(word)[0][0].split('<')[0]
    except IndexError as e:
        return "Unable to stem"


class MyApp:
    def __init__(self, parent):        
        self.myParent = parent 
        self.myParent.geometry("640x500")
        
        # Our topmost frame is called myContainer
        self.myContainer = Frame(parent)
        self.myContainer.pack()
        self.myContainer.pack(expand=1, fill='both')

        # We will use HORIZONTAL (left/right) orientation inside myContainer.
        # Inside myContainer1, we create top_frame and bottom_frame.

        # top frame
        self.top_frame = Frame(self.myContainer, height=200)
        self.top_frame.pack(side='top', fill='x')  ###

        # bottom frame
        self.bottom_frame = Frame(self.myContainer, borderwidth=5,  relief=RIDGE, height=200, bg="cyan")
        self.bottom_frame.pack(side='top', fill='x')
                
        # inside top_frame we create a textbox         
        self.eng_text = Text(self.top_frame)
        self.eng_text.pack()
        self.eng_text.bind("<Key>", self.translate) ### (2)        
       
        # inside bottom_frame we create a textbox         
        self.mal_text = Text(self.bottom_frame)
        self.mal_text.pack()
            
    def translate(self, event):
        if event.keysym in ('space', 'Return'):
            mang = str(self.eng_text.get(0.0, END)).strip()
            #print(f"'{mang}'")
            str_res=''
            for w in mang.split():
                t = transliterate(w)
                try:
                    str_res += f"{t} -> {stem(t)}\n"

                except ValueError:
                    str_res += f"{t} -> Unable to stem\n"
            self.mal_text.delete(0.0, END)
            self.mal_text.insert(0.0, str_res)



