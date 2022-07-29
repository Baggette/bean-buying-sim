print("Beans are 500$ \n Please insert cash")
cash = input()

try:
    cash = int(cash)
    if int(cash) == 500:
        print("Ok you got some beans")
    elif int(cash) < 500:
        print("Get more money you scrub")
    elif int(cash) > 500:
        change = int(cash) - 500
        print("You had more than enough for your beans. \n Heres your change " + str(change) + "$")
except ValueError:
    print("Thats not a fucking number")
    bean = input("Press enter to exit...")
    if str(bean) == "beans":
        print("Insert easter egg here. \n Bean sim created by Baggette \n I would Like to give a Special thanks to the \n one \n the \n only \n BEANS!!!!!! \n Press enter to exit (fr this time)...")
        input()
    else:
        exit()