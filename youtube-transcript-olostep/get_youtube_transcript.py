import os
from getpass import getpass

from olostep import Olostep  # make sure you've installed the Python SDK

VIDEO_URL = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"  # paste your video link here

# 1. Retrieve the API key
api_key = os.getenv("OLOSTEP_API_KEY")
if not api_key:
    api_key = getpass("Please enter your Olostep API Key: ")
    os.environ["OLOSTEP_API_KEY"] = api_key

# 2. Initialize the client
client = Olostep(api_key=api_key)

# 3. Get the transcript
try:
    result = client.scrapes.create(
        url_to_scrape=VIDEO_URL,
        formats=["json"],
        parser="@olostep/youtube-transcript",
    )
    data = result.json_content
    print(data["channel"]["name"], data["language"])
    for segment in data["segments"]:
        print(f"{segment['offset']:.0f}s  {segment['text']}")
except Exception as e:
    print(f"An error occurred while fetching the transcript: {e}")
