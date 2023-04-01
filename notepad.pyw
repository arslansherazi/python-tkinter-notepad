from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def message_window():
    _message_window = Tk()

    # The following code place the window at the top of any screen when it is created.User then can move it if we allow him to do so.
    x = 435
    y = 208
    w = _message_window.winfo_screenwidth()  # gives the width of any screen
    h = _message_window.winfo_screenheight()  # gives the height of any screen
    width = (w / 2) - (x / 2)
    height = (h / 2) - (y / 2)

    _message_window.geometry('%dx%d+%d+%d' % (x, y, width, height))

    _message_window.overrideredirect(True)  # This line removes the window border from window.(used for displaying initial messages etc)

    photo = PhotoImage(file='images/pyco_editor.png')
    label = Label(_message_window, image=photo)
    label.pack()

    _message_window.after(2000, lambda: main_window(_message_window))  # Destroy the Window after 5 seconds.5000milli seconds=5 econds

    _message_window.mainloop()


def main_window(window_message):
    window_message.destroy()

    _main_window = Tk()

    _main_window.geometry(
        "600x500")  # Original size of window(if user tries to resize or move window then it converts to this size.)

    _main_window.title('Pyco Editor')
    _main_window.wm_iconbitmap('images/icon.ico')

    _main_window.state('zoomed')  # this line display the window with zoom mode(full possible size of window)

    menu_bar(_main_window)  # Calling the menuBar Function to create menu bar in Window
    option_bar(_main_window)

    text_box(_main_window)

    _main_window.mainloop()


def new_file():
    _main_window = Tk()

    _main_window.geometry("600x500")

    _main_window.title('Pyco Editor')
    _main_window.wm_iconbitmap('images/icon.ico')

    menu_bar(_main_window)
    option_bar(_main_window)

    text_box(_main_window)

    _main_window.mainloop()


def menu_bar(_main_window):
    _menu_bar = Menu()

    file_list = Menu(tearoff=0)
    view_list = Menu(tearoff=0)
    edit_list = Menu(tearoff=0)
    format_list = Menu(tearoff=0)
    help_list = Menu(tearoff=0)

    _menu_bar.add_cascade(label="File", menu=file_list)
    _menu_bar.add_cascade(label="Edit", menu=edit_list)
    _menu_bar.add_cascade(label="Format", menu=format_list)
    _menu_bar.add_cascade(label="View", menu=view_list)
    _menu_bar.add_cascade(label="Help", menu=help_list)

    # File Item

    file_list.add_command(label="New File              Ctrl+N", command=new_file)
    file_list.add_command(label="Open File             Ctrl+O", command=open_file)
    file_list.add_separator()
    file_list.add_command(label="Save File               Ctrl+S")
    file_list.add_command(label="Save As                 Ctrl+Shift+S", command=save_as_file)
    file_list.add_separator()
    file_list.add_command(label="Exit                        Ctrl+Q", command=lambda: _exit(_main_window))

    # View Item

    view_list.add_checkbutton(label="Option Bar")

    # Format Item

    format_list.add_command(label="Text Formatting")

    # Help Item

    help_list.add_command(label="FAQs")

    # Edit Item

    edit_list.add_command(label="Undo                Ctrl+Z")
    edit_list.add_command(label="Redo                 Ctrl+Shift+Z", command=redo)
    edit_list.add_separator()
    edit_list.add_command(label="Cut                   Ctrl+X")
    edit_list.add_command(label="Copy                Ctrl+C")
    edit_list.add_command(label="Paste                Ctrl+V")
    edit_list.add_separator()
    edit_list.add_command(label="Select All          Ctrl+A")

    _main_window.config(menu=_menu_bar)


def text_box(_main_window):
    box_width = _main_window.winfo_width() - 20
    box_height = _main_window.winfo_height() - 130

    frame = Frame(_main_window, bg="white")
    frame.place(x=10, y=110, width=box_width, height=box_height)

    global text_box

    text_box = Text(frame, bg="white", fg="black", insertbackground="black", font=("Calibri", 12), bd=0, undo=True)
    text_box.place(x=20, y=20, width=box_width - 50, height=box_height - 20)

    scrollbar = Scrollbar(frame, width=10)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_box['yscrollcommand'] = scrollbar.set
    scrollbar.config(command=text_box.yview)


