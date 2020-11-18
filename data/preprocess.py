import os
import glob

if __name__ == '__main__':
  BASE = './pytorch_classification/data/'
  traindata_path = BASE + 'train'
  valdata_path = BASE + 'val'

  with open(BASE + 'train.txt', 'w')as f:
    for label in os.listdir(traindata_path):
      imglist = glob.glob(os.path.join(traindata_path, str(label), '*.jpg'))
      for img in imglist:
        f.write(img + ' ' + str(label))
        f.write('\n')

  with open(BASE + 'val.txt', 'w')as f:
    for label in os.listdir(valdata_path):
      imglist = glob.glob(os.path.join(valdata_path, str(label), '*.jpg'))
      for img in imglist:
        f.write(img + ' ' + str(label))
        f.write('\n')
