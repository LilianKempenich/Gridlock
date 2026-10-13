import tkinter as tk

# Main window
window = tk.Tk()

# Window configurations
window.title("Gridlock")
window.configure(bg="purple")
window.minsize(700, 700)
window.geometry("700x700+450+50")

# Setup the sudoku board
board = tk.Canvas(master=window, width=700, height=700, bg="black")

# Puts it inside the window to actually see it
board.pack()

# Builds the 9 major squares for a sudoku board with a black out line
for row in range(3):
    for col in range(3):
        x1 = col * (700/3)
        y1 = row * (700/3)

        x2 = x1 + (700/3)
        y2 = y1 + (700/3)

        board.create_rectangle(x1, y1, x2, y2, fill="white", outline="black", width=2)

window.mainloop()