def option_bar(_main_window):
    box_width = _main_window.winfo_width()
    upper_frame = Frame(_main_window)
    upper_frame.place(x=0, y=0, width=box_width, height=100)

    photo1 = PhotoImage(file='images/new_file.png')
    button1 = Button(upper_frame, text="New File", compound="top", image=photo1, relief=FLAT, command=new_file)
    button1.image = photo1
    button1.place(x=10, y=10)

    # Hover Effect
    button1.bind("<Enter>", lambda event: button1.configure(bg="#e0e0e0"))
    button1.bind("<Leave>", lambda event: button1.configure(bg="#F0F0F0"))

    photo2 = PhotoImage(file='images/open_file.png')
    button2 = Button(upper_frame, text="Open File", compound="top", image=photo2, relief=FLAT, command=open_file)
    button2.image = photo2
    button2.place(x=100, y=10)

    # Hover Effect
    button2.bind("<Enter>", lambda event: button2.configure(bg="#e0e0e0"))
    button2.bind("<Leave>", lambda event: button2.configure(bg="#F0F0F0"))

    photo3 = PhotoImage(file='images/save.png')
    button3 = Button(upper_frame, text="Save", compound="top", image=photo3, relief=FLAT)
    button3.image = photo3
    button3.place(x=190, y=10)

    # Hover Effect
    button3.bind("<Enter>", lambda event: button3.configure(bg="#e0e0e0"))
    button3.bind("<Leave>", lambda event: button3.configure(bg="#F0F0F0"))

    photo_3 = PhotoImage(file='images/save_as.png')
    button_3 = Button(upper_frame, text="Save As", compound="top", image=photo_3, relief=FLAT, command=save_as_file)
    button_3.image = photo_3
    button_3.place(x=280, y=10)

    # Hover Effect
    button_3.bind("<Enter>", lambda event: button_3.configure(bg="#e0e0e0"))
    button_3.bind("<Leave>", lambda event: button_3.configure(bg="#F0F0F0"))

    cut_photo = PhotoImage(file='images/cut.png')
    cut = Button(upper_frame, text="Cut", compound="top", image=cut_photo, relief=FLAT)
    cut.image = cut_photo
    cut.place(x=370, y=10)

    # Hover Effect
    cut.bind("<Enter>", lambda event: cut.configure(bg="#e0e0e0"))
    cut.bind("<Leave>", lambda event: cut.configure(bg="#F0F0F0"))

    c = PhotoImage(file='images/copy.png')
    c1 = Button(upper_frame, text="Copy", compound="top", image=c, relief=FLAT)
    c1.image = c
    c1.place(x=460, y=10)

    # Hover Effect
    c1.bind("<Enter>", lambda event: c1.configure(bg="#e0e0e0"))
    c1.bind("<Leave>", lambda event: c1.configure(bg="#F0F0F0"))

    p = PhotoImage(file='images/paste.png')
    p1 = Button(upper_frame, text="Paste", compound="top", image=p, relief=FLAT)
    p1.image = p
    p1.place(x=550, y=10)

    # Hover Effect
    p1.bind("<Enter>", lambda event: p1.configure(bg="#e0e0e0"))
    p1.bind("<Leave>", lambda event: p1.configure(bg="#F0F0F0"))

    u = PhotoImage(file='images/undo.png')
    u1 = Button(upper_frame, text="Undo", compound="top", image=u, relief=FLAT)
    u1.image = u
    u1.place(x=640, y=10)

    # Hover Effect
    u1.bind("<Enter>", lambda event: u1.configure(bg="#e0e0e0"))
    u1.bind("<Leave>", lambda event: u1.configure(bg="#F0F0F0"))

    r = PhotoImage(file='images/redo.png')
    r1 = Button(upper_frame, text="Redo", compound="top", image=r, relief=FLAT, command=redo)
    r1.image = r
    r1.place(x=730, y=10)

    # Hover Effect
    r1.bind("<Enter>", lambda event: r1.configure(bg="#e0e0e0"))
    r1.bind("<Leave>", lambda event: r1.configure(bg="#F0F0F0"))

    photo_33 = PhotoImage(file='images/font.png')
    button_33 = Button(upper_frame, text="Formatting", compound="top", image=photo_33, relief=FLAT)
    button_33.image = photo_33
    button_33.place(x=820, y=10)

    # Hover Effect
    button_33.bind("<Enter>", lambda event: button_33.configure(bg="#e0e0e0"))
    button_33.bind("<Leave>", lambda event: button_33.configure(bg="#F0F0F0"))

    photo4 = PhotoImage(file='images/internet.png')
    button4 = Button(upper_frame, text="Save to Cloud", compound="top", image=photo4, relief=FLAT)
    button4.image = photo4
    button4.place(x=910, y=10)

    # Hover Effect
    button4.bind("<Enter>", lambda event: button4.configure(bg="#e0e0e0"))
    button4.bind("<Leave>", lambda event: button4.configure(bg="#F0F0F0"))

    photo5 = PhotoImage(file='images/exit.png')
    button5 = Button(upper_frame, text="Exit", compound="top", image=photo5, relief=FLAT, command=lambda: _exit(_main_window))
    button5.image = photo5
    button5.place(x=1000, y=10)

    # Hover Effect
    button5.bind("<Enter>", lambda event: button5.configure(bg="#e0e0e0"))
    button5.bind("<Leave>", lambda event: button5.configure(bg="#F0F0F0"))


def _exit(_main_window):
    opt = messagebox.askyesno(title="Exit", message="Are you want to Exit?")
    if opt == 1:
        _main_window.destroy()


def open_file():
    file1 = filedialog.askopenfile(title="Open File", mode='r', filetypes=(('text files', '.txt'), ('all files', '.*')))

    file2 = file1.name

    f = open(file2)

    text = f.read()

    text_box.insert("1.0", text)


def save_as_file():
    file = filedialog.asksaveasfile(title="Save File As", filetypes=(('text files', '.txt'), ('all files', '.*')),
                                    initialfile='myFile.txt', defaultextension='.txt')
    text = text_box.get("1.0", END)
    file.write(text)
    file.close()


def redo():
    text_box.edit_redo()


if __name__ == "__main__":
    message_window()
