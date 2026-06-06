import customtkinter as ctk
import threading

from assistant import run_assistant

# APP SETTINGS
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# WINDOW
app = ctk.CTk()

app.geometry("1000x650")

app.title("JARVIS AI")

# TITLE
title = ctk.CTkLabel(
    app,
    text="JARVIS AI ASSISTANT",
    font=("Orbitron", 34, "bold")
)

title.pack(pady=30)

# STATUS LABEL
status_label = ctk.CTkLabel(
    app,
    text="SYSTEM ONLINE",
    font=("Arial", 22)
)

status_label.pack(pady=20)

# OUTPUT BOX
output_box = ctk.CTkTextbox(
    app,
    width=800,
    height=300,
    font=("Consolas", 18)
)

output_box.pack(pady=20)

output_box.insert("0.0", "Jarvis Initialized...\n")


# UPDATE UI FUNCTION
def update_ui(text):

    output_box.insert("end", f"\n{text}")

    output_box.see("end")

    status_label.configure(text=text)


# START ASSISTANT
def start_assistant():

    thread = threading.Thread(
        target=run_assistant,
        args=(update_ui,),
        daemon=True
    )

    thread.start()


# MIC BUTTON
mic_button = ctk.CTkButton(
    app,
    text="🎤 Start Jarvis",
    width=300,
    height=70,
    font=("Arial", 24, "bold"),
    corner_radius=20,
    command=start_assistant
)

mic_button.pack(pady=40)

app.mainloop()