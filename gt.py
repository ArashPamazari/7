def show_menu():
    print('1-add new word')
    print('2-translation english to persian')
    print('3-translation persian to english')
    print('4-exit')

mainFile = []

def load():
    print('loading...')
    try:
        databaseGT = open('translate.txt', 'r').read()
    except FileNotFoundError:
        print("File does not exist!")
    
    D = databaseGT.split('\n')
    print(D)  
    for i in range(len(D)):
        #data = D[i].split(',')
        if i%2==0:
            mainFile.append({'english':D[i], 'persian':D[i+1]})
  
    print('program is ready to use')  
    print(mainFile) 
   
   
load() 
        
def add_new_word():
    english = input('english: ')
    persian = input('persian: ')
    mainFile.append({'english':english, 'persian':persian})


def english_to_persian():
    sentence = input('sentence in english : ').split(' ')

    for i in range(len(mainFile)):
        for j in range(len(sentence)):
            if mainFile[i]['english']==sentence[j]:
                print(mainFile[i]['persian'],end=' ')

    print()            

def persian_to_english():
    sentence = input('sentence in persian : ').split(' ')

    for i in range(len(mainFile)):
        for j in range(len(sentence)):
            if mainFile[i]['persian']==sentence[j]:
                print(mainFile[i]['english'],end=' ')   
    print()             
   

def save_and_exit():
    databaseGT = open('translate.txt', 'w')
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
