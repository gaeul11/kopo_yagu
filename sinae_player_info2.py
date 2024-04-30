import os
import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget

# 기타 모듈 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# UI 파일 로드
root = os.path.dirname(os.path.abspath(__file__))
MainUI = uic.loadUiType(os.path.join(root, 'kbo_ver04.ui'))[0]


# ChromeDriver 자동 관리
service = Service(executable_path=ChromeDriverManager().install())

# 옵션 설정 예 (headless 모드)
options = webdriver.ChromeOptions()
options.headless = True

# 드라이버 초기화
driver = webdriver.Chrome(service=service, options=options)

# 웹 페이지 열기
driver.get('https://statiz.sporki.com/player/')

class MainDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.setWindowTitle("KBO")
        self.populate_list_weekly_widget()
        self.populate_list_ttl_widget()  # tableWidget에 데이터 채우기

    def populate_list_weekly_widget(self):
        # topnews_elements 가져오기
        topnews_elements = driver.find_elements('xpath', '/html/body/div[2]/div[3]/section/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr')

        ranklist = []
        namelist = []
        viewlist = []
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            ranklist.append(text[0])
            namelist.append(text[1])
            viewlist.append(text[2])


        self.ui.tableWidget_week.setRowCount(len(topnews_elements))
        self.ui.tableWidget_week.setColumnCount(3)
        #self.ui.tableWidget.setHorizontalHeaderLabels(["순위", "이름", "조회수"])

        self.ui.tableWidget_week.setColumnWidth(0, 50)  # 첫 번째 열의 너비를 50으로 설정
        self.ui.tableWidget_week.setColumnWidth(1, 180)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget_week.setColumnWidth(2, 180)

        self.ui.tableWidget_week.setShowGrid(False)
        header = self.ui.tableWidget_week.horizontalHeader()
        header.setVisible(False)
        vertical_header = self.ui.tableWidget_week.verticalHeader()
        vertical_header.setVisible(False)  # 수직 헤더 숨기기

        # 데이터를 tableWidget에 추가
        for i in range(len(ranklist)):
            item_rank = QTableWidgetItem(ranklist[i])
            item_rank.setTextAlignment(Qt.AlignCenter)
            item_name = QTableWidgetItem(namelist[i])
            item_name.setTextAlignment(Qt.AlignCenter)
            item_view = QTableWidgetItem(viewlist[i])
            item_view.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_week.setItem(i, 0, QTableWidgetItem(item_rank))
            self.ui.tableWidget_week.setItem(i, 1, QTableWidgetItem(item_name))
            self.ui.tableWidget_week.setItem(i, 2, QTableWidgetItem(item_view))


    def populate_list_ttl_widget(self):
        # topnews_elements 가져오기
        topnews_elements = driver.find_elements('xpath', '/html/body/div[2]/div[3]/section/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr')

        ranklist = []
        namelist = []
        viewlist = []
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            ranklist.append(text[0])
            namelist.append(text[1])
            viewlist.append(text[2])

        self.ui.tableWidget_2.setRowCount(len(topnews_elements))
        self.ui.tableWidget_2.setColumnCount(3)
        #self.ui.tableWidget.setHorizontalHeaderLabels(["순위", "이름", "조회수"])

        self.ui.tableWidget_2.setColumnWidth(0, 50)  # 첫 번째 열의 너비를 50으로 설정
        self.ui.tableWidget_2.setColumnWidth(1, 180)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget_2.setColumnWidth(2, 180)

        self.ui.tableWidget_2.setShowGrid(False)

        header = self.ui.tableWidget_2.horizontalHeader()
        header.setVisible(False)
        vertical_header = self.ui.tableWidget_2.verticalHeader()
        vertical_header.setVisible(False)  # 수직 헤더 숨기기

        # 데이터를 tableWidget에 추가
        for i in range(len(ranklist)):
            item_rank = QTableWidgetItem(ranklist[i])
            item_rank.setTextAlignment(Qt.AlignCenter)
            item_name = QTableWidgetItem(namelist[i])
            item_name.setTextAlignment(Qt.AlignCenter)
            item_view = QTableWidgetItem(viewlist[i])
            item_view.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(item_rank))
            self.ui.tableWidget_2.setItem(i, 1, QTableWidgetItem(item_name))
            self.ui.tableWidget_2.setItem(i, 2, QTableWidgetItem(item_view))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainDialog()
    mainWindow.show()
    sys.exit(app.exec_())