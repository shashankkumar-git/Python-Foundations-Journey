#PROBLEM STATEMENT - Take the string text = " Python_Programming_is_fun ". Clean the whitespace and replace the underscores with spaces

text = " Python_Programming_is_fun "
text = text.strip()
text = text.replace("_", " ")
print(text)
