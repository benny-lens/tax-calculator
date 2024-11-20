print(input("Hello dear, what would you like to buy from us?"))
purchase_amount = int(input("Input purchase price of items in ($): "))

if purchase_amount < 100:
    discount = 0
    tax = 0.05 * purchase_amount
    actual_purchase_price = purchase_amount - discount + tax

elif purchase_amount <= 500:
    discount = 0.1 * purchase_amount
    tax = 0.05 * purchase_amount
    actual_purchase_price = purchase_amount - discount + tax

elif purchase_amount > 500:
    discount = 0.2 * purchase_amount
if discount < 200:
     tax = 0.05 * purchase_amount
     actual_purchase_price = purchase_amount - discount + tax
else:
    tax = 0.08 * purchase_amount
    actual_purchase_price = purchase_amount - discount- tax  
print(f"Your purchase price is ${purchase_amount}")
print(f"Your Discount: ${discount}")
print(f"Tax Applied: ${tax}")
print(f"Total Amount To Pay: ${actual_purchase_price}")
print("Thank you and have a nice day.")