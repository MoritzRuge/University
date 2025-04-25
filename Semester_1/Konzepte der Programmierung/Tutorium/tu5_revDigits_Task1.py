user_list = input("Geben sie Ihre natürlichen Zahlen ein: ")

def revDigits(list):
    rev_list = list[::-1]
    return rev_list


print(revDigits(user_list))
