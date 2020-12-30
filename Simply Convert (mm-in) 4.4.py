# -*- coding: utf-8 -*-

import tkinter as tk
import pyperclip as pc
import decimal as Dec

Dec.getcontext().prec = 8

root = tk.Tk()
root.geometry("410x225+755+300")
root.title('Simply Convert (mm/in) v4.4')
root.configure(bg="#212326")

root.resizable(0, 0)  # sets the window to non-resizable
root.after(1, lambda: root.focus_force())  # brings the window on top of everything else open

mmvar = tk.StringVar(root, value='')  # sets up a tk string variable to pass around
invar = tk.StringVar(root, value='')  # sets up a tk string variable to pass around

mmprec = tk.IntVar(value='4') # sets up a tk string variable for precision
inprec = tk.IntVar(value='4') # sets up a tk string variable for precision

in_out_var = tk.StringVar()  # sets up a tk string variable to pass around
mm_out_var = tk.StringVar()  # sets up a tk string variable to pass around


# this is the function called when the inch entry is changed, no more buttons
def btnClickFunction_inch(*args):  # *args is needed for the trace, it just dumps everything that is passed.
    try:
        conversion = "25.4"
        Dec.getcontext().prec = 14
        inch_input.configure(bg='#3e4247', fg="#99a1ad")
        x1 = str(inch_input.get())
        if x1 != '':
            # x1=Dec.Decimal(x1)
            mmvar.set('')  # clears the mm entry as not to confuse you with numbers everywhere
            mm_out_var.set('')  # clears the mm entry as not to confuse you with numbers everywhere
            inprec.set(int(inch_spin.get())) #sets prec to the spinbox value
            decimals_inch = inprec.get()  # get the # of decimals from the spinbox
            Dec.getcontext().prec = decimals_inch
            x1 = Dec.Decimal(x1) * Dec.Decimal(conversion)  # ,decimals_inch)
            pc.copy(str(x1))
            in_out_var.set(str(x1))

    except:  # a bug in decimal produces decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>] error that
        # cant be trapped otherwise it would be a value error
        inch_input.configure(bg='#360e1a', fg="#99a1ad")
        in_out_var.set('Enter a number')  # error message
        if inch_input.get() == '' or inch_input.get() == '.':  # sets the backgound color back to white and removes
            # the error message
            inch_input.configure(bg='#3e4247', fg="#99a1ad")
            in_out_var.set('')


# this is the function called when the mm entry is changed, no more buttons
def btnClickFunction_mm(*args):  # *args is needed for the trace
    # import decimal as Decimal
    try:
        Dec.getcontext().prec = 14
        conversion = "25.4"
        mm_input.configure(bg='#3e4247', fg="#99a1ad")
        x2 = str(mm_input.get())
        if x2 != '':
            invar.set('')  # clears the inch entry as not to confuse you with numbers everywhere
            in_out_var.set('')  # clears the inch entry as not to confuse you with numbers everywhere
            mmprec.set(int(mm_spin.get())) # sets prec to the spinbox value
            decimals_mm = mmprec.get() #get the # of decimals from the spinbox
            Dec.getcontext().prec = decimals_mm
            x2 = Dec.Decimal(x2) / Dec.Decimal(conversion)
            pc.copy(str(x2))
            mm_out_var.set(str(x2))

    except:  # a bug in decimal produces decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>] error that
        # cant be trapped
        mm_input.configure(bg='#360e1a', fg="#99a1ad")
        mm_out_var.set('Enter a number')  # error message
        if mm_input.get() == '' or mm_input.get() == '.':  # the if sets the background color back to white and
            # removes the error message
            mm_input.configure(bg='#3e4247', fg="#99a1ad")
            mm_out_var.set('')

        # this section is called by the popup menu


def paste_in():
    invar.set(pc.paste())
    root.update()


def paste_mm():
    mmvar.set(pc.paste())
    root.update()


###################################
# start inch tk section

