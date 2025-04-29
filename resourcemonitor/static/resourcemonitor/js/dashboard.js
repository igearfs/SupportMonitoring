let isRequestInProgress = false;
let isGraphRequestInProgress = false;  // Flag for graph data

// Ensure the DOM is loaded before attaching event listeners
document.addEventListener('DOMContentLoaded', function() {

    // Function to update data (tables) from the server
    function updateData() {
        if (isRequestInProgress) return;
        isRequestInProgress = true;
        document.getElementById('spinner').style.display = 'block';

        fetch("/refresh/")
            .then(response => response.json())
            .then(data => {
                let tcpHTML = '<tr><th>Name</th><th>Host</th><th>Port</th><th>Status</th></tr>';
                data.tcp_results.forEach(item => {
                    tcpHTML += `<tr><td>${item.name}</td><td>${item.host}</td><td>${item.port}</td><td>${item.status}</td></tr>`;
                });
                document.getElementById('tcp-table').innerHTML = tcpHTML;

                let apiHTML = '<tr><th>Name</th><th>Host</th><th>Port</th><th>TCP Status</th><th>HTTP Status</th></tr>';
                data.api_results.forEach(item => {
                    apiHTML += `<tr><td>${item.name}</td><td>${item.host}</td><td>${item.port}</td><td>${item.tcp}</td><td>${item.http}</td></tr>`;
                });
                document.getElementById('api-table').innerHTML = apiHTML;

                let sftpHTML = '<tr><th>Name</th><th>Host</th><th>File Count</th><th>Status</th></tr>';
                data.sftp_results.forEach(item => {
                    sftpHTML += `<tr><td>${item.name}</td><td>${item.host}</td><td>${item.file_count}</td><td>${item.status}</td></tr>`;
                });
                document.getElementById('sftp-table').innerHTML = sftpHTML;
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            })
            .finally(() => {
                isRequestInProgress = false;
                document.getElementById('spinner').style.display = 'none';
            });
    }

    // Initial load of data
    updateData();
    setInterval(updateData, 10000);  // Update every 10 seconds for tables

    // Function to update the graph data (file count)
    function updateGraph(host) {
        if (!host || isGraphRequestInProgress) {
            // If no host or request is in progress, clear the graph
            Plotly.purge('file-count-chart'); // This will clear the existing graph
            return;
        }

        isGraphRequestInProgress = true;
        fetch(`/sftp-history-data?host=${encodeURIComponent(host)}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                    return;
                }

                const timestamps = data.data.map(item => new Date(item.timestamp * 1000));
                const counts = data.data.map(item => item.count);

                const trace = {
                    x: timestamps,
                    y: counts,
                    type: 'scatter',
                    mode: 'lines+markers',
                    name: `File Count for ${data.host}`,
                    line: { shape: 'spline' },
                    marker: { color: 'green' }
                };

                const layout = {
                    title: `File Count Over Time - ${data.host}`,
                    xaxis: { title: 'Time' },
                    yaxis: { title: 'File Count' }
                };

                Plotly.newPlot("file-count-chart", [trace], layout);
            })
            .catch(error => {
                console.error("Error fetching history:", error);
                alert("Failed to load file count history.");
            })
            .finally(() => {
                isGraphRequestInProgress = false;
            });
    }

    // Event listener for host selection to update the graph
    const sftpHostSelect = document.getElementById("sftp-host-select");
    sftpHostSelect.addEventListener("change", function () {
        const host = this.value;
        updateGraph(host);  // Update the graph when a new host is selected

        // If "Choose a Host" is selected, clear the graph and reset the dropdown
        if (!host) {
            Plotly.purge('file-count-chart');
            // Reset the dropdown to its default value
            this.value = "";  // This will set it to the first option, i.e., "-- Choose a Host --"
        }
    });

    // Auto-refresh graph every 10 seconds
    setInterval(() => {
        const host = sftpHostSelect.value;
        if (host) {
            updateGraph(host);  // Only update if there's a selected host
        } else {
            Plotly.purge('file-count-chart');  // Clear the graph if no host is selected
        }
    }, 10000);  // 10 seconds for graph updates

    // On page load, ensure the dropdown is reset to the default value
    sftpHostSelect.value = ""; // Make sure the dropdown is at "-- Choose a Host --" on page load

});
