def hide_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in s:
        if ch in vowels:
            result += "*"
        else:
            result += ch

    return result

print(hide_vowels("Hello World!"))  # Example usage