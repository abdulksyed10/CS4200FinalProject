from PyQt5.QtWidgets import QMainWindow, QFileDialog
from imageUi import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python import keras
from keras import datasets, layers, models

class imageUiAttached(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()
        self.imgPath = ""
        self.pushButton.clicked.connect(self.insertBtnClicked)
        self.submitBtn.clicked.connect(self.submitBtnClicked)
    
    def insertBtnClicked(self):
        self.outputTxt.setText("Click the button on the right")
        fname = QFileDialog.getOpenFileNames(self, "Open File", "C:\\Users\\syedz\\Downloads", "All Files (*);;JPG Files (*.jpg);;PNG Files (*.png)")
        #self.pixmap = QPixmap(fname[0])
        self.imgPath = fname[0][0]
        #self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.setStyleSheet(f"image: url({self.imgPath});")

    def submitBtnClicked(self):
        (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
        training_images, testing_images = training_images / 255, testing_images / 255

        class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

        training_images = training_images[:20000000]
        training_labels = training_labels[:20000000]
        testing_images = testing_images[:400000]
        testing_labels = testing_labels[:400000]

        model = models.load_model('image_classifier.model')

        img = cv.imread(self.imgPath)
        img = cv.resize(img, (32, 32), interpolation=cv.INTER_AREA)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        plt.imshow(img, cmap=plt.cm.binary)

        prediction = model.predict(np.array([img]) / 255)
        index = np.argmax(prediction)
        print(f'Prediction is {class_names[index]}')
        self.outputTxt.setText(f'Prediction is {class_names[index]}')