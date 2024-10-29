from flask import Flask, request
import datetime
import socket
import netifaces as ni

app = Flask(__name__)

def get_mac_address():
    # Function to get the MAC address of the host
    for iface in ni.interfaces():
        try:
            mac = ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']
            if mac:
                return mac
        except KeyError:
            continue
    return "N/A"

@app.route('/')
def user_info():
    # Get user IP
    user_ip = request.remote_addr
    
    # Get system username (from environment)
    username = request.headers.get('Username', 'Guest')
    
    # Get MAC address
    mac_address = get_mac_address()
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Display all details
    return f"""
    <html>
    <body>
        <p><b>IP Address:</b> {user_ip}</p>
        <p><b>MAC Address:</b> {mac_address}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Timestamp:</b> {timestamp}</p>
        <br>
        <h3>Assignment completed successfully!</h3>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
