PRICE = 200

discount_10 = ['STUDENT10','SPRING10','MEMBER123']

buyer_code = input("Please type your discount code: ")

print('processing....\n')

if buyer_code in discount_10:
    final_price = PRICE * 0.9
    print("10% discount applied \n")
else:
    final_price = PRICE
    print("No discount applied \n")


print("Please pay pound{} at checkout".format(final_price))
