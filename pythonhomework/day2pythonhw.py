paragraph = """
This Python course is designed to introduce students to the basics of programming using Python.
It covers topics such as data types, control structures, functions, and object-oriented programming.
The course aims to provide a solid foundation for further study in Python and other programming languages.
"""

print(f"Length of the paragraph: {len(paragraph)} characters")

print(f"First character: '{paragraph[0]}'")
print(f"Last character: '{paragraph[-1]}'")

print(f"Preview (first 50 characters): '{paragraph[:50]}'")

modified_paragraph = paragraph.replace("Python", "PYTHON")
print(f"Modified paragraph with 'Python' replaced by 'PYTHON':\n{modified_paragraph}")

lowercase_paragraph = paragraph.lower()
print(f"Paragraph in lowercase:\n{lowercase_paragraph}")

stripped_paragraph = paragraph.strip()
print(f"Paragraph with extra whitespaces removed from start/end:\n{stripped_paragraph}")

words = paragraph.split()
print(f"Words in the paragraph: {words}")

if "course" in paragraph.lower():
    print("The word 'course' is found in the paragraph.")
else:
    print("The word 'course' is not found in the paragraph.")
    
print("The course description is {} characters long and has {} words.".format(len(paragraph), len(words)))