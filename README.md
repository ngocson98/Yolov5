# Yolov5
Yolov4 Customer Data

# 1. Build Dataset
Using: https://www.makesense.ai/ to get labels

zip folder *'images'*
# 2. Open Colab
- Create folder project named "Yolov5"

- git clone *yolov5* inside folder *Yolov5*

(Tutorials in file *'Train_Yolov5.ipynb'*)

# 3. Install in requirements.txt
# 4. Up folder *images.zip* inside folder *Yolov5*
|---Yolov5

|   |---yolov5

|   |---images.zip

unzip folder images.zip

# 5. Folder reorganization

## train
##   - images
##    - labels
## test
##    - images
##    - labels

*|---Yolov5*

*|   |---yolov5*

*|   |---images.zip*

*|   |---train_data*

# 6. Edit PATH to train, PATH to est, number classes, my dataset
# 7. Training
# 8. Test
get file *.pt* on *yolov5/runs/train/exp/weights/*
