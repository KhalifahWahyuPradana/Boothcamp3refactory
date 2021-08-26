def is_palindrome(input_string):
    new_string = ""
    for string in input_string.lower():
        if string.replace(" ",""):
            new_string = string + new_string
            reverse_string = string + reverse_string
    if new_string[::-1]==reverse_string
        return True
    return False

    print(is_palindrome("Radar")) # should be True
    print(is_palindrome("Malam")) # should be True
    print(is_palindrome("Kasur ini rusak")) # should be True
    print(is_palindrome("Ibu Ratna antar ubi")) # should be True
    print(is_palindrome("Malas")) # should be False
    print(is_palindrome("Makan nasi goreng")) # should be False
    print(is_palindrome("Balonku ada lima")) # should be False