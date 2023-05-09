from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

"""
with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
"""
from tkinter import * 
import tkinter.messagebox as tkMessageBox
#from win10toast import ToastNotifier
import tkinter as tk
from tkinter import ttk


root = Tk()
root.title("Python - Basic Register Form")
 
width = 1000
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


#=======================================VARIABLES=====================================
USER = StringVar()
NAME = StringVar()

#=======================================METHODS=======================================
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Register():   
    if USER.get == "" or  NAME.get() == "" :
        lbl_result.config(text="Please complete the required field!", fg="orange")
    else:
        lbl_result.config(text="It works!", fg="red")
        
        #toaster = ToastNotifier()
        #toaster.show_toast("Demo notification", "Hello world", duration=10)
        tkMessageBox.showinfo("Welcome to GFG.",  "Hi I'm your message")


#=====================================FRAMES====================================
TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)


#=====================================LABEL WIDGETS=============================
lbl_title = Label(TitleFrame, text="Posez votre question sur StackOverFlow", font=('arial', 18), bd=1, width=640)
lbl_title.pack()
lbl_username = Label(RegisterFrame, text="Titre:", font=('arial', 18), bd=18)
lbl_username.grid(row=1)

lbl_firstname = Label(RegisterFrame, text="Question:", font=('arial', 18), bd=18)
lbl_firstname.grid(row=2)

lbl_tags = Label(RegisterFrame, text="Choisissez des Tags:", font=('arial', 18), bd=18)
lbl_tags.grid(row=3)

lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=5, columnspan=2)

#=======================================ENTRY WIDGETS===========================
user = Entry(RegisterFrame, font=('arial',18), textvariable=USER, width=50)
user.grid(row=1, column=1)

name = Entry(RegisterFrame, font=('arial', 18), textvariable=NAME, width=50)
name.grid(row=2, column=1)

lbl_tags_result = Label(RegisterFrame, text="", font=('arial', 18), bd=18)
lbl_tags_result.grid(row=3, column=1)

#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
#========================================ComboBox=========================================
def action(event):
    
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    lbl_tags_result.config(text=select, fg="red")
    #print("Vous avez sélectionné : '", select,"'")

# 2) - créer la liste Python contenant les éléments de la liste Combobox
listeProduits=["Laptop", "Imprimante","Tablette","SmartPhone"]

# 3) - Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(root, values=listeProduits)
 
# 4) - Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)

listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>", action)
#========================================BUTTON WIDGETS=========================
btn_register=Button(font=('arial', 20), text="Register", command=Register)
btn_register.pack()
#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
   