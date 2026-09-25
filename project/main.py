from menu import display_menu
from order import take_order
from summary import display_summary
#Main function
def main():
    print("\n===============================")
    print(("    COLLEGE CANTEEN MENU"))
    print(("=============================="))
    while True:
        print("\n1.Display menu")
        print("2.Place Order")
        print("3.Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            display_menu()
        elif choice=="2":
            order=take_order()
            if len(order)==0:
                print("No items were ordered.")
            else:
                display_summary(order)
        elif choice=="3":
            print("Thank you! Visit again.")
            break
        else:
            print("Invalid choice. Please try again.")
#Start
if __name__ == "__main__":
    main()
    