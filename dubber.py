from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip

video = VideoFileClip("video.mp4")
tts = gTTS("Yeh ek Hindi dubbing demo hai", lang='hi')
tts.save("audio.mp3")

audio = AudioFileClip("audio.mp3").set_duration(video.duration)
final = video.set_audio(audio)
final.write_videofile("final_dubbed_video.mp4")
