# QAP 4 - Graph

"""
 A program that takes the total monthly sales for each month for
 a business and then makes a bar graph to represent the data.
"""

# Date: 2023-03-21
# Author: Michael Bennett

# Imports
import matplotlib.pyplot as plt

# Get the total sales for each month from the user.
# And put those values in a list.
monthly_sales = []
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for month in months:
    sales = float(input(f'Enter the total sales for {month}: '))
    monthly_sales.append(sales)

# Make the graph
plt.figure(facecolor='#A6ACAF')
plt.bar(months, monthly_sales, color='#1F618D')
plt.title('Total Sales by Month', fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales ($)', fontsize=14)
plt.grid(axis='y')
plt.xticks(rotation=45)

plt.show()
