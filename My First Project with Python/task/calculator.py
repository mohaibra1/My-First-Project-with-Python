# Write your code here
print("""
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80
Income: $5405.0
""")

print('Income: $5405')
print('Staff expenses:')
staff_expense = int(input())
print('Other expenses:')
other_expense = int(input())
print('Net income: $' + str(5405 -(staff_expense + other_expense)))