"""
Write a function that takes in two strigns: a main string and a potential
substring of the main string. The funciton should return a version of the main
string with every instance of the substring in it wrapped between underscores.
If tow instances of the substring in the main string overlap each other or sit
side by side, the underscores relevant to these two substring should only
appear on the far left of the left substring and on the far right of the
right substring. If the main string does not contain the other string at all,
return the main string intact

"""
def underscorify_substring(string, substring):
    # Write your code here.
    
string = "this is a test to see if it works"
substring = "test"
print(underscorify_substring(string, substring))
