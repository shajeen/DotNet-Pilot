
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_directory(working_directory_var, dir_var):
    try:
        initial_dir = working_directory_var.get() if working_directory_var.get() else "."
        directory = filedialog.askdirectory(initialdir=initial_dir)
        if directory:
            working_directory_var.set(directory)
            dir_var.set(directory)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to browse directory: {str(e)}")

def browse_package_file(package_file_var):
    try:
        file_path = filedialog.askopenfilename(
            title="Select Package File",
            filetypes=[("NuGet Package", "*.nupkg"), ("All Files", "*.*")]
        )
        if file_path:
            package_file_var.set(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to browse package file: {str(e)}")

def clear_output(output_text):
    output_text.delete(1.0, tk.END)

def save_output(output_text):
    content = output_text.get(1.0, tk.END)
    if content.strip():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(content)
                messagebox.showinfo("Success", "Output saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    else:
        messagebox.showwarning("Warning", "No output to save.")
