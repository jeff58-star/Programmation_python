# initialisation
from tkinter import *
import random
import time
from math import *

frame = Tk()
frame['bg'] = "blue"
frame.geometry("500x500")
frame.title("Devinez le nombre")
l = Label(text="Bienvenue dans mon jeu de devinette!!!", font=("Arial", 18))
l.place(x=20, y=50)
nombre3 = random.randint(1, 500)
nombre2 = random.randint(1, 250)
nombre1 = random.randint(1, 100)
va1 = log(100) / log(2)
va2 = log(250) / log(2)
va3 = log(500) / log(2)
print(nombre1)
print(nombre2)
print(nombre3)
i = 0


# démarrer
def startFunction():
    frame.destroy()
    frame2 = Tk()
    frame2.geometry("500x247")
    frame2.title("Bienvenue dans mon jeu de devinette")
    frame2['bg'] = "blue"
    l1 = Label(text="Choisissez un niveau", font=("Arial", 24), bd='8')
    l1.place(x=20, y=10)

    #
    def selection():
        selected = 'vous avez sélectionné' + " " + (Var1.get())
        label.config(text=selected)

        def print_answerrs():
            print("Selected Option: {}".format(var1.get()))
            return None

        submit_button = frame2.Button(frame2, text='Submit', command=print_answerrs)
        submit_button.pack()
        # selected='vous avez sélectionné'+" "+(Var1.get())
        # label.config(text=selected)

    # ouvrir une nouvelle fenêtre pour jouer

    def continuer():
        # 1èr niveau
        if Var1.get() == 'la déviniette entre 1 et 100':
            frame2.destroy()
            frame3 = Tk()
            frame3.geometry("500x300")
            frame3['bg'] = "blue"
            frame3.title("dévinette entre 1 et 100")

            # minuteur
            def horloge():
                try:
                    # the input provided by the user is
                    # stored in here :temp
                    temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
                except:
                    print("Please input the right value")
                while temp > -1:

                    # divmod(firstvalue = temp//60, secondvalue = temp%60)
                    mins, secs = divmod(temp, 60)

                    # Converting the input entered in mins or secs to hours,
                    # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                    # 50min: 0sec)
                    hours = 0
                    if mins > 60:
                        # divmod(firstvalue = temp//60, secondvalue
                        # = temp%60)
                        hours, mins = divmod(mins, 60)

                    # using format () method to store the value up to
                    # two decimal places
                    hour.set("{0:2d}".format(hours))
                    minute.set("{0:2d}".format(mins))
                    second.set("{0:2d}".format(secs))

                    # updating the GUI window after decrementing the
                    # temp value every time
                    frame3.update()
                    time.sleep(1)

                    # when temp value = 0; then a messagebox pop's up
                    # with a message:"Time's up"
                    if (temp == 0):
                        messagebox.showinfo("le compte à reboure est terminé", "fin \n ")

                    # after every one sec the value of temp will be decremented
                    # by one
                    temp -= 1

            hour = StringVar()
            minute = StringVar()
            second = StringVar()
            # setting the default value as 0
            hour.set("00")
            minute.set("00")
            second.set("30")
            # Use of Entry class to take input from the user
            hourEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                              textvariable=hour)
            hourEntry.place(x=300, y=50)

            minuteEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                                textvariable=minute)
            minuteEntry.place(x=350, y=50)

            secondEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                                textvariable=second)
            secondEntry.place(x=400, y=50)
            #
            lh = Label(frame3, text='Vous avez' + ' ' + str(hour.get()) + ' ' + ' heures ' + str(
                minute.get()) + ' ' + '  minutes et ' + ' ' + str(second.get()) + ' ' + 'secondes',
                       fg='red', bg='blue', font=("Helvetica", 8))
            lh.place(x=250, y=5)
            # button widget
            btn = Button(frame3, text='Démarer le compte', font=("Arial", 12), bd='3', bg="red", fg='white',
                         command=horloge)
            btn.place(x=300, y=120)

            sai_nomb = Label(frame3, text='saisir votre nombre', font=('time new rom', 12), bd='5', bg='grey',
                             fg='black').place(x=50, y=10)
            ent_nomb = Entry(frame3, font=('time new roman', 12), bg='lightgrey')
            ent_nomb.place(x=50, y=60)
            tit_res = Label(frame3, text='Resultat', font=('time new rom', 12), bg='grey',
                            fg='black').place(x=100, y=100)
            result = Entry(frame3, font=('time new roman', 12), bg='lightgrey')
            result.place(x=50, y=150)

            def app_dev():
                result.delete(0, END)
                global i
                while i < va1:
                    i = i + 1
                    if int(ent_nomb.get()) == nombre1:
                        frame3.destroy()
                        frame4 = Tk()
                        frame4['bg'] = "blue"
                        frame4.geometry("500x247")
                        frame4.title("Bravo!!! vous avez trouvez le nombre mystère")
                        tit_res = Label(frame4, text='Hourra!! Vous avez trouvé le resultat en' + ' ' + str(
                            i) + ' ' + 'itérative', font=('time new rom', 12), bg='grey',
                                        fg='green').place(x=100, y=100)
                        btn_quit = Button(frame4, text="QUITTER !", width=13, height=2, command=quit)
                        btn_quit.place(x=200, y=200)
                    elif int(ent_nomb.get()) > nombre1:
                        result.insert(END, 'mystére est plus petit\n')
                        ent_nomb.delete(0, END)
                    else:
                        int(ent_nomb.get()) < nombre1
                        result.insert(END, 'mystère est plus grand\n')
                        ent_nomb.delete(0, END)
                    break
                else:
                    frame3.destroy()
                    frame4 = Tk()
                    frame4['bg'] = "blue"
                    frame4.geometry("500x247")
                    frame4.title("Echec")
                    tit_res = Label(frame4, text='Domage! Vous n avez pas pu déviner' + ' ' + str(nombre1),
                                    font=('time new rom', 12),
                                    bg='grey',
                                    fg='white').place(x=100, y=100)
                    btn_quit = Button(frame4, text="QUITTER !", fg="red", bg="red", width=13, height=2, command=quit)
                    btn_quit.place(x=200, y=200)

            bout2 = Button(text="entrer", width=12, height=2, command=app_dev)
            bout2.place(x=300, y=200)
            btn_quit = Button(frame3, text="QUITTER !", fg="white", bg="red", width=13, height=2, command=quit)
            btn_quit.place(x=100, y=200)
        # deuxième niveau
        elif Var1.get() == 'la dévinette entre 1 et 250':
            frame2.destroy()
            frame3 = Tk()
            frame3['bg'] = "blue"
            frame3.geometry("500x247")
            frame3.title("dévinette entre 1 et 250")

            # %#
            def horloge():
                try:
                    # the input provided by the user is
                    # stored in here :temp
                    temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
                except:
                    print("Please input the right value")
                while temp > -1:

                    # divmod(firstvalue = temp//60, secondvalue = temp%60)
                    mins, secs = divmod(temp, 60)

                    # Converting the input entered in mins or secs to hours,
                    # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                    # 50min: 0sec)
                    hours = 0
                    if mins > 60:
                        # divmod(firstvalue = temp//60, secondvalue
                        # = temp%60)
                        hours, mins = divmod(mins, 60)

                    # using format () method to store the value up to
                    # two decimal places
                    hour.set("{0:2d}".format(hours))
                    minute.set("{0:2d}".format(mins))
                    second.set("{0:2d}".format(secs))

                    # updating the GUI window after decrementing the
                    # temp value every time
                    frame3.update()
                    time.sleep(1)

                    # when temp value = 0; then a messagebox pop's up
                    # with a message:"Time's up"
                    if (second.get() == 0):
                        messagebox.showinfo("le compte à reboure est terminé", "fin \n ")

                    # after every one sec the value of temp will be decremented
                    # by one
                    temp -= 1

            hour = StringVar()
            minute = StringVar()
            second = StringVar()
            # setting the default value as 0
            hour.set("00")
            minute.set("00")
            second.set("100")

            # Use of Entry class to take input from the user
            hourEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                              textvariable=hour)
            hourEntry.place(x=300, y=20)

            minuteEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                                textvariable=minute)
            minuteEntry.place(x=350, y=20)

            secondEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                                textvariable=second)
            secondEntry.place(x=400, y=20)

            lh = Label(frame3, text='Vous avez' + ' ' + str(hour.get()) + ' ' + ' heures ' + str(
                minute.get()) + ' ' + '  minutes et ' + ' ' + str(second.get()) + ' ' + 'secondes',
                       fg='red', bg='blue', font=("Helvetica", 8))
            lh.place(x=250, y=5)
            # button widget
            btn = Button(frame3, text='Démarer le compte', font=("Arial", 12), bd='3', bg="red", fg='white',
                         command=horloge)
            btn.place(x=300, y=120)
            # %#
            sai_nomb = Label(frame3, text='saisir votre nombre', font=('time new rom', 15), bg='grey',
                             fg='black').place(x=50, y=10)
            ent_nomb = Entry(frame3, font=('time new roman', 15), bg='lightgrey')
            ent_nomb.place(x=50, y=60)
            tit_res = Label(frame3, text='Resultat', font=('time new rom', 15), bg='grey',
                            fg='black').place(x=100, y=100)
            result = Entry(frame3, font=('time new roman', 15), bg='lightgrey')
            result.place(x=50, y=150)

            def app_dev():
                result.delete(0, END)
                global i
                while i < va2:
                    i = i + 1
                    if int(ent_nomb.get()) == nombre2:
                        frame3.destroy()
                        frame4 = Tk()
                        frame4.geometry("500x247")
                        frame4.title("Félicitation")
                        tit_res = Label(frame4, text='Vous avez trouvé le resultat en' + ' ' + str(i) + ' ''tentative',
                                        font=('time new rom', 15), bg='grey',
                                        fg='green').place(x=100, y=100)
                        btn_quit = Button(frame4, text="QUITTER !", fg="red", width=13, height=2, command=quit)
                        btn_quit.place(x=200, y=200)
                    elif int(ent_nomb.get()) > nombre2:
                        result.insert(END, 'mystère est plus petit\n')
                        ent_nomb.delete(0, END)
                    else:
                        int(ent_nomb.get()) < nombre2
                        result.insert(END, 'mystère est plus grand\n')
                        ent_nomb.delete(0, END)
                    break
                else:
                    frame3.destroy()
                    frame4 = Tk()
                    frame4['bg'] = "blue"
                    frame4.geometry("500x247")
                    frame4.title("Echec")
                    tit_res = Label(frame4, text='Domage! vous n avez pa pu déviner' + ' ' + str(nombre2),
                                    font=('time new rom', 15),
                                    bg='grey',
                                    fg='red').place(x=50, y=100)
                    btn_quit = Button(frame4, text="Fermer la fenêtre !", width=13, height=2, fg="white", bg="red",
                                      command=quit)
                    btn_quit.place(x=200, y=200)

            bout2 = Button(text="entrer", width=12,
                           height=2, font=('Arial', 10), bg="green", bd='3', command=app_dev)
            bout2.place(x=300, y=200)
            btn_quit = Button(frame3, text="Fermer la fenêtre !", width=13, height=2, command=quit)
            btn_quit.place(x=100, y=200)
        # 3ème niveau
        elif Var1.get() == 'la dévinette entre 1 et 500 ':
            frame2.destroy()
            frame3 = Tk()
            frame3.geometry("500x247")
            frame3.title("dévinette entre 1 et 500")

            # %#
            def horloge():
                try:
                    # the input provided by the user is
                    # stored in here :temp
                    temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
                except:
                    print("Please input the right value")
                while temp > -1:

                    # divmod(firstvalue = temp//60, secondvalue = temp%60)
                    mins, secs = divmod(temp, 60)

                    # Converting the input entered in mins or secs to hours,
                    # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                    # 50min: 0sec)
                    hours = 0
                    if mins > 60:
                        # divmod(firstvalue = temp//60, secondvalue
                        # = temp%60)
                        hours, mins = divmod(mins, 60)

                    # using format () method to store the value up to
                    # two decimal places
                    hour.set("{0:2d}".format(hours))
                    minute.set("{0:2d}".format(mins))
                    second.set("{0:2d}".format(secs))

                    # updating the GUI window after decrementing the
                    # temp value every time
                    frame3.update()
                    time.sleep(1)

                    # when temp value = 0; then a messagebox pop's up
                    # with a message:"Time's up"
                    if (temp == 0):
                        messagebox.showinfo("le compte à reboure est terminé", "fin \n ")

                    # after every one sec the value of temp will be decremented
                    # by one
                    temp -= 1

            hour = StringVar()
            minute = StringVar()
            second = StringVar()
            # setting the default value as 0
            hour.set("00")
            minute.set("00")
            second.set("100")
            # Use of Entry class to take input from the user
            hourEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                              textvariable=hour)
            hourEntry.place(x=300, y=20)

            minuteEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                                textvariable=minute)
            minuteEntry.place(x=350, y=20)

            secondEntry = Entry(frame3, width=3, font=("Arial", 12), bd='3', bg="black", fg='white',
                                textvariable=second)
            secondEntry.place(x=400, y=20)

            lh = Label(frame3, text='Vous avez' + ' ' + str(hour.get()) + ' ' + ' heures ' + str(
                minute.get()) + ' ' + '  minutes et ' + ' ' + str(second.get()) + ' ' + 'secondes',
                       fg='red', bg='blue', font=("Helvetica", 8))
            lh.place(x=250, y=5)

            # button widget
            btn = Button(frame3, text='Démarer le compte', font=("Arial", 12), bd='3', bg="red", fg='white',
                         command=horloge)
            btn.place(x=300, y=120)
            # %#
            frame3['bg'] = "blue"
            sai_nomb = Label(frame3, text='saisir votre nombre', font=('time new rom', 15), bg='grey',
                             fg='black').place(x=50, y=10)
            ent_nomb = Entry(frame3, font=('time new roman', 15), bg='lightgrey')
            ent_nomb.place(x=50, y=60)
            tit_res = Label(frame3, text='Resultat', font=('time new rom', 15), bg='grey',
                            fg='black').place(x=50, y=100)
            result = Entry(frame3, font=('time new roman', 15), bg='lightgrey')
            result.place(x=50, y=150)

            def app_dev():
                result.delete(0, END)
                global i
                while i < va3:
                    i = i + 1
                    if int(ent_nomb.get()) == nombre3:
                        frame3.destroy()
                        frame4 = Tk()
                        frame4.geometry("500x247")
                        frame4.title("Félicitation")
                        frame4['bg'] = "blue"
                        tit_res = Label(frame4, text='Hourra!! Vous avez trouvé le resultat en' + ' ' + str(
                            i) + ' ' + 'tentative',
                                        font=('time new rom', 15), bg='grey',
                                        fg='green', bd='5').place(x=50, y=100)
                        btn_quit = Button(frame4, text="Fermer la fenêtre !", width=13, height=2, bd='5', command=quit)
                        btn_quit.place(x=200, y=200)
                    elif int(ent_nomb.get()) > nombre3:
                        result.insert(END, 'mystère est plus petit\n')
                        ent_nomb.delete(0, END)
                    else:
                        int(ent_nomb.get()) < nombre3
                        result.insert(END, 'mystère est plus grand \n')
                        ent_nomb.delete(0, END)
                    break
                else:
                    frame3.destroy()
                    frame4 = Tk()
                    frame4['bg'] = "blue"
                    frame4.geometry("500x247")
                    frame4.title("Echec")
                    tit_res = Label(frame4, text='Domage! Vous n avez pas pu dévinez' + ' ' + str(nombre3),
                                    font=('time new rom', 15),
                                    bg='grey',
                                    fg='white').place(x=50, y=100)
                    btn_quit = Button(frame4, text="Fermer la fenêtre !", width=13, height=2, command=quit)
                    btn_quit.place(x=200, y=200)

            bout2 = Button(text="entrer", width=12, height=2, command=app_dev)
            bout2.place(x=300, y=200)
            btn_quit = Button(frame3, text="Fermer la fenêtre !", width=13, height=2, command=quit)
            btn_quit.place(x=100, y=200)

    frame2.geometry("500x247")
    frame2['bg'] = "blue"
    bout2 = Button(text="Démarrer", width=12, height=2, bg="black", fg="green", font=('Arial', 10), bd='4',
                   command=continuer)
    bout2.place(x=300, y=200)
    btn_quit = Button(frame2, text="Fermer la fenêtre !", width=13, height=2, bg="red", fg="white", font=('Arial', 10),
                      bd='4', command=quit)
    btn_quit.place(x=100, y=200)
    Var1 = StringVar()
    niveau = ['Niveau 1', 'Niveau 2', 'Niveau 3']
    valeur = ['la déviniette entre 1 et 100', 'la dévinette entre 1 et 250', 'la dévinette entre 1 et 500 ']
    for i in range(3):
        bout = Radiobutton(text=niveau[i], value=valeur[i], variable=Var1, font=('Arial', 10), bd='4',
                           command=selection)
        bout.pack(side=LEFT, padx=7)
        label = Label(frame2)
        label.place(x=100, y=150)


# demarrage du jeu
b1 = Button(text="Démarrer", width=12, height=2, bg="black", fg="green", bd='8', command=startFunction)
b1.place(x=160, y=110)
frame.geometry("500x247")
frame.mainloop()