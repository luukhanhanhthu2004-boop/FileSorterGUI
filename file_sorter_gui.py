import tkinter as tk
from tkinter import filedialog, messagebox

# Hàm đọc file
def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

# Hàm ghi file
def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

# Hàm sắp xếp (bubble sort - tự viết)
def bubble_sort(lines):
    n = len(lines)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lines[j].lower() > lines[j + 1].lower():
                lines[j], lines[j + 1] = lines[j + 1], lines[j]
    return lines

# Hàm xử lý khi nhấn nút
def process_files():
    input_file = filedialog.askopenfilename(title="Select input file")
    if not input_file:
        return
    output_file = filedialog.asksaveasfilename(title="Save sorted file as")
    if not output_file:
        return

    try:
        lines = read_file(input_file)
        sorted_lines = bubble_sort(lines)
        write_file(output_file, sorted_lines)
        messagebox.showinfo("Success", "File sorted and saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Giao diện GUI
root = tk.Tk()
root.title("File Sorter")

label = tk.Label(root, text="Sort lines from one file to another", font=("Arial", 12))
label.pack(pady=10)

btn = tk.Button(root, text="Select File and Sort", command=process_files, bg="#4CAF50", fg="white", width=25)
btn.pack(pady=20)

root.geometry("350x200")
root.mainloop()
