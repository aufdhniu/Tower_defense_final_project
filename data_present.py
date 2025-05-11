import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

def show_turret_data(turn_data):
    def open_window():
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        root = ctk.CTk()
        root.title("Turrets Deployed Per Turn")
        root.geometry("500x400")
        root.eval('tk::PlaceWindow . center')

        label = ctk.CTkLabel(root, text="Turret Deployment Stats", font=("Arial", 18, "bold"))
        label.pack(pady=10)

        fig, ax = plt.subplots(figsize=(6, 3.5))
        turns = list(range(1, len(turn_data)+1))
        ax.bar(turns, turn_data, color = "skyblue")
        ax.set_xlabel("Turn")
        ax.set_ylabel("Turrets Deployed")
        ax.set_title("Turrets Deployed Per Turn")
        ax.grid(True, linestyle="--", alpha=0.5)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

        close_btn = ctk.CTkButton(root, text="Close", command=root.destroy)
        close_btn.pack(pady=5)

        root.mainloop()

    # Start in a new thread
    threading.Thread(target=open_window, daemon=True).start()