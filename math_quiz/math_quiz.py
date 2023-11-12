import random


def function_A(min, max):
    """
    Random integer.
    The function use is to output a random number between min and max given
    """
    return int(random.randint(int(min), int(max)))


def function_B():
    # function is to give out a random operation
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
    # the function use is to do one of three operations 
    # either add or substract or multiplz
    p = f"{n1} {o} {n2}"
    try:
        if o == '+': a = n1 + n2
        elif o == '-': a = n1 - n2
        else: a = n1 * n2
        return p, a
    except :
        print("The value given is not a number")

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # the idea here is to given questions and be asked to solve them 
    # as well as comparing them with the actual answer if right increase the  score by one 
    # if not decrease by one
    for _ in range(int(3)):
        n1 = function_A(1, 10) 
        n2 = function_A(1, 5.5)
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{int(t_q)}")

if __name__ == "__main__":
    math_quiz()
