#Question 1
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
#Question 2 
try:
    price = float(input("Enter original price of item"))
    
    discount_percent = float(input("Enter discount percent"))
    
    final_price = calculate_discount(price, discount_percent)
    
    if discount_percent >= 20:
        print(f"The final price after applying discount is: {final_price}")
    else:
        print(f"Discount less than 20%. Original price remains: {price}")

except ValueError:
    print("Enter valid numeric values for price and discount percentage.")
