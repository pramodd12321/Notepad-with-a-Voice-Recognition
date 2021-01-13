import datetime
import webbrowser
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askyesno
from tkinter import filedialog
import speech_recognition as sr


def New_File():
    if askyesno('Pramod Notepad', "Save Existing Word ?"):
        filename = filedialog.asksaveasfilename()
        if filename:
            alltext = text.get(1.0, END)
            open(filename, 'w').write(alltext)

    if askyesno("Pramod Notepad", "Open Existing File ?"):
        text.delete(1.0, END)
        file = open(filedialog.askopenfilename(), 'r')
        if file != '':
            txt = file.read()
            text.insert(INSERT, txt)
        else:
            pass

    else:
        text.delete(1.0, END)


def Open_File():
    text.delete(1.0, END)
    file = open(filedialog.askopenfilename(), 'r')
    if file != '':
        txt = file.read()
        text.insert(INSERT, txt)

    else:
        pass


def Save_As():
    filename = filedialog.asksaveasfilename()
    if filename:
        alltext = text.get(1.0, END)
        open(filename, 'w').write(alltext)


def Close():
    if askyesno('Pramod Notepad', "Save Existing Word ?"):
        filename = filedialog.asksaveasfilename()
        if filename:
            alltext = text.get(1.0, END)
            open(filename, 'w').write(alltext)
        root.destroy()
    else:
        root.destroy()


def Cut():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)


def Copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())


def Paste():
    try:
        txt = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, txt)
    except:
        pass

def Erase():
    sel =text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)


def Clear_Screen():
    text.delete(1.0, END)


def Date():
    data = datetime.date.today()
    text.insert(INSERT, data)


def Text_Color():
    (triple,color) = askcolor()

    if color:
        text.config(foreground=color)


def No_Format():
    text.config(font=("Arial",10))


def Bold():
    current_tags = text.tag_names('sel.first')
    if 'bt' in current_tags:
        text.tag_remove('bt', 'sel.first', 'sel.last')
        text.tag_config('bt', font=('Arial',10,'bold'))

    else:
        text.tag_add("bt", 'sel.first', 'sel.last')
        text.tag_config('bt', font=('Arial', 10, 'bold'))


def Italic():
    current_tags = text.tag_names('sel.first')
    if 'bt' in current_tags:
        text.tag_remove('bt', 'sel.first', 'sel.last')
        text.tag_config('bt', font=('Arial', 10, 'italic'))

    else:
        text.tag_add("bt", 'sel.first', 'sel.last')
        text.tag_config('bt', font=('Arial', 10, 'italic'))


def Underline():
    # text.tag_add("here", '1.0', '1.4')
    # text.tag_config('here', font=('Arial',10,'underline')

    current_tags = text.tag_names('sel.first')
    if 'bt' in current_tags:
        text.tag_remove('bt', 'sel.first', 'sel.last')
        text.tag_config('bt', font=('Arial', 10, 'underline'))

    else:
        text.tag_add("bt", 'sel.first', 'sel.last')
        text.tag_config('bt', font=('Arial', 10, 'underline'))


def Background():
    (triple, color) = askcolor()
    if color:
        text.config(background=color)


def Online_Help():
    webbrowser.open("https://www.google.com/")


def Start_Speaking():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            text1 = r.recognize_google(audio)
            text.insert(INSERT, text1)
            a = '\n'
            text.insert(INSERT, a)

        except:
            msg = 'Sorry, could not recognize your voice or you may be offline!\n'
            text.insert(INSERT, msg)


if __name__ == "__main__":
    # Below are the coding for main window
    root = Tk()     # Tk() is the tkinter object
    root.title("Pramod Notepad")
    Main_Menu = Menu(root)
    Commands = Menu(root)
    root.config(menu=Main_Menu)

    Main_Menu.add_cascade(label="File", menu=Commands)
    Commands.add_command(label="New File", command=New_File)
    Commands.add_command(label="Open...", command=Open_File)
    Commands.add_command(label="Save As..", command=Save_As)
    Commands.add_command(label="Close", command=Close)

    Edit_Menu = Menu(root)
    Main_Menu.add_cascade(label="Edit", menu=Edit_Menu)
    Edit_Menu.add_command(label="Cut", command=Cut)
    Edit_Menu.add_command(label='Copy', command=Copy)
    Edit_Menu.add_command(label='Paste', command=Paste)
    Edit_Menu.add_command(label='Delete', command=Erase)
    Edit_Menu.add_command(label='Clear Screen', command=Clear_Screen)

    Insert_in_Menu = Menu(root)
    Main_Menu.add_cascade(label='Insert', menu=Insert_in_Menu)
    Insert_in_Menu.add_command(label='Current Date', command=Date)

    Change_Format = Menu(root)
    Main_Menu.add_cascade(label='Format', menu=Change_Format)
    Change_Format.add_command(label='Font', command=Text_Color)
    Change_Format.add_separator()
    Change_Format.add_command(label='No Format', command=No_Format)
    Change_Format.add_command(label='Bold', command=Bold)
    Change_Format.add_command(label='Italic', command=Italic)
    Change_Format.add_command(label='Underline', command=Underline)

    Personalize = Menu(root)
    Main_Menu.add_cascade(label='Personalize', menu=Personalize)
    Personalize.add_command(label='Background', command=Background)

    User_Help = Menu(root)
    Main_Menu.add_cascade(label='Help', menu=User_Help)
    User_Help.add_command(label='Online Help', command=Online_Help)

    Speech_Text = Menu(root)
    Main_Menu.add_cascade(label='Speech_Text', menu=Speech_Text)
    Speech_Text.add_command(label='Start Speaking', command=Start_Speaking)

    text = Text(root, height=30, width=100, font=("Arial", 10))
    scrollbar = Scrollbar(root, command=text.yview)
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.pack()
    root.resizable(0, 0)

    root.mainloop()














