__all__ = "get_base64_of_bin_file"

import base64

import streamlit


def get_base64_of_bin_file(bin_file: str):
    """
    Read a binary file and return its Base64 encoded representation as a string.

    Args:
        bin_file (str): Path to the binary file.

    Returns:
        str or None: The Base64 encoded string representation of the binary file, or None if the file is not found.

    """
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        streamlit.error("File not found.")
        return None
