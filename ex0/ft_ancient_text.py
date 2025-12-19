# ft_ancient_text.py
"""
Cyber Archives - Data Recovery System.

This script attempts to read and display the content of an ancient
text fragment stored in a file.
"""

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print("Accessing Storage Vault: ancient_fragment.txt")

try:
    file = open("ancient_fragment.txt", "r", encoding="utf-8")
    print("Connection established...")
    print("RECOVERED DATA:")

    content = file.read()
    print(content)

    file.close()
    print("Data recovery complete. Storage unit disconnected.")

except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
