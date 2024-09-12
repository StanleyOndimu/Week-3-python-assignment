def calculate_discount():
  price = int(input('Enter the price of your item: '))
  discount_percent = int(input('Enter the discount for you item: '))
  if discount_percent > 20:
    discount = price * discount_percent/100
    new_price = price - discount
    print(new_price)
  else:
    print(price)
    

calculate_discount()