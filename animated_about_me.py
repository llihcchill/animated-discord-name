import json
import requests
import time

server_id = "server id"

headers = {
  "authorization": "authorisation key (under network tab in developer tools, a request called 'science' should contain your auth key)"
}

# to make nickname animation, input each animation frame into nickname_frames
about_me_frames = ["Test", "tEst", "teSt", "tesT"]
about_me_array = []

# properly format the frames for a PATCH request using a for loop with the output going into the nickname_array
for text in about_me_frames:
  about_me_array.append({"bio": f"{text}"})

while(True):
  for text in about_me_array:
    request = requests.patch(f"https://discord.com/api/v9/users/%40me/profile", headers=headers, json=text)
    time.sleep(10)
