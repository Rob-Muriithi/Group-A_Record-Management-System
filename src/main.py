import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from GUI import root

def main():
    # Initialize application
    root.title("Travel Agent Record Management System")
    root.geometry("500x500")
    root.configure(bg="#fff4f4")
    
    # Start main loop
    root.mainloop()

if __name__ == "__main__":
    main()