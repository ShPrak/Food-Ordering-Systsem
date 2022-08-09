import sqlite3
conn = sqlite3.connect('menu.db')
# creating table food_menu

# conn.execute('''Create table food_menu
# (f_no integer primary key not null,
# item text not null,
# price integer not null)''')
# conn.close
# for i in conn.execute('''pragma table_info('food_menu')'''):
#    print(i)

# inserting values
'''
conn.execute("insert into food_menu values(1, 'TOMATO SOUP', 80)")
conn.execute("insert into food_menu values(2, 'GARLIC BREAD', 110)")
conn.execute("insert into food_menu values(3, 'SPRING ROLLS', 110)")
conn.execute("insert into food_menu values(4, 'CHEESE SANDWICH', 90)")
conn.execute("insert into food_menu values(5, 'VEG SALAD', 50)")

conn.execute("insert into food_menu values(6, 'FILTER COFFEE', 30)")
conn.execute("insert into food_menu values(7, 'TEA', 20)")
conn.execute("insert into food_menu values(8, 'BOTTLED WATER', 20)")
conn.execute("insert into food_menu values(9, 'MANGO JUICE', 60)")
conn.execute("insert into food_menu values(10,'ORANGE JUICE', 60)")
conn.execute("insert into food_menu values(11, 'FRESH LIME SODA', 60)")
conn.execute("insert into food_menu values(12, 'NORTH INDIAN THALI', 140)")
conn.execute("insert into food_menu values(13, 'SOUTH INDIAN THALI', 130)")
conn.execute("insert into food_menu values(14, 'EGG FRIED RICE', 190)")
conn.execute("insert into food_menu values(15, 'VEG HAKKA NOODLES', 130)")
conn.execute("insert into food_menu values(16, 'BUTTER NAAN', 70)")
conn.execute("insert into food_menu values(17, 'PASTA', 210)")
conn.execute("insert into food_menu values(18, 'BREAKFAST BURRITO', 350)")
conn.execute("insert into food_menu values(19, 'CHICKEN LASAGNA', 250)")
conn.execute("insert into food_menu values(20, 'TIRAMASU CAKE', 200)")
conn.execute("insert into food_menu values(21, 'CHOCOLATE ICE-CREAM', 85)")
conn.execute("insert into food_menu values(22, 'VANILLA ICE-CREAM', 60)")
conn.execute("insert into food_menu values(23, 'FALOODA', 90)")
conn.execute("insert into food_menu values(24, 'CUSTARD', 90)")
conn.execute("insert into food_menu values(25, 'MOUSSE', 120 )")

conn.commit()
# conn.close()
'''
'''
# all the stuff below was me figuring out how selecting stuff from a table would work

id = int(1)


for i in conn.execute("select * from food_menu where f_no = ?", (id,)):
    for j in i:
        print(j, end=' ')
    print('')
conn.close()


for i in conn.execute("select * from food_menu"):
    for j in i:
        print(j, end=' ')
    print('')
conn.close()

bill = 'Item\t\tQty\tPrice\n'
while(input('Shall I place the order: ') == 'no'):
    x = int(input("What item_no would you like to order?: "))
    amount = int(input('What is the quantity?: '))
    for i in conn.execute("select item, price from food_menu where f_no = ?", (x,)):
        bill += i[0] + '\t' + str(amount) + '\t' + str(amount*i[1]) + '\n'

print(bill)
'''
