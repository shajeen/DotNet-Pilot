import tkinter as tk
from dotnet_pilot.gui import DotNetGUI

def main():
    root = tk.Tk()
    app = DotNetGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()