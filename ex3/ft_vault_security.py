print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols")

print("SECURE EXTRACTION:")

with open("classified_data.txt", "r") as file:
    content = file.read()
    print(content)

print("SECURE PRESERVATION:")

with open("vault_log.txt", "w") as file:
    file.write("{[}CLASSIFIED{]} New security protocols archived\n")

print("Vault automatically sealed upon completion")
print("All vault operations completed with maximum security.")
