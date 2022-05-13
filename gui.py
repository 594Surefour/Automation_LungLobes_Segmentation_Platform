import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from time import sleep
from tqdm import tqdm
import subprocess


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('')
        self.resize(600,400)

        layout = QVBoxLayout()

        self.label = QLabel('')
        self.label.setFixedHeight(400)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(QPixmap(f""))
        layout.addWidget(self.label)

        self.btn4 = QPushButton('dcm格式转换为nii格式')
        self.btn4.clicked.connect(self.dcm2nii)

        self.cb = QComboBox()
        self.cb.addItems(['选择要使用的模型名称','R231','R231CovidWeb','LTRCLobes_R231'])
        self.cb.currentTextChanged.connect(self.selectionChange)
        layout.addWidget(self.cb)


        self.btn=QPushButton('nii格式转换为JPG格式')
        self.btn.clicked.connect(self.nii2jpg)


        self.btn2=QPushButton('2维结果展示')
        self.btn2.clicked.connect(self.start_timer)

        self.btn3 = QPushButton('3维结果展示')
        self.btn3.clicked.connect(self.display)

        layout.addWidget(self.btn4)
        layout.addWidget(self.btn)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        self.setLayout(layout)

        self.timer=QTimer()
        self.timer.timeout.connect(self.showImage)

        self.n = -1
        self.imagelist=[]
        self.flag=True


    def selectionChange(self):
        modelname = self.cb.currentText()
        print(modelname)
        command = ""
        for i in tqdm(range(1, 500)):
            if modelname == "R231":
                #print("**************")
                command = "lungmask ./seg/sample_ct.nii ./res/test.nii --modelname R231 --modelpath ./model/unet_r231-d5d2fc3d.pth"
            elif modelname == "R231CovidWeb":
                #print("**************")
                command = "lungmask ./seg/sample_ct.nii ./res/test.nii --modelname R231CovidWeb --modelpath ./model/unet_r231covid-0de78a7e.pth"
            elif modelname == "LTRCLobes_R231":
                #print("**************")
                command = "lungmask ./sge/sample_ct.nii.nii ./res/test.nii --modelname LTRCLobes_R231 --modelpath ./unet_r231-d5d2fc3d.pth ./mode/unet_ltrclobes-3a07043d.pth"
            else:
                print("input false")
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process.wait()
            command_output = process.stdout.read().decode('utf-8')
            # # 处理ls的返回值
            print(command_output)
            sleep(0.01)
        sleep(0.5)

    def nii2jpg(self):
        os.system('python convert.py')
        self.imagelist = os.listdir('./jpgs/')
        print(self.imagelist)
        pass

    def display(self):
        os.system('python 3ddisplay.py')

    def dcm2nii(self):
        os.system('python dcm2nii.py')

    def start_timer(self):
        self.imagelist = os.listdir('./jpgs/')
        print(self.imagelist)
        if self.imagelist:
            if self.flag:
                self.timer.start()
            else:
                self.timer.stop()
            self.flag=not self.flag


    def showImage(self):
        self.imagelist = os.listdir('./jpgs/')
        print(self.imagelist)
        print(self.n)
        self.n+=1
        if self.n>=len(self.imagelist):
            self.n=0
        self.label.setPixmap(QPixmap(f"jpgs/{self.imagelist[self.n]}"))
        self.timer.setInterval(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())