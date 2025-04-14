import re

print('Ex1: --------------------------------------------------------')
# Check if a given string is a palindrome or not.

def is_palindrome(given_string):
    for x in range(int(len(given_string)/2)):
        if given_string[x] != given_string[len(given_string) - x - 1]:
            return False
    return True

string = 'pan a nap'

if is_palindrome(string):
    print('The string is palindrome')
else:
    print('The string is not palindrome')

print('Ex2: --------------------------------------------------------')
# Find the first most frequent character in a given string (edited)
# Sample output: The given string is : successes
# The first most frequent char in the string is: s

def most_frequent(given_string):
    frequency_dict = {}
    for char in given_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    max_count = 1
    max_char = None
    for char in frequency_dict:
        if frequency_dict[char] > max_count:
            max_count = frequency_dict[char]
            max_char = char

        return max_count, max_char

string = 'successes'
count, char  = most_frequent(string)

print(f'The first most frequent ({count} times) char in the string is: "{char}"')

print('Ex3: --------------------------------------------------------')
# From the below string extract, IP DATE PICS URL , and print it
# Input String
# '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248
# "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)'

def extract_info(given_string):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    date_pattern = r'\b\d{2}/[A-Za-z]{3}/\d{4}\b'
    pic_pattern = r'\b\w+\.(?:jpg|jpeg|png|gif)\b'
    url_pattern = r'http?://[^\s]+'

    ips = re.findall(ip_pattern, given_string)
    dates = re.findall(date_pattern, given_string)
    pics = re.findall(pic_pattern, given_string)
    urls = re.findall(url_pattern, given_string)

    print("IP Addresses: ", ips)
    print("Dates: ", dates)
    print("Pictures: ", pics)
    print("URLs: ", urls)

string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)'

extract_info(string)

print('Ex4: --------------------------------------------------------')
# Remove the duplicate characters from the String and print it
# Sample Output:
# The given string is: resources
# After removing duplicates characters the new string is: resouc

def remove_duplicates(given_string):
    result = ""
    unique_chars = set()

    for char in given_string:
        if char not in unique_chars:
            result += char
            unique_chars.add(char)

    return result

string = 'resources'
print(f'After removing duplicates characters, the new string is: "{remove_duplicates(string)}"')

print('Ex5: --------------------------------------------------------')
# Given a String find whether it is a valid 10-digit phone number. Number should be in format
# xxx-xxx-xxxx E.g 234-456-9999

def extract_phone_number(given_string):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    match = re.search(pattern, given_string)
    if match:
        return match.group()
    return None

string = '234-456-9999'

if extract_phone_number(string):
    print(f'Phone number found: {extract_phone_number(string)}')
else:
    print('No valid phone number found')