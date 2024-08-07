from tkinter import *
from tkinter import messagebox
import base64

# Function to encrypt the message
def encrypt_message():
    message = text_input.get("1.0", END).strip()
    if message == "":
        messagebox.showwarning("Warning", "Please enter a message to encrypt.")
        return
    encoded_message = base64.b64encode(message.encode("utf-8")).decode("utf-8")
    text_output.delete("1.0", END)
    text_output.insert(END, encoded_message)

# Function to decrypt the message
def decrypt_message():
    encoded_message = text_input.get("1.0", END).strip()
    if encoded_message == "":
        messagebox.showwarning("Warning", "Please enter a message to decrypt.")
        return
    try:
        decoded_message = base64.b64decode(encoded_message.encode("utf-8")).decode("utf-8")
        text_output.delete("1.0", END)
        text_output.insert(END, decoded_message)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input for decryption.")

# Main screen setup
def main_screen():
    screen = Tk()
    screen.geometry("400x500")
    screen.title("CryptApp")
    
    screen.configure(bg="#f0f0f0")
    
    header = Label(screen, text="Text Encryption and Decryption", fg="#333", bg="#f0f0f0", font=("Helvetica", 16, "bold"))
    header.pack(pady=10)
    
    Label(screen, text="Enter text below", fg="#666", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    
    global text_input
    text_input = Text(screen, height=8, width=40, font=("Helvetica", 12), bg="#fff", fg="#333", relief=SOLID, bd=1)
    text_input.pack(pady=10)
    
    encrypt_button = Button(screen, text="Encrypt", height=2, width=20, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), command=encrypt_message, relief=SOLID, bd=1)
    encrypt_button.pack(pady=10)
    
    decrypt_button = Button(screen, text="Decrypt", height=2, width=20, bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), command=decrypt_message, relief=SOLID, bd=1)
    decrypt_button.pack(pady=10)
    
    Label(screen, text="Output text below", fg="#666", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    
    global text_output
    text_output = Text(screen, height=8, width=40, font=("Helvetica", 12), bg="#fff", fg="#333", relief=SOLID, bd=1)
    text_output.pack(pady=10)
    
    screen.mainloop()

main_screen()
