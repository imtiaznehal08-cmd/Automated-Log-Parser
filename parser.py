#!/usr/bin/env python3
import re
import sys
from collections import Counter

# --- REGEX PATTERNS ---
# Matches SSH failed attempts
SSH_FAIL_RE = r"Failed password for (?:invalid user )?(\w+) from ([\d\.]+) port"
# Matches suspicious Web/Apache queries (SQLi or Directory Traversal)
WEB_SUSP_RE = r"(?:' OR '1'='1'|/etc/passwd|Hydra)"

def parse_logs(file_path):
    failed_attempts = []
    suspicious_web_requests = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # 1. Check for SSH Brute Force
                ssh_match = re.search(SSH_FAIL_RE, line)
                if ssh_match:
                    username = ssh_match.group(1)
                    ip_address = ssh_match.group(2)
                    failed_attempts.append((username, ip_address))

                # 2. Check for Web Attacks
                if re.search(WEB_SUSP_RE, line, re.IGNORECASE):
                    suspicious_web_requests += 1
                    print(f"[!] Alert: Suspicious Web Activity Detected: {line.strip()}")

        return failed_attempts, suspicious_web_requests

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

def generate_report(failed_data, web_count):
    print("\n" + "="*40)
    print("      CYBERSECURITY LOG REPORT")
    print("="*40)

    # Summarize SSH Failures
    ip_counts = Counter(ip for user, ip in failed_data)
    
    print(f"\n[+] SSH Brute Force Analysis:")
    if not ip_counts:
        print("    No failed logins detected.")
    for ip, count in ip_counts.items():
        status = "CRITICAL" if count > 3 else "Warning"
        print(f"    - IP: {ip:<15} | Attempts: {count:<3} | [{status}]")

    # Summarize Web Attacks
    print(f"\n[+] Web Application Security:")
    print(f"    - Suspicious Patterns Found: {web_count}")
    
    print("\n" + "="*40)

if __name__ == "__main__":
    # Ensure the user provided a log file argument
    if len(sys.argv) < 2:
        print("Usage: python3 parser.py <log_file>")
    else:
        log_to_scan = sys.argv[1]
        failed_list, web_total = parse_logs(log_to_scan)
        generate_report(failed_list, web_total)
