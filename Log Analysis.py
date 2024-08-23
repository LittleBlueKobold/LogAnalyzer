import re           #module import

def analyze_logs(log_file):   #analyze logs
    with open(log_file, 'r') as file:
        for line in file:
            if re.search(r'failed login', line, re.IGNORECASE):
                print(f"Suspicious Activity Detected: {line.strip()}")

log_file = "system_logs.txt"    #desired log file to scan
analyze_logs(log_file)