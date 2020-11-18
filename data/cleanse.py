import os
import glob
import cv2 as cv
import pandas as pd

# Dataset image input dir
Train_Dir = './Train'
Dev_Dir = './Dev'

def make_dir(path):
  if not os.path.isdir(path):
    os.makedirs(path)
    os.makedirs(path + '/0')
    os.makedirs(path + '/1')
    os.makedirs(path + '/2')
    os.makedirs(path + '/3')
    os.makedirs(path + '/4')

def crop(input_path, output_path, df, row):
  index = 0
  img_name = df.loc[row, 0]
  img = cv.imread(input_path + '/' + img_name)
  for col in range(5, len(df.columns), 5):
    if pd.notna(df.loc[row, col]):
      x, y, w, h = df.loc[row, col - 4:col - 1].astype(int)
      crop_img = img[y:y+h, x:x+w]
      filename, extension = os.path.splitext(img_name)
      cv.imwrite(output_path + '/' + str(df.loc[row, col].astype(int)) + '/' + filename + '_' + str(index) + extension, crop_img)
      index += 1

# Crop image output dir
Train_Crop_Dir = './data/train'
Dev_Crop_Dir = './data/val'

df_train = pd.read_csv('train.csv', header=None, low_memory=False)
df_dev = pd.read_csv('dev.csv', header=None, low_memory=False)
#df_train.head()
#df_dev.head()
labels = ['不良-乳汁吸附', '不良-機械傷害', '不良-炭疽病', '不良-著色不佳', '不良-黑斑病']
label_index = [0, 1, 2, 3, 4]
df_train = df_train.replace(labels, label_index)
df_dev = df_dev.replace(labels, label_index)
#df_train.head()
#df_dev.head()
make_dir(Train_Crop_Dir)
make_dir(Dev_Crop_Dir)

for row in range(len(df_train)):
  crop(Train_Dir, Train_Crop_Dir, df_train, row)

for row in range(len(df_dev)):
  crop(Dev_Dir, Dev_Crop_Dir, df_dev, row)

Dir = Train_Crop_Dir
df_sum = pd.DataFrame([len(os.listdir(Dir + '/' + str(label_index[0]))), 
              len(os.listdir(Dir + '/' + str(label_index[1]))),
              len(os.listdir(Dir + '/' + str(label_index[2]))),
              len(os.listdir(Dir + '/' + str(label_index[3]))),
              len(os.listdir(Dir + '/' + str(label_index[4])))], labels)
print('Train', df_sum)

Dir = Dev_Crop_Dir
df_sum = pd.DataFrame([len(os.listdir(Dir + '/' + str(label_index[0]))), 
              len(os.listdir(Dir + '/' + str(label_index[1]))),
              len(os.listdir(Dir + '/' + str(label_index[2]))),
              len(os.listdir(Dir + '/' + str(label_index[3]))),
              len(os.listdir(Dir + '/' + str(label_index[4])))], labels)
print('Val', df_sum)