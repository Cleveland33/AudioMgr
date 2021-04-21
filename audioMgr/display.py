import os 

def print_menu():
    print("-" * 20)
    print("** Audio Mgr 3000**")
    print("-" * 20)

    print("[1] Register a new Album")
    print("[2] Register a new Song")
    print("[3] Display album catalog")
    print("[4] Print the songs inside album")
    print("[5] Display songs in System")
    print("[6] Total $ in the catalog")
    print("[7] Most Expensive Album")
    print("[10] Change the title of an specific Album")

    print("[q] Quit")



def print_header(text):
    clear()
    print("-" * 30)
    print(text)
    print("-" * 30)    



def clear():
    if(os.name == 'nt' ):
        return os.system("cls")
    else:
        return os.system("clear")

    #return os.system('cls' if os.name == 'nt' else 'clear')