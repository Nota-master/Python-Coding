#Activitys and costs
print("These are the activites and costs")
print("number   activity                days  difficulty    cost")
print("0        cultural immersion      5     easy          800")
print("1        kayaking and pancakes   3     moderate      400")
print("2        mountain biking         4     difficult     900")

#What is your name?
first_name = ""
current_age = ""

# Get name (no digits allowed)
while len(first_name) == 0 or first_name.isdigit():
    first_name = input("What is your name: ")
    if len(first_name) == 0:
        print("You must enter a name!")
    elif first_name.isdigit():
        print("Name cannot be numbers!")

# Get age (digits only)
# Prompt user for age
age_input = input("Enter your age (15-18): ")
current_age = ""

# Check if input is digits only
if age_input.isdigit():
    age = int(age_input)
    # Check the range (15-18)
    if 15 <= age <= 18:
        print("welcome to the camp, " + first_name + "!")
    else:
        print("Sorry, you must be between 15 and 18 years old.")
else:
    print("Invalid input. Please enter numbers only.")


#Age limit to become camp leader
# Camp Leader Age Checker
def check_leader_eligibility():
    try:
        # Prompt user for age
        print("Do you want to become camp leader?")
        age = int(input("Enter your age: "))
        
        # Check eligibility
        if 15 <= age <= 18:
            print("Yes, you are old enough to become a camp leader!")
        elif age < 15:
            print("You are too young to be a leader, but can join as a camper.")
        else:
            print("You are too old to be a camper/leader, try our adult workshops.")
            
    except ValueError:
        print("Please enter a valid numerical age.")

# Run the function
check_leader_eligibility()

#lists activities = ["cultural immersion", "kayaking and pancakes", "mountain biking"]
meal = input("What meal do you want (standard, vegetarian, vegan):")
print(f"You have chosen the {meal} meal.")
camp_number = [0,1,2]
camp_choice = input("Enter camp number (0, 1, or 2): ")
print(f"You have chosen camp {camp_choice}")
activity_choice = input("What activity do you want to do? (cultural immersion, kayaking and pancakes, mountain biking): ")
print(f"You have chosen the activity: {activity_choice}")
days = input("How many days do you want to stay? (5, 3, or 4): ")
print(f"You have chosen to stay for {days} days.")
difficulty = input("What difficulty level do you want to do? (easy, moderate, difficult): ")
print(f"You have chosen the difficulty level: {difficulty}")
cost = input("What is your budget for the camp? (800, 400, or 900): ")
print(f"You have a budget of: {cost}")
print("You have chosen the following options:")
print(f"Meal: {meal}")
print(f"Camp: {camp_choice}")
print(f"Activity: {activity_choice}")
print(f"Days: {days}")
print(f"Difficulty: {difficulty}")
print(f"Cost: {cost}")
print("Do you want anything else?: ")