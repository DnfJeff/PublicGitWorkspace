import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to get all files and directories with file name, directory, and file extension
def get_files_and_dirs(root_dir):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            file_name = file  # Just the file name with extension (e.g., File.xyz)
            file_ext = os.path.splitext(file)[1]  # Get file extension (not used directly here, but can be added if needed)
            file_list.append((file_name, dirpath))  # Store file name and directory
    return file_list

# Function to write data to CSV
def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["File Name", "Full Directory"])  # CSV header
        csvwriter.writerows(data)

# Function to generate the CSV from a selected directory
def generate_csv(selected_dir, output_dir, csv_name):
    if not selected_dir or not output_dir or not csv_name:
        messagebox.showerror("Error", "All fields must be filled in.")
        return

    try:
        # Collect files and directories
        data = get_files_and_dirs(selected_dir)

        # Define the output CSV file path with the provided CSV name
        output_file = os.path.join(output_dir, f"{csv_name}.csv")
        write_to_csv(data, output_file)

        # Success message
        messagebox.showinfo("Success", f"CSV saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main function to create the GUI
def main():
    selected_dir = ""
    output_dir = ""
    csv_name = ""

    # Create the main window
    root = tk.Tk()
    root.title("Directory to CSV")

    # Remove the default window frame (minimize, maximize, and close buttons)
    root.overrideredirect(True)

    # Make the window not resizable
    root.resizable(False, False)

    # Create custom title bar frame
    title_frame = tk.Frame(root, bg="#a8d7e5", relief="flat", height=50)
    title_frame.pack(fill="x", pady=0)  # Make the title frame take the full width

    # Add a label for the program name or logo
    title_label = tk.Label(title_frame, text="Directory to CSV", font=("Helvetica", 14, "bold"), bg="#a8d7e5", fg="#ffffff")
    title_label.pack(side="left", padx=10)

    # Close Button (to close the custom title bar window)
    def close_window():
        root.quit()

    close_button = tk.Button(title_frame, text="X", command=close_window, bg="#a8d7e5", fg="#ffffff", font=("Helvetica", 12), relief="flat", padx=5)
    close_button.pack(side="right", padx=5)

    # Minimize Button (optional, just hides the window)
    def minimize_window():
        root.iconify()  # Minimize the window using iconify()

    minimize_button = tk.Button(title_frame, text="_", command=minimize_window, bg="#a8d7e5", fg="#ffffff", font=("Helvetica", 12), relief="flat", padx=5)
    minimize_button.pack(side="right", padx=5)

    # Drag functionality for custom title bar
    def start_drag(event):
        root.x = event.x
        root.y = event.y

    def do_drag(event):
        delta_x = event.x - root.x
        delta_y = event.y - root.y
        root.geometry(f"+{root.winfo_x() + delta_x}+{root.winfo_y() + delta_y}")

    # Bind the drag events to the title bar frame
    title_frame.bind("<Button-1>", start_drag)
    title_frame.bind("<B1-Motion>", do_drag)

    # Add a label
    label = tk.Label(
        root, 
        text="Generate CSV of Files and Directories", 
        font=("Helvetica", 14, "bold"), 
        bg="#f7f2d1", 
        fg="#444444", 
        wraplength=400
    )
    label.pack(pady=10)

    # Function to select directory
    def select_input_dir():
        nonlocal selected_dir
        selected_dir = filedialog.askdirectory(title="Select a Directory")
        if selected_dir:
            input_label.config(text=f"Selected Input: {selected_dir}")

    # Function to select output directory
    def select_output_dir():
        nonlocal output_dir
        output_dir = filedialog.askdirectory(title="Select Output Folder")
        if output_dir:
            output_label.config(text=f"Selected Output: {output_dir}")

    # Input directory selection button
    input_button = tk.Button(
        root, 
        text="Select Input Directory", 
        command=select_input_dir, 
        font=("Helvetica", 12), 
        bg="#d5a6d2", 
        fg="#333333", 
        activebackground="#c09fbb", 
        activeforeground="#000000", 
        relief="flat", 
        borderwidth=2,
        width=20,
        height=2,
        padx=5
    )
    input_button.pack(pady=10)

    # Output directory selection button
    output_button = tk.Button(
        root, 
        text="Select Output Directory", 
        command=select_output_dir, 
        font=("Helvetica", 12), 
        bg="#d5a6d2", 
        fg="#333333", 
        activebackground="#c09fbb", 
        activeforeground="#000000", 
        relief="flat", 
        borderwidth=2,
        width=20,
        height=2,
        padx=5
    )
    output_button.pack(pady=10)

    # Labels to show selected directories
    input_label = tk.Label(
        root, 
        text="Selected Input: None", 
        font=("Helvetica", 10), 
        bg="#f7f2d1", 
        fg="#555555"
    )
    input_label.pack()

    output_label = tk.Label(
        root, 
        text="Selected Output: None", 
        font=("Helvetica", 10), 
        bg="#f7f2d1", 
        fg="#555555"
    )
    output_label.pack(pady=10)

    # Text input field for the CSV name with placeholder text
    def on_entry_click(event):
        if csv_name_entry.get() == 'CSV name here':
            csv_name_entry.delete(0, "end")  # Delete the placeholder text
            csv_name_entry.config(fg="black")

    def on_focusout(event):
        if csv_name_entry.get() == '':
            csv_name_entry.insert(0, 'CSV name here')
            csv_name_entry.config(fg="grey")

    csv_name_entry = tk.Entry(
        root, 
        font=("Helvetica", 12), 
        fg="grey", 
        bg="#f7f2d1", 
        bd=2, 
        width=30
    )
    csv_name_entry.insert(0, "CSV name here")  # Placeholder text
    csv_name_entry.bind("<FocusIn>", on_entry_click)
    csv_name_entry.bind("<FocusOut>", on_focusout)
    csv_name_entry.pack(pady=10)

    # Start button to generate CSV
    start_button = tk.Button(
        root, 
        text="Start CSV Creation", 
        command=lambda: generate_csv(selected_dir, output_dir, csv_name_entry.get()), 
        font=("Helvetica", 12), 
        bg="#a8d7e5", 
        fg="#333333", 
        activebackground="#8ec1d1", 
        activeforeground="#000000", 
        relief="flat", 
        borderwidth=2,
        width=20,  # Horizontal size
        height=1,  # Adjusted vertical size (half as tall)
        padx=5
    )
    start_button.pack(pady=20)

    # Footer frame to hold footer label
    footer_frame = tk.Frame(root, bg="#f7f2d1")
    footer_frame.pack(side="bottom", fill="x", pady=10)

    # Footer label
    footer = tk.Label(
        footer_frame, 
        text="Powered by Python\nMade by Dnf_Jeff", 
        font=("Helvetica", 9, "italic"), 
        bg="#f7f2d1", 
        fg="#777777",
        justify="center"
    )
    footer.pack()

    # Run the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
