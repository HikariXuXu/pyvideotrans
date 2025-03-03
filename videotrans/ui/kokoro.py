# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from videotrans.configure import config
from videotrans.util import tools


class Ui_kokoroform(object):
    def setupUi(self, kokoro):
        self.has_done = False
        kokoro.setObjectName("kokoro")
        kokoro.setWindowModality(QtCore.Qt.NonModal)
        kokoro.resize(500, 223)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(kokoro.sizePolicy().hasHeightForWidth())
        kokoro.setSizePolicy(sizePolicy)
        kokoro.setMaximumSize(QtCore.QSize(500, 300))


        self.verticalLayout = QtWidgets.QVBoxLayout(kokoro)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(kokoro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.kokoro_address = QtWidgets.QLineEdit(kokoro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kokoro_address.sizePolicy().hasHeightForWidth())
        self.kokoro_address.setSizePolicy(sizePolicy)
        self.kokoro_address.setMinimumSize(QtCore.QSize(400, 35))
        self.kokoro_address.setObjectName("kokoro_address")

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kokoro_address)
        self.verticalLayout.addLayout(self.formLayout_2)


        self.set_kokoro = QtWidgets.QPushButton(kokoro)
        self.set_kokoro.setMinimumSize(QtCore.QSize(0, 35))
        self.set_kokoro.setObjectName("set_kokoro")

        self.test = QtWidgets.QPushButton(kokoro)
        self.test.setMinimumSize(QtCore.QSize(0, 30))
        self.test.setObjectName("test")
        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText("查看填写教程" if config.defaulelang == 'zh' else "Fill out the tutorial")
        help_btn.clicked.connect(lambda: tools.open_url(url='https://pyvideotrans.com/kokorotts'))

        self.layout_btn = QtWidgets.QHBoxLayout()
        self.layout_btn.setObjectName("layout_btn")

        self.layout_btn.addWidget(self.set_kokoro)
        self.layout_btn.addWidget(self.test)
        self.layout_btn.addWidget(help_btn)

        self.verticalLayout.addLayout(self.layout_btn)



        self.retranslateUi(kokoro)
        QtCore.QMetaObject.connectSlotsByName(kokoro)

    def retranslateUi(self, kokoro):
        kokoro.setWindowTitle("Kokoro TTS")
        self.label.setText("http地址" if config.defaulelang == 'zh' else 'kokoro api')
        self.kokoro_address.setPlaceholderText(
            'kokoro-uiapi启动后的地址,默认请填写 http://127.0.0.1:5066' if config.defaulelang == 'zh' else 'Fill in the HTTP address after the kokoro program starts')
        self.set_kokoro.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.test.setText('测试' if config.defaulelang == 'zh' else "Test")
