
# 🏦 Mini Budget Manager Challenge #

income = int(input("Enter your monthly income: "))
rent = int(input("Enter your rent: "))
food = int(input("Enter your food expenses: "))
transport = int(input("Enter your transport expenses: "))
entertainment = int(input("Enter your entertainment expenses: "))

# Calculate total expenses

total_expenses = rent + food + transport + entertainment
print(f"Your Total Expense is: ${total_expenses}")

# Calculate remaining moneyv

remaining_money = income - total_expenses
print(f"Your remaining money is: ${remaining_money}")

# Store expenses in a dictionary

expenses ={
            
            "Rent"          : rent,
            "Food"          : food,
            "Transport"     : transport,
            "Entertainment" : entertainment
}

# Calculate percentage of income spent on each category

for item, amount in expenses.items():
    percent = round((amount * 100) / income, 2)
    print(f"You spent {percent}% of your money on {item}")

# Check savings condition

if remaining_money >= 10000:
    print('You are saving well this month!')

elif 0 < remaining_money < 10000:
    print("In this month you are not saving well.")
elif remaining_money < 0:
    print("You are overspending! Reduce expenses!")

# Summary

all_together = (f"A family spends their money on different things. After the month ends, their income is ${income}, total expenses are ${total_expenses}, so they have ${remaining_money} left.")

print(all_together)
