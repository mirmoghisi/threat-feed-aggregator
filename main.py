from src.extractor import extract_valid_ips


def main():
    # 1. Define the path to your log file
    file_path = "data/sample_logs.txt"

    print(f"[*] Opening {file_path}...")

    try:
        # 2. Open the file in 'read' mode ('r')
        with open(file_path, 'r') as file:
            # 3. Read the entire file into a single string variable
            raw_text = file.read()

        print("[*] File read successfully. Extracting IPs...")

        # 4. Pass the massive string into your extractor function
        found_ips = extract_valid_ips(raw_text)

        # 5. Output the results cleanly
        print(f"\n[SUCCESS] Found {len(found_ips)} valid IPs:")
        for ip in found_ips:
            print(f" - {ip}")

    except FileNotFoundError:
        print(f"[ERROR] Could not find the file at {file_path}")


if __name__ == "__main__":
    main()