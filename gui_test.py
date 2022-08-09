from tkinter import *
import sqlite3

# defining the bill generator function billing


def billing():
    x = 3
    conn = sqlite3.connect('menu.db')
    bill = 'Item\t\tQty\tPrice\n'
    total = 0
    for i in range(0, 25):
        if(items[i].get() != ""):
            for j in conn.execute("select item, price from food_menu where f_no = ?", (i+1,)):
                bill += j[0] + '\t' + items[i].get() + '\t' + str(int(items[i].get())*j[1]) + '\n'
                total += int(items[i].get())*j[1]

    print(bill)
    print('\t\tTotal', total)
    exit(1)


# quantity list
items = list('0'*25)

app = Tk()

# app geometry
app.geometry('700x1000')

# creating the labels

# 1st entry
#part_text1 = StringVar()
items[0] = StringVar()
part_label1 = Label(app, text='TOMATO SOUP 80 Rs', pady=5)
part_entry1 = Entry(app, textvariable=items[0])
part_label1.grid(row=0, column=0, sticky=W)
part_entry1.grid(row=0, column=1)

# 2nd entry
#part_text2 = StringVar()
items[1] = StringVar()
part_label2 = Label(app, text='GARLIC BREAD 110 Rs ', pady=5)
part_entry2 = Entry(app, textvariable=items[1])
part_label2.grid(row=1, column=0, sticky=W)
part_entry2.grid(row=1, column=1)

# 3d entry
#part_text3 = StringVar()
items[2] = StringVar()
part_label3 = Label(app, text='SPRING ROLLS 110 Rs ', pady=5)
part_entry3 = Entry(app, textvariable=items[2])
part_label3.grid(row=2, column=0, sticky=W)
part_entry3.grid(row=2, column=1)

# 4th entry
#part_text4 = StringVar()
items[3] = StringVar()
part_label4 = Label(app, text='CHEESE SANDWICH 90 Rs ', pady=5)
part_entry4 = Entry(app, textvariable=items[3])
part_label4.grid(row=3, column=0, sticky=W)
part_entry4.grid(row=3, column=1)


# 5th entry
#part_text5 = StringVar()
items[4] = StringVar()
part_label5 = Label(app, text='VEG SALAD 50 Rs ', pady=5)
part_entry5 = Entry(app, textvariable=items[4])
part_label5.grid(row=4, column=0, sticky=W)
part_entry5.grid(row=4, column=1)


# 6th entry
#part_text2 = StringVar()
items[5] = StringVar()
part_label6 = Label(app, text='FILTER COFFEE 30 Rs ', pady=5)
part_entry6 = Entry(app, textvariable=items[5])
part_label6.grid(row=5, column=0, sticky=W)
part_entry6.grid(row=5, column=1)

# 7th entry
#part_text3 = StringVar()
items[6] = StringVar()
part_label7 = Label(app, text='TEA 20 Rs ', pady=5)
part_entry7 = Entry(app, textvariable=items[6])
part_label7.grid(row=6, column=0, sticky=W)
part_entry7.grid(row=6, column=1)

# 8th entry
#part_text4 = StringVar()
items[7] = StringVar()
part_label8 = Label(app, text='BOTTLED WATER 20 Rs ', pady=5)
part_entry8 = Entry(app, textvariable=items[7])
part_label8.grid(row=7, column=0, sticky=W)
part_entry8.grid(row=7, column=1)


# 9th entry
#part_text5 = StringVar()
items[8] = StringVar()
part_label9 = Label(app, text='MANGO JUICE 60 Rs ', pady=5)
part_entry9 = Entry(app, textvariable=items[8])
part_label9.grid(row=8, column=0, sticky=W)
part_entry9.grid(row=8, column=1)


# 10th entry
#part_text2 = StringVar()
items[9] = StringVar()
part_label10 = Label(app, text='10 ORANGE JUICE 60 Rs ', pady=5)
part_entry10 = Entry(app, textvariable=items[9])
part_label10.grid(row=9, column=0, sticky=W)
part_entry10.grid(row=9, column=1)

# 11th entry
#part_text3 = StringVar()
items[10] = StringVar()
part_label11 = Label(app, text='FRESH LIME SODA 60 Rs ', pady=5)
part_entry11 = Entry(app, textvariable=items[10])
part_label11.grid(row=10, column=0, sticky=W)
part_entry11.grid(row=10, column=1)


# 12th entry
#part_text4 = StringVar()
items[11] = StringVar()
part_label12 = Label(app, text='NORTH INDIAN THALI 140 Rs ', pady=5)
part_entry12 = Entry(app, textvariable=items[11])
part_label12.grid(row=11, column=0, sticky=W)
part_entry12.grid(row=11, column=1)


