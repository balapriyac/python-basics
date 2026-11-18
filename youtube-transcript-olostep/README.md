# YouTube Transcript with Python and Olostep

Get a YouTube video's transcript in a few lines of Python. The script sends one request to the [Olostep](https://www.olostep.com) Scrapes API with the `@olostep/youtube-transcript` parser and prints the channel, the language and every line with its timestamp.

Read the step-by-step tutorial: [link to article]

## Prerequisites

- Python 3.11 - 3.13
- An Olostep API key. New accounts get 500 free credits: [olostep.com/auth](https://www.olostep.com/auth)

## Setup

```bash
pip install olostep
export OLOSTEP_API_KEY="your-api-key"
```

If `OLOSTEP_API_KEY` is not set, the script prompts for the key when it runs.

## Usage

1. Open `get_youtube_transcript.py` and replace `VIDEO_URL` with your video link.
2. Run the script:

```bash
python get_youtube_transcript.py
```

The first line of output is the channel name and the language code. Each line after it is a timestamp in seconds followed by the spoken text.

## Supported links

Any single-video link works: `youtube.com/watch`, `youtu.be`, Shorts, live and embed links, and the like. Playlists and channels are not supported.

## Notes

- The parser reads a video's existing captions, auto-generated ones included. It does not transcribe the audio, so a video with no captions has no transcript.
- Each transcript uses 3 credits. Failed requests are not charged. 
- For all request options, see the [Scrapes API reference](https://docs.olostep.com/api-reference/scrapes/create).
