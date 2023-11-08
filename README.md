# Port Scanning Program Readme

## User Testing Guide

Welcome to our Python port scanning program! This program is designed to help you scan open ports on a target host using both a Command Line Interface (CLI) and a Graphical User Interface (GUI). This guide will walk you through the steps to set up your environment and run the program successfully.

### Set Up Your Environment

Before you can use our port scanning program, you need to set up your environment. Please follow these steps:

1. Ensure you have Python installed on your system. You can download Python from [Python's official website](https://www.python.org/downloads/).

2. Download the program files to your local machine.

3. Open your terminal or command prompt and navigate to the directory where you have saved the program files.

4. Install the required Python libraries, if not already installed, by running the following command:

pip install -r requirements.txt


### Running the Program

Our program is designed to be run in two ways: using the CLI or the GUI. Follow the instructions below to run the program using your preferred method.

#### Using the CLI

1. Open your terminal or command prompt.

2. Navigate to the directory where you have saved the program files.

3. Run the program by executing the following command:

python scan.py


4. You can also use the `-g` flag to enable the GUI mode:

python scan.py -g


#### Using the GUI

1. Open your terminal or command prompt.

2. Navigate to the directory where you have saved the program files.

3. Run the program in GUI mode by executing the following command:

python scan.py -g


### Scanning Ports

After launching the program, you will be prompted to input the following information:

1. Target Host: Enter the IP address of the host you want to scan for open ports.

2. Port Range: Specify a range of ports by providing a valid starting port and a valid ending port (e.g., 1-1024).

- The program will only accept port ranges between 1 and 65535.
- The starting port must be valid and less than the ending port.

### Program Functionality

Once you have provided the necessary input, the program will:

1. Scan the specified range of ports on the target host to determine if they are open or closed.

2. Display the results of the scan, indicating which ports are open and which are closed.

3. Implement error handling for cases where the target host is unreachable or invalid input is provided.

4. Log the results of the scan, and the program will provide you with the name of the log file that was created for later analysis.

## Key Features

Our port scanning program offers the following key features:

- **User Input:** You can input the target host and a range of ports to scan, making it easy to customize your scanning preferences.

- **Port Scanning:** The program implements a reliable port scanning algorithm to check the status of the specified ports on the target host, determining whether they are open or closed.

- **Output:** It displays the results of the scan, making it clear which ports are open and which are closed, enabling you to assess the security of the target host.

- **Error Handling:** The program handles errors gracefully, ensuring that it provides informative feedback in cases where the target host is unreachable or when invalid input is provided.

- **Logging:** It logs the results of the scan, allowing you to review and analyze the findings at a later time, which can be valuable for security analysis and monitoring.

We hope you find our port scanning program useful for your scanning needs. If you encounter any issues or have any feedback, please feel free to reach out to us. Happy scanning!


