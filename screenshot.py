import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))           #generating a random number to save another screenshot
    name = 'C:/Users/HP/JPMC-tech-task-3-PY3/Project/screenshots data{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show

#creating UI window
root = tk.Tk()
root.geometry("200x200")
frame = tk.Frame(root)

frame.pack()

#creating buttons
button = tk.Button(
    frame,
    text = 'Take Screenshot',
    command=screenshot
    )
button.pack(side=tk.LEFT)

def close_window():
    root.destroy()  # destroying the main window

close = tk.Button(frame)
close['text'] ="Quit"
close['command'] = close_window
close.pack(side=tk.LEFT)

root.mainloop()