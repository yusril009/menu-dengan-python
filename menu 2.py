def show_menu():
    print("""
    1. menampilkan
    2. exit
    """)
    menu = input("masukan nomor: ")

    if menu == "1":
        text = input("masukan text: ")
        print(text)
        show_tanya()
    elif menu == "2":
        print("Have a Nice Day!\n")
    else:
        print("masukan nomor yang ada!")
        show_menu()

def show_tanya():
    tanya = input("Apakah mau melanjutkan ke menu y/n? ")

    if tanya == "y" or tanya == "Y":
        show_menu()
    elif tanya == "n" or tanya == "N":
        print("Have a nice day!\n")
    else:
        print("masukan yang bener dong!")
        show_tanya()

show_menu()
