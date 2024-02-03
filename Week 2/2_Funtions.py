bill_input = input("Enter total bill: ")
bill = float(bill_input)
rate_input = input("Enter the total tax rate: ")
tax_rate = float(rate_input)


# Without functions in computation
# total_tax = (bill*tax_rate)

# print("Total tax charged for amount "+str(bill)+" is "+str(total_tax))
# Using function to compute
def compute_tax(bill, tax_rate):
    return bill * tax_rate


print("Total tax charged for amount " + str(bill) + " is " + str(compute_tax(bill, tax_rate)))
