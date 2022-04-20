安裝sublime
https://www.sublimetext.com/
安裝python3(64位元3.7)
https://www.python.org/downloads/
設定python
C:\Users\user\AppData\Local\Programs\Python\Python37
https://www.itread01.com/content/1549847019.html 設定環境變數

安裝Visual C++ 2017(網路下載免費版本)

安裝tensorflow
pip3 install --user --upgrade tensorflow

安裝keras
pip3 install keras

安裝opencv
pip3 install opencv-python

安裝scikit-image
pip3 install scikit-image


keras-facenet-master目錄及檔案說明:
./googleface.py 原本的程式碼
./main.py 修改過的(由googleface.py更改)

googleface.py程式說明:
valid 資料庫圖片
compares 要與valid資料庫比對的圖片
validPicPath 放圖片的資料夾位置
model_path 模組路徑
路徑不能有中文

會比對valid跟每個compares，並顯示特徵值差距

原教學網站(原程式碼下載keras-facenet-master):
https://makerpro.cc/2018/12/introduction-to-face-recognition-model-google-facenet/






執行01.py
執行結果:
-----------------------------------------------------------------------------------------------------------------------------

WARNING:tensorflow:No training configuration found in the save file, so the model was *not* compiled. Compile it manually.
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0101.jpg
Diff with 0101.jpg is 0.0
{'0101.jpg': 0.0}
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0101.jpg
Diff with 0202.jpg is 0.5862999558448792
{'0101.jpg': 0.0, '0202.jpg': 0.5862999558448792}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0101.jpg
Diff with 0404.jpg is 0.7740429639816284
{'0101.jpg': 0.0, '0202.jpg': 0.5862999558448792, '0404.jpg': 0.7740429639816284}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0101.jpg is closet with:
('0404.jpg', 0.7740429639816284)
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0202.jpg
Diff with 0101.jpg is 0.5862999558448792
{'0101.jpg': 0.5862999558448792}
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0202.jpg
Diff with 0202.jpg is 0.0
{'0101.jpg': 0.5862999558448792, '0202.jpg': 0.0}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0202.jpg
Diff with 0404.jpg is 0.6442162394523621
{'0101.jpg': 0.5862999558448792, '0202.jpg': 0.0, '0404.jpg': 0.6442162394523621}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0202.jpg is closet with:
('0404.jpg', 0.6442162394523621)
Cannot find any face in image: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
Diff with 0101.jpg is 0.5862999558448792
{'0101.jpg': 0.5862999558448792}
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
Diff with 0202.jpg is 0.0
{'0101.jpg': 0.5862999558448792, '0202.jpg': 0.0}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
Diff with 0404.jpg is 0.6442162394523621
{'0101.jpg': 0.5862999558448792, '0202.jpg': 0.0, '0404.jpg': 0.6442162394523621}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg is closet with:
('0404.jpg', 0.6442162394523621)
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0404.jpg
Diff with 0101.jpg is 0.7740429639816284
{'0101.jpg': 0.7740429639816284}
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0404.jpg
Diff with 0202.jpg is 0.6442162394523621
{'0101.jpg': 0.7740429639816284, '0202.jpg': 0.6442162394523621}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0404.jpg
Diff with 0404.jpg is 0.0
{'0101.jpg': 0.7740429639816284, '0202.jpg': 0.6442162394523621, '0404.jpg': 0.0}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0404.jpg is closet with:
('0101.jpg', 0.7740429639816284)
Cannot find any face in image: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
Diff with 0101.jpg is 0.7740429639816284
{'0101.jpg': 0.7740429639816284}
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
Diff with 0202.jpg is 0.6442162394523621
{'0101.jpg': 0.7740429639816284, '0202.jpg': 0.6442162394523621}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0303.jpg
compared img: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
Diff with 0404.jpg is 0.0
{'0101.jpg': 0.7740429639816284, '0202.jpg': 0.6442162394523621, '0404.jpg': 0.0}
aligned image is None: C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg
C:\Users\user\Desktop\googlefacenet\keras-facenet-master\members\0505.jpg is closet with:
('0101.jpg', 0.7740429639816284)
[Finished in 36.9s]
-----------------------------------------------------------------------------------------------------------------------------
以上說明