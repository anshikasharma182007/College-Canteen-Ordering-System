from billing import calculate_subtotal
from billing import apply_discount
#display order summary
def display_summary(order):
   print("\n===============================")
   print(("        ORDER SUMMARY"))
   print(("=============================="))
   for item in order:
       print(
           item["name"],
           "x",
           item["quantity"],
           "= Rs.",
           item["total"]
           )
   subtotal=calculate_subtotal(order)
   discount_rate,discount_amount,final_amount=apply_discount(subtotal)
   print("----------------------------------")
   print("Subtotal        : Rs.",subtotal)
   print("Discount        : Rs.",discount_rate,"%")
   print("Discount Amount : Rs.",discount_amount)
   print("Final Amount    : Rs.",final_amount)
   print("==================================")
   print(("    THANK YOU FOR YOUR ORDER!"))
   print(("================================="))