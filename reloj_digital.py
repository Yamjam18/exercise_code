import tkinter as tk
from time import strftime

class RelojApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reloj Digital")
        self.root.geometry("400x200")
        self.root.configure(bg="black")

        self.label = tk.Label(
            root,
            font=("Helvetica", 48, "bold"),
            background="black",
            foreground="white"
        )

        self.label.pack(expand=True)

        self.actualizar_reloj()

    def actualizar_reloj(self):
        hora = strftime("%H:%M:%S")
        self.label.config(text=hora)
        self.root.after(1000, self.actualizar_reloj)


if __name__ == "__main__":
    root = tk.Tk()
    app = RelojApp(root)
    root.mainloop()