from pyfiglet import Figlet
f = Figlet(font='standard')
print(f.renderText('Arash Store'))
###################################
PRODUCTS = []
###################################
def load():
    print('loading...')
    f = open('database.txt' , 'r')
    rows = f.read().split('\n')
    for i in range(len(rows)):
        info = rows[i].split(',')
        PRODUCTS.append({'id': int(info[0]) ,'name': info[1],'price': float(info[2]) ,'count': int(info[3])})
    f.close()    
    print('program is ready to use')    
###################################
def show_menu():
    print('1-Add Product')
    print('2-Edit Product')
    print('3-Delete Product')
    print('4-search')
    print('5-show list')
    print('6-Buy')
    print('7-exit')
##################################-1
def add_products():
    id = int(input('enter id: '))
    name = input('enter name: ')
    price = float(input('enter price: '))
    count = int(input('enter count: '))
    PRODUCTS.append({'id': id , 'name': name, 'price': price , 'count': count })
    print('new product added successfully ')
##################################-2
def show_edit_menu():
    print('1- name ')
    print('2- price ')
    print('3- count ')
    print('4 - exit ')
    
def edit_products():
    id = int(input('please enter product id: '))
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i] ['id']== id :
            while True:
                show_edit_menu()
                choice = int(input('choose form edit menu: '))
                if choice == 1:
                    PRODUCTS [i]['name'] = input('enter new name')
                elif choice == 2 :
                    PRODUCTS [i]['price'] = float(input('enter new price'))
                elif choice == 3:
                    PRODUCTS [i]['count'] = int(input('enter new count'))
                elif choice == 4:
                    break
                else :
                    print('error value')
##################################-3
def delet_products():
    id = int(input('choose id : '))
    
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id :
            PRODUCTS.pop(i)
            print('remove')
            break
##################################-4
def search_products():
    user_keyword = input('enter id or name: ')
    
    for i in range(len(PRODUCTS )):
        if PRODUCTS[i]['name']== user_keyword or str(PRODUCTS[i]['id']) == user_keyword: 
            print(PRODUCTS[i])
        
##################################-5
def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i]['id'],PRODUCTS[i]['name'],PRODUCTS[i]['price'],PRODUCTS[i]['count'])
##################################-6
def buy():
    basket =[ ]
    show_list()
    while True:
        id = int(input('enter id'))
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['id'] == id:
                count = int(input('enter count: '))
                if PRODUCTS[i]['count'] >= count:
                    basket.append({'name': PRODUCTS[i]['name']  , 'price': PRODUCTS[i]['price'], 'count': PRODUCTS[i]['count']}  )
                    
                    PRODUCTS[i]['count'] -= count
                    print('products added')
                              
                else:
                    print('not exist')
                    print('we have', PRODUCTS[i]['count'], 'from this product'  )

        choice= input('do you want to continue y/n ')
        if choice == 'N' or choice == 'n':
            break
            
    print(basket)            
    total_price = 0 
    for i in range(len(basket)):
        total_price += basket[i]['price'] * basket[i]['count']
        
    print('total price is ' , total_price )
    print('thanks')
###################################-7
def save_and_exit():
    f = open('database.txt', 'w')

    for i in range(len(PRODUCTS)):
        row = str(PRODUCTS[i]['id'])+ ','+ PRODUCTS[i]['name']+ ',' + str(PRODUCTS[i]['price'])+ ',' + str(PRODUCTS[i]['count']) + '\n'
        f.write(row)
    f.close()
    exit()
###################################
load()
while True:
    show_menu()
    choice = int(input("please choose a number: "))
###################################
    if choice == 1:
        add_products()
    elif choice == 2:
        edit_products()
    elif choice == 3:
        delet_products()
    elif choice == 4:
        search_products()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        save_and_exit() 