# Basic Phishing Link Scanner - No external libraries

# Simulated blacklist and suspicious words
blacklist = ["badsite.com", "phishingsite.net"]
suspicious_words = ["login", "verify", "secure", "account", "update", "bank"]

def is_ip_format(url):
    # Very simple IP address check (not perfect, but good enough for beginner)
    parts = url.split('/')
    for part in parts:
        if part.count('.') == 3:
            nums = part.split('.')
            if all(num.isdigit() and 0 <= int(num) <= 255 for num in nums):
                return True
    return False

def check_blacklist(url):
    for bad in blacklist:
        if bad in url:
            return True
    return False

def check_suspicious_words(url):
    for word in suspicious_words:
        if word in url.lower():
            return True
    return False

# Main function
def scan_url():
    url = input("Enter a URL to scan: ")
    print("\nScanning URL:", url)

    flagged = False

    if is_ip_format(url):
        print("⚠ Warning: URL contains an IP address.")
        flagged = True

    if check_blacklist(url):
        print("🚫 Alert: URL is in the blacklist.")
        flagged = True

    if check_suspicious_words(url):
        print("⚠ Warning: URL contains suspicious keywords.")
        flagged = True

    if not flagged:
        print("✅ This URL looks clean (basic scan).")

# Run the program
scan_url()