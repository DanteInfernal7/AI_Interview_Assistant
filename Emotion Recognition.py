import pandas as pd
from fer import FER
from fer import Video

location_videofile = r"C:\Users\hwala\Downloads\Rohan.mp4"

face_detector = FER(mtcnn=True)
input_video = Video(location_videofile)

processing_data = input_video.analyze(face_detector, display=True)

vid_df = input_video.to_pandas(processing_data)
vid_df = input_video.get_first_face(vid_df)
vid_df = input_video.get_emotions(vid_df)

pltfig = vid_df.plot(figsize=(20, 8), fontsize=16).get_figure()
pltfig.savefig(r'output\data.png')

angry = sum(vid_df.angry)
disgust = sum(vid_df.disgust)
fear = sum(vid_df.fear)
happy = sum(vid_df.happy)
sad = sum(vid_df.sad)
surprise = sum(vid_df.surprise)
neutral = sum(vid_df.neutral)

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
emotions_values = [angry, disgust, fear, happy, sad, surprise, neutral]

score_comparisons = pd.DataFrame(emotions, columns = ['Human Emotions'])
score_comparisons['Emotion Value from the Video'] = emotions_values