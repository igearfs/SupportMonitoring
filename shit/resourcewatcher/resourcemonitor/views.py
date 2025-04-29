from django.shortcuts import render
from .tcp_monitor import check_tcp_port

def dashboard(request):
    targets = [
        {"name": "Google DNS", "host": "8.8.8.8", "port": 53},
        {"name": "Example.com", "host": "example.com", "port": 80},
    ]

    results = []
    for target in targets:
        is_up = check_tcp_port(target["host"], target["port"])
        results.append({
            **target,
            "status": "🟢 UP" if is_up else "🔴 DOWN"
        })

    return render(request, "resourcemonitor/dashboard.html", {"results": results})
