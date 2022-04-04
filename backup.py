import os
from pytube import YouTube

Link = "https://www.youtube.com/watch?v=O3EB844h2nU"
Title = YouTube(Link)
Title = Title.title
os.startfile(f"E:\\Programming\\AI ASSISTANT\\Database\\Youtube\\{Title}.mp4")