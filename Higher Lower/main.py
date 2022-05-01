import random
from game_data import data
# TODO 1: Pull data from dictionary and present it to user
    # Only display relevant information
a = random.choice(data)
b = random.choice(data)
# while b == a:
#     b = random.choice(data)
print("Welcome to the higher/lower game! Your goal is to guess which Instagram account has more followers.")
continue_variable = 1

while continue_variable == 1:
    while b == a:
        b = random.choice(data)
    a_name = a['name']
    a_followers = a['follower_count']
    a_description = a['description']
    a_country = a['country']

    b_name = b['name']
    b_followers = b['follower_count']
    b_description = b['description']
    b_country = b['country']

    print(f"Option a is: {a_name}, {a_description}, {a_country}. ")
    print(f"Option b is: {b_name}, {b_description}, {b_country}. ")

    # TODO 2: Give user option a or b
    user_answer = input("Who has more followers? Type 'a' or 'b'. ").lower()

    # TODO 3: Determine if user is correct
        # Make way for game to end when user is wrong
            # done by making it a while loop
    correct_answer = "none"
    def compare(a_option, b_option):
        global correct_answer
        if a_followers > b_followers:
            correct_answer = a_option
            return "a"
        elif a_followers < b_followers:
            correct_answer = b_option
            return "b"

    compare_variable = compare(a, b)

    if user_answer == compare_variable:
        print(f"Correct! {correct_answer['name']} has {correct_answer['follower_count']} million followers.")
    elif user_answer != compare_variable:
        print(f"Wrong! Game over!")
        continue_variable - 1
        break


    # TODO 4: Make option b the new a
    a = b

    # TODO 5: Pull new item from dictionary as option b
    b = random.choice(data)

# TODO 6: Repeat steps 1-5
    #  done by making it a while loop
