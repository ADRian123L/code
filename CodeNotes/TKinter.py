# -*- coding: utf-8 -*-

"""
    Practice for the tkinter nodule.
"""

import tkinter

class GUIwindow:

    def __init__(self : any) -> None:
        """The method initializers the object with an attribute
        that adds a widget and other features."""
        # Creates a widget:
        self.window = tkinter.Tk()
        # Adds a title to the widget:
        self.window.title("Index")
        # Creates a button:
        self.button = tkinter.Button(master=self.window, text="Button")
        # The loop:
        tkinter.mainloop()
        return None

    def quite(self : any) -> None:
        """The method breaks the widget loop."""
        tkinter.Message.quit()
        return None

class Widget:
    
    def __init__(self : any) -> None:
        """The method initializers the object with an attribute
        that adds a widget and other features."""
        # Creates a widget:
        self.window = tkinter.Tk()
        self.window.title("Password")
        # Creates an input box:
        self.frame = tkinter.Frame()
        self.frame2nd = tkinter.Frame()
        self.prompt = tkinter.Label(self.frame)
        # Starts the loop:
        tkinter.mainloop()
        return None

def main(first=False, second=False) -> None:
    """The function drives the program."""
    # Creates the objects:
    if (first == True):
        window = GUIwindow()
    if (second == True):
        window2 = Widget()
    return None

if __name__ == "__main__":
    main(second=True)