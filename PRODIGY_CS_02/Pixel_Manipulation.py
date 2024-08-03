import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

def encrypt_decrypt_images(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    encrypted_array = img_array ^ key
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def process_images():
    input_path = input_entry.get()
    output_path = output_entry.get()
    key = int(key_entry.get())
    
    if not input_path or not output_path:
        messagebox.showerror("Error", "Please select input and output files.")
        return
    
    try:
        encrypt_decrypt_images(input_path, output_path, key)
        messagebox.showinfo("Success", "Image processed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Image Encryption Tool")

tk.Label(root, text="Input Image Path: ").grid(row=0, column=0, sticky="e")
input_entry = tk.Entry(root, width=60)
input_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=3)

tk.Label(root, text="Output Image Path: ").grid(row=1, column=0, sticky="e")
output_entry = tk.Entry(root, width=60)
output_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=select_output_file).grid(row=1, column=3)

tk.Label(root, text="Encryption Key (integer):").grid(row=2, column=0, sticky="e")
key_entry = tk.Entry(root, width=40)
key_entry.grid(row=2, column=1)
tk.Button(root, text="Encrypt/Decrypt", command=process_images).grid(row=3, column=1)

root.mainloop()