import cv2
import os
from moviepy.editor import *

# Directory containing your image files (in alphabetical order)
image_folder = 'C:/Users/pc/Desktop/AI Images'
audio_file = 'C:/Users/pc/Downloads/audio.mp3'
video_name = 'output_video2.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort()  # Sort the images alphabetically

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as needed
video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

# Combine video and audio
video_clip = VideoFileClip(video_name)
audio_clip = AudioFileClip(audio_file)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile("final_output1.mp4")

# Clean up temporary files
os.remove(video_name)
