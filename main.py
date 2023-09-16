def create_char_map(start_char, end_char):
  char_mapping = {}
  start = ord(start_char)
  end = ord(end_char)

  if not (start < end):
    # I'a unfamiliar with Python error handling best
    # practices so this might be improved upon
    raise ValueError(f"Char {start_char} must come before {end_char}")
  
  # range stop index is exclusive, so add 1
  for origin in range(start, end + 1):
    to = end - (origin - start)
    char_mapping[chr(origin)] = chr(to)

  return char_mapping

# This should have some documentation, uncertain how to best do this in Python
# 1. If the mapping does not contain a char (a parital map), we use the original char
# 2. If the mapping is non-unique we might lose data
def transcode_string(mapping, message):
  # While list comprehension is ok, inlcuding conditionals gets messy
  return ''.join([mapping[char] if char in mapping else char for char in list(message)])

lower_case_mapping = create_char_map('a', 'z')
upper_case_mapping = create_char_map('A', 'Z')

mapping = {**lower_case_mapping, **upper_case_mapping}


# Simple decorater
def encode(message):
  return transcode_string(mapping, message)


string = "Hello World"

print(string)
print(encode(string))
print(encode(encode(string)))
