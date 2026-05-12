

# Automated-Log-Parser

A Python-based cybersecurity utility designed to parse Linux system logs for security threats. This tool identifies **SSH Brute Force** attempts and **Suspicious Web Activity** (SQL Injection, Directory Traversal, and Automated Scanners) using regular expression pattern matching.

## 🚀 Features

* 
**SSH Analysis:** Automatically extracts usernames and IP addresses from failed login attempts.


* 
**Threat Categorization:** Flags IPs with more than 3 failed attempts as `CRITICAL`.


* 
**Web Security Auditing:** Detects common attack signatures in web logs, such as `' OR '1'='1'` and access attempts to `/etc/passwd`.


* 
**Automated Reporting:** Generates a clean, formatted terminal report summarizing the security posture of the log file.



## 🛠️ Installation & Requirements

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/Automated-Log-Parser.git
cd Automated-Log-Parser

```


2. **Ensure you have Python 3.x installed:**
```bash
python3 --version

```



*No external libraries are required as the script uses standard Python modules (`re`, `sys`, `collections`).*

## 💻 Usage

To run the parser against a log file (such as the provided `test_logs.log`), use the following command:

```bash
python3 parser.py test_logs.log

```

## 📊 Sample Output

Based on the provided test logs, the tool detects several threats, including brute force attacks from `185.209.0.12` and suspicious web queries:

```text
[!] Alert: Suspicious Web Activity Detected: 127.0.0.1 ... "GET /index.php?id=1' OR '1'='1 HTTP/1.1"
[!] Alert: Suspicious Web Activity Detected: 127.0.0.1 ... "GET /etc/passwd HTTP/1.1"

========================================
      CYBERSECURITY LOG REPORT
========================================

[+] SSH Brute Force Analysis:
    - IP: 185.209.0.12    | Attempts: 5   | [CRITICAL]
    - IP: 203.0.113.5     | Attempts: 2   | [Warning]
    - IP: 45.33.2.145     | Attempts: 4   | [CRITICAL]

[+] Web Application Security:
    - Suspicious Patterns Found: 3

========================================

```

## 🔍 Log Patterns Detected

The script currently monitors for:

* 
**SSH:** `Failed password for (user) from (IP)`.


* 
**SQLi:** `' OR '1'='1` patterns.


* 
**LFI/Traversal:** `/etc/passwd` access attempts.


* 
**Scanners:** User-agents matching `Hydra`.



## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
