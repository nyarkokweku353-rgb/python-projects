#print f and l name
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print(f"Your name is {first_name} {last_name}.") #assignment 1a

#greeting message
print("Good day, welcome to the Goat Assignment!")
pet = input("What is your pet's name? ")
city = input("What city do you live in? ")
print(f"Your new twitter handle and bio @cyber{pet} from {city}.") #assignment 2a

#scores 101
print("Good day, welcome to the Goat Assignment3!")
score = int(input("Score should be between 0 and 188: "))
if score < 0 or score > 188:
  print("Invalid score. Please enter a score between 0 and 188.")
else:
  if score >= 97:
    print("Grade A")
  elif score >= 77:
    print("Grade B")
  elif score >= 67:
    print("Grade C")
  else:
    print("Grade D")

#scores 102
print("Good day, welcome to the Goat Assignment3!")
score = int(input("Score should be between 0 and 188: "))
if score < 0 or score > 188:
  print("Invalid score. Please enter a score between 0 and 188.")
else:
  match score:
    case s if s >= 97:
        print("Grade A")
    case s if s >= 77:
      print("Grade B")
    case s if s >= 67:
      print("Grade C")
    case _ :
      print("Grade D")#assignment3

#Fizzbuzz challenge
print("Welcome to Fizzbuzz!")
number = int(input("Please enter a number: "))
for num in range(1, number + 1):
  if num % 3 == 0 and num % 5 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("buzz")
  elif num % 3 == 0:
    print("Fizzbuzz")
  else:
    print("sorry")#assignment4a

#New Fizzbuzz challenge
print("Welcome to Fizzbuzz!")
number = int(input("Please enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Fizzbuzz")
elif number % 5 == 0:
    print("buzz")
elif number % 3 == 0:
    print("Fizz")
else:
    print("sorry")#assignment4b

print("Welcome to the Goat")

#mearsurment project
def calculate(w, h):   
    s = w * h
    print(s)

w = float(input("Width: "))
h = float(input("Height: "))

calculate(w, h)#assignment6
