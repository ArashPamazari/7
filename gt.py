def show_menu():
    print('1-add new word')
    print('2-translation english to persian')
    print('3-translation persian to english')
    print('4-exit')

mainFile = []

def load():
    print('loading...')
    try:
        databaseGT = open('databasegt.txt', 'r').read()
    except FileNotFoundError:
        print("File does not exist!")
    
    D = databaseGT.split('\n')
      
    for i in range(len(D)):
        data = D[i].split(',')
        mainFile.append({'english':data[0], 'persian':data[1]} )
  
    print('program is ready to use')  
    print(mainFile) 
   
   
load() 
        
def add_new_word():
    english = input('english: ')
    persian = input('persian: ')
    mainFile.append({'english':english, 'persian':persian})


def english_to_persian():
    words = []

    sentence = input('sentence in english : ').split(' ')

    for i in range(len(sentence)):
        data = sentence[i].split(',')
        words.append({'english':data[0]} )

    
    for i in range(len(words)):
        if mainFile[i]['english'] == words[i]['english']: 
            print(mainFile[i]['persian'])
        else:
            pass    
                                   

            
                  
            

def persian_to_english():
    pass    



def search(argument):
    for item in mainFile:
        if item['english'] == argument or item['persian'] == argument:
            return item
    return False    

def save_and_exit():
    databaseGT = open('databasegt.txt', 'w')
    for item in mainFile:
        databaseGT.write(item['english'] + '\n' + item['persian'] + '\n')
    databaseGT.close()
    exit()
        
   
while True:
    show_menu()    
    choice = int(input('Please choose a number: '))

    if choice == 1:
        add_new_word()
    elif choice == 2:
        english_to_persian()
    elif choice == 3:
        persian_to_english()
    elif choice == 4:
        save_and_exit()
