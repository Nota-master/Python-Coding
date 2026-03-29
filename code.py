#Activitys and costs.
print("These are the activites and costs")
print("number   activity                days  difficulty    cost")
print("0        cultural immersion      5     easy          800")
print("1        kayaking and pancakes   3     moderate      400")
print("2        mountain biking         4     difficult     900")

#What is your name?.
first_name = ""
current_age = ""

# Get name (no digits allowed).
while len(first_name) == 0 or first_name.isdigit():
    first_name = input("What is your name: ")
    if len(first_name) == 0:
        print("You must enter a name!")
    elif first_name.isdigit():
        print("Name cannot be numbers!")

# Get age (digits only).
# Prompt user for age.
age_input = input("Enter your age (15-18): ")
current_age = ""

# Check if input is digits only.
if age_input.isdigit():
    age = int(age_input)
    # Check the range (15-18).
    if 15 <= age <= 18:
        print("welcome to the camp, " + first_name + "!")
    else:
        print("Sorry, you must be between 15 and 18 years old.")
else:
    print("Invalid input. Please enter numbers only.")

# do you want to be a camp leader?.
leader_choice = input("Do you want to be a camp leader? (yes or no): ")
if leader_choice.lower() == "yes":
    print("Great! You will be a camp leader.")
elif leader_choice.lower() == "no":
    print("No problem! You can still enjoy the camp activities.")

#lists activities = ["cultural immersion", "kayaking and pancakes", "mountain biking"].
meal =  input("What meal do you want standarad vegetraian or vegan? (standard, vegetarian, vegan): ")     
print(f"You have chosen the meal: {meal}")  
camp_number = [0,1,2]
camp_choice = input("Enter camp number (0, 1, or 2): ")
if camp_choice in ["0", "1", "2"]:
print(f"You have chosen camp number {camp_choice}")
activity_choice = input("Enter activity number (0, 1, or 2): ")
print(f"You have chosen activity {activity_choice}")
days = input("How many days do you want to stay? (5, 3, or 4): ")
print(f"You have chosen to stay for {days} days.")
difficulty = input("What difficulty level do you want to do? (easy, moderate, difficult): ")
print(f"You have chosen the difficulty level: {difficulty}")

#Your choices you have chosen.
print("You have chosen the following options:")
print(f"Meal: {meal}")
print(f"Camp: {camp_choice}")
print(f"Activity: {activity_choice}")
print(f"Days: {days}")
print(f"Difficulty: {difficulty}")

#total cost'
if activity_choice == "0":
    cost = 800
elif activity_choice == "1":
    cost = 400
elif activity_choice == "2":
    cost = 900
print(f"The total cost of your chosen activity is: ${cost}")

#shuttle bus.
shuttle_choice = input("Do you want to use the shuttle bus service it will be an extra $80 (yes or no): ")
if shuttle_choice.lower() == "yes":
    print("You have chosen to use the shuttle bus service.")
    total_cost = cost + 80
    print(f"The total cost including shuttle bus service is: ${total_cost}")
elif shuttle_choice.lower() == "no":
    print("You have chosen not to use the shuttle bus service.")
    print(f"The total cost of your chosen activity is: ${cost}")

#enjoy your camp experience.
print("Enjoy your camp experience, " + first_name + "!")