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
        # The loop:
        tkinter.mainloop()
        return None
        
if __name__ == "__main__":
    # Creates an object with attributes of a widget:
    window = GUIwindow()
