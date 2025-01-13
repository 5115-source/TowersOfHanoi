# Recursively count the occurrences of a character in a string
def count(s, ch, high):
    if len(s) == 0:  # Base case: empty string
        return high
    # Check if the first character matches and recurse
    if ch == s[0]:
        return count(s[1:], ch, high + 1)
    return count(s[1:], ch, high)


# Iterate through the words of the string and count occurrences
def count_main(s, ch):
    string_list = s.split()  # Split the string into words
    occurrence = 0
    for i in range(len(string_list)):
        occurrence += count(string_list[i], ch, 0)
    return occurrence


# Main function to handle user input and display the result
def main():
    string = str(input("Enter a string: "))
    character = str(input("Enter a character: "))
    while len(character) != 1:  # Ensure input is a single character
        character = input("Please enter a single character: ")
    number_times = count_main(string, character)
    print(f"{character} appears {number_times} time{
          's' if number_times != 1 else ''}.")


if __name__ == "__main__":
    main()
