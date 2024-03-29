# 説明
物体検出深層学習モデル「YOLOv5」を用いた顔検出Webアプリケーション

# デモ動画

https://user-images.githubusercontent.com/83805342/197713489-ded3061e-849e-4618-a792-17c19400988e.mp4

# 技術スタック
- Webフレームワーク: **Flask**
- 深層学習モデル構築フレームワーク: **PyTorch**

# 動作バージョン情報
- **Python**: 3.8.0 以上
- **PyTorch**: 1.7.0 以上

# 実行方法
- 事前準備: Pythonの仮想環境内にPyTorchをインストールしてください
- 作成した仮想環境内で以下のコマンドを入力してください
```
git clone https://github.com/Umadachi564/python_app
cd python_app
python3 app.py
```

# 挙動確認
- 開発者が所有するPCで構築したDockerコンテナ環境下でアプリが正常動作することを確認.
- Render.comにてデプロイを試みたが, Freeプランのメモリが少なすぎるため動作しませんでした. 
