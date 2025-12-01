

# 🏦 Mini Budget Manager Challenge #

income = 50000
rent = 12000
food = 8000
transport = 5000
entertainment = 3000

total_expenses = rent + food + transport + entertainment
print(f"Your Total Expense is: ${total_expenses}")


remaining_money = income - total_expenses
print(f"Your remaining money is: ${remaining_money}")


expenses ={
            
            "Rent"          : rent,
            "Food"          : food,
            "Transport"     : transport,
            "Entertainment" : entertainment
}

for item, amount in expenses.items():
    percent = round((amount * 100) / income, 2)
    print(f"You spent {percent}% of your money on {item}")


if remaining_money >= 10000:
    print('You are saving well this month!')

elif 0 < remaining_money < 10000:
    print("In this month you are not saving well.")
elif remaining_money < 0:
    print("You are overspending! Reduce expenses!")


all_together = (f"A family spends their money on different things. After the month ends, their income is ${income}, total expenses are ${total_expenses}, so they have ${remaining_money} left.")


print(all_together)