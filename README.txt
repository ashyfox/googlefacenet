�w��sublime
https://www.sublimetext.com/
�w��python3(64�줸3.7)
https://www.python.org/downloads/
�]�wpython
C:\Users\user\AppData\Local\Programs\Python\Python37
https://www.itread01.com/content/1549847019.html �]�w�����ܼ�

�w��Visual C++ 2017(�����U���K�O����)

�w��tensorflow
pip3 install --user --upgrade tensorflow

�w��keras
pip3 install keras

�w��opencv
pip3 install opencv-python

�w��scikit-image
pip3 install scikit-image


keras-facenet-master�ؿ����ɮ׻���:
./googleface.py �쥻���{���X
./main.py �ק�L��(��googleface.py���)

googleface.py�{������:
valid ��Ʈw�Ϥ�
compares �n�Pvalid��Ʈw��諸�Ϥ�
validPicPath ��Ϥ�����Ƨ���m
model_path �Ҳո��|
���|���঳����

�|���valid��C��compares�A����ܯS�x�Ȯt�Z

��оǺ���(��{���X�U��keras-facenet-master):
https://makerpro.cc/2018/12/introduction-to-face-recognition-model-google-facenet/






����01.py
���浲�G:
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
�H�W����