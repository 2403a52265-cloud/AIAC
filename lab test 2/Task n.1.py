import re

def mask_sensitive(log_line):
    email_pattern = r'([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    def mask_email(match):
        username = match.group(1)
        return f"{username}@*.com"

    phone_pattern = r'\b\d{7,}\b'
    def mask_phone(match):
        number = match.group(0)
        masked = '*' * (len(number) - 5) + number[-5:]
        return masked

    masked = re.sub(email_pattern, mask_email, log_line)
    masked = re.sub(phone_pattern, mask_phone, masked)
    return masked

if __name__ == "__main__":
    sample = (
        "User harsha logged in with email harsha.chary@example.com and phone\n"+
        
        "9876543210"
    )
    for line in sample.split('\n'):
        print(mask_sensitive(line))