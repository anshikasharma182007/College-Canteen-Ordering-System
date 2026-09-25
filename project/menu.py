#COLLEGE CANTEEN FOOD ORDERING SYSTEM
#Food menu
menu={
      1: ("Burger",80),
      2: ("Pizza",120),
      3: ("Sandwich",60),
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