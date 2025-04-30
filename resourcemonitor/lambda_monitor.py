import requests  # To make HTTP requests to the Lambda endpoint
import logging  # To log the responses

# Configure logging settings
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def check_lambda_status(url: str):
    """
    Check the status of a Lambda function through its API Gateway URL.
    Returns a tuple of (status, response_code), where:
        - status: "🟢" (green) if the Lambda is healthy, "🔴" (red) if not
        - response_code: The HTTP status code of the response
    """
    try:
        logging.info(f"Checking Lambda status for URL: {url}")
        response = requests.get(url, timeout=5)  # 5 second timeout for the HTTP request

        # Log the response status code
        logging.info(f"Response received with status code: {response.status_code}")

        if response.status_code == 200:
            return "🟢", response.status_code  # Green if the status is OK (200)
        else:
            return "🔴", response.status_code  # Red if the status is not OK (not 200)
    except requests.exceptions.RequestException as e:
        # Log the error if a request exception occurs
        logging.error(f"RequestException occurred: {str(e)}")
        return "🔴", str(e)  # Red status and the error message

