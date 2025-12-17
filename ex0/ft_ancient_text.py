# ft_ancient_text.py

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print("Accessing Storage Vault: ancient_fragment.txt")

try:
    file = open("ancient_fragment.txt", "r")
    print("Connection established...")
    print("RECOVERED DATA:")

    content = file.read()
    print(content)

    file.close()
    print("Data recovery complete. Storage unit disconnected.")

except:
    print("ERROR: Storage vault not found. Run data generator first.")
