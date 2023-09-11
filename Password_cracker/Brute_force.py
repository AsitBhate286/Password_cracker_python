import random
import pyautogui #if not installed rin pip install pyautogui

character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)

password = pyautogui.password("Enter Password Here: ")

guess_password = ''
while (guess_password!=password):
    guess_password = random.choices(character_list, k=len(password))

    print("------"+str(guess_password)+"------")

    if(guess_password==list(password)):
        print("Your Passwordis:"+"".join(guess_password))
        break