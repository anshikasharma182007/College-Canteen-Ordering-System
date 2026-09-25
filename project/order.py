from menu import menu,display_menu
#To take order
def take_order():
    order=[]
    while True:
        display_menu()
        try:
            choice=int(input("Enter food item number:"))
            if choice not in menu:
                print("Invalid choice! Please select from the menu.")
                continue
            quantity=int(input("Enter quantity:"))
            if quantity<=0:
                print("Quantity must be greater than 0.")
                continue
            item_name=menu[choice][0]
            price=menu[choice][1]
            item_total=price*quantity
            order.append({
                "name":item_name,
                "price":price,
                "quantity":quantity,
                "total":item_total
                })
            print(quantity,item_name,"added to your order.")
            more=input("Do you want to order another item?(yes/no):")
            if more.lower()=="no":
                break
        except ValueError:
            print("Please enter a valid number.")
    return order