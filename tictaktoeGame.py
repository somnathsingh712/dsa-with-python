import tkinter as tk
from tkinter import messagebox


class TicTacToe:

    def __init__(self, root):

        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"

        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.status_label = tk.Label(
            root,
            text="Player X's Turn",
            font=("Arial", 16)
        )

        self.status_label.pack(pady=10)

        frame = tk.Frame(root)
        frame.pack()

        for row in range(3):
            for col in range(3):

                btn = tk.Button(
                    frame,
                    text="",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )

                btn.grid(row=row, column=col)

                self.buttons[row][col] = btn

    def on_click(self, row, col):

        if self.board[row][col] != "":
            return

        self.board[row][col] = self.current_player

        self.buttons[row][col].config(
            text=self.current_player,
            fg="blue" if self.current_player == "X" else "red"
        )

        if self.check_winner(row, col):
            messagebox.showinfo(
                "Winner",
                f"Player {self.current_player} Wins!"
            )
            self.reset_board()

        elif self.is_draw():
            messagebox.showinfo(
                "Draw",
                "It's a Draw!"
            )
            self.reset_board()

        else:
            self.current_player = "O" if self.current_player == "X" else "X"

            self.status_label.config(
                text=f"Player {self.current_player}'s Turn"
            )

    def check_winner(self, r, c):

        p = self.current_player

        if all(self.board[r][i] == p for i in range(3)):
            return True

        if all(self.board[i][c] == p for i in range(3)):
            return True

        if r == c:
            if all(self.board[i][i] == p for i in range(3)):
                return True

        if r + c == 2:
            if all(self.board[i][2 - i] == p for i in range(3)):
                return True

        return False

    def is_draw(self):

        return all(
            self.board[r][c] != ""
            for r in range(3)
            for c in range(3)
        )

    def reset_board(self):

        self.current_player = "X"

        self.status_label.config(text="Player X's Turn")

        self.board = [["" for _ in range(3)] for _ in range(3)]

        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(
                    text="",
                    fg="black"
                )


if __name__ == "__main__":

    root = tk.Tk()

    game = TicTacToe(root)

    root.mainloop()