import os
import socket
import concurrent.futures
from datetime import datetime
from tqdm import tqdm

def create_output_directory():
    directory_name = 'port_scanner_results'
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name

def scan_port(target_host, target_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target_host, target_port))
            return True
    except (socket.timeout, socket.error):
        return False

def port_scanner(target_host, port_range, output_filename, progress_bar=None, cli=True):
    with open(output_filename, 'w') as output_file:
        output_file.write(f"Scanning target host \"{target_host}\" for ports {port_range}:\n")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_port = {executor.submit(scan_port, target_host, port): port for port in range(*port_range)}
            for future in concurrent.futures.as_completed(future_to_port):
                port = future_to_port[future]
                try:
                    if future.result():
                        output_file.write(f"Port {port} is open\n")
                except Exception as e:
                    output_file.write(f"An error occurred while scanning port {port}: {e}\n")
                finally:
                        # Update the cli progress bar
                        if cli:
                            progress_bar.update(1)
                        elif progress_bar:
                            progress_bar['value'] += 1

        if cli:
          progress_bar.update()
          progress_bar.close()

def run():
  try:
      target_host = input("Enter target host: ")
      start_port = int(input("Enter start port: "))
      end_port = int(input("Enter end port: "))

      if start_port > end_port or not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
          raise ValueError("Invalid port range")

      progress_bar = tqdm(total=end_port - start_port + 1, desc="Scanning Ports", unit="port")

      output_directory = create_output_directory()
      timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
      output_filename = f"{output_directory}/scan_result_{timestamp}.txt"
      port_scanner(target_host, (start_port, end_port), output_filename, progress_bar)

      print(f"Scan results saved in {output_filename}")
  except ValueError as e:
      print(f"Error: {e}")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")