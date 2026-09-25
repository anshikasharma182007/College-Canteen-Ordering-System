#COLLEGE CANTEEN FOOD ORDERING SYSTEM
#Food menu
menu={
      1: ("Burger",80),
      2: ("Pizza",120),
      3: ("Sandwhich",60),
      4: ("Momos",70),
      5: ("Coke",40)
      }
#To display menu
def display_menu():
    print("\n===============================")
    print(("    COLLEGE CANTEEN MENU"))
    print(("=============================="))
    for number,item in menu.items():
        print(number,".",item[0],"-Rs.",item[1])
    print("===============================")
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
#To calculate subtotal
def calculate_subtotal(order):
    subtotal=0
    for item in order:
        subtotal=subtotal+item["total"]
    return subtotal 
#To apply discount
def apply_discount(subtotal):
    if subtotal>=500:
        discount_rate=20
    elif subtotal>=300:
        discount_rate=10
    else:
        discount_rate=0
    discount_amount=subtotal*discount_rate/100
    final_amount=subtotal-discount_amount
    return discount_rate,discount_amount,final_amount
#display order summary
def display_summary(order):
   print("\n===============================")
   print(("        ORDER SUMMARY"))
   print(("=============================="))
   for item in order:
       print(
           item["name"],
           "x",
           item["quantity"],
           "= Rs.",
           item["total"]
           )
   subtotal=calculate_subtotal(order)
   discount_rate,discount_amount,final_amount=apply_discount(subtotal)
   print("----------------------------------")
   print("Subtotal        : Rs.",subtotal)
   print("Discount        : Rs.",discount_rate,"%")
   print("Discount Amount : Rs.",discount_amount)
   print("Final Amount    : Rs.",final_amount)
   print("==================================")
   print(("    THANK YOU FOR YOUR ORDER!"))
   print(("================================="))
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
    