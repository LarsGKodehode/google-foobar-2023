def create_char_mapping(start_char: str, end_char: str):
  """
  Create a character mapping dictionary between start_char and end_char.
  
  Args:
    start_char (str): The starting character.
    end_char (str): The ending character.
  
  Returns:
    dict: A dictionary with character mappings.
  
  Raises:
    ValueError: If start_char is not before end_char in the Unicode sequence.
  """

  char_mapping = {}
  start = ord(start_char)
  end = ord(end_char)

  if not (start < end):
    # I'am unfamiliar with Python error handling best
    # practices so this might be improved upon
    raise ValueError(f"Char {start_char} must come before {end_char}")
  
  # range end index is exclusive, so add 1
  for origin in range(start, end + 1):
    to = end - (origin - start)
    char_mapping[chr(origin)] = chr(to)

  return char_mapping

def transcode_string(mapping: dict, message: str) -> str:
  """
  Transcodes a string using the provided mapping
  - If the mapping does not contain a char (a partial map)
    the original char is used
  - If the mapping is non-unique data is lost

  Args:
    mapping: A dictionary containing mappings to use
    message: the input message
  
  Returns:
    str: The transcoded message
  """
  
  # Loop through each char in message
  # and append the associated mapping value
  # or the character if no mapping exists
  result = []
  for char in message:
    if char in mapping:
      result.append(mapping[char])
    else:
      result.append(char)

  return ''.join(result)


def test(test_string = "Foobar"):
  """
  Runs a simple test on this modules functionality

  Args:
    test_string (str): Optional custom string to test
  """

  # Create mappings
  lower_case_mapping = create_char_mapping('a', 'z')
  upper_case_mapping = create_char_mapping('A', 'Z')
  mapping = {**lower_case_mapping, **upper_case_mapping}

  # Test Case
  print(f"Original string: {test_string}")
  print(f"Transcoded once: {transcode_string(mapping, test_string)}")
  print(f"Transcoded twice: {transcode_string(mapping, transcode_string(mapping, test_string))}")