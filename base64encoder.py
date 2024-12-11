import base64
import customtkinter as ctk
from tkinter import filedialog

# Function to encode text into base64
def encode_text():
    input_text = text_input.get("1.0", "end-1c")  # Get text from input box
    if input_text:
        encoded_text = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')
        result_text.delete("1.0", "end")
        result_text.insert("1.0", encoded_text)
    else:
        result_text.delete("1.0", "end")
        result_text.insert("1.0", "Please enter some text.")
        
# def decode_text():
            

# Function to encode file into base64
def decode_text():
    
    input_text = text_input.get("1.0", "end-1c")
    if input_text:
        base64_bytes = input_text.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        result_text.delete("1.0", "end")
        result_text.insert("1.0", sample_string)
    else:
        result_text.delete("1.0", "end")
        result_text.insert("1.0", "Please enter some text.")



# Set up the main window
root = ctk.CTk()

# Configure window size and title
root.geometry("600x500")
root.title("Base64-Encoder")

# Label for instruction
label = ctk.CTkLabel(root, text="Base64-Encoder")
label.pack(pady=10)

# Textbox for user input
text_input = ctk.CTkTextbox(root, height=10, width=100)
text_input.pack(pady=10)

# Button to encode text input
encode_text_button = ctk.CTkButton(root, text="Encode Text", command=encode_text)
encode_text_button.pack(pady=5)

# Button to encode file
encode_file_button = ctk.CTkButton(root, text="decode Text", command=decode_text)
encode_file_button.pack(pady=5)

# Label for result
result_label = ctk.CTkLabel(root, text="Encoded Base64 Result:")
result_label.pack(pady=10)

# Textbox to display encoded result
result_text = ctk.CTkTextbox(root, height=10, width=200)
result_text.pack(pady=10)

# Start the main event loop
root.mainloop()
