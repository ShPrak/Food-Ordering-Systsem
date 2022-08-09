from tkinter import *
import sqlite3

# defining the bill generator function billing


def billing():
    x = 3
    max = 0
    conn = sqlite3.connect('menu.db')
    print(f"{'Item' : <20} {'Qty' : ^10} {'Price': >10}")
    total = 0
    for i in range(0, 25):
        if(items[i].get() != ""):
            for j in conn.execute("select item, price from food_menu where f_no = ?", (i+1,)):
                add = int(items[i].get())*j[1]
                print(f"{j[0] : <20} {items[i].get() : ^10} {add: >10}")
                total += int(items[i].get())*j[1]
                if(add > max):
                    max = add

    print("-"*(40 + len(str(add))))
    print("Total Rs ", total)
    exit(1)


# quantity list
items = list('0'*25)

app = Tk()

# app geometry
app.geometry('700x1000')
r = 0
# creating the labels
conn = sqlite3.connect('menu.db')
for i in conn.execute("select item, price from food_menu"):
    items[r] = StringVar()
    if(r < 13):
        Label(app, text=i[0] + '\t', pady=5).grid(row=r+1, column=0, sticky=W)
        Label(app, text='Rs ' + str(i[1]), pady=5).grid(row=r+1, column=1, sticky=W)
        Entry(app, textvariable=items[r], width=5).grid(row=r+1, column=2)
    else:
        Label(app, text='\t' + i[0] + '\t', pady=5).grid(row=r - 12, column=3, sticky=W)
        Label(app, text='Rs ' + str(i[1]), pady=5).grid(row=r-12, column=4, sticky=W)
        Entry(app, textvariable=items[r], width=5).grid(row=r-12, column=5)
    r = r + 1

# buttons
order_btn = Button(app, text='Place Order', width=10, command=billing)
order_btn.grid(row=13, column=5, sticky=W)

app.mainloop()
