import sys

import win32gui, win32con
import threading
import tkinter

isActive = False
root = tkinter.Tk()
label = tkinter.Label(root, text="Not Running", fg="grey", font=("Helvetica", 16))


def keepActive():
    while(isActive): #Ya really gotta figure out a better way
        hwnd = win32gui.FindWindow(None, 'CounterSide')
        # print(hwnd)
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, None)

keepActiveThread = threading.Thread(target = keepActive)

def switch():
    global isActive
    global keepActiveThread
    # Determine is on or off

    isActive = not isActive
    #print(isActive)
    if isActive:
        label.config(text="Running",
                        fg="green")
        on_button.config(bg ="#ffcccb", text="Turn Off")
        keepActiveThread.start()
    else:
        label.config(text="Not Running", fg="grey")
        on_button.config(bg ="#90EE90", text="Turn On")
        keepActiveThread.join()
        keepActiveThread = threading.Thread(target=keepActive)
def exitCode():
    global keepActiveThread
    global isActive
    if(isActive):
        isActive = False
        keepActiveThread.join()
    sys.exit()

on_button = tkinter.Button(root, text="Turn On",  bd=0,
                   command=switch, bg="#90EE90")
if __name__ == '__main__':
    root.title("CounterSide Keep Active")
    w = 250
    h = 120
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    label.pack(pady = 10)

    # Define Our Images
    # on = tkinter.PhotoImage(file="on.png")
    # off = tkinter.PhotoImage(file="off.png")
    # Create A Button
    on_button.pack(pady=10)
    root.protocol('WM_DELETE_WINDOW', exitCode)
    # Execute Tkinter
    root.mainloop()