import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import json
from datetime import datetime

def get_ip_info():
    """Fetch IP and location information from ipapi.co"""
    try:
        response = requests.get('http://ip-api.com/json/')
        return response.json()
    except Exception as e:
        st.error(f"Error fetching IP information: {str(e)}")
        return None

def create_map(lat, lon, location_info):
    """Create a Folium map centered on the user's location"""
    # Create map centered on location
    folmap = folium.Map(location=[lat, lon], zoom_start=4)
    
    # Add a circular marker with popup
    folium.CircleMarker(
        location=[lat, lon],
        radius=8,
        popup=f"Your Location: {location_info}",
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(folmap)
    
    return folmap

def main():
    # st.set_page_config(page_title="MyLoc - IP Location Tracker", layout="wide")
    
    # Add custom CSS for the glowing effect
    st.markdown("""
        <style>
        .glow {
            animation: glow 1.5s ease-in-out infinite alternate;
        }
        @keyframes glow {
            from {
                text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #ff0000;
            }
            to {
                text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #ff0000;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("🌍 MyLoc - IP Location Tracker")
    
    # Add refresh button
    refr = "refloc"
    if st.button("🔄 Refresh Location", key=refr):
        st.cache_data.clear()
    
    # Fetch IP info
    ip_info = get_ip_info()

    # # Test ip location (write to page).
    # st.write(ip_info)
    
    if ip_info:
        # Display IP information in a card
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📍 Location Details")
            st.markdown(f"""
            - **IP Address:** {ip_info.get('ip')}
            - **City:** {ip_info.get('city')}
            - **Region:** {ip_info.get('region')}
            - **Country:** {ip_info.get('country_name')}
            - **ISP:** {ip_info.get('org')}
            """)
        
        lat = "latitude"
        lon = "longitude"

        with col2:
            st.markdown("### 🌐 Geographic Coordinates")
            st.markdown(f"""
            - **Latitude:** {ip_info.get('lat')}
            - **Longitude:** {ip_info.get('lon')}
            - **Timezone:** {ip_info.get('timezone')}
            - **Current Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """)
        
        # Create and display map
        st.markdown("### 🗺️ Your Location on Map")
        location_info = f"{ip_info.get('city')}, {ip_info.get('country_name')}"
        m = create_map(ip_info.get('lat'), ip_info.get('lon'), location_info)
        st_folium(m, width=1000, height=500)
        
        # Add timestamp
        st.markdown("---")
        st.markdown(f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        
    else:
        st.error("Unable to fetch location data. Please try again later.")

if __name__ == "__main__":
    main()

# # Test ipify.org data.
# ipify_address = requests.get('https://api.ipify.org').text

# st.write(ipify_address)

# response = requests.get(f'http://ip-api.com/json/{ipify_address}').json()
# st.write(response)