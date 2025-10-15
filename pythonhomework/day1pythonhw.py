p_rice = 45
p_sugar = 40
p_oil = 130

q_rice = 3
q_sugar = 2.5
q_oil = 1.8

totalprice_rice = p_rice * q_rice
totalprice_sugar = p_sugar * q_sugar
totalprice_oil = p_oil * q_oil

print("Total price of rice :" , totalprice_rice)
print("Total price of sugar :" , totalprice_sugar)
print("Total price of oil :" , totalprice_oil)

total_bill = totalprice_rice + totalprice_sugar + totalprice_oil

print("Total bill is :" , total_bill)

tot_bill_int = int(total_bill)
tot_bill_str = str(tot_bill_int)

print( "Total_billstr :",  tot_bill_str)

import random

delivery_charge = random.randint(5, 10)

final_bill = tot_bill_int + delivery_charge

print("Final bill is :" , final_bill)