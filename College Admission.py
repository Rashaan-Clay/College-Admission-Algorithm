import random

def clear():
    print("\033c", end='')

def wait():
    input("\nPress [ENTER] to continue...")

def header(text):
    print("-" * (len(text) + 4))
    print("|", str(text), "|")
    print("-" * (len(text) + 4))
    print("\n" * 1)

def prompt(question, answer_type, dictionary):
    response = input(question)

    while response.lower() == "quit":
        clear()

    if response.isdigit() and answer_type != int:
        print("\nThat is not a valid response. Try again!\n")
        prompt(question, answer_type, dictionary)

    if dictionary == "stype" and response.lower() not in ["public", "private"]:
        print("\nThat is not a valid response. Try again!\n")
        prompt(question, answer_type, dictionary)

    if dictionary == LOCATION and response.lower() not in ["in", "out", "international"]:
        print("\nThat is not a valid response. Try again!\n")
        prompt(question, answer_type, dictionary)

    if (dictionary in [DISABILITY, SUSPENSION, EXPULSION, CRIMINAL]) and response.lower() not in ["y", "n"]:
        print("\nThat is not a valid response. Try again!\n")
        prompt(question, answer_type, dictionary)

    try:
        return dictionary[response]
    except KeyError:
        if dictionary == DUAL and int(response) >= 6:
            return 10
        elif dictionary == AGE and (int(response) < 18 or int(response) > 21):
            if int(response) < 18:
                return 10
            else:
                return 6
        elif dictionary == "stype":
            return SCHOOL_TYPE[response]
        else:
            return int(response)

# point values for various aspects of the student's life
# (previously defined as global variables)
EXTRACURRICULAR = {3: 4, 2: 3, 1: 2, 0: 0}
SCHOOL_TYPE = {"public": 9, "private": 10}
DUAL = {0: 0, 1: 5, 2: 6, 3: 7, 4: 8, 5: 9}
AGE = {18: 10, 19: 9, 20: 8, 21: 7}
RIGOR = {0: 0, 10: 1, 20: 2, 30: 3, 40: 4, 50: 5, 60: 6, 70: 7, 80: 8, 90: 9, 100: 10}
WGPA = {5: 10, 4: 9.5, 3: 8, 2: 1, 1: 0.5, 0: 0}
LOCATION = {"in": 6, "out": 8, "international": 10}
DISABILITY = {"y": 0.5, "n": 1}
SUSPENSION = {"y": -2, "n": 0}
EXPULSION = {"y": -5, "n": 0}
CRIMINAL = {"y": -2, "n": 0}

# initial score (will be calculated later)
score = 0

# INITIAL WELCOME SCREEN
intro = "Welcome to the UMD Admissions Portal!"
print(intro)
wait()
clear()

# EXPLANATION OF THE SERVICE PROVIDED
explanation = "This portal will inform you of your chances of getting admitted to the University, as well as give you an estimate as to the cost of attendance at UMD, should you be accepted. To do this, we must collect several pieces of information from you, including:\n - Age\n - Location\n - Family Income\n - Academic History/Performance Data\n\nEach time we ask you for information, please type it below, and press enter to continue to the next screen."
print(explanation)
wait()
clear()

# PERSONAL INFORMATION - INTRODUCTION
personal_intro = "Let's begin! First, we'll need some of your more personal information."
print(personal_intro)
wait()
clear()

# PERSONAL INFORMATION SECTION
header("PERSONAL INFORMATION")
score += prompt("What is your name?\n", str, "name")
score += prompt("How old are you?\n", int, AGE)
score += prompt("Where are you located?\n - Type \"in\" for in-state\n - Type \"out\" for out of state\n - Type \"international\" for international.\n", str, LOCATION)
score += prompt("How much is your yearly household income?\n$", int, "income")
score += prompt("Do you have any physical disabilities? (Y/N)\n", str, DISABILITY)
score += prompt("Have you ever been suspended from any school? (Y/N)\n", str, SUSPENSION)
score += prompt("Have you ever been expelled from any school? (Y/N)\n", str, EXPULSION)
score += prompt("Do you have a criminal record? (Y/N)\n", str, CRIMINAL)

# ACADEMIC INFORMATION - INTRODUCTION
academic_intro = "Great! Now we can get started with your academic information from high school."
print(academic_intro)
wait()
clear()

# ACADEMIC INFORMATION SECTION
def high_school(year):
    header("ACADEMICS - " + str(year))
    global score
    score += prompt("Did you go to a public or private school? \n(type \"public\" or \"private\".)\n", str, "stype")
    score += prompt("How many extracurriculars were you involved in this year (please enter a number)\n", int, EXTRACURRICULAR)
    score += prompt("How many classes did you take this year? (please enter a number)\n", int, "class_total")
    score += prompt("How many of these classes were advanced level classes? (think Honors, GT, AP, or IB.) (please enter a number)\n", int, "adv_class_num")
    score += prompt("How many dual-enrollment classes did you take this year? (please enter a number)\n", int, DUAL)
    score += prompt("What was your weighted GPA for this school year? (an 'A' for a standard class is worth 4 points, and an 'A' for Honors, GT, AP, or IB classes is worth 5. Additionally, please round your GPA up to the nearest point.)", int, WGPA)
    wait()