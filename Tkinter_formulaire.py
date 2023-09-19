# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 00:57:44 2022

@author: DELL
"""

import tkinter
from tkinter import ttk
from tkcalendar import *

from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            birth  = birth_date_date.get()
            Sex= Sex_combobox.get()
            # Course info
            registration_status = reg_status_var.get()
            duration_ENSAE = numdate_spinbox .get()
            
            
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality,"birth: ", birth,"Sex: ", Sex)
            print("# duration_ENSAE: ", duration_ENSAE)
            print("Registration status", registration_status)
            print("------------------------------------------")
            
            # Create Table
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            table = '''CREATE TABLE IF NOT EXISTS Student_Data \
                (firstname TEXT, lastname TEXT, title TEXT, age INT, \
                 nationality TEXT, birth TEXT,Sex TEXT , \
                     registration_status TEXT, duration_ENSAE INT)'''
            cur.execute(table)
            
            # Insert Data
            data_inf= '''INSERT INTO Student_Data (firstname, lastname, title,age,\
                nationality,birth,Sex, registration_status,duration_ENSAE) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
            # data_insert_tuple = (firstname, lastname, title,\
            #                      age, nationality,birth,Sex, registration_status, duration_ENSAE)
            
            cur.execute(data_inf, (firstname, lastname, title,age,nationality,birth,Sex, registration_status, duration_ENSAE))
            conn.commit()
            conn.close()

            
                
         # Reset form
            reset_data()
            tkinter.messagebox.showinfo(title="Success", message="Data successfully saved!")
            
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")
        
def reset_data():
    # Clear all form data
    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    title_combobox.set('')
    age_spinbox.delete(0, 'end')
    nationality_combobox.set('')
    birth_date_date.set_date(None)
    Sex_combobox.set('')
    reg_status_var.set('Not registered')
    numdate_spinbox.delete(0, 'end')
    
def quit():
    window.destroy()
        

window = tkinter.Tk()
window.title("Formulaire d'inscription")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="Personal Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Togolese", "Senegalese", "Southern Africa", "Egypt", "Marroco", "Ghanaian ", "Algeria"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

birth_date_label = tkinter.Label(user_info_frame, text="birth_date")
birth_date_date = DateEntry(user_info_frame,state='readonly',date_pattern="dd\mm\yy")
birth_date_label.grid(row=2, column=2)
birth_date_date.grid(row=3, column=2)

Sex_label = tkinter.Label(user_info_frame, text="Sex")
Sex_combobox = ttk.Combobox(user_info_frame, values=[" ","Male", "Female"])
Sex_label.grid(row=4, column=0)
Sex_combobox.grid(row=5, column=0)



for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Info_site
Ensae_Info_frame = tkinter.LabelFrame(frame,text="Knowledge of ENSAE")
Ensae_Info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(Ensae_Info_frame, text="# Website registred status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(Ensae_Info_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=1)
registered_check.grid(row=1, column=1)

numdate_label = tkinter.Label(Ensae_Info_frame, text= " # Duration of Knowledge at ENSAE (Months)")
numdate_spinbox = tkinter.Spinbox(Ensae_Info_frame, from_=0, to='infinity')
numdate_label.grid(row=0, column=3)
numdate_spinbox.grid(row=1, column=3)

for widget in Ensae_Info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept that these information are mine and can be considered as real.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)


##Boutons 
button1 = tkinter.Button(frame, text="Submit", command=enter_data)
button1.grid(row=3, column=0, padx=40, pady=50, sticky="w")

button2 = tkinter.Button(frame, text="Reset", command=reset_data)
button2.grid(row=3, column=0, padx=200, pady=50, sticky="w")

button3 = tkinter.Button(frame, text="Quit", command=quit)
button3.grid(row=3, column=0, padx=120, pady=50, sticky="e")


#soumission

 
window.mainloop()