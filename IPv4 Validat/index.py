def is_valid_ip(ip):
    parts = ip.split(".")

    # Must have exactly 4 parts
    if len(parts) != 4:
        return False

    for part in parts:
        # Each part must be numeric
        if not part.isdigit():
            return False

        number = int(part)

        # Each number must be between 0 and 255
        if number < 0 or number > 255:
            return False

    return True


# User input
ip_input = input("Enter an IP address: ")

if is_valid_ip(ip_input):
    print("✅ Valid IPv4 address")
else:
    print("❌ Invalid IPv4 address")
