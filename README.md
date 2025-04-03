# PyBank: Financial Analysis

# Project Description
In the PyBank challenge, we analyze a company’s financial records to calculate key metrics, including total months, net profit/loss, average changes, and the greatest increases and decreases in profits.

# Key Calculations
Total Months: Counts the number of unique months in the dataset.
Net Total Profit/Loss: Sums up all the "Profit/Losses" entries.
Average Change: Calculates the average change in profit/loss between consecutive months.
Greatest Increase in Profits: Identifies the month and value of the highest profit increase.
Greatest Decrease in Profits: Identifies the month and value of the highest profit decrease.

# How to Run
Navigate to the PyBank directory:
cd python-challenge/PyBank
Run the script:
python main.py

The results will be displayed in the terminal and saved to financial_analysis.txt in the analysis/ folder.
PyPoll: Election Analysis

# Project Description
The PyPoll challenge involves analyzing a rural town’s election data to calculate voting outcomes, including total votes, candidate vote percentages, and the overall winner.

# Key Calculations
Total Votes Cast: Counts the number of entries in the dataset.
Candidate List: Identifies all unique candidates who received votes.
Vote Percentage: Calculates the percentage of votes each candidate won.
Vote Count: Determines the total number of votes each candidate received.
Election Winner: Identifies the candidate with the most votes.

# How to Run
Navigate to the PyPoll directory:
cd python-challenge/PyPoll
Run the script:
python main.py

The results will be displayed in the terminal and saved to election_results.txt in the analysis/ folder.
 
# Libraries and Modules

csv: To read and process the input CSV files.
os: To handle file paths and directory operations.
Challenges and Solutions

# Challenge: Handling Large Datasets
Solution: Implemented optimized list processing and efficient data aggregation to reduce processing time.

Challenge: Data Formatting and Output
Solution: Used formatted strings to ensure consistent presentation of numeric data and percentages.

Challenge: Script Reusability
Solution: Modularized code to make it easily adaptable to different datasets.# python-challenge
