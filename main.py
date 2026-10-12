import tkinter as tk

# main window
root = tk.Tk()

# window configurations
root.title("Gridlock")
root.configure(bg="purple")
root.minsize(700, 700)
root.geometry("700x700+450+50")

# setup the sudoku board
board = tk.Frame(root, width=600, height=600, bg="black")
board.pack(padx=10, pady=50)
board.rowconfigure(0, weight=1)
board.rowconfigure(1, weight=1)
board.rowconfigure(2, weight=1)
board.columnconfigure(0, weight=1)
board.columnconfigure(1, weight=1)
board.columnconfigure(2, weight=1)

# the 9 larger squares of the sudoku board
sq_a = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=0, column=0)
sq_b = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=0, column=1)
sq_c = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=0, column=2)
sq_d = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=1, column=0)
sq_e = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=1, column=1)
sq_f = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=1, column=2)
sq_g = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=2, column=0)
sq_h = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=2, column=1)
sq_i = tk.Frame(board, width=100, height=100, bg="white", padx=2, pady=2).grid(row=2, column=2)

# square A tiles
# tile_a1 = tk.Entry

root.mainloop()
