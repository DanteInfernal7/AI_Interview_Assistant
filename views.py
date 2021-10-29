import pandas as pd
from fer import FER
from fer import Video
import csv
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import Resume_Parser
import ResumeFeedbackCreator
from flask import Flask, render_template, url_for, request, redirect, Blueprint, send_file
from datetime import datetime

import AudioVideoSplitter
import Speech_To_Text
import Speech_Parser
import videoFeedbackCreator

views = Blueprint(__name__, "views")

@views.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@views.route('/resumeanalyzer/', methods=['POST', 'GET'])
def resumeanalyzer_page():
    return render_template("resumeanalyzer.html")

@views.route('/login/', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@views.route('/blog/', methods=['POST', 'GET'])
def blog():
    return render_template("blog-single.html")

@views.route('/uploader2/', methods=['POST', 'GET'])
def analyzeResume():
    if request.method == 'POST':
        f2 = request.files['resume_file']
        f2.save(secure_filename(f2.filename))
    
        name2 = "Name2"

        n2 = str(f2)
        n2 = n2[15:-78]
        n2 = n2.replace(" ", "_")
        print(n2)

        resumeWordCorrections = Resume_Parser.resumeAnalyzer(n2)
        ResumeFeedbackCreator.resumeFeedbackGenerator(name2, resumeWordCorrections)
        return down(name2)

@views.route('/uploader/', methods=['POST', 'GET'])
def analyze():
 
    if request.method == 'POST':
        f = request.files['resume']
        f.save(secure_filename(f.filename))

        name = "Name"

        n = str(f)
        n = n[15:-16]
        print(n)

        location_videofile = n

        AudioVideoSplitter.splitAudio(name,location_videofile)
        
        userSpeech = Speech_To_Text.speechToText(name)

        speechFeedback = Speech_Parser.speechAnalyzer(userSpeech)

        face_detector = FER(mtcnn=True)
        input_video = Video(location_videofile)

        processing_data = input_video.analyze(face_detector, display=False)

        vid_df = input_video.to_pandas(processing_data)
        vid_df = input_video.get_first_face(vid_df)
        vid_df = input_video.get_emotions(vid_df)

        pltfig = vid_df.plot(figsize=(20, 8), fontsize=16).get_figure()
        pltfig.savefig('output\\'+name+'.png')

        angry = sum(vid_df.angry)
        disgust = sum(vid_df.disgust)
        fear = sum(vid_df.fear)
        happy = sum(vid_df.happy)
        sad = sum(vid_df.sad)
        surprise = sum(vid_df.surprise)
        neutral = sum(vid_df.neutral)

        emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        emotions_values = [angry, disgust, fear, happy, sad, surprise, neutral]

        score_comparisons = pd.DataFrame(emotions, columns = ['Emotions'])
        score_comparisons['Value'] = emotions_values
        score_comparisons.to_csv(name+'.csv', index=False)

        videoFeedbackCreator.interviewFeedbackGenerator(name, speechFeedback)
        return down()


@views.route('/down')
def down(name):
    path = (name+'.docx')
    return send_file(path,as_attachment=True)