# port_scanner_ui.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import port_scanner.scanner as scanner

class PortScannerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Port Scanner")

        self.target_host_label = ttk.Label(root, text="Target Host:")
        self.target_host_entry = ttk.Entry(root)

        self.start_port_label = ttk.Label(root, text="Start Port:")
        self.start_port_entry = ttk.Entry(root)

        self.end_port_label = ttk.Label(root, text="End Port:")
        self.end_port_entry = ttk.Entry(root)

        self.scan_button = ttk.Button(root, text="Scan Ports", command=self.scan_ports)

        self.target_host_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.target_host_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.start_port_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.start_port_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.end_port_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.end_port_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.scan_button.grid(row=3, column=0, columnspan=2, pady=10)

    def scan_ports(self):
        try:
            target_host = self.target_host_entry.get()
            start_port = int(self.start_port_entry.get())
            end_port = int(self.end_port_entry.get())

            if start_port > end_port or not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
                raise ValueError("Invalid port range")

            output_directory = scanner.create_output_directory()
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            output_filename = f"{output_directory}/scan_result_{timestamp}.txt"
            scanner.port_scanner(target_host, (start_port, end_port), output_filename)

            messagebox.showinfo("Scan Complete", f"Scan results saved in {output_directory}")
        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def run():
  root = tk.Tk()
  app = PortScannerUI(root)
  root.mainloop()