from pypresence import Presence  # The simple rich presence client in pypresence
import time

client_id = "649288547869786122"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client

RPC.connect()  # Start the handshake loop

while True:  # The presence will stay on as long as the program is running
    RPC.update(state="Rich Presence using pypresence!")  # Updates our presence
    time.sleep(15)  # Can only update rich presence every 15 seconds

