import os
import re
from datetime import datetime

FILE_PATH = "security.log"
USERS_FILE = "users.txt"
parsed_logs = []
failed_logins_by_ip = {}

def load_logs():
    global parsed_logs, failed_logins_by_ip
    parsed_logs = []
    failed_logins_by_ip = {}
    
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            pass
            
    log_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\d{1,3}(?:\.\d{1,3}){3})\s+([A-Z\s]+?)(?:\s+user=(\S+))?$")
    
    with open(FILE_PATH, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            match = log_pattern.match(line)
            if match:
                timestamp = match.group(1)
                ip = match.group(2)
                event_type = match.group(3).strip()
                username = match.group(4) if match.group(4) else "N/A"
                
                parsed_logs.append({
                    "timestamp": timestamp,
                    "ip": ip,
                    "event": event_type,
                    "user": username,
                    "raw": line
                })
                
                if event_type == "LOGIN FAILED":
                    failed_logins_by_ip[ip] = failed_logins_by_ip.get(ip, 0) + 1

def register_user():
    print("\n--- Register New User ---")
    username = input("Enter a new username: ").strip()
    password = input("Enter a new password: ").strip()
    
    # Save the new username and password to users.txt separated by a comma
    with open(USERS_FILE, 'a') as f:
        f.write(f"{username},{password}\n")
    print(f"[SUCCESS] User '{username}' registered! You can now log in.")

def simulate_login():
    print("\n--- Login Portal ---")
    ip = input("Enter your simulated IP address: ").strip()
    
    if failed_logins_by_ip.get(ip, 0) >= 3:
        print(f"[BLOCKED] IP Address {ip} is locked due to multiple failed attempts.")
        return
        
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    # Check if credentials match the default admin OR a user in users.txt
    is_authenticated = False
    if username == "admin" and password == "admin123":
        is_authenticated = True
    elif os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            for line in f:
                # Read the file and split the username and password
                stored_user, stored_pass = line.strip().split(',')
                if username == stored_user and password == stored_pass:
                    is_authenticated = True
                    break
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FILE_PATH, 'a') as file:
        if is_authenticated:
            print("[SUCCESS] Access Granted.")
            file.write(f"\n{timestamp} {ip} LOGIN SUCCESS user={username}")
        else:
            print("[FAILED] Access Denied.")
            file.write(f"\n{timestamp} {ip} LOGIN FAILED user={username}")
            
    load_logs()

def print_report():
    event_counts = {}
    for log in parsed_logs:
        event_counts[log["event"]] = event_counts.get(log["event"], 0) + 1
        
    print("\n=====================================")
    print("       Security Log Analysis         ")
    print("=====================================\n")
    
    print("--- Event Counts ---")
    for event, count in event_counts.items():
        print(f"{event}: {count}")
        
    print("\n--- SUSPICIOUS IPS (3+ Failed Logins) ---")
    suspicious = {ip: count for ip, count in failed_logins_by_ip.items() if count >= 3}
    if suspicious:
        for ip, count in suspicious.items():
            print(f"[ALERT] {ip} ({count} failed attempts)")
    else:
        print("None detected.")
    print("=====================================\n")

def run_interactive_menu():
    while True:
        print("\nSearch Logs By: [1] IP Address  [2] Event Type  [3] Username  [4] Return to Main Menu")
        choice = input("Select an option: ").strip()
        
        if choice == '4':
            break
            
        term = input("Enter search term: ").strip()
        results = []
        
        if choice == '1':
            results = [log for log in parsed_logs if term in log["ip"]]
        elif choice == '2':
            term = term.upper()
            results = [log for log in parsed_logs if term in log["event"]]
        elif choice == '3':
            results = [log for log in parsed_logs if term.lower() == log["user"].lower()]
        else:
            print("Invalid option.")
            continue
            
        print("\n--- Search Results ---")
        if results:
            for res in results:
                print(res["raw"])
        else:
            print("No logs found matching your criteria.")

def main():
    load_logs()
    
    while True:
        print("\n--- Main Menu ---")
        print("[1] Simulate Login")
        print("[2] Register New User")
        print("[3] Analyze Logs & Search")
        print("[4] Exit")
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            simulate_login()
        elif choice == '2':
            register_user()
        elif choice == '3':
            print_report()
            run_interactive_menu()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()