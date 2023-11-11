import random
import tkinter

main_window = tkinter.Tk()
main_window.title("PassGenie")
main_window.geometry('290x200')
pad = 70
pad1 = 20
main_window['padx'] = pad
main_window['pady'] = pad1

# <----------Define Variable-------------> #

chk1 = tkinter.IntVar()
chk2 = tkinter.IntVar()
chk3 = tkinter.IntVar()


# <----------Define Function-------------> #

def pass_generate(length):
    valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.sample(valid_char, length))
    display_result.delete(0, tkinter.END)
    display_result.insert(0, password)


def checkbox():
    if chk1.get() == 8:
        pass_generate(8)
    elif chk2.get() == 10:
        pass_generate(10)
    elif chk3.get() == 12:
        pass_generate(12)
    else:
        pass_generate(8)


# <----------Label-----------> #
title_text = tkinter.Label(text='Your Password :')
title_text.grid(row=0, column=0)

display_result = tkinter.Entry()
display_result.grid(row=1, column=0)

# <----------Checkboxes-------------> #

chkone = tkinter.Checkbutton(text='8 Character Password', onvalue=8, offvalue=0, variable=chk1)
chkone.grid(row=3, column=0)

chktwo = tkinter.Checkbutton(text='10 Character Password', onvalue=10, offvalue=0, variable=chk2)
chktwo.grid(row=4, column=0)

chkthree = tkinter.Checkbutton(text='12 Character Password', onvalue=12, offvalue=0, variable=chk3)
chkthree.grid(row=5, column=0)

# <----------Generate Button-------------> #

pass_G = tkinter.Button(text='Generate', command=checkbox)
pass_G.grid(row=7, column=0)

main_window.mainloop()