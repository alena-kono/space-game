def read_file(filename: str) -> str:
    """Read file with filename given and return string."""
    with open(filename, "r", encoding="utf-8") as input_file:
        file_content = input_file.read()
    return file_content
