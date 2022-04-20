import numpy as np
import pickle
import sys
import decimal
import os, time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2

from skimage.transform import resize

from scipy.spatial import distance

from keras.models import load_model

#驗證compares列表中相片的人與valid相片中的人


valid = ["0101.jpg", "0202.jpg", "0303.jpg", "0404.jpg" , "0505.jpg" ]

compares = ["0101.jpg", "0202.jpg", "0303.jpg", "0404.jpg" , "0505.jpg" ]

#用OpenCV的Cascade classifier來偵測臉部，不一定跟Facenet一樣要用MTCNN。

cascade_path = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"

#我們的人像相片都放置於validPicPath

validPicPath = "C:\\Users\\user\\Desktop\\googlefacenet\\keras-facenet-master\\members\\"

#此版Facenet model需要的相片尺寸為160×160

image_size = 160

#使用MS-Celeb-1M dataset pretrained好的Keras model

model_path = "C:\\Users\\user\\Desktop\\googlefacenet\\keras-facenet-master\\model\\keras\\facenet_keras.h5"

model = load_model(model_path)

#————————————————————

#圖像白化（whitening）可用於對過度曝光或低曝光的圖片進行處理，處理的方式就是改變圖像的平均像素值為 0 ，改變圖像的方差為單位方差 1。

def prewhiten(x):

    if x.ndim == 4:

        axis = (1, 2, 3)

        size = x[0].size

    elif x.ndim == 3:

        axis = (0, 1, 2)

        size = x.size

    else:

        raise ValueError("Dimension should be 3 or 4")

    mean = np.mean(x, axis=axis, keepdims=True)

    std = np.std(x, axis=axis, keepdims=True)

    std_adj = np.maximum(std, 1.0/np.sqrt(size))

    y = (x - mean) / std_adj

    return y

#使用L1或L2標準化圖像，可強化其特徵。

def l2_normalize(x, axis=-1, epsilon=1e-10):

    output = x / np.sqrt(np.maximum(np.sum(np.square(x), axis=axis, keepdims=True), epsilon))

    return output

#偵測並取得臉孔area，接著再resize為模型要求的尺寸(下方例子並未作alignment)

def align_image(img, margin):

    cascade = cv2.CascadeClassifier(cascade_path)

    faces = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)

    if(len(faces)>0):

        (x, y, w, h) = faces[0]

        face = img[y:y+h, x:x+w]

        faceMargin = np.zeros((h+margin*2, w+margin*2, 3), dtype = "uint8")

        faceMargin[margin:margin+h, margin:margin+w] = face

        #cv2.imwrite(str(time.time())+".jpg", faceMargin)

        aligned = resize(faceMargin, (image_size, image_size), mode="reflect")

        #cv2.imwrite(str(time.time())+"_aligned.jpg", aligned)

        return aligned

    else:

        return None

#圖像的預處理(即前述的幾項步驟)

def preProcess(img):

    whitenImg = prewhiten(img)

    whitenImg = whitenImg[np.newaxis, :]

    return whitenImg

#————————————————-
for member in valid:

    imgValid = validPicPath + member

    aligned = align_image(cv2.imread(imgValid), 6)

    if(aligned is None):

        print("Cannot find any face in image: {}".format(imgValid))

    else:

        faceImg = preProcess(aligned)

    #–> model會輸出128維度的臉孔特徵向量，接著我們將它們合併並進行L2正規化。Z

        embs_valid = l2_normalize(np.concatenate(model.predict(faceImg)))
#    print(embs_valid)
#    exit(0)
    data = (embs_valid)
    with open('file.pickle','wb') as file:
        pickle.dump(data,file)
        file.close()

#with open('file.pickle','rb') as file1:
#    dataload = pickle.load(file1)

  #同上方的valid圖片，依序取得各圖片人臉的臉孔特徵向量，再與valid進行歐氏距離計算。
    result={}
    for member in compares:
        with open('file.pickle','rb') as file1:
             dataload = pickle.load(file1)
             file1.close()

        img_file = validPicPath + member

        aligned = align_image(cv2.imread(img_file), 6)

        

        if(aligned is not None):
            
            faceImg = preProcess(aligned)
            embs = l2_normalize(np.concatenate(model.predict(faceImg)))

            distanceNum = distance.euclidean(dataload, embs)
            print("compared img: "+imgValid)

            print("Diff with {} is {}".format(member, distanceNum))


            result[member] = distanceNum
            print(result)
            
        else:
            print("aligned image is None: "+img_file)

    result = sorted(result.items(),reverse=True ,key=lambda v: v[1])[0]
    print("{} is closet with:".format(imgValid))
    print(result)




           