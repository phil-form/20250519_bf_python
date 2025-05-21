wrong_input = True

while wrong_input:
    try:
        x = int(input("enter a number: "))
        print('riri')
        wrong_input = False
        y = x / 0
    except ValueError:
        print("Error: you did not enter a number")
    except:
        print("other errors")