import json
import requests
import time

server_id = "server id"

headers = {
  "authorization": "authorisation key (under network tab in developer tools, a request called 'science' should contain your auth key)"
}

# to make nickname animation, input each animation frame into nickname_frames
nickname_frames = ["Test", "tEst", "teSt", "tesT"]
nickname_array = []

# properly format the frames for a PATCH request using a for loop with the output going into the nickname_array
for nick in nickname_frames:
  nickname_array.append({"nick": f"{nick}"})

while(True):
  for nick in nickname_array:
    request = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me", headers=headers, json=nick)
    time.sleep(1)






