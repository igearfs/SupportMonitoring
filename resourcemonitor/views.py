#
# Copyright (c) 2025 In-Game Event, A Red Flag Syndicate LLC.
# All rights reserved.
#
# Import necessary modules for rendering templates, handling JSON responses,
# and performing the monitoring functions.
from django.shortcuts import render
from django.http import JsonResponse
from .tcp_monitor import check_tcp_port  # Import the TCP monitoring function
from .api_monitor import check_http_response  # Import the HTTP response checker
from .sftp_monitor import check_sftp_file_activity, get_file_count_history  # Import SFTP-related functions

# Global list of monitoring targets (TCP, API, SFTP) with their respective details
# BELOW ARE PUBLIC SFTP'S WITH PUBLIC INFO FOR USER/PASS So don't give me grief about user/pass being in here.
# SEE: https://www.sftp.net/public-online-sftp-servers
# ALSO that last SFTP is for TCP Ping because there is no login or files to count. It's just a ping check. So it's really TCP at that point.
targets = [
    {"name": "Google", "host": "google.com", "port": 443, "type": "TCP"},
    {"name": "Cloudflare", "host": "1.1.1.1", "port": 443, "type": "TCP"},
    {"name": "Mirth Connect - Hospital A", "host": "localhost", "port": 6661, "type": "TCP"},
    {"name": "OpenAI API", "host": "api.openai.com", "port": 443, "url": "https://api.openai.com/v1/", "type": "API"},
    {"name": "GitHub API", "host": "api.github.com", "port": 443, "url": "https://api.github.com/", "type": "API"},
    {"name": "FakeAPI Test", "host": "example.com", "port": 443, "url": "https://example.com/", "type": "API"},
    {"name": "FTP - test.rebex.net", "host": "test.rebex.net", "port": 22, "username": "demo", "password": "password", "remote_dir": "/pub/example/", "type": "SFTP"},
    {"name": "FTP - itcsubmit.wustl.edu", "host": "itcsubmit.wustl.edu", "port": 22, "type": "TCP"}
]

def dashboard(request):
    """
    Dashboard view that renders the main page with the results of all monitoring targets.
    It checks the status of TCP connections, API responses, and SFTP file counts.
    """
    tcp_results = []  # List to hold TCP results
    sftp_results = []  # List to hold SFTP results
    api_results = []  # List to hold API results

    # Loop through all targets to check their status based on the type (TCP, API, SFTP)
    for target in targets:
        if target["type"] == "SFTP":
            # Perform SFTP monitoring for the target and append result to sftp_results
            ok, count, status = check_sftp_file_activity(
                host=target["host"],
                port=22,
                username=target.get("username", ""),
                password=target.get("password", ""),
                remote_dir=target.get("remote_dir", "/")
            )
            sftp_results.append({
                "name": target["name"],
                "host": target["host"],
                "file_count": count,
                "status": status
            })

        elif target["type"] == "API":
            # Perform TCP and HTTP monitoring for API targets and append the result to api_results
            tcp_status = "🟢" if check_tcp_port(target["host"], target["port"]) else "🔴"
            http_status = check_http_response(target["url"])
            api_results.append({
                "name": target["name"],
                "host": target["host"],
                "port": target["port"],
                "tcp": tcp_status,
                "http": http_status
            })

        else:  # Handle regular TCP monitoring
            status = "🟢" if check_tcp_port(target["host"], target["port"]) else "🔴"
            tcp_results.append({
                "name": target["name"],
                "host": target["host"],
                "port": target["port"],
                "status": status
            })

    # Retrieve the file count history for visualization
    file_count_history = get_file_count_history()

    # Pass the results and history to the template for rendering
    context = {
        "tcp_results": tcp_results,
        "sftp_results": sftp_results,
        "api_results": api_results,
        "file_count_history": file_count_history  # Include the file count history in the context
    }

    return render(request, "resourcemonitor/dashboard.html", context)  # Render the dashboard template

def refresh_data(request):
    """
    View to refresh data, performing the same monitoring checks and returning updated results in JSON format.
    """
    tcp_results = []  # List to hold refreshed TCP results
    sftp_results = []  # List to hold refreshed SFTP results
    api_results = []  # List to hold refreshed API results

    # Loop through all targets and perform the same checks as in the dashboard view
    for target in targets:
        if target["type"] == "SFTP":
            # Perform SFTP monitoring for the target
            ok, count, status = check_sftp_file_activity(
                host=target["host"],
                port=22,
                username=target.get("username", ""),
                password=target.get("password", ""),
                remote_dir=target.get("remote_dir", "/")
            )
            sftp_results.append({
                "name": target["name"],
                "host": target["host"],
                "file_count": count,
                "status": status
            })

        elif target["type"] == "API":
            # Perform TCP and HTTP monitoring for API targets
            tcp_status = "🟢" if check_tcp_port(target["host"], target["port"]) else "🔴"
            http_status = check_http_response(target["url"])
            api_results.append({
                "name": target["name"],
                "host": target["host"],
                "port": target["port"],
                "tcp": tcp_status,
                "http": http_status
            })

        else:  # Handle regular TCP monitoring
            status = "🟢" if check_tcp_port(target["host"], target["port"]) else "🔴"
            tcp_results.append({
                "name": target["name"],
                "host": target["host"],
                "port": target["port"],
                "status": status
            })

    # Retrieve the file count history for visualization
    file_count_history = get_file_count_history()

    # Return the updated results as a JSON response
    return JsonResponse({
        "tcp_results": tcp_results,
        "api_results": api_results,
        "sftp_results": sftp_results,
        "file_count_history": file_count_history  # Include the file count history in the response
    })

def sftp_history_page(request):
    """
    View to display the SFTP history page with available SFTP monitoring targets.
    """
    # Filter only SFTP targets based on the presence of a 'remote_dir' field
    sftp_targets = [t for t in targets if t.get("remote_dir") is not None]
    return render(request, "resourcemonitor/sftp_history.html", {"sftp_targets": sftp_targets})  # Render the SFTP history page

def sftp_history_data(request):
    """
    View to fetch historical file count data for a selected SFTP host.
    """
    host = request.GET.get("host")  # Retrieve the host parameter from the GET request
    if not host:
        return JsonResponse({"error": "Missing host"}, status=400)  # Return an error if host is not provided

    # Get the file count history
    history = get_file_count_history()

    # Filter the history for the selected host
    filtered = [(ts, count) for (ts, count, h) in history if h == host]

    # Return the filtered history as a JSON response
    return JsonResponse({
        "host": host,
        "data": [{"timestamp": ts, "count": count} for ts, count in filtered]
    })
