#	Asosiy boshqaruv: foydalanuvchi bilan ishlash


# main.py

import sys
from Valyuta_kurs.meny import print_menu
from Valyuta_kurs.EUR  import EUR_Valyuta
from Valyuta_kurs.USD import USD_Valyuta


def main():
    while True:
        print_menu()
        choice = input("Tanlang (1-3): ")

        if choice == "1":
            EUR_Valyuta()
        elif choice == "2":
            USD_Valyuta()
        elif choice == "3":
            print("Dastur tugadi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov, qaytadan urinib ko‘ring!")

if __name__ == "__main__":
    main()

    
