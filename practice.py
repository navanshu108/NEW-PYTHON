# short hand if else
# a=int(input("type any nummber"))
# b=int(input("type any nummber"))
# print(f"{a}") if a>b else print(f"{b}")

#using  guards (extra conditions with if)
month= int(input("type month no. :"))
day =int(input("type day :"))
match month :
    case 1 if day == 1:
        print("monday in month january")
    case 2 if day == 2:
        print("tuesday in month february")
    case 3 if day == 3:
        print(" wednesday in month march")
    case 4 if day == 4:
        print("thursday in month april")
    case 5 if day == 5:
        print("friday in month may")
    case 6 if day ==6 :
        print("saturday in month june")
    case 7|8|9|10|11|12 if day ==7:
        print("sunday")
    case _:
        print("invalid")
        