import socket
import time
import datetime
import plotly.graph_objs as go
import plotly.offline as opy
from django.shortcuts import render

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            return True
    except (socket.timeout, socket.error):
        return False

def monitor_port(host, port, duration=30, interval=5):
    timestamps = []
    statuses = []

    start_time = time.time()
    next_check = start_time
    current_status = check_port(host, port)

    while time.time() - start_time < duration:
        now = time.time()
        if now >= next_check:
            new_status = check_port(host, port)
            if not timestamps or new_status != current_status:
                timestamps.append(now)
                statuses.append(new_status)
                current_status = new_status
            next_check += interval
        time.sleep(0.5)

    timestamps.append(time.time())
    statuses.append(current_status)
    return timestamps, statuses

def plot_lifeline(timestamps, statuses, host, port):
    times = [datetime.datetime.fromtimestamp(ts) for ts in timestamps]
    y = [1 if status else 0 for status in statuses]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=times,
        y=y,
        mode='lines+markers',
        line_shape='hv',
        line=dict(width=4),
        marker=dict(size=6),
        name=f"{host}:{port}"
    ))

    fig.update_layout(
        title=f"TCP Port Monitoring: {host}:{port}",
        xaxis_title="Time",
        yaxis=dict(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=['Down', 'Up'],
            range=[-0.1, 1.1]
        ),
        yaxis_title="Status",
        template='plotly_white'
    )

    div = opy.plot(fig, auto_open=False, output_type='div')
    return div

def monitor_view(request):
    host = 'localhost'  # You can later make this configurable via form
    port = 6661
    duration = 30  # 30 seconds monitoring
    interval = 5   # every 5 seconds check

    timestamps, statuses = monitor_port(host, port, duration, interval)
    plot_div = plot_lifeline(timestamps, statuses, host, port)

    return render(request, 'resourcemonitor/resourcemonitor.html', context={'plot_div': plot_div})
