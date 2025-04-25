def main():
    grocery_list()




def grocery_list():
    grocerys = {}
    


    print("Bitte Produkt eingeben:")
    while True:
        try:
            product = input("").upper()
            if product in grocerys:
                # return the value for key if key is in the dictionary
                item = grocerys.get(product)
                item += 1 # updated the value of the product +1
                grocerys[product] = item # updates the value in the dictionary
                
            else:
                # if the product is not in the dictionary, set the value of the product to 1
                grocerys[product] = 1
        except EOFError:
            # Sort the grocery_list
            
            # print every product of the grocery_list
            print("Ihre Einkaufsliste:")
            # Sort the grocerys dict
            ## begin with sorting of the origianl dict keys
            sorted_keys = sorted(grocerys.keys())
            # create a new dict to store the sorted key and assaign the corosponding values
            sorted_dict = {key: grocerys[key] for key in sorted_keys}

            for key in sorted_dict:
                print(sorted_dict[key], key)
            # break the loop or something else
            break
    
    


if __name__ == "__main__":
    main()