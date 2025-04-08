import tkinter
import tkinter as tk
import random

root = tk.Tk()

root.geometry("1024x1024+300+0")
root.title("Project")


# Загружаем изображения

mainPhoto = tkinter.PhotoImage(file="images/bg.png")
playPhoto = tkinter.PhotoImage(file="images/play.png")
exitPhoto = tkinter.PhotoImage(file="images/exit.png")
soundPhoto = tkinter.PhotoImage(file="images/sound.png")

def play():
    play_button.place_forget()
    exit_button.place_forget()
    fifty_fifty_button.place(x=150, y=500, width=125, height=50)
    ask_the_audience_button.place(x=850, y=500, width=125, height=50)
    call_a_friend_button.place(x=850, y=600, width=125, height=50)
    switch_button.place(x=150, y=600, width=125, height=50)
    question_text.place(x=150, y=200, width=700, height=100)
    answer1.place(x=325, y=500, width=225, height=50)
    answer2.place(x=575, y=500, width=225, height=50)
    answer3.place(x=325, y=600, width=225, height=50)
    answer4.place(x=575, y=600, width=225, height=50)

def sound():
    print("i am too lazy to code this cuz yes")
    print("sound.exe has left the chat")
    print("o_o")

def close():
    root.destroy()



mainPic = tkinter.Label(root, image=mainPhoto)
mainPic.place(x = 0, y = 0)

play_button = tk.Button(root, image=playPhoto, command=play)
play_button.place(x=412, y=512, width=200, height=200)

sound_button = tk.Button(root, image="", command=sound)
sound_button.place(x=10, y=720, width=100, height=100)

exit_button = tk.Button(root, image="", command=close)
exit_button.place(x=964, y=10, width=50, height=50)

# Lifeline widgets

fifty_fifty_button = tk.Button(root, text="50/50")
call_a_friend_button = tk.Button(root, text="Call a friend")
ask_the_audience_button = tk.Button(root, text="Ask the audience")
switch_button = tk.Button(root, text="Switch")

# Game widgets

questions = ["Who is the richest man alive"]
question_text = tk.Label(root, text=random.choice(questions), font=("Arial", 32))

# Answers

answer1 = tk.Button(root, text="Bill Gates")
answer2 = tk.Button(root, text="Elon Musk")
answer3 = tk.Button(root, text="Jeff Bezos")
answer4 = tk.Button(root, text="Logan Paul")

root.mainloop()