# Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a
# product name and print the corresponding price or a message if the product is not in the
# dictionary.

number = int(input("Enter the number of products :"))
dictionary = {}
for i in range (number):
    product_name = input("Enter the name of product :")
    price = int(input("Enter the price of the product :"))
    dictionary.update({product_name:price})

while(i):
    print("Enter -1 to exit")
    search = input("Enter the product :")
    if search in dictionary:
        print("Price :",dictionary[search])
    if search == '-1':
        print("Exiting...")
        exit(1)
    if not(search in dictionary):
        print("Product not found ")
    