# 13th entry
#part_text5 = StringVar()
items[12] = StringVar()
part_label13 = Label(app, text='SOUTH INDIAN THALI 130 Rs ', pady=5)
part_entry13 = Entry(app, textvariable=items[12])
part_label13.grid(row=12, column=0, sticky=W)
part_entry13.grid(row=12, column=1)


# 14th entry
#part_text2 = StringVar()
items[13] = StringVar()
part_label14 = Label(app, text='\tEGG FRIED RICE 190 Rs ', pady=5)
part_entry14 = Entry(app, textvariable=items[13])
part_label14.grid(row=0, column=2, sticky=W)
part_entry14.grid(row=0, column=3)

# 15th entry
#part_text3 = StringVar()
items[14] = StringVar()
part_label15 = Label(app, text='\tVEG HAKKA NOODLES 130 Rs ', pady=5)
part_entry15 = Entry(app, textvariable=items[14])
part_label15.grid(row=1, column=2, sticky=W)
part_entry15.grid(row=1, column=3)

# 16th entry
#part_text4 = StringVar()
items[15] = StringVar()
part_label16 = Label(app, text='\tBUTTER NAAN 70 Rs ', pady=5)
part_entry16 = Entry(app, textvariable=items[15])
part_label16.grid(row=2, column=2, sticky=W)
part_entry16.grid(row=2, column=3)


# 17th entry
#part_text5 = StringVar()
items[16] = StringVar()
part_label17 = Label(app, text='\tPASTA 210 Rs ', pady=5)
part_entry17 = Entry(app, textvariable=items[16])
part_label17.grid(row=3, column=2, sticky=W)
part_entry17.grid(row=3, column=3)


# 18th entry
#part_text2 = StringVar()
items[17] = StringVar()
part_label18 = Label(app, text='\tBREAKFAST BURRITO 350 Rs ', pady=5)
part_entry18 = Entry(app, textvariable=items[17])
part_label18.grid(row=4, column=2, sticky=W)
part_entry18.grid(row=4, column=3)

# 19th entry
#part_text3 = StringVar()
items[18] = StringVar()
part_label19 = Label(app, text='\tCHICKEN LASAGNA 250 Rs ', pady=5)
part_entry19 = Entry(app, textvariable=items[18])
part_label19.grid(row=5, column=2, sticky=W)
part_entry19.grid(row=5, column=3)

# 20th entry
#part_text4 = StringVar()
items[19] = StringVar()
part_label20 = Label(app, text='\tTIRAMASU CAKE 200 Rs ', pady=5)
part_entry20 = Entry(app, textvariable=items[19])
part_label20.grid(row=6, column=2, sticky=W)
part_entry20.grid(row=6, column=3)


# 21th entry
#part_text5 = StringVar()
items[20] = StringVar()
part_label21 = Label(app, text='\tCHOCOLATE ICE-CREAM 85 Rs ', pady=5)
part_entry21 = Entry(app, textvariable=items[20])
part_label21.grid(row=7, column=2, sticky=W)
part_entry21.grid(row=7, column=3)

# 22nd entry
#part_text2 = StringVar()
items[21] = StringVar()
part_label22 = Label(app, text='\tVANILLA ICE-CREAM 60 Rs ', pady=5)
part_entry22 = Entry(app, textvariable=items[21])
part_label22.grid(row=8, column=2, sticky=W)
part_entry22.grid(row=8, column=3)

# 23d entry
#part_text3 = StringVar()
items[22] = StringVar()
part_label23 = Label(app, text='\tFALOODA 90 Rs ', pady=5)
part_entry23 = Entry(app, textvariable=items[22])
part_label23.grid(row=9, column=2, sticky=W)
part_entry23.grid(row=9, column=3)

#part_text4 = StringVar()
# 24th entry
items[23] = StringVar()
part_label24 = Label(app, text='\tCUSTARD 90 Rs ', pady=5)
part_entry24 = Entry(app, textvariable=items[23])
part_label24.grid(row=10, column=2, sticky=W)
part_entry24.grid(row=10, column=3)


# 25th entry
#part_text5 = StringVar()
items[24] = StringVar()
part_label25 = Label(app, text='\tMOUSSE 120 Rs ', pady=5)
part_entry25 = Entry(app, textvariable=items[24])
part_label25.grid(row=11, column=2, sticky=W)
part_entry25.grid(row=11, column=3)

# buttons
order_btn = Button(app, text='Place Order', width=10, command=billing)
order_btn.grid(row=13, column=3, sticky=W)
# starting the program
app.mainloop()
