import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from gtts import gTTS
import subprocess
import speech_recognition as sr
import pyaudio
import socket
import time
import win32api
import database
from PIL import Image, ImageTk
import webbrowser
from audioplayer import AudioPlayer



########################################################################################################################




class Window3(tk.Tk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("1980x1080")
        self.title("תוכנה")
        self.entry1 = tk.Text(width=150, font=("Ariel", 12, "bold"))
        self.entry1.place(x=200, y=255, height=150)
########################################################################################################################
        self.my_menu = Menu(tearoff=False)
        self.my_menu.add_command(label="פתיחת סרטון ההמרה",command=self.open2,accelerator="Ctrl+O")
        self.my_menu.add_command(label="פתיחת מסמך ההמרה",command=self.open,accelerator="Ctrl+A")
        self.my_menu.add_command(label="הדבק",command=lambda:self.entry1.event_generate('<Control v>'),accelerator="Ctrl+V")
        self.my_menu.add_command(label="פותר בעיות",accelerator="Ctrl+H",command=self.help)
        self.my_menu.add_separator()
        self.my_menu.add_command(label="שלח דואר",command=self.send_mail,accelerator="F5")
        self.my_menu.add_command(label="יציאה", command=self.destroy,accelerator="Ctrl+Q")

        self.bind("<Button-3>",self.my_poup)
        self.bindkeys()

#######################################################################################################################
        self.frame = tk.Frame(self, width=700, height=250, highlightbackground="black", highlightthickness=10)
        #self.frame.place(x=250, y=200)
        self.frame2 = tk.Frame(self, width=700, height=300, highlightbackground="black", highlightthickness=10)
        #self.frame2.place(x=250, y=500)
        self.show_edit1 = tk.BooleanVar()
        self.show_edit1.set(True)










        self.show_edit2 = tk.BooleanVar()
        self.show_edit2.set(True)

        self.my_menu2 = Menu(tearoff=False)
        self.file = Menu(self.my_menu2, tearoff=False)
        self.edit = Menu(self.my_menu2, tearoff=False)
        self.view = Menu(self.my_menu2, tearoff=False)
        self.help_1 = Menu(self.my_menu2, tearoff=False)
        self.link = Menu(self.my_menu2, tearoff=False)
        self.file.add_command(label="פתיחת סרטון ההמרה",command=self.open2,accelerator="Ctrl+O")
        self.file.add_command(label="פתיחת מסמך ההמרה", command=self.open,accelerator="Ctrl+A")
        self.file.add_command(label="יציאה", command=lambda *args:self.destroy(),accelerator="Ctrl+Q")
        self.edit.add_command(label="היסטוריה",command=self.history)




        self.view.add_radiobutton(label="כתום",command=self.orange,value="First opiton")
        self.view.add_radiobutton(label="שחור",command=self.black,value="Second opiton")
        self.view.add_radiobutton(label="סגול",command=self.purple,value="Third option")
        self.view.add_radiobutton(label="אדום",command=self.red,value=4)
        self.view.add_radiobutton(label="לבן",command=self.white,value=5)
        self.view.add_radiobutton(label="כחול",command=self.blue,value=6)
        self.view.add_radiobutton(label="ירוק",command=self.grin,value=7)
        self.view.add_radiobutton(label="ברירת מחדל", command=self.SystemButtonFace, value=8)


        self.help_1.add_command(label="פותר בעיות",accelerator="Ctrl+H",command=self.help)
        self.help_1.add_command(label="שלח דואר",accelerator="F5",command=self.send_mail)

        self.link.add_command(label="דרך האיימיל",command=self.send_email2)
        self.link.add_command(label="דרך יוטיוב", command=self.send_youtube)


        self.my_menu2.add_cascade(label="פתח",menu=self.file)
        self.my_menu2.add_cascade(label="הצג",menu=self.edit)
        self.my_menu2.add_cascade(label="רקע",menu=self.view)
        self.my_menu2.add_cascade(label="מתקדם",menu=self.help_1)
        self.my_menu2.add_cascade(label="שיתוף",menu=self.link)

########################################################################################################################



        self.label1 = tk.Label(text="המרת טקסט לדיבור ולהפך",font=("Ariel",30,"bold"),fg="#414169")
        self.label1.grid(padx=800,pady=100)
        self.label2 = tk.Label(text="הכנס טקסט",font=("Ariel",20,"bold"),fg="#414169")
        self.label2.place(x=1600,y=300)


        self.label5 = tk.Label(text="הקלט קול", font=("Ariel", 20, "bold"),fg="#414169")
        self.label5.place(x=1500, y=650)
        self.label6 = tk.Label(text="גודל ההמרה\n בדקות", font=("Ariel", 20, "bold"),fg="#414169")
        self.label6.place(x=1500, y=770)
        self.label7 = tk.Label(text="שפה", font=("Ariel", 20, "bold"), fg="#414169")
        self.label7.place(x=435, y=830)







        self.open_sound = Image.open("images\\sound.gif")
        self.photo_image = ImageTk.PhotoImage(self.open_sound)
        self.label18 = tk.Label(self,font=("Ariel", 15, "bold"), fg="#414169",image=self.photo_image)
        self.label18.image = self.photo_image
        self.label18.place(x=200,y=630,height=100,width=1100)







        self.scrollbar = ttk.Scrollbar(self,command=self.entry1.yview)
        self.scrollbar.place(height=150,x=185,y=255)
        self.entry1["yscrollcommand"] = self.scrollbar.set


        self.button3 = tk.Button(text="המר",command=self.convert_abc,font=("Ariel",15,"bold"),fg="#414169")
        self.button3.place(x=800,y=420,width=300,height=50)
        image_spekear = Image.open("images\\spe.png")
        photo_spekear = ImageTk.PhotoImage(image_spekear)
        self.button6 = tk.Button(image=photo_spekear,command=lambda :AudioPlayer("example5.mp3").play(block=True))
        self.button6.image = photo_spekear
        self.button6.place(x=700,y=420,width=32,height=32)

        self.button5 = tk.Button(text="המר", font=("Ariel", 15, "bold"),fg="#414169",command= self.convert_text)
        self.button5.place(x=800, y=850, width=300, height=50)
        textvar2 = tk.StringVar()

        leng = ["עברית","אנגלית"]
        self.spinbox = tk.Spinbox(values=leng, font=("Ariel",30))

        self.spinbox.place(x=400,y=900,height=70,width=150)
        self.spinbox["state"] = "readonly"



        self.variable = tk.IntVar()







        self.scale_button = ttk.LabeledScale(variable=self.variable,borderwidth=3)
        self.scale_button.place(x=200,y=750,width=1000)




        ########################################################################################################################


        self.config(menu=self.my_menu2)



    def send_email2(self):
        win32api.ShellExecute(0, 'open', 'mailto:', None, None, 0)

    def send_youtube(self):
        webbrowser.open('https://studio.youtube.com')



    ########################################################################################################################
    def my_poup(self,e):
        self.my_menu.tk_popup(e.x_root, e.y_root)

    def convert_abc(self,*args):
        with open("hystory.txt","a") as his:
            his.write("!המרת בטקסט")
            his.write("\n")

        mytext2 = self.entry1.get(1.0, "end")
        try:
            if mytext2.strip() == "":
                messagebox.showerror("","לא הכנסת טקסט")
            elif self.spinbox.get() == "עברית":
                self.audio1 = gTTS(text=mytext2, lang="iw", slow=False)
                self.audio1.save("example5.mp3")
                AudioPlayer("example5.mp3").play(block=True)








            elif self.spinbox.get() == "אנגלית":
                self.audio2 = gTTS(text=mytext2, lang="en", slow=False)
                self.audio2.save("example5.mp3")
                AudioPlayer("example5.mp3").play(block=True)









        except Exception as e:
            print(e)
            messagebox.showerror("המרת טקסט","אין אינטרנט התחבר לאינטרנט ונסה שוב")









    def orange(self):
        self.config(bg="orange")
        self.label1.config(bg="orange",fg="brown")
        self.label2.config(bg="orange",fg="brown")


        self.label5.config(bg="orange",fg="brown")
        self.label6.config(bg="orange",fg="brown")



        self.button3.config(bg="orange",activebackground="orange",fg="brown",activeforeground="brown")

        self.button5.config(bg="orange",activebackground="orange",fg="brown",activeforeground="brown")

        self.label18.config(bg="orange",fg="brown")
        self.scale_button.configure(borderwidth=1)
        self.label7.config(bg="orange", fg="brown")






    def black(self):
        self.config(bg="black")
        self.label1.config(bg="black",fg="white")
        self.label2.config(bg="black",fg="white")


        self.label5.config(bg="black",fg="white")
        self.label6.config(bg="black",fg="white")


        self.frame.config(bg="white")
        self.frame2.config(bg="white")


        self.button3.config(bg="black",fg="white",activebackground="black",activeforeground="white")

        self.button5.config(bg="black",fg="white",activebackground="black",activeforeground="white")

        self.label18.config(bg="black",fg="white")
        self.scale_button.configure(borderwidth=1)
        self.label7.config(bg="black", fg="black")


    def purple(self):
        self.config(bg="purple")
        self.label1.config(bg="purple",fg="white")
        self.label2.config(bg="purple",fg="white")


        self.label5.config(bg="purple",fg="white")
        self.label6.config(bg="purple",fg="white")



        self.button3.config(bg="purple",fg="white",activebackground="purple",activeforeground="white")

        self.button5.config(bg="purple",fg="white",activebackground="purple",activeforeground="white")

        self.label18.config(bg="purple",fg="white")
        self.scale_button.configure(borderwidth=1)
        self.label7.config(bg="purple", fg="black")


    def red(self):
        self.config(bg="red")
        self.label1.config(bg="red",fg="white")
        self.label2.config(bg="red",fg="white")


        self.label5.config(bg="red",fg="white")
        self.label6.config(bg="red",fg="white")



        self.button3.config(bg="red",fg="white",activebackground="red",activeforeground="white")

        self.button5.config(bg="red",fg="white",activebackground="red",activeforeground="white")

        self.label18.config(bg="red",fg="white")
        self.scale_button.configure(borderwidth=1)
        self.label7.config(bg="red", fg="black")


    def white(self):
        self.config(bg="white")
        self.label1.config(bg="white",fg="black")
        self.label2.config(bg="white",fg="black")


        self.label5.config(bg="white",fg="black")
        self.label6.config(bg="white",fg="black")


        self.button3.config(bg="white",fg="black",activebackground="white",activeforeground="black")

        self.button5.config(bg="white",fg="black",activebackground="white",activeforeground="black")

        self.label18.config(bg="white",fg="black")
        self.scale_button.configure(borderwidth=1)
        self.label7.config(bg="white", fg="black")




    def blue(self):
        self.config(bg="Azure")
        self.label1.config(bg="Azure",fg="black")
        self.label2.config(bg="Azure",fg="black")


        self.label5.config(bg="Azure",fg="black")
        self.label6.config(bg="Azure",fg="black")


        self.button3.config(bg="Azure",fg="black",activebackground="Azure",activeforeground="black")

        self.button5.config(bg="Azure",fg="black",activebackground="Azure",activeforeground="black")

        self.label18.config(bg="Azure",fg="black")
        self.scale_button.configure(borderwidth=1)
        self.label7.config(bg="Azure", fg="black")



    def grin(self):
        self.config(bg="#40E0D0")
        self.label1.config(bg="#40E0D0",fg="black")
        self.label2.config(bg="#40E0D0",fg="black")


        self.label5.config(bg="#40E0D0",fg="black")
        self.label6.config(bg="#40E0D0",fg="black")



        self.button3.config(bg="#40E0D0",fg="black",activebackground="#40E0D0",activeforeground="black")
        self.button5.config(bg="#40E0D0", fg="black", activebackground="#40E0D0", activeforeground="black")



        self.label18.config(bg="#40E0D0",fg="black")

        self.label7.config(bg="#40E0D0", fg="black")


    def SystemButtonFace(self):
        self.config(bg="SystemButtonFace")
        self.label1.config(bg="SystemButtonFace", fg="black")
        self.label2.config(bg="SystemButtonFace", fg="black")

        self.label5.config(bg="SystemButtonFace", fg="black")
        self.label6.config(bg="SystemButtonFace", fg="black")

        self.button3.config(bg="SystemButtonFace", fg="black", activebackground="SystemButtonFace", activeforeground="black")
        self.button5.config(bg="SystemButtonFace", fg="black", activebackground="SystemButtonFace", activeforeground="black")

        self.label18.config(bg="SystemButtonFace", fg="black")

        self.label7.config(bg="SystemButtonFace", fg="black")





    def history(self):
        try:
            with open("hystory.txt", "r") as file:
                read = file.read().splitlines()
                line = [line.strip() for line in read]
        except FileNotFoundError:
            pass




        new = Toplevel(self)
        new.geometry("500x500")
        new.title("היסטוריה")
        new.resizable(False,False)

        column = "המרה"
        records = ttk.Treeview(new,columns=column,show="headings")
        records.place(x=0,y=0,height=500,width=500)
        records.heading("המרה", text="המרה")
        for record in line:
            records.insert("", "end", values=(record,))









    def convert_text(self):
        with open("hystory.txt","a") as his:
            his.write("!המרת בקול")
            his.write("\n")

        try:
            with open("example.txt","w") as w:
                pass
        except FileNotFoundError:
            pass

        get1 = self.variable.get()

        init_rec = sr.Recognizer()
        try:
            if get1 == 0:
                messagebox.showerror("קול","בחרת אפס שניות")
            else:

                with sr.Microphone() as source:


                    audio_data = init_rec.record(source, duration=get1*20)

                    if self.spinbox.get() == "עברית":
                        text = init_rec.recognize_google(audio_data, language="iw")

                    elif self.spinbox.get() == "אנגלית":
                        text = init_rec.recognize_google(audio_data, language="en")

                self.new2 = Toplevel(self)
                self.new2.geometry("700x500+500+250")
                self.new2.title("הטקסט")
                self.new2.resizable(False,False)

                self.my_menu3 = Menu(self.new2,tearoff=False)
                self.my_menu3.add_command(label="העתק",command=self.copy,accelerator="Ctrl+C")
                self.my_menu3.add_command(label="הדבק",command=lambda :self.text2.event_generate("<Control v>"),accelerator="Ctrl+V")
                self.my_menu3.add_separator()
                self.my_menu3.add_command(label="יציאה",command=lambda *args:self.new2.destroy(),accelerator="Ctrl+Q")


                self.text2 = tk.Text(self.new2,font=("Ariel",20,"bold"))
                self.text2.place(x=0,y=0,width=700,height=500)
                self.text2.delete(1.0, "end")
                self.text2.insert(1.0,text)

                file1 =  open("example.txt","a")
                file1.write(text)
                file1.close()

                self.new2.bind("<Control-q>", lambda *args:self.new2.destroy())
                self.new2.bind("<Button-3>", self.my_poup2)
                self.new2.mainloop()


        except Exception as e:
            mbox = messagebox.askretrycancel("קול שגיאה!","התוכנה לא קלטה את המיקרופון שלך\n לנסות שנית או להפסיק")

            if mbox is True:
                try:
                    with sr.Microphone() as source:
                        audio_data2 = init_rec.record(source, duration=get1*20)

                        if self.spinbox.get() == "עברית":
                            text = init_rec.recognize_google(audio_data2, language="iw")

                        elif self.spinbox.get() == "אנגלית":
                            text = init_rec.recognize_google(audio_data2, language="en")

                    self.text2.delete(1.0, "end")
                    self.text2.insert(1.0,text)
                    file =  open("example.txt", "a")
                    file.write(text)
                    file.close()

                except Exception:
                    messagebox.showerror("קול שגיאה","התוכנה לא הצליחה לקלוט קול מהמיקרופון שלך\n בדוק אותו ולאחר מכן נסה שנית")


            else:
                pass

    def open(self,*args):
        try:
            subprocess.call("example.txt",shell=True)
        except FileNotFoundError:
            messagebox.showerror("פתיחה","לא המרת כלום ולכן אין מסמך לפתיחה")


    def open2(self,*args):
        subprocess.call("example5.mp3",shell=True)


    def my_poup2(self,e):
        self.my_menu3.tk_popup(e.x_root, e.y_root)





    def help(self=None,*args):

        def help2():
            for x in range(7):
                my_label.config(text=my_progres["value"])
                my_progres["value"] += 15
                root.update_idletasks()
                time.sleep(1)
            my_progres.stop()
            mylabel2 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel2.place(x=450, y=250)
            mylabel3 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel3.place(x=150, y=300)
            mylabel4 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel4.place(x=10, y=350)
            mylabel5 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel5.place(x=10, y=400)
            mylabel6 = tk.Label(root, font=("Ariel", 15, "bold"), bg="white")
            mylabel6.place(x=250, y=450)
            if str(self.entry1.get(1.0, "end")).strip() == "":
                mylabel2.config(text="!לא הכנסת טקסט להמרה", fg="red")
            else:
                mylabel2.config(text="בסדר הכנסת טקסט להמרה", fg="blue")

            IPaddress = socket.gethostbyname(socket.gethostname())
            if IPaddress == "127.0.0.1":
                mylabel3.config(text=" !אינך מחובר לאינטרנט", fg="red")

            else:
                mylabel3.config(text=f" בסדר אתה מחובר לאינטרנט עם הכתובת הזו {IPaddress}", fg="blue")
            try:
                file = open("example.txt")
                file.close()
                mylabel4.config(text="בסדר הצלחנו לפתוח את מסמך ההמרה", fg="blue")
            except FileNotFoundError:
                mylabel4.config(text="לא הצלחנו לפתוח את מסמך ההמרה אם ניסית להמיר בקול בדוק את המיקרופון שלך",
                                fg="red")
            try:
                file = open("example5.mp3")
                file.close()
                mylabel5.config(text="בסדר הצלחנו לפתוח את סרטון ההמרה", fg="blue")
            except FileNotFoundError:
                mylabel5.config(text="לא הצלחנו לפתוח את סרטון ההמרה אם ניסית להמיר בדוק את חיבור האינטרנט שלך",
                                fg="red")
            if str(self.entry1.get(1.0, "end")).strip() != "" and IPaddress != "127.0.0.1" and open("example.txt") and open("example5.mp3"):
                mylabel6.config(text="!!!ואו הכל בסדר לא הצלחנו למצוא בעיות",fg="blue")

        def stop():
            my_progres.stop()
            root.destroy()

        root = Toplevel(self)
        root.geometry("700x500+500+100")
        root.title("פותר בעיות")
        root.resizable(False, False)

        root.configure(bg="white")

        label = tk.Label(root, text="פתרון בעיות", font=("Ariel", 20, "bold"), bg="white")
        label.place(x=300, y=70)

        my_progres = ttk.Progressbar(root, orient="horizontal",
                                     length=350, mode="determinate")
        my_progres.place(x=190, y=130)

        my_button = ttk.Button(root, text="התחל",command=help2)
        my_button.place(x=450, y=160)
        my_button2 = ttk.Button(root, text="ביטול",command=stop)
        my_button2.place(x=200, y=160)

        my_label = tk.Label(root, text="", bg="white")
        my_label.place(x=350, y=160)
        my_label2 = tk.Label(root, text="", bg="white")
        my_label2.place(x=450, y=250)

        root.mainloop()




    def copy(self):
        self.new2.clipboard_clear()
        self.clipboard_append(self.text2.get(1.0,"end"))







    def send_mail(self,*args):
        win32api.ShellExecute(0, 'open', 'mailto:ymb6143@gmail.com', None, None, 0)



    def bindkeys(self,*args):
        self.bind("<Control-o>", self.open2)
        self.bind("<Control-a>", self.open)
        self.bind("<Control-q>",lambda *args:self.destroy())
        self.bind("<Control-h>",self.help)
        self.bind("<KeyPress-F5>",self.send_mail)

        
        








########################################################################################################################





#######################################################################################################################
















class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("הרשמה")
        self.geometry("800x600+500+200")
        self.resizable(False, False)





########################################################################################################################
        container = tk.Frame(width=800,height=600,bg="white")
        container.pack()
########################################################################################################################
        label1 = tk.Label(container,text="הרשמה למערכת",font=("Ariel",30,"bold"),fg="#414169",bg="white")
        label1.place(x=300,y=70)
        label2 = tk.Label(container,text="הכנס את שמך",font=("Ariel", 20, "bold"),fg="#414169",bg="white")
        label2.place(x=500,y=200)
        label3 = tk.Label(container, text="הכנס את סיסמתך", font=("Ariel", 20, "bold"), fg="#414169", bg="white")
        label3.place(x=500, y=270)
        label4 = tk.Label(container, text="הכנס שוב את סיסמתך", font=("Ariel", 20, "bold"), fg="#414169", bg="white")
        label4.place(x=500, y=340)
        label5 = tk.Label(container, text="הכנס שם זיהוי", font=("Ariel", 20, "bold"), fg="#414169", bg="white")
        label5.place(x=500, y=410)
########################################################################################################################
        self.entry1 = ttk.Entry(container,width=35)
        self.entry1.place(x=250,y=210,height=30)
        self.entry2 = ttk.Entry(container, width=35)
        self.entry2.place(x=250, y=280, height=30)
        self.entry3 = ttk.Entry(container, width=35)
        self.entry3.place(x=250, y=350, height=30)
        self.entry4 = ttk.Entry(container, width=35)
        self.entry4.place(x=250, y=420, height=30)
########################################################################################################################
        button1 = tk.Button(container,text="התחבר",font=("Ariel",20,"bold"),fg="#414169",bg="white",width=10, command=self.login2)
        button1.place(x=440,y=490)
        button2 = tk.Button(container, text="הרשם", font=("Ariel", 20, "bold"),fg="#414169", bg="white", width=10,command=self.signup)
        button2.place(x=220, y=490)
########################################################################################################################

    def signup(self):
        database.create_table()
        get1 = self.entry1.get()
        get2 = self.entry2.get()
        get3 = self.entry3.get()
        get4 = self.entry4.get()

        if len(get1) < 5:
            messagebox.showerror("","הכנס שם משתמש גדול יותר")
        elif len(get2) < 8:
            messagebox.showerror("","הכנס סיסמה ארוכה יותר")
        elif get2 != get3:
            messagebox.showerror("","הסיסמאות אינן תואמות")
        elif len(get4) < 5:
            messagebox.showerror("","הכנס שם זיהוי גדול יותר")
        else:
            database.add(get4,get1,get2)
            messagebox.showinfo("","!נרשמת בהצלחה")


    def login2(self):
        self.destroy()
        root3 = Window2()
        root3.mainloop()






########################################################################################################################


########################################################################################################################




is_on2 = True


########################################################################################################################
class Window2(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600+500+200")
        self.title("התחברות")
        self.resizable(False, False)
        with open("name and password.txt", "a"):
            pass
########################################################################################################################
        container = tk.Frame(self,width=800,height=600,bg="white")
        container.pack()
        self.image_on = PhotoImage(file="images\\eye.png")
        self.image_off = PhotoImage(file="images\\eye_clese.png")
########################################################################################################################
        label1 = tk.Label(container,text="התחברות למערכת",font=("Ariel",30,"bold"),bg="white",fg="#414169")
        label1.place(x=300,y=70)
        label2 = tk.Label(container, text="הכנס שם משתמש", font=("Ariel", 20, "bold"), bg="white", fg="#414169")
        label2.place(x=500, y=200)
        label3 = tk.Label(container, text="הכנס סיסמה", font=("Ariel", 20, "bold"), bg="white", fg="#414169")
        label3.place(x=500, y=270)
        label4 = tk.Label(container, text="הכנס את המספר 5713", font=("Ariel", 20, "bold"), bg="white", fg="#414169")
        label4.place(x=500, y=340)
        label5 = tk.Label(container, text="כדי לוודא שאתה לא רובוט", font=("Ariel", 12, "bold"), bg="white", fg="#414169")
        label5.place(x=550, y=380)
########################################################################################################################
        self.textvar = tk.StringVar()
        self.textvar2 = tk.StringVar()
        self.entry1 = ttk.Entry(container, width=35, textvariable=self.textvar)
        self.entry1.place(x=250, y=210, height=30)
        self.entry2 = ttk.Entry(container, width=35,show="*", textvariable=self.textvar2)
        self.entry2.place(x=250, y=280, height=30)
        self.entry3 = ttk.Entry(container, width=35)
        self.entry3.place(x=250, y=350, height=30)
########################################################################################################################
        self.check = tk.IntVar()
        self.check.set(True)
        self.check2 = tk.IntVar()


        button1 = tk.Button(container, text="התחבר", font=("Ariel", 20, "bold"),fg="#414169", bg="white", width=10,command=self.login)
        button1.place(x=440, y=490)
        button2 = tk.Button(container, text="הרשם", font=("Ariel", 20, "bold"),fg="#414169", bg="white", width=10,command=self.signup2)
        button2.place(x=220, y=490)
        button3 = ttk.Checkbutton(container,onvalue=True,offvalue=1,variable=self.check,text="שמור סיסמה ושם משתמש לפעם הבאה\n או מחק סיסמה שמורה")
        button3.place(x=250,y=405)
        self.button4 = ttk.Checkbutton(container,onvalue=1,offvalue=False,variable=self.check2,text="הראה סיסמה שמורה",command=self.show)
        self.button4.place(x=250, y=450)
        self.button5 = tk.Button(container,image=self.image_off,command=self.show_entry)
        self.button5.place(x=195,y=280)

        fileopen1 =  open('name and password.txt')
        fileopen = [line.strip() for line in fileopen1.read()]
        fileopen1.close()
        if fileopen == list():
            self.button4["state"] = "disabled"

    def login(self):
        get1 = self.entry1.get()
        get2 = self.entry2.get()
        get3 = self.entry3.get()

        login = database.login(get1,get2)


        if not login:
            messagebox.showerror("", "שם משתמש או סיסמה לא חוקיים")
        elif get3 != "5713":
            messagebox.showerror("","קוד אימות לא נכון")
        elif login:
            messagebox.showinfo("", "התחברת בהצלחה")
            self.destroy()
            root1 = Window3()
            root1.mainloop()



        if self.check.get() == 1:
            with open("name and password.txt","r+") as a:
                b = [line.strip() for line in a.read()]
                if b == list():
                    a.write(self.textvar.get())
                    a.write("\n")
                    a.write(self.textvar2.get())
                else:
                    pass

        elif self.check.get() == 0:
            with open("name and password.txt","w") as w:
                pass


    def signup2(self):
        self.destroy()
        root = Window()
        root.mainloop()



    def show(self):

        fileopen1 =  open('name and password.txt')
        fileopen = [line.strip() for line in fileopen1]
        fileopen1.close()

        if self.check2.get() == 1:
            self.entry1.insert(0,fileopen[0])
            self.entry2.insert(0,fileopen[1])
        elif self.check2.get() == 0:
            self.entry1.delete(0,"end")
            self.entry2.delete(0,"end")




    def show_entry(self):
        global is_on2

        if is_on2:
            self.button5.config(image=self.image_on)
            self.entry2.config(show="")
            is_on2 = False
        else:
            self.button5.config(image=self.image_off)
            self.entry2.config(show="*")
            is_on2 = True







root1 = Window2()
root1.mainloop()





########################################################################################################################


