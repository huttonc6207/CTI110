## CTI-110
##M2HW2 - TIP TAX AND TOTAL
#CHARLES HUTTON
#31 AUG 2017


#Variables
#foodCost - tipAmmount 0.18 - totalCost - salesTax 0.07

#coDe - with set tip and tax

foodCost = float(input('How much was your meal?'))

tipAmmount = 0.18 * foodCost

tipTotal = tipAmmount + foodCost

print('The total cost of meal with tip is $', format(tipTotal, ',.2f'))

salesTax = 0.07 * foodCost

taxTotal = salesTax

print('The tax for your meal is $', format(taxTotal, ',.2f'))

totalCost = foodCost + tipAmmount + salesTax

print('The total cost of your meal plus tax and tip is $', format(totalCost, ',.2f'))

