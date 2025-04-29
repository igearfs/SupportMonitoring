#
# Copyright (c) 2025 In-Game Event, A Red Flag Syndicate LLC.
# All rights reserved.
#
# Import necessary module for TCP connection handling
import socket  # The socket module is used for creating network connections and handling network-related tasks

def check_tcp_port(host, port, timeout=3):
    """
    This function checks if a TCP connection can be established to a given host and port.

    Args:
        host (str): The host to which the TCP connection is to be made (e.g., "localhost").
        port (int): The port on the host to which the TCP connection is to be made.
        timeout (int, optional): The timeout in seconds to wait before failing (default is 3 seconds).

    Returns:
        bool: True if the TCP connection was successful, False if it failed or timed out.
    """
    try:
        # Try to create a TCP connection to the provided host and port with a specified timeout
        with socket.create_connection((host, port), timeout=timeout):
            return True  # Return True if the connection is successful
    except (socket.timeout, socket.error):
        # If a timeout or error occurs, return False to indicate the connection was unsuccessful
        return False
