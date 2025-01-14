import inventory
import menu

def deductResource(str):
    storageIHave= inventory.storage
    required = menu.menu[str]['ingredient']

    for key,value in required.items():
        storageIHave[key]-=required[key]

    storageIHave["Money"]+=menu.menu[str]["cost"]


def returnChange(moneyGiven,inp):
    moneyReq= menu.menu[inp]["cost"]

    return moneyGiven-moneyReq




def isFulfillable(str):
    storageIHave= inventory.storage
    #print(str)
    required= menu.menu[str]

    orgReq= required['ingredient']
    #print(orgReq)

    for key,value in orgReq.items():
        #print(key,value)
        if storageIHave[key]<value:
            print("There is insufficient ",key)
            return False

    return True

while True:
    print("===============================Welcome to Prajwal's Coffee Dispenser============================")
    inp= input("What do you want(espresso/latte/cappuccino)?:")

    if inp=='report' or inp=='Report':
        rep=inventory.storage
        for key,value in rep.items():
            if key=='Water' or key=='Milk':
                print(key,value,'ml')

            elif key=='Coffee':
                print(key,value, 'gm')

            else:
                print(key,'Rs.',value)

    elif inp=='off':
        break

    #elif inp=='refill':


    else:
        if isFulfillable(inp):
            moneyGiven=0
            fiveHundred= int(input("Rs.500 Bills:"))
            twoHundred = int(input("Rs.200 Bills:"))
            oneHundred= int(input("Rs.100 Bills:"))
            fifty= int(input("Rs.50 Bills:"))

            moneyGiven= fiveHundred*500+ twoHundred*200+ oneHundred*100+ fifty*50

            if moneyGiven< menu.menu[inp]['cost']:
                print("Insufficient money paid, your money will be refunded!")
                pass

            else:
                print("Making your coffee!")
                deductResource(inp)
                print("Here is your coffee!")
                change= returnChange(moneyGiven,inp)
                print("Here is your change of, Rs.",change)
                print("Enjoy your Coffee!")


        else:
            print("Sorry, try another coffee or please come tomorrow")