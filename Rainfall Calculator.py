# Program to calculate and display the average rainfall over a certain number of years

# List of months available to input
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

# Have user input number of years with exception handling
while True:
    try:
        num_years = int(input("Enter the number of years: "))
        if num_years <= 0:
            print("Error: Number of years cant be negative.")
        else:
            break
    except ValueError:
        print("Error: Please enter a integer for the number of years.")

# Initialize total rainfall accumulator
total_rainfall = 0

# Loop through each year
for year in range(1, num_years + 1):
    print(f"For year {year}:")

    # Loop through each month
    for month in months:
        while True:
            try:
                rainfall = float(input(f"Enter the rainfall amount for {month}: "))
                if rainfall < 0:
                    print("Error: Rainfall amount cannot be negative. Redo and enter a valid value.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a numeric value for the rainfall amount.")

        # Add to running taly total of rainfall.
        total_rainfall += rainfall

# Calculate total months
total_months = num_years * 12

# Calculate average rainfall per month with the formula.
average_rainfall = total_rainfall / total_months

# Display results
print(f"For {total_months} months:")  # f-strings allow  variables directly be in the strings.
print(f"Total rainfall: {total_rainfall:.2f} inches")  # .2f ensures the number is formatted to two decimal places
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")

