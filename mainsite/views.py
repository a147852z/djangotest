from django.shortcuts import render
from datetime import datetime
from .models import Post
import cv2
from django.http import StreamingHttpResponse
import numpy as np
from django.http import HttpResponse
import threading
import time
import math
global src

src = cv2.imread("C:/Users/Gslab/Desktop/c109112107/django/django/55555.jpg")
src = cv2.resize(src,(480,270))
def job(video,i):
    global p

    if len(a) == 1:
        while True:
            success, frame = video.read()  
            frame = cv2.resize(frame, (480, 270))
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            p = (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    else: 
        frames.append(src)
        while True:
            try:
                success, frame = video.read()  
                frame = cv2.resize(frame, (480, 270))
                frames[i] = frame            
            except:
                pass

def yy():
    x = math.ceil(len(a) / 4)
    global p  
    d = 0
    if x == 1:
        print('ok2')
        while True:
            try:
                frame = np.hstack(frames)
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                p = (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except:
                pass
    elif x > 1:
        q = []
        qs = []
        q2 = []
        for i in range(4):
            q.append(src)
        for i in range(x * 4 - len(frames)):
            frames.append(src)
        while True:
            for j in range(x):
                for i in range(4):
                    q[i] = frames[j*4+i]
                qs = np.hstack(q)
                q2.append(qs)
            qf = np.vstack(q2)
            q2 = []
            ret, buffer = cv2.imencode('.jpg', qf)
            frame = buffer.tobytes()
            p = (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        

    
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    word = "1123"
    return render(request, 'index.html', locals())
def gen(camera):
    print('len:',len(a))
    ii = len(a)
    threads = []
    for i in range(ii):
        camera = a[i]
        video=cv2.VideoCapture()
        video.open(camera)  
        print("streaming live feed of ",camera)
        threads.append(threading.Thread(target = job, args = (video,i)))
        threads[i].start()    
    if ii>1:
        print('ok')
        tt = threading.Thread(target = yy, args = ())
        tt.start()
    while True:
        try:
            yield p
        except:
            pass
    

def camerafeed(request): 
    return StreamingHttpResponse(gen("camera"),content_type="multipart/x-mixed-replace;boundary=frame")

# /views
global a,b,frames,x
x = 0
a = []
b = []
frames = []
def test_view(request):
    word = "123"
    now = datetime.now()
    if request.method == 'POST':
        data_from_html = request.POST.get('word')
        data_from_html2 = request.POST.get('word2')
        if not data_from_html=="":
            a.append(request.POST.get('word'))
            HttpResponse(f'views得到表单数据{data_from_html}')
            print(request.POST.get('word'))
            b.append("img"+str(len(a)))
        try:
            int(data_from_html2)
            if not data_from_html2=="":
                a.pop(int(data_from_html2)-1)
        except:
            pass
    python_data = "python里的数据"
    return render(request, "index.html", {"html_data_name":python_data,"list":a})