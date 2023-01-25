def deposit():
    while True:
        amount = input("How much money do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0.")
        else:
            print("Please input number.")
    return amount

deposit()