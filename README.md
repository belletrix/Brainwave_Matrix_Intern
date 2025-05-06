Phishing Link Scanner
Basic Phishing Link Scanner (No External Libraries)

Introduction

This is a simple Python-based phishing link scanner created for beginners in cybersecurity and Python programming. The scanner analyzes a URL entered by the user and checks it against a simulated blacklist, suspicious keywords, and IP address formats to identify potentially dangerous links.

The project does not use any external libraries, making it lightweight and easy to understand for educational purposes.


What is a Phishing Link Scanner?

A Phishing Link Scanner is a tool designed to detect and warn users about potentially malicious or fraudulent URLs. Phishing links are typically crafted to look like legitimate websites but are actually meant to steal sensitive information such as login credentials, bank details, or personal data.

Such scanners help users avoid falling victim to phishing attacks by identifying:

Blacklisted domains known for malicious behavior.

Suspicious keywords commonly used in phishing URLs (e.g., "verify", "secure", "update").

IP-based URLs, which are often used to hide the real identity of a malicious site.

Features

Checks if the URL contains an IP address.

Scans the URL for suspicious keywords.

Matches the URL against a predefined blacklist.

Gives a simple, clear result: flagged or clean.

Requires no external Python libraries.


How to Use

1. Run the Python script.


2. When prompted, enter the URL you want to scan.


3. The scanner will analyze the URL and print the results.

Example

Enter a URL to scan: http://192.168.1.1/login

⚠ Warning: URL contains an IP address.
⚠ Warning: URL contains suspicious keywords.


Disclaimer

This tool performs a basic scan and is intended for learning purposes only. It does not replace advanced threat detection systems or antivirus software.
