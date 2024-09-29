
import tkinter as tk
from tkinter import ttk, messagebox, LabelFrame, PhotoImage
import pyshorteners
import os
from datetime import datetime

# File to store the history of shortened URLs
HISTORY_TEXT_FILE = "url_history.txt"

# Function to shorten the URL
def shorten_url():
    long_url = url_entry.get()
    if long_url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(long_url)
            result_entry.delete(0, tk.END)
            result_entry.insert(0, short_url)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_entry = f"{short_url} (Time: {timestamp})"
            history_listbox.insert(tk.END, history_entry)
            save_to_history(history_entry)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a URL to shorten.")

# Function to save the shortened URL and timestamp to the history file
def save_to_history(history_entry):
    with open(HISTORY_TEXT_FILE, "a") as file:
        file.write(history_entry + "\n")

# Function to load the history from the file
def load_history():
    if os.path.exists(HISTORY_TEXT_FILE):
        with open(HISTORY_TEXT_FILE, "r") as file:
            for line in file:
                history_listbox.insert(tk.END, line.strip())

# Setting up the main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("500x610")

# Creating object of photoimage class 
# Image should be in the same folder 
# in which script is saved 
p1 = PhotoImage(file = 'logo.png') 
  
# Setting icon of root window 
root.iconphoto(False, p1) 
  

# Disable the maximize button
root.resizable(False, False)

# Apply a theme
style = ttk.Style(root)
style.theme_use('clam')

# URL input
url_label = ttk.Label(root, text="Enter URL to Shorten:")
url_label.pack(pady=10)
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

# Shorten button
shorten_button = ttk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

# Result display
result_label = ttk.Label(root, text="Shortened URL:")
result_label.pack(pady=10)
result_entry = ttk.Entry(root, width=50)
result_entry.pack(pady=5)

# History display
history_label = ttk.Label(root, text="History:")
history_label.pack(pady=10)
history_listbox = tk.Listbox(root, width=50, height=10)
history_listbox.pack(pady=5)

# This will create a LabelFrame
label_frame = LabelFrame(root, text='About',fg="blue")
label_frame.pack(expand='yes', fill='both')

aboutSection = "The Link will never expire\nShorten as many URL's you want.\nSimple URL Shortner\nCreated By : Rushikesh\n@2024"

# Result display
created_by = ttk.Label(label_frame, text=aboutSection)
created_by.pack(pady=10)

# Load the history when the application starts
load_history()

# Run the application
root.mainloop()
