room_available = True
nights = 3
price_per_night = 2500
is_member = True 
#  Task1 check room availability and valid nights 
if room_available  == True and nights> 0  :
    print("Rooms Available")
    # total price
    total_price = nights*price_per_night
    print("Original Price:", total_price)
    #  discount 
    if is_member and nights >=3:
         discount_rate = 15
         print("Discount Rate:", discount_rate, "%")
    elif not is_member and nights>=3:
         discount_rate =13
         print("Discount Rate:", discount_rate, "%")
    else:
         discount_rate = 0
         print("Discount Rate:", discount_rate, "%")
    # calculate the discount 
    discount = total_price*discount_rate/100
    print("Discount Amount:", discount)
    final_bill = total_price - discount
    print("Final Bill:", final_bill)
else:
     print("Booking Unavailabe")
