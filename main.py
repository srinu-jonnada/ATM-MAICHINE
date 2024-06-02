from tkinter import *
import time

root = Tk()
root.geometry("900x850")
root.title("ATM MACHINE")
root.configure(bg="black")

Tops = Frame(root, bg="white", width=800, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, bg="black", width=300, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, bg="black", width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lbl1 = Label(Tops, font=('aria', 30, 'bold'), text="ATM MACHINE", fg="Powder Blue", bg="black", bd=10, anchor='w')
lbl1.grid(row=0, column=0)

lbl2 = Label(Tops, font=('aria', 20, 'bold'), text=localtime, fg="Powder Blue", bg="black", bd=10, anchor='w')
lbl2.grid(row=1, column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
acca = 0  # Initial balance set to 0

def bank():
    global acca
    accno = ["0092", "27833", "78364"]
    account = number.get()
    if account in accno:
        label.config(text="Registered User")
        bank_balances = {"0092": 10000, "27833": 20000, "78364": 30000}
        acca = bank_balances[account]
    else:
        label.config(text="Non Registered User")

def deposit():
    global acca
    amo = float(amount.get())
    acca += amo
    label3.config(text="Net Balance: " + str(acca))

def withdrawn():
    global acca
    wd = float(withd.get())
    if acca >= wd:
        acca -= wd
        label4.config(text="Net Balance: " + str(acca))
    else:
        label4.config(text="Insufficient Balance")

def bal():
    global acca
    label5.config(text="Net Balance: " + str(acca))

def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")

lbl3 = Label(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="black", bd=10, anchor='w', text="Enter the account number")
lbl3.grid(row=0, column=0)
text = Entry(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="white", bd=10, textvariable=number)
text.grid(row=0, column=1)
btnsubmit = Button(f1, padx=16, pady=4, bd=10, fg="black", font=('aria', 16, 'bold'), width=7, text="SUBMIT", bg="Powder Blue", command=bank)
btnsubmit.grid(row=0, column=2,padx=(10,0))
label = Label(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="black", bd=10, anchor='w')
label.grid(row=1, column=1, columnspan=2)

lbl4 = Label(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="black", bd=10, anchor='w', text="Enter amount to deposit")
lbl4.grid(row=2, column=0)
entry_amount = Entry(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="white", bd=10, textvariable=amount)
entry_amount.grid(row=2, column=1)
btn_deposit = Button(f1, padx=16, pady=4, bd=10, fg="black", font=('aria', 16, 'bold'), width=7, text="DEPOSIT", bg="Powder Blue", command=deposit)
btn_deposit.grid(row=2, column=2, padx=(10,0),pady=(15,0))

lbl5 = Label(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="black", bd=10, anchor='w', text="Enter amount to withdraw")
lbl5.grid(row=3, column=0)
entry_withd = Entry(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="white", bd=10, textvariable=withd)
entry_withd.grid(row=3, column=1 )
btn_withdraw = Button(f1, padx=16, pady=4, bd=10, fg="black", font=('aria', 16, 'bold'), width=7, text="WITHDRAW", bg="Powder Blue", command=withdrawn)
btn_withdraw.grid(row=3, column=2,pady=(10,0),padx=(10,0))

btn_balance = Button(f1, padx=16, pady=4, bd=10, fg="black", font=('aria', 16, 'bold'), width=7, text="BALANCE", bg="Powder Blue", command=bal)
btn_balance.grid(row=4, column=1, padx=(0, 10),pady=(10,0))  # Add padding to the right

btn_reset = Button(f1, padx=16, pady=4, bd=10, fg="black", font=('aria', 16, 'bold'), width=7, text="RESET", bg="Powder Blue", command=reset)
btn_reset.grid(row=4, column=2, padx=(10, 0),pady=(10,0))  # Add padding to the left

label3 = Label(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="black", bd=10, anchor='w')
label3.grid(row=6, column=1, columnspan=2)

label4 = Label(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="black", bd=10, anchor='w')
label4.grid(row=7, column=1, columnspan=2)

label5 = Label(f1, font=('aria', 16, 'bold'), fg="Powder Blue", bg="black", bd=10, anchor='w')
label5.grid(row=8, column=1, columnspan=2)

root.mainloop()
