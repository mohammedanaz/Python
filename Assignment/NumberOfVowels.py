def count_vowels(string):
    print(sum(1 for x in string if x in "aeiouAEIOU"))

my_string = "An elephant is running towards you"
count_vowels(my_string)