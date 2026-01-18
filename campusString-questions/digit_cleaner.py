def extract_digits(s):
    result=""

    for ch in s:
        if ch.isdigit():
            result += ch
    return result

print(extract_digits("a1b2c3d4"))  # Example usage