inch_to_mm_frame = tk.LabelFrame(root, text="Convert inch to mm", height=100, width=400, border=3,
                                 font=('arial', 12, 'normal'), bg="#212326", fg="#99a1ad").place(x=5, y=5)
inch_input = tk.Entry(root, textvariable=invar, bg="#3e4247", fg="#99a1ad", bd=0)  # assignes the entry to the tk variable
inch_input.place(x=15, y=50)

clip_lbl = tk.Label(root, text='Clipboard Output: ', font=('arial', 10, 'normal'), bg="#212326", fg="#99a1ad").place(x=150, y=50)
invar.trace('w', btnClickFunction_inch)  # watches for changes in the mm entry field
in_out_label = tk.Label(root, textvariable=in_out_var, font=('arial', 10, 'normal'), bg="#212326", fg="#99a1ad").place(x=270, y=50)
# inch_input.focus_set() # sets the cursor active in the inch entry box when the app is opened

inch_spin = tk.Spinbox(root, from_=0, textvariable=inprec, to=13, width=3, bg="#3e4247", fg="#99a1ad", bd=0)
inprec.trace('w', btnClickFunction_inch)  # watches for changes in the precision entry field
inch_spin.place(x=160, y=75)
inch_spin_lbl = tk.Label(root, text='Precision', font=('arial', 10, 'normal'), bg="#212326", fg="#99a1ad").place(x=195, y=71)
inch_spin.delete(0, 'end')  # clears the spinbox
inch_spin.insert(0, 4)  # sets the default spinbox value

###################################
# start mm tk section

mm_to_inch_frame = tk.LabelFrame(root, text="Convert mm to inch", height=100, width=400, border=3,
                                 font=('arial', 12, 'normal'), bg="#212326", fg="#99a1ad").place(x=5, y=120)
mm_input = tk.Entry(root, textvariable=mmvar, bg="#3e4247", fg="#99a1ad", bd=0)
mm_input.place(x=15, y=165)

clip_lbl2 = tk.Label(root, text='Clipboard Output: ', font=('arial', 10, 'normal'), bg="#212326", fg="#99a1ad").place(x=150, y=165)
mmvar.trace('w', btnClickFunction_mm)  # watches for changes in the mm entry field
mm_out_label = tk.Label(root, textvariable=mm_out_var, font=('arial', 10, 'normal'), bg="#212326", fg="#99a1ad").place(x=270, y=165)

mm_spin = tk.Spinbox(root, from_=0, textvariable=mmprec, to=13, width=3, bg="#3e4247", fg="#99a1ad", bd=0)  # spinbox
#mmprec.trace('w', btnClickFunction_mm)  # watches for changes in the precision entry field
mmprec.trace('w', btnClickFunction_mm)  # watches for changes in the precision entry field
mm_spin.place(x=160, y=190)
mm_spin_lbl = tk.Label(root, text='Precision', font=('arial', 10, 'normal'), bg="#212326", fg="#99a1ad").place(x=195, y=186)
mm_spin.delete(0, 'end')  # clears the spinbox
mm_spin.insert(0, 4)  # sets the default spinbox value

###################################
# tk popup menu for paste
inch_popup = tk.Menu(root, tearoff=0)
inch_popup.add_command(label="Paste", command=paste_in)


def do_popup_in(event):
    try:
        inch_popup.tk_popup(event.x_root, event.y_root)
    finally:
        inch_popup.grab_release()


mm_popup = tk.Menu(root, tearoff=0)
mm_popup.add_command(label="Paste", command=paste_mm)


def do_popup_mm(event):
    try:
        mm_popup.tk_popup(event.x_root, event.y_root)
    finally:
        mm_popup.grab_release()


inch_input.bind("<Button-3>", do_popup_in)
mm_input.bind("<Button-3>", do_popup_mm)

# root.update() #forces root window update
root.mainloop()  # go forever

# to create exe
# navigate to pyinstaller.exe directory in cmd.exe
# pyinstaller -–onefile -–windowed c:blahblah\myApp.py
# icon if you want otherwise delete that.  
# The file will appear in dist folder in same folder as pyinstaller.exe
