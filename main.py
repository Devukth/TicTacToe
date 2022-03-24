from tabnanny import check
from tkinter import *
import tkinter.messagebox as msgbox

# Window Setup
root = Tk()
root.title("Tic Tac Toe")

# Player Symbol Labels
Label(root, text = "Player 1: X", font = "sans-serif 15").grid(row = 0, column = 1)
Label(root, text = "Player 2: O", font = "sans-serif 15").grid(row = 0, column = 2)

# Game Code
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark = ""
count = 0
panels = ["panel"] * 10

def check_possibillity(x, y, z, mark):
    return (panels[x] == panels[y] == panels[z] == mark)

def check_win(panels, mark):
    return (
        check_possibillity(1, 2, 3, mark) or
        check_possibillity(4, 5, 6, mark) or
        check_possibillity(7, 8, 9, mark) or
        check_possibillity(1, 4, 7, mark) or
        check_possibillity(2, 5, 8, mark) or
        check_possibillity(3, 6, 9, mark) or
        check_possibillity(1, 5, 9, mark) or
        check_possibillity(3, 5, 7, mark)
        )

def place_mark(digit):
    global mark, count, digits
    digits.remove(digit)
    if(count % 2 == 0): mark = "X"
    elif(count % 2 != 0): mark = "O"
    panels[digit] = mark
    buttons[digit - 1].config(text = mark)
    count += 1

    if(check_win(panels, mark) and mark == "X"):
        msgbox.showinfo("Result:", "Player 1 Wins!")
        root.destroy()
    elif(check_win(panels, mark) and mark == "O"):
        msgbox.showinfo("Result:", "Player 2 Wins!")
        root.destroy()

def checker(digit):
    global mark, count, digits
    for i in range(1, 10):
        if(digit == i and digit in digits):
            place_mark(digit)

buttons = []
for y in range(3):
    for x in range(3):
        button = Button(root, width = 4, height = 2, font = "sans-serif 32 bold")
        button.grid(row = (x + 1), column = (y + 1))
        buttons.append(button)

buttons[0].config(command = lambda: checker(1))
buttons[1].config(command = lambda: checker(2))
buttons[2].config(command = lambda: checker(3))
buttons[3].config(command = lambda: checker(4))
buttons[4].config(command = lambda: checker(5))
buttons[5].config(command = lambda: checker(6))
buttons[6].config(command = lambda: checker(7))
buttons[7].config(command = lambda: checker(8))
buttons[8].config(command = lambda: checker(9))

root.mainloop()