#
# Copyright (c) 2025 In-Game Event, A Red Flag Syndicate LLC.
# All rights reserved.
#
# Import necessary modules
import paramiko  # Paramiko is used to interact with remote SFTP servers
import time  # Time module is used for timestamps
import logging  # Logging module is used to log activity for debugging and tracing

# A list to hold the file counts for visualization
file_count_history = []

# Setup basic logging configuration
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG for detailed logs

def check_sftp_file_activity(host, port, username=None, password=None, remote_dir="/"):
    """
    This function connects to an SFTP server and fetches the file count in a specified directory.

    Args:
        host (str): The SFTP server host.
        port (int): The port to connect to on the server.
        username (str, optional): The username for authentication (default is None).
        password (str, optional): The password for authentication (default is None).
        remote_dir (str, optional): The remote directory to check for files (default is "/").

    Returns:
        tuple: A tuple containing a status ("OK" or "ERROR"), the file count, and a message.
    """
    global file_count_history  # Use the global list to store file count history

    try:
        # Initialize the SFTP connection using paramiko
        transport = paramiko.Transport((host, port))

        # If username and password are provided, connect using them
        if username and password:
            logging.debug(f"Attempting to connect with credentials: {username}/{password}")
            transport.connect(username=username, password=password)
        else:
            # Otherwise, attempt an anonymous connection
            logging.debug(f"Attempting anonymous connection")
            transport.connect()

        # Create the SFTP client from the transport session
        sftp = paramiko.SFTPClient.from_transport(transport)

        # List the files in the remote directory
        files = sftp.listdir(remote_dir)
        file_count = len(files)  # Get the count of files in the directory

        # ✅ Record the file count with the current timestamp and host
        timestamp = time.time()  # Get the current timestamp
        file_count_history.append((timestamp, file_count, host))  # Append the data to history

        logging.debug(f"Successfully fetched file count: {file_count} at {timestamp}")

        # Close the SFTP and transport connections
        sftp.close()
        transport.close()

        # Return success status, file count, and a success message
        return ("OK", file_count, "Successfully fetched file count")

    except paramiko.ssh_exception.SSHException as e:
        # Handle SSH errors (e.g., failed to connect)
        return ("ERROR", 0, f"SSHException: {str(e)}")
    except paramiko.sftp.SFTPError as e:
        # Handle SFTP-specific errors
        return ("ERROR", 0, f"SFTPError: {str(e)}")
    except Exception as e:
        # Handle all other exceptions
        return ("ERROR", 0, f"Error: {str(e)}")


def get_file_count_history():
    """
    This function returns the file count history as a list of tuples where each tuple
    contains a timestamp and a file count.

    Returns:
        list: A list of tuples containing timestamp, file count, and host.
    """
    return file_count_history  # Return the history of file counts
