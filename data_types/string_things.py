name = "fancy pants"
print(name.title())
print(name.upper())
print(name.lower())

# String interpolation
first_name = "john"
last_name = "doe"
full_name = f"{first_name} {last_name}"
print(full_name.title())

# Stripping Whitespace
whitespace_string = "   Hello, World!   "
print(whitespace_string.strip())

# Removing Prefixes and Suffixes
filename = "report_final_draft.txt"
print(filename.removeprefix("report_"))
print(filename.removesuffix(".txt"))