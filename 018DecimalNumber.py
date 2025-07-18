from decimal import *
orderTotal = Decimal('100.05')
discountPercent = Decimal('0.10')
discount = orderTotal * discountPercent
finalAmount = orderTotal - discount
taxPercent = Decimal('0.05')
tax = finalAmount * taxPercent
invoiceTotal = finalAmount + tax
print(F"Invoice Total : {invoiceTotal}")