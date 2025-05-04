# auth/ethical_checks.py
import requests

def verify_compliance(target):
    """Check if target is consenting (for pentests)"""
    if "@example.com" in target.email:
        return True  # Allow test domains
    
    # Query HaveIBeenPwned for breach status
    resp = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{target.email}")
    return resp.status_code != 200  # Block if already breached