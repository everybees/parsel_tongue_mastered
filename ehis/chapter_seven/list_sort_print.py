from typing import List

list_of_chars: List[str] = [char for char in input("""
Enter a string
I will sort the characters in it 
And reverse it! -> """)]
string_result: str = "".join(sorted(list_of_chars))
print(string_result)
