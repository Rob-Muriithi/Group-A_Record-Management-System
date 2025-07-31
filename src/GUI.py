import tkinter as tk
from tkinter import messagebox
import os
import sys

# Fix path so conf modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "conf")))

from recordmanager import RecordManager

manager = RecordManager()

# Initialize window
root = tk.Tk()
root.title("Travel Agent Record Management System")
root.geometry("500x500")
root.configure(bg="#fff4f4")

# Header
header = tk.Label(
    root,
    text="Travel Agent Record\nManagement System",
    font=("Arial", 18, "bold"),
    bg="#fff4f4",
    fg="#d62828"
)
header.pack(pady=30)

# Button frame
btn_frame = tk.Frame(root, bg="#fff4f4")
btn_frame.pack(pady=10)

# Dummy function for unimplemented features
def not_implemented():
    messagebox.showinfo("Notice", "This feature is not yet implemented.")

# Create Client Record form
def create_client_form():
    form = tk.Toplevel(root)
    form.title("Create Client Record")

    labels = [
        "ID", "Name", "Address Line 1", "Address Line 2", "Address Line 3",
        "City", "State", "ZIP Code", "Country", "Phone Number"
    ]
    entries = {}

    for idx, label in enumerate(labels):
        tk.Label(form, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(form, width=30)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[label] = entry

    def submit():
        client_data = {
            "id": int(entries["ID"].get()),
            "name": entries["Name"].get(),
            "address1": entries["Address Line 1"].get(),
            "address2": entries["Address Line 2"].get(),
            "address3": entries["Address Line 3"].get(),
            "city": entries["City"].get(),
            "state": entries["State"].get(),
            "zip_code": entries["ZIP Code"].get(),
            "country": entries["Country"].get(),
            "phone": entries["Phone Number"].get()
        }
        result = manager.add_client(client_data)
        messagebox.showinfo("Result", result)
        form.destroy()

    submit_btn = tk.Button(
        form,
        text="Submit",
        command=submit,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=3
    )
    submit_btn.grid(row=len(labels), column=0, pady=10)

    cancel_btn = tk.Button(
        form,
        text="Cancel",
        command=form.destroy,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=3
    )
    cancel_btn.grid(row=len(labels), column=1, pady=10)


# Placeholder for combined search/manage records window
def open_record_manager_window():
    form = tk.Toplevel(root)
    form.title("Search / Manage Records")

    # Record type dropdown
    tk.Label(form, text="Record Type:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    record_type_var = tk.StringVar(value="Client")
    tk.OptionMenu(form, record_type_var, "Client", "Airline", "Flight").grid(row=0, column=1, padx=10, pady=5)

    # Record ID input
    tk.Label(form, text="Record ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    record_id_entry = tk.Entry(form, width=30)
    record_id_entry.grid(row=1, column=1, padx=10, pady=5)

    # Output display
    result_text = tk.Text(form, height=10, width=50, state="disabled", bg="#fff")
    result_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def search_record():
        record_type = record_type_var.get().lower() + "s"
        record_id = int(record_id_entry.get())

        found = None
        for record in manager.data[record_type]:
            if record.get("id") == record_id:
                found = record
                break

        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        if found:
            for k, v in found.items():
                result_text.insert(tk.END, f"{k}: {v}\n")
        else:
            result_text.insert(tk.END, "Record not found.")
        result_text.config(state="disabled")

    def delete_record():
        record_type = record_type_var.get().lower()
        record_id = int(record_id_entry.get())

        if record_type == "client":
            success = manager.delete_client(record_id)
        elif record_type == "airline":
            success = manager.delete_airline(record_id)
        elif record_type == "flight":
            success = manager.delete_flight(record_id)
        else:
            success = False

        result_text.config(state="normal")
        if success:
            messagebox.showinfo("Success", "Record deleted successfully.")
            result_text.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", "Failed to delete record.")
        result_text.config(state="disabled")

    def view_all_records():
        record_type = record_type_var.get().lower() + "s"
        records = manager.data.get(record_type, [])
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        if not records:
            result_text.insert(tk.END, "No records found.")
        else:
            for r in records:
                result_text.insert(tk.END, "-" * 40 + "\n")
                for k, v in r.items():
                    result_text.insert(tk.END, f"{k}: {v}\n")
        result_text.config(state="disabled")

    tk.Button(
        form,
        text="Search",
        command=search_record,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold")
    ).grid(row=2, column=0, pady=5)
    tk.Button(
        form,
        text="Delete",
        command=delete_record,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold")
    ).grid(row=2, column=1, pady=5)
    tk.Button(
        form,
        text="View All",
        command=view_all_records,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold")
    ).grid(row=2, column=2, pady=5)

def create_airline_form():
    form = tk.Toplevel(root)
    form.title("Create Airline Record"),

    tk.Label(form, text="Airline ID").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    airline_id_entry = tk.Entry(form, width=30)
    airline_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form, text="Company Name").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    company_name_entry = tk.Entry(form, width=30)
    company_name_entry.grid(row=1, column=1, padx=10, pady=5)

    def submit():
        airline_data = {
            "id": int(airline_id_entry.get()),
            "company_name": company_name_entry.get()
        }
        result = manager.add_airline(airline_data)
        messagebox.showinfo("Result", result)
        form.destroy()

    tk.Button(
        form,
        text="Submit",
        command=submit,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold")
    ).grid(row=2, column=0, pady=10)
    tk.Button(
        form,
        text="Cancel",
        command=form.destroy,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold")
    ).grid(row=2, column=1, pady=10)

def create_flight_form():
    form = tk.Toplevel(root)
    form.title("Create Flight Record")

    labels = ["Flight ID", "Client ID", "Airline ID", "Date (YYYY-MM-DD)", "Start City", "End City"]
    entries = {}

    for idx, label in enumerate(labels):
        tk.Label(form, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(form, width=30)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[label] = entry

    def submit():
        flight_data = {
            "id": int(entries["Flight ID"].get()),
            "client_id": int(entries["Client ID"].get()),
            "airline_id": int(entries["Airline ID"].get()),
            "date": entries["Date (YYYY-MM-DD)"].get(),
            "start_city": entries["Start City"].get(),
            "end_city": entries["End City"].get()
        }
        result = manager.add_flight(flight_data)
        messagebox.showinfo("Result", result)
        form.destroy()

    tk.Button(
        form,
        text="Submit",
        command=submit,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold")
    ).grid(row=len(labels), column=0, pady=10)
    tk.Button(
        form,
        text="Cancel",
        command=form.destroy,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold")
    ).grid(row=len(labels), column=1, pady=10)

btns = [
    ("Create Client Record", create_client_form),
    ("Create Airline Record", create_airline_form),
    ("Create Flight Record", create_flight_form),
    ("Search / Manage Records", open_record_manager_window),
    ("Exit", root.destroy),
]

for i, (text, cmd) in enumerate(btns):
    tk.Button(
        btn_frame,
        text=text,
        width=30,
        height=2,
        command=cmd,
        bg="#ff6b6b",
        fg="#d62828",
        activebackground="#ffcccc",
        activeforeground="black",
        font=("Arial", 12, "bold"),
        relief="flat",
        state="normal"
    ).grid(row=i, column=0, pady=5)

# Start main loop
root.mainloop()