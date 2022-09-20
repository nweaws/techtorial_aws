

# ask user's name and last name and print first name and last name together
print("please enter your first name ")
first_name = input()

#print(first_name)

print("please enter your last name")
last_name = input()

#print(first_name+ " "+ last_name)
print(first_name,last_name)

#input() function will always creata a string value
# Ask user to enter my string value, then ask user to guess the length of the string.
# If user's guess is true print true , if not print false

print("Enter any text")
text = input()
# length
print("please guess the length of the text")
user_guess = input()


# Can we do it without converting in to an integer?
# We can do it using str() function.
# str() function will convert given value in to a string
length_of_str = str(len(text))
print(user_guess == length_of_str)
print(type(user_guess))
user_guess = int(user_guess)
# To compear user's guess with the actual length of the string
# I have to convert user's guess in to integer type

is_user_correct = len(text)== user_guess
print(is_user_correct)




