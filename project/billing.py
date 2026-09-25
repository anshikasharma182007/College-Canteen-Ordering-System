#To calculate subtotal
def calculate_subtotal(order):
    subtotal=0
    for item in order:
        subtotal=subtotal+item["total"]
    return subtotal 
#To apply discount
def apply_discount(subtotal):
    if subtotal>=500:
        discount_rate=20
    elif subtotal>=300:
        discount_rate=10
    else:
        discount_rate=0
    discount_amount=subtotal*discount_rate/100
    final_amount=subtotal-discount_amount
    return discount_rate,discount_amount,final_amount