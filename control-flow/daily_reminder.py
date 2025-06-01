task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")


match priority :
    case 'high' :
        reminder = f"'{task}' is a high priority task"
    case 'medium' : 
        reminder = f"'{task}' is medium priority task"
    case 'low':
        reminder = f"'{task}' is low priority task"
    case _:
        reminder = f"'{task}' has unknown priority"
if time_bound == "yes" :
    if priority in ['high','medium']:
        reminder+= " that requires immediate attention today!"
    else :
        reminder += "."
elif time_bound == "no":
    if priority == 'low' :
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."
    
if time_bound == 'yes':
    print(f"Reminder: {reminder}")
else :
    print(f"Note: {reminder}")
        