import torch
import shutil
from flask import Flask, render_template, request, redirect, url_for, abort
from datetime import datetime


app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def upload_file():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        # 画像をアップロードする
        f=request.files["file"]
        image_name=datetime.now().strftime("%Y%m%d%H%M%S")
        filepath='./static/'+image_name+'.png'
        f.save(filepath)

        # YoLov5のセッティング
        device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        model=torch.hub.load('ultralytics/yolov5','custom',path='./best.pt')
        model.to(device)

        #予測実行&予測結果保存
        result=model(filepath)
        result.save()
        Judge=True
        #検出画像をWeb上で表示する処理
        detect_image_path="runs/detect/exp/"+image_name+'.jpg'
        html_file_path='./static/'+image_name+'_detect'+'.jpg'
        shutil.move(detect_image_path,html_file_path)
        shutil.rmtree('runs')

        return render_template("index.html",filepath=html_file_path,Judge=Judge)

if __name__=="__main__":
    app.run(debug=True)