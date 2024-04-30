import os
import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget

# 기타 모듈 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# UI 파일 로드
root = os.path.dirname(os.path.abspath(__file__))
MainUI = uic.loadUiType(os.path.join(root, 'kbo.ui'))[0]


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
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            ranklist.append(text[0])


        namelist = []
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            namelist.append(text[1])
            # 다시 요소를 찾아야 하므로 반복문 내에서 요소를 다시 찾습니다.

        viewlist = []
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            viewlist.append(text[2])
            # 다시 요소를 찾아야 하므로 반복문 내에서 요소를 다시 찾습니다.

        self.ui.tableWidget_week.setRowCount(len(topnews_elements))
        self.ui.tableWidget_week.setColumnCount(2)
        #self.ui.tableWidget.setHorizontalHeaderLabels(["순위", "이름", "조회수"])
        header = self.ui.tableWidget_week.horizontalHeader()
        header.setVisible(False)

        # 데이터를 tableWidget에 추가
        for i in range(len(ranklist)):
            #self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(' '))
            self.ui.tableWidget_week.setItem(i, 0, QTableWidgetItem(namelist[i]))
            self.ui.tableWidget_week.setItem(i, 1, QTableWidgetItem(viewlist[i]))


    def populate_list_ttl_widget(self):
        # topnews_elements 가져오기
        topnews_elements = driver.find_elements('xpath', '/html/body/div[2]/div[3]/section/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr')


        ranklist = []
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            ranklist.append(text[0])


        namelist = []
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            namelist.append(text[1])
            # 다시 요소를 찾아야 하므로 반복문 내에서 요소를 다시 찾습니다.

        viewlist = []
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            viewlist.append(text[2])
            # 다시 요소를 찾아야 하므로 반복문 내에서 요소를 다시 찾습니다.

        self.ui.tableWidget.setRowCount(len(topnews_elements))
        self.ui.tableWidget.setColumnCount(2)
        #self.ui.tableWidget.setHorizontalHeaderLabels(["순위", "이름", "조회수"])
        header = self.ui.tableWidget.horizontalHeader()
        header.setVisible(False)

        # 데이터를 tableWidget에 추가
        for i in range(len(ranklist)):
            #self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(' '))
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(namelist[i]))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(viewlist[i]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainDialog()
    mainWindow.show()
    sys.exit(app.exec_())