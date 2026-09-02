savings_goal = 10000
user_savings = int(input("Enter your initial saving amount? "))
while True:
    
    if (user_savings < savings_goal):
        print(f"You are: {savings_goal-user_savings}ksh away from your goal. Your current savings is: {user_savings}ksh. Keep pushing")
        additional_savings = int(input("Enter your additional savings from the last check: "))
        user_savings += additional_savings
        continue
    elif (user_savings == savings_goal):
        print("You have reached your savings goal. Congrats big man")
        break
    elif (user_savings > savings_goal):
        print(f"You have exceeded your goal by: {user_savings - savings_goal}ksh. Wow, that's impressive")
        break
    else:
        print("Enter a valid number")