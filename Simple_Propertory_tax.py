# Global constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Get the amount of the purchase
purchase = float(input('Enter the purchase amount: '))

# Calculate the state tax
stateTax = purchase * STATE_TAX_RATE

# Calculate the county tax
countyTax = purchase * COUNTY_TAX_RATE

# Calculate total tax
totalTax = stateTax + countyTax

# Calculate total sale amount
totalSale = purchase + totalTax

# Display the results
print(f'Purchase amount: {purchase:,.2f}')
print(f'State tax: {stateTax:,.2f}')
print(f'County tax: {countyTax:,.2f}')
print(f'Total tax: {totalTax:,.2f}')
print(f'Sale total: {totalSale:,.2f}')
