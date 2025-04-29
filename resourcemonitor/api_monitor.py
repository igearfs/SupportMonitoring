#
# Copyright (c) 2025 In-Game Event, A Red Flag Syndicate LLC.
# All rights reserved.
#
# Import necessary modules
import socket  # Import socket to handle TCP connections
import requests  # Import requests to make HTTP requests

def check_tcp_port(host, port, timeout=3):
    """
    This function attempts to establish a TCP connection to the specified host and port.

    Args:
        host (str): The host to connect to.
        port (int): The port on the host to connect to.
        timeout (int, optional): Timeout for the connection attempt, default is 3 seconds.

    Returns:
        bool: Returns True if the TCP connection is successful, otherwise False.
    """
    try:
        # Attempt to create a TCP connection to the provided host and port within the timeout
        with socket.create_connection((host, port), timeout=timeout):
            return True  # Return True if the connection is successful
    except Exception:
        # Return False if there is any exception (indicating failure to connect)
        return False

def check_http_response(url, timeout=3):
    """
    This function checks the HTTP response by making a HEAD request to the given URL.

    Args:
        url (str): The URL to check the HTTP response for.
        timeout (int, optional): Timeout for the HTTP request, default is 3 seconds.

    Returns:
        str: A status message indicating success or failure of the HTTP request.
    """
    try:
        # Send an HTTP HEAD request to the URL with the specified timeout
        r = requests.head(url, timeout=timeout)
        # Return a success message along with the HTTP status code
        return f"🟢 {r.status_code}"
    except Exception as e:
        # Return a failure message along with the error details if the request fails
        return f"🔴 {str(e)}"
