import socket
import time

# 81 01 04 07 02 FF        zoom in          ptzoptics
# 81 01 04 07 03 FF        zoom out         ptzoptics
# 81 01 06 04 FF           home position    ptzoptics


# VISCA camera IP address and port                      81 01 04 66 03 ff        flip from packet sender/wireshark
ip_address = '10.0.0.106'
port = 5678

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the camera
sock.connect((ip_address, port))

def pack_bytes(bytestring):
    bytestring = bytestring.replace(" ", "")
    return bytes.fromhex(bytestring)

# Function to send VISCA commands
def send_visca_command(command):
    command_bytes = pack_bytes(command)
    sock.sendall(command_bytes)

# Example VISCA commands:
# client.send("Hello World! from client".encode('UTF-8'))
# Pan left
# send_visca_command("81 01 04 07 02 FF")           # ptz zoom in     8x 01 04 07 02 FF from user manual  81 01 06 01 10 10 01 01 ff
# send_visca_command("81 01 06 01 10 10 01 01 ff")
# send_visca_command("01 06 01 01 00 00 00 00")     # pan left
# time.sleep(2)  # Wait for pan to complete

# Pan right    81 01 06 04 FF
# send_visca_command("81 01 06 04 FF")                  # ptz home
# send_visca_command("81 01 06 01 10 10 02 01 ff")      # ptz zoom out                  81 01 06 01 10 10 02 01 ff
# send_visca_command("01 06 01 02 00 00 00 00")       # pan right
# time.sleep(2)  # Wait for pan to complete

# Tilt up
# send_visca_command("01 06 02 01 00 00 00 00")       # tilt up
# time.sleep(2)  # Wait for tilt to complete

# Tilt down
# send_visca_command("01 06 02 02 00 00 00 00")        # tilt down
# time.sleep(2)  # Wait for tilt to complete

# Zoom in
# send_visca_command("01 07 01 01 00 00 00 00")        # zoom in
# time.sleep(2)  # Wait for zoom to complete

# Zoom out
# send_visca_command("01 07 01 02 00 00 00 00")         # zoom out
# time.sleep(2)  # Wait for zoom to complete

# Home position
# 81 01 06 04 FF
# send_visca_command("81 01 06 04 FF")                     # home position ptzoptics
# send_visca_command("01 06 01 00 00 00 00 00")          # home position
# time.sleep(2)  # Wait for home position to complete

time.sleep(3)
send_visca_command("81 01 04 a4 03 ff")             # flip frame      ascii   \81\01\04\a4\03\ff
time.sleep(2)
# send_visca_command("\81\01\04\a4\03\ff")
# time.sleep(2)

send_visca_command("81 01 04 a4 02 ff")             # flip frame      ascii   \81\01\04\a4\02\ff
time.sleep(2)
# send_visca_command("\81\01\04\a4\02\ff")
# time.sleep(2)

# Close the socket
sock.close()
