print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")


def handle_archive_access(filename):
    try:
        if filename == "standard_archive.txt":
            print("ROUTINE ACCESS: Attempting access to '" + filename + "'")
        else:
            print("CRISIS ALERT: Attempting access to '" + filename + "'")

        with open(filename, "r") as file:
            content = file.read()
            print("SUCCESS: Archive recovered - \"" + content.strip() + "\"")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis contained, diagnostics complete")


handle_archive_access("lost_archive.txt")
handle_archive_access("classified_vault.txt")
handle_archive_access("standard_archive.txt")

print("All crisis scenarios handled successfully. Archives secure.")
