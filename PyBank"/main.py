# Dependencies
# Import necessary libraries
import csv

# Define the file path
file_path = '''/Users/esteban/Desktop/Data Analyst BC/Module 3_Python/python-challenge/PyBank"/Resource"/budget_data.csv'''

# variables
total_months = 0
total_profit_losses = 0
changes = []
previous_profit = None
max_increase = {"date": "", "value": float('-inf')}
max_decrease = {"date": "", "value": float('inf')}

# Open and read the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        date, profit_loss = row[0], int(row[1])
        
        # Increment total months and add to total profit/losses
        total_months += 1
        total_profit_losses += profit_loss

        # Calculate changes in profit/losses
        if previous_profit is not None:
            change = profit_loss - previous_profit
            changes.append(change)

            # Check for max increase
            if change > max_increase["value"]:
                max_increase = {"date": date, "value": change}

            # Check for max decrease
            if change < max_decrease["value"]:
                max_decrease = {"date": date, "value": change}

        previous_profit = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase['date']} (${max_increase['value']})")
print(f"Greatest Decrease in Profits: {max_decrease['date']} (${max_decrease['value']})")

# Write results to a text file
output_path = 'financial_analysis.txt'
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Net Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {max_increase['date']} (${max_increase['value']})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease['date']} (${max_decrease['value']})\n")
