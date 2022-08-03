import string
import random
import tkinter as tk

#this program was created by DarguzTV
#YT: https://www.youtube.com/channel/UC78TLhhkBfVHEG3Nrt0CFNQ
#Git Hub: https://github.com/DarguzTV

class Application(object):

    def __init__(self, f):

        self.pwlungh = tk.IntVar()
        self.finestra = f

        self.welcome = tk.Label(f, text="Welcome", background="gray", font="Times 17 bold")
        self.welcome.pack(side="top")
        self.welcome.configure(foreground="blue")

        self.istructions = tk.Label(f, text="Insert password langth", background="gray", font="Arial 14")
        self.istructions.pack(side="top", pady="15")

        self.input_lungh = tk.Entry(f, cursor="hand2", text="4", textvariable=self.pwlungh)
        self.input_lungh.pack(side="top", pady="5", ipady="10", ipadx="20")
        self.input_lungh.configure(justify=tk.CENTER)
        self.input_lungh.bind("<ButtonPress-1>", self.deletelungh())

        self.generabutton = tk.Button(f, text="Generate", command=lambda:[self.switch(), self.generate()])
        self.generabutton.pack(side="top", pady="5", ipady="10", ipadx="20")

        self.scritta1 = tk.Label(f, text="Your password has been generated", background="gray", foreground="light green", font="Times 20")

        self.pwout = tk.Entry(f, text="", cursor="hand1", background="gray", show="")
        self.pwout.config(justify=tk.CENTER, font="arial 20")

        self.buuttoncopy = tk.Button(f, text="Copy", command=self.copy)

        self.buttonregenerate = tk.Button(f, text="←", background="gray", foreground="black", font="arial 12 bold", command=lambda:[self.returnto(), self.deletepwout()])

        self.valore = tk.StringVar()
        self.buttonshow = tk.Checkbutton(f, text="Hide", onvalue="on", offvalue="off", variable=self.valore, command=self.show)
        self.buttonshow.deselect()
        
        self.credits = tk.Label(f, text="Created by DarguzTV", foreground="blue", bg="gray", font="times 12")
        self.credits.place(x="150", y="270")

        self.statuscopyed = tk.Label(f, text="", foreground="red", background="gray")

    def switch(self):
        self.welcome.pack_forget()
        self.istructions.pack_forget()
        self.input_lungh.pack_forget()
        self.generabutton.pack_forget()
    
        self.scritta1.pack(side="top", pady="5")
        self.pwout.pack(side="left", padx="30", ipadx="70", ipady="35")
        self.buttonshow.place(x="35", y="90")
        self.buuttoncopy.place(x="322", y="90")
        self.statuscopyed.place(x="270", y="92")
        
        self.buttonregenerate.place(x="1", y="270")

    def generate(self):
        
        car = str('''ABCDEFGHIKLMNOPQRSTUVXYZabcdefghiklmnopqrstuvxyz%&-?!''')
        pw = ""

        lunghezza = self.pwlungh.get()
        
        for i in range(lunghezza):
            if (random.randint(1, 10) % 2 == 0): 
                pw = pw + random.choice(car)
            else:
                pw = pw + random.choice(string.digits)
        
        self.pwout.insert(0, pw)
        
    def returnto(self):

        self.scritta1.pack_forget()
        self.pwout.pack_forget()
        self.buttonshow.place_forget()
        self.buuttoncopy.place_forget()
        self.statuscopyed.place_forget()

        self.welcome.pack(side="top")
        self.istructions.pack(side="top", pady="15")
        self.input_lungh.pack(side="top", pady="5", ipady="10", ipadx="20")
        self.input_lungh.configure(justify=tk.CENTER)
        self.input_lungh.bind("<ButtonPress-1>", self.deletelungh())
        self.generabutton.pack(side="top", pady="5", ipady="10", ipadx="20")

        self.statuscopyed.config(text="")
        
    def deletepwout(self):
        self.pwout.delete(0, 99999)
    
    def deletelungh(self):
        self.input_lungh.delete(0, 99999)

    def copy(self):
        self.finestra.clipboard_clear()
        self.finestra.clipboard_append(self.pwout.get())
        self.statuscopyed.config(text="copiato!")

    def show(self):
        if self.valore.get() == "on":
            self.pwout.config(show="*")
            self.buttonshow.config(text="Show")
        else:
            self.pwout.config(show="")
            self.buttonshow.config(text="Hide")

def main():
    f = tk.Tk()
    f.title("Password generator")
    f.geometry("400x300")
    f.configure(bg="gray")
    mysoftware = Application(f)
    f.mainloop()

if __name__=='__main__':
    main()