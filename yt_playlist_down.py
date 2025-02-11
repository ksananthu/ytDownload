import yt_dlp

# Replace 'Playlist_URL' with the URL of the YouTube playlist you want to download
playlist_url = 'https://www.youtube.com/watch?v=sPEFXwsYytY&list=PLQnVQWG46dr3yLgnU_kEy4iRSLYPtzbAe'

# Options for yt-dlp
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'errorDict/%(title)s.%(ext)s', # Save the downloaded files in the 'Downloads' folder
    'skip_private': True,  # Skip private videos
}

# Download the playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print('Download completed!')