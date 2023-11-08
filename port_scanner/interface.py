# port_scanner_ui.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from datetime import datetime
import threading
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

        self.scan_button = ttk.Button(
            root, text="Scan Ports", command=self.start_scan)
        
        self.scan_progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
        self.results_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)

        self.target_host_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.target_host_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.start_port_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.start_port_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.end_port_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.end_port_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.scan_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.results_text.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        self.scan_progress_bar.grid(row=5, column=0, columnspan=2, sticky=tk.W + tk.E)

    def start_scan(self):
        self.results_text.delete(1.0, tk.END)
        self.scan_button.config(state=tk.DISABLED)
        self.scan_button.config(text="Scanning Ports...")
        self.scan_progress_bar['value'] = 0
        threading.Thread(target=self.scan_ports).start()

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

            self.scan_progress_bar["maximum"] = end_port - start_port

            scanner.port_scanner(target_host, (start_port, end_port), output_filename, self.scan_progress_bar, False)

            # Display results in the Text widget
            with open(output_filename, 'r') as result_file:
                results_content = result_file.read()
                self.results_text.insert(tk.END, results_content)

            self.scan_button.config(text="Scan Ports")
            messagebox.showinfo(
                "Scan Complete", f"Scan results saved in \"{output_filename}\"")
            self.scan_button.config(state=tk.NORMAL)
        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def update_status_bar(self, message):
        self.status_var.set(message)


def run():
    root = tk.Tk()
    app = PortScannerUI(root)
    root.mainloop()
