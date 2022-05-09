
def main():
    print("XO Game (1.1)  made by Darsh & karkar")
    print()
    print("note: \nYou can choose the required field by entering the place number")
    Box = [True,True,True,True,True,True,True,True,True]
    xo =  ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    _win_or_loss = False
    count = 1
    show_xo(xo)
    while count <= 5:
        number = int(input("First player (X):\n"))
        change(xo ,number ,"X",Box)
        show_xo(xo)
        if count > 2:
            if win_or_loss(xo):
                _win_or_loss = True
                break
        if count == 5:
            break
        number = int(input("Second player (O):\n"))
        change(xo ,number ,"O",Box)
        show_xo(xo)
        if count > 2:
            if win_or_loss(xo):
                _win_or_loss = True
                break
        count += 1
    if _win_or_loss:
        good_by()
    else:
        print("Draw -_-")
        good_by()


        
def show_xo(xo):
    print("______________")
    print(f"| {xo[0]}    {xo[1]}    {xo[2]}|")
    print(f"| {xo[3]}    {xo[4]}    {xo[5]}|")
    print(f"| {xo[6]}    {xo[7]}    {xo[8]}|")
    print("______________")

def change(xo, number, sign,Box):
    count = True
    xo_position = number - 1
    while count:
        if 1 <= number <= 9:
            if verify(Box,number):
                xo[xo_position] = sign ; break
            else:
                number = int(input("Error This box was previously selected\n"))
                xo_position = number - 1 ; continue
        else:
            number = int(input("Wrong number, please choose the number again\n"))
            xo_position = number - 1

def verify (Box,number):
    xo_position = number - 1
    if Box[xo_position] == False:
        return False
    else:
        Box[xo_position] = False
        return True

def win_or_loss (xo):
    if xo[2] == xo[4] == xo[6]:
        how_won(xo,2)
        return True
    elif xo[0] == xo[4] == xo[8]:
        how_won(xo,0)
        return True
    else:
            shift = 0
            while shift != 3:
                if xo[0+shift] == xo[3+shift] == xo[6+shift]:
                    how_won(xo, shift)
                    return True
                shift += 1
            shift = 0
            while shift != 9:
                if xo[0+shift] == xo[1+shift] == xo[2+shift]:
                    how_won(xo,shift)
                    return True
                shift += 3

    return False


def how_won(xo,shift):
    if xo[0 + shift] == "X":
        print("Congratulations\nThe first player won (X)")
    else:
        print("Congratulations\nThe second player won (O)")

def good_by():
    if input("Do u want to try again? y/n \n") == "y" or "Y":
        print("Let's start again (:")
        main()
    else:
        print("/Good by\\")


main()
