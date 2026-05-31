# gui.py
import tkinter as tk
from tkinter import messagebox
from weather import get_weather

def show_weather():
    city = entry.get()
    result = get_weather(city)

    if result:
        output.config(text=
            f"City: {result['city']}\n"
            f"Temp: {result['temp']}°C\n"
            f"Condition: {result['desc']}\n"
            f"Humidity: {result['humidity']}%\n"
            f"Wind Speed: {result['wind']} m/s"
        )
    else:
        messagebox.showerror("Error", "City not found / API key problem")

root = tk.Tk()
root.configure(bg="lightblue")
root.title("Weather App")
root.geometry("300x300")

tk.Label(root, text="Enter City", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12, "bold"))
entry.pack(pady=5)

tk.Button(root, text="Get Weather", bg="#6ab04c" ,command=show_weather).pack(pady=10)
output = tk.Label(root, text="", font=("Arial", 11))
output.pack(pady=10)

root.mainloop()