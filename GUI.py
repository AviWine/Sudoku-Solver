import tkinter as tk
from tkinter import messagebox
from solver import find_solution  # backtracking solver

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        master.title('9×9 Sudoku Solver')

        # ————— Grid Frame —————
        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Prepare 9×9 entries
        self.entries = [[None]*9 for _ in range(9)]
        font = ('Courier', 16)
        for i in range(9):
            self.grid_frame.rowconfigure(i, weight=1)
            for j in range(9):
                self.grid_frame.columnconfigure(j, weight=1)
                e = tk.Entry(self.grid_frame, font=font, width=2, justify='center')
                e.grid(row=i, column=j, sticky='nsew',
                       padx=(4 if j%3==0 else 1, 1),
                       pady=(4 if i%3==0 else 1, 1))
                self.entries[i][j] = e

        # ————— Button Frame —————
        btn_frame = tk.Frame(master)
        btn_frame.pack(fill='x', pady=(0,10))

        solve_btn = tk.Button(btn_frame, text='Solve', command=self.on_solve)
        solve_btn.pack(side='left', padx=5)

        clear_btn = tk.Button(btn_frame, text='Clear', command=self.on_clear)
        clear_btn.pack(side='left')

    def on_solve(self):

        # 1) Read current board into a 2D list of ints, 0 for blank
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                raw = self.entries[i][j].get().strip()

                # Blank cell
                if raw == "":
                    row.append(0)
                    continue

                # Must be a single digit
                if not raw.isdigit() or len(raw) != 1:
                    messagebox.showerror("Invalid input", "Only digits 1–9 or blank allowed.")
                    return

                v = int(raw)
                # Must be in range 1–9
                if v < 1 or v > 9:
                    messagebox.showerror("Invalid input", "Only digits 1–9 or blank allowed.")
                    return

                row.append(v)
            board.append(row)


        # 2) Solve
        solved, val = find_solution(board)

        if not val:
            messagebox.showerror("","No solution")
            return

        # 3) Fill in solution
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, 'end')
                self.entries[i][j].insert(0, str(solved[i][j]))

    def on_clear(self):
        for row in self.entries:
            for e in row:
                e.delete(0, 'end')

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('450x500')
    SudokuGUI(root)
    root.mainloop()




