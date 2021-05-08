# lobe-tensorflowlite
codes for jkd-web article

May09, 2021

うちの実験的Web: Microsoft lobeで機械学習：[得られたtfliteモデルを使ってRaspberry pi上でLegoブロックの分類をする](https://makeintoshape.com/microsoft-lobe-tfliteraspberry-pi/)

- buildDatasets.py

  camera control program to build datasets (still image)

- idLegoBlock.py

  infer block type in video stream

  - my_tflite_example.py
    original file was exported from lobe.  To adjust model file path handling, a minor modification was made to make my_ version of the file. TFLiteModel class is called in idLegoBlock.py.  

