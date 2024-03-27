#--------------------------------------------------Importing modules------------------------------------------------

from tkinter import *
from tkinter import messagebox
from random import *
from string import *
#--------------------------------------------------Creating Constants--------------------------------------------------

BLACK ="#050504"
GREY ="#f0f1f2"
FONT = ("Adobe Arabic", 12 , "bold")
wid = 0



#----------------------------------------- Creating functions----------------------------------------------------------
def generate_pwd():
    letters = list(ascii_letters)
    numbers = list(digits)
    special_characters = list(punctuation)
    password = []
    generated_entry.delete(0, END)

    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showinfo("INPUT WARNING", "A password must have at least 8 characters")
    except ValueError:
        messagebox.showerror(" ERROR", "Length Value must be numeric")
    try:
        alpha_n = int(alphabet_entry.get())
        if alpha_n > length:
            raise Exception
        num_n = int(number_entry.get())
        if num_n > length:
            raise Exception
        special_n = int(special_entry.get())
        if special_n > length:
            raise Exception
        if alpha_n + num_n + special_n != length:
            messagebox.showwarning(" INPUT ERROR", "Total number of characters must be equal to selected length")
    except ValueError:
        messagebox.showerror(" INPUT ERROR", "values must be numeric")
    except Exception:
        messagebox.showerror(" INPUT ERROR", " entered value must be less than or equal to selected length")
    else:

        exclude = list(excluded_entry.get().split())

        for i in exclude:
            if i in letters:
                letters.remove(i)
            if i in numbers:
                numbers.remove(i)
            if i in special_characters:
                special_characters.remove(i)


        for i in range(alpha_n):
            password += choice(letters)

        for i in range(num_n):
            password += choice(numbers)

        for i in range(special_n):
            password += choice(special_characters)


        shuffle(password)

        result = ""
        for i in password:
            result += i
        generated_entry.insert(0, result)


def clear_values():
    length_entry.delete(0, END)
    alphabet_entry.delete(0, END)
    number_entry.delete(0, END)
    special_entry.delete(0, END)
    excluded_entry.delete(0, END)
    generated_entry.delete(0, END
                           )
#------------------------------------------------------UI setup--------------------------------------------------------

window = Tk()
window.geometry("1150x630")
window.configure(bg=GREY)
window.title("PASSWORD GENERATOR")


#---------------------------------------------------Importing Image----------------------------------------------------

canvas = Canvas(width=200, height=200, highlightthickness=0)
chart_image = PhotoImage(file="pass.png")
canvas.create_image(150,150,image=chart_image)
canvas.grid(column=2, row=1)






#----------------------------------------------- Creating label---------------------------------------------------------


title_label = Label(window, text="PASSWORD GENERATOR", padx=30, pady=15, bg=GREY, font=("Adobe Arabic", 20, "bold"),fg=BLACK)
length_label = Label(window, text="Enter the length for your Password : ", padx=13, pady=10, font=FONT, fg=BLACK, bg= GREY)
alphabet_label = Label(window, text="Number of Alphabets :", padx=13, pady=10, font=FONT, fg=BLACK, bg= GREY)
number_label = Label(window, text="Number of Digits :", padx=13, pady=10, font=FONT, fg=BLACK, bg= GREY)
special_label = Label(window, text="Number of special characters : ", padx=13, pady=10, font=FONT, fg=BLACK, bg= GREY)
excluded_label = Label(window, text="Characters to be excluded from \n your password (separated by spaces) : ", padx=30, pady=20, font=FONT, fg=BLACK, bg= GREY)
generated_label = Label(window, text="Generated Password : ", padx=30, pady=20, font=FONT, fg=BLACK, bg= GREY)



#----------------------------------------------------- Creating  entry--------------------------------------------------

length_entry = Entry(window, width=20, font=FONT)
alphabet_entry = Entry(window, width=20, font=FONT)
number_entry = Entry(window, width=20, font=FONT)
special_entry = Entry(window, width=20, font=FONT)
excluded_entry = Entry(window, width=20, font=FONT)
generated_entry = Entry(window, width=wid, font=FONT)



#------------------------------------------------ Creating buttons------------------------------------------------------

gen_btn = Button(window, text="GENERATE",borderwidth=0, padx=10, pady=10, bg="#042f59", fg="#8AaEE0", font=("Sans-serif", 12, "bold"),
                 command=generate_pwd)
reset_btn = Button(window, text="RESET",borderwidth=0, padx=10, pady=10, bg="#042f59", fg="#8AaEE0", font=("Sans-serif", 12, "bold"),
                   command=clear_values)

#-----------------------------------Placing label on window using tkinter layout manager-------------------------------


title_label.grid(row=0, column=2)
length_label.grid(row=2, column=0)
alphabet_label.grid(row=3, column=0)
number_label.grid(row=4, column=0)
special_label.grid(row=5, column=0)
excluded_label.grid(row=6, column=0)
generated_label.grid(row=8, column=0)


#---------------------------------- placing entries on window using tkinter layout manager------------------------------

length_entry.grid(row=2, column=4)
alphabet_entry.grid(row=3, column=4)
number_entry.grid(row=4, column=4)
special_entry.grid(row=5, column=4)
excluded_entry.grid(row=6, column=4)
reset_btn.grid(row=7, column=0)
gen_btn.grid(row=7, column=4)
generated_entry.grid(row=8, column=4)

#--------------------------------Always display window------------------------------------------------------------------

window.mainloop()
