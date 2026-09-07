# SY: Security Log Analyzer

A command-line security log analyzer and login simulator built in Python to detect suspicious authentication activity and parse structured log files.

## Features
- **Regex Log Parsing:** Reads and parses timestamped security logs while safely skipping malformed entries without crashing.
- **Event Counting & Threat Detection:** Tallies event types and flags any IP address with 3 or more failed login attempts.
- **Login Simulation & User Registration:** Allows registering new users to `users.txt` and simulates login attempts with automatic IP blocking for suspicious addresses.
- **Interactive Search:** Filter logs dynamically by IP address, event type, or username.

## Log Format
Log entries follow the format:
`YYYY-MM-DD HH:MM:SS <IP_ADDRESS> <EVENT_TYPE> user=<USERNAME>`

Example:
`2026-08-20 10:15:29 192.168.1.20 LOGIN FAILED user=admin`

## Data Structures & Complexity
- **`dict` (Hash Map):** Used for `failed_logins_by_ip` and `event_counts` to ensure $O(1)$ average time complexity for lookups and counter increments.
- **`list`:** Stores parsed `LogEntry` records to preserve chronological order for sequential filtering ($O(N)$).
- **Time Complexity:** $O(N)$ for parsing and linear search queries, where $N$ is the number of log lines.
- **Space Complexity:** $O(N)$ to store parsed records in memory.

## How to Run
1. Place `main.py` and `security.log` in the same directory.
2. Run the script:
   ```bash
   python main.py
