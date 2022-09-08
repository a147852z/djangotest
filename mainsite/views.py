from django.shortcuts import render
from datetime import datetime
from .models import Post
import cv2
from django.http import StreamingHttpResponse
import numpy as np
from django.http import HttpResponse
import threading
import time
def job(video):
    global p,i
    i=1
    while True:
        success, frame = video.read()  
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        p = (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        i = 0
    
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    word = "1123"
    return render(request, 'index.html', locals())
def gen(camera):
    camera = a[0]
    video = cv2.VideoCapture()
    video.open(camera)
    print("streaming live feed of ",camera)
    t = threading.Thread(target = job, args = (video,))
    t.start()
    while True:
        if i == 0:
            yield p
    

def camerafeed(request): 
    return StreamingHttpResponse(gen("camera"),content_type="multipart/x-mixed-replace;boundary=frame")

def select_art(request):
    if request.method == 'GET':
        que = request.GET.get('que')
    request.session['que'] = que

# /views
global a
a = []

def test_view(request):
    if request.method == 'POST':
        data_from_html = request.POST.get('word')
        a.append(request.POST.get('word'))
        HttpResponse(f'views得到表单数据{data_from_html}')
        print(request.POST.get('word'))
    python_data = "python里的数据"
    return render(request, "index.html", {"html_data_name":python_data})