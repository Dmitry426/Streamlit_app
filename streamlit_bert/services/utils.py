from typing import Dict

import requests
import streamlit

from streamlit_bert.core.settings import settings


def query(data: Dict):
    """
    Send a POST request to the API URL with provided data and return the JSON response.

    Args:
        data (dict): The data to be sent in the request body.

    Returns:
        dict or None: A dictionary containing the JSON response from the API, or None if an error occurred.

    """
    try:
        response = requests.post(settings.API_URL, headers=settings.headers, data=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        streamlit.error(f"Error occurred during API request: {e}")
        return None
