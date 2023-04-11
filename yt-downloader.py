import pytube
import validators
import os
from moviepy.editor import *

validInput = False
while not validInput:
    link = input("Enter url: ")
    validation = validators.url(link)
    if validation:
        validInput = True
    else:
        print("Invalid input. Please enter only youtube URL.")


def downloadProgress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(percent)


yt = pytube.YouTube(link)

# for stream in yt.streams:
# print(stream)

video = False
validInput = False
while not validInput:
    question = input("Video or Audio ? (v, a):")
    if question in ["v", "a"]:
        if question == "a":
            tag = 248
            convertion = True
        else:
            tag = 248
            video = True
            convertion = False
        validInput = True
    else:
        print("Invalid input. Please enter only v or a.")

print(f"Download of \"{yt.title}\" in progress please wait...")
yt.register_on_progress_callback(downloadProgress)
yt.streams.get_by_itag(251).download("./download/audio")

if video == True:
    yt.streams.get_by_itag(tag).download("./download/video")

    old_name_1 = os.path.join(f"./download/audio/{yt.title}.webm")
    new_name_1 = os.path.join("./download/audio/audio.webm")
    old_name_2 = os.path.join(f"./download/video/{yt.title}.webm")
    new_name_2 = os.path.join("./download/video/video.webm")
    os.rename(old_name_1, new_name_1)
    os.rename(old_name_2, new_name_2)

    video_clip = VideoFileClip(f"./download/video/video.webm")
    audio_clip = AudioFileClip(f"./download/audio/audio.webm")
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(f"./download/{yt.title}.mp4")

if convertion == True:
    print(f"Convertion of \"{yt.title}\" in progress please wait...")
    audio = AudioFileClip(f"./download/audio/{yt.title}.webm")
    audio.write_audiofile(f"./download/audio/{yt.title}.mp3")

# yt.streams.filter(progressive=True, only_audio=True)
# yt.register_on_progress_callback(downloadProgress)
# stream = yt.streams.get_highest_resolution()
# stream.download()
print("The download is done")
