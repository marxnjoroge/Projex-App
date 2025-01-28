document.addEventListener('DOMContentLoaded', function() {
  const dot = document.getElementById('location-dot');
  const ipInfo = document.getElementById('ip-info');

  // Function to convert lat/long to x/y coordinates on our map
  function coordsToPixels(lat, lon) {
    const mapWidth = 280;
    const mapHeight = 140;
    
    // Convert longitude to x coordinate
    const x = (lon + 180) * (mapWidth / 360);
    
    // Convert latitude to y coordinate
    const latRad = lat * Math.PI / 180;
    const mercN = Math.log(Math.tan((Math.PI / 4) + (latRad / 2)));
    const y = (mapHeight / 2) - (mapWidth * mercN / (2 * Math.PI));
    
    return { x, y };
  }

  // Fetch IP info from ipapi.co
  fetch('https://ipapi.co/json/')
    .then(response => response.json())
    .then(data => {
      // Update IP info text
      ipInfo.innerHTML = `
        IP: ${data.ip}<br>
        Location: ${data.city}, ${data.country_name}<br>
        Coordinates: ${data.latitude.toFixed(2)}, ${data.longitude.toFixed(2)}
      `;

      // Position the dot
      const coords = coordsToPixels(data.latitude, data.longitude);
      dot.style.left = `${coords.x}px`;
      dot.style.top = `${coords.y}px`;
      dot.style.display = 'block';
    })
    .catch(error => {
      ipInfo.textContent = 'Error loading location data';
      console.error('Error:', error);
    });
});
