document.addEventListener('DOMContentLoaded', function () {
    const tempElement = document.getElementById('temp');
    const vibrationElement = document.getElementById('vibration');
    const pressureElement = document.getElementById('pressure');
    const rpmElement = document.getElementById('rpm');
    const maintenanceElement = document.getElementById('maintenance');
    const ctx = document.getElementById('myChart').getContext('2d');

    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Temperature (°C)',
                borderColor: 'rgb(255, 99, 132)',
                data: []
            }, {
                label: 'Vibration (mm/s)',
                borderColor: 'rgb(54, 162, 235)',
                data: []
            }, {
                label: 'Pressure (Pa)',
                borderColor: 'rgb(75, 192, 192)',
                data: []
            }, {
                label: 'RPM',
                borderColor: 'rgb(153, 102, 255)',
                data: []
            }]
        },
        options: {}
    });

    function updateDashboard() {
        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                tempElement.textContent = data['Temperature (°C)'].toFixed(2);
                vibrationElement.textContent = data['Vibration (mm/s)'].toFixed(2);
                pressureElement.textContent = data['Pressure (Pa)'].toFixed(2);
                rpmElement.textContent = data['RPM'].toFixed(2);
                maintenanceElement.textContent = data['Maintenance Required'];

                chart.data.labels.push(data.Timestamp);
                chart.data.datasets[0].data.push(data['Temperature (°C)']);
                chart.data.datasets[1].data.push(data['Vibration (mm/s)']);
                chart.data.datasets[2].data.push(data['Pressure (Pa)']);
                chart.data.datasets[3].data.push(data['RPM']);

                chart.update();
            });
    }

    setInterval(updateDashboard, 2000);
});
