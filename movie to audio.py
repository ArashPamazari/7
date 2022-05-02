from moviepy import editor

video = editor.VideoFileClip('musice mored nazar.mp4')
video.audio.write_audiofile('musice mored nazar.mp3')

