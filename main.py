import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QFormLayout, 
QGroupBox, QLabel, QCheckBox, QLineEdit, QDialogButtonBox)


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.box_mu = QCheckBox()
        self.box_tianocore = QCheckBox()
        self.box_fg = QCheckBox()
        self.box_arm = QCheckBox()
        self.box_intel = QCheckBox()
        self.text_manufacturer = QLineEdit()
        self.text_device = QLineEdit()

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('UEFI Configuration')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.checks_section())
        main_layout.addWidget(self.text_section())
        main_layout.addWidget(self.button_section())

        self.setLayout(main_layout)

    def extract_values(self):
        vals = {}
        vals['mu'] = self.box_mu.isChecked()
        vals['tianocore'] = self.box_tianocore.isChecked()
        vals['fg'] = self.box_fg.isChecked()
        vals['arm'] = self.box_arm.isChecked()
        vals['intel'] = self.box_intel.isChecked()
        vals['manufacturer'] = self.text_manufacturer.text()
        vals['device'] = self.text_device.text()
        return vals
    
    def checks_section(self):
        checks_group_box = QGroupBox()
        checks_layout = QFormLayout()
        checks_layout.setHorizontalSpacing(15)
        checks_layout.addRow(QLabel('Which of the following would you like?'))
        
        checks_layout.addRow(self.box_mu, QLabel('MU Value-Add'))
        checks_layout.addRow(self.box_tianocore, QLabel('TianoCore Value-Add'))
        checks_layout.addRow(self.box_fg, QLabel('Frontpage and Graphics'))
        checks_layout.addRow(self.box_arm, QLabel('ARM Silicon'))
        checks_layout.addRow(self.box_intel, QLabel('Intel Silicon'))
        
        checks_group_box.setLayout(checks_layout) 
        return checks_group_box
    
    def text_section(self):
        text_group_box = QGroupBox()
        text_layout = QFormLayout()
        text_layout.addRow(QLabel('Manufacturer Name:'), self.text_manufacturer)
        text_layout.addRow(QLabel('Device Name:'), self.text_device)
        
        text_group_box.setLayout(text_layout)
        return text_group_box

    def button_section(self):
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        return button_box


if __name__ == '__main__':
    app = QApplication([])
    
    window = MainWindow()
    window.show()

    result = window.exec_()

    if result == QDialog.Accepted:
        print(window.extract_values())