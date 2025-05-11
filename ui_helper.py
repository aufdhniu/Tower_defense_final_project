import tkinter as tk

def show_pause_menu():
    root = tk.Tk()
    root.title("Game Paused")

    root.geometry("250x150")
    root.eval('tk::PlaceWindow . center')

    label = tk.Label(root, text="Game is Paused", font=("Arial", 14))
    label.pack(pady=20)

    resume = False

    def on_resume():
        nonlocal resume
        resume = True
        root.destroy()

    def on_quit():
        root.destroy()
        quit()

    btn_resume = tk.Button(root, text="Resume", width=10, command=on_resume)
    btn_resume.pack(pady=5)

    btn_quit = tk.Button(root, text="Quit", width=10, command=on_quit)
    btn_quit.pack()

    root.mainloop()
    return resume