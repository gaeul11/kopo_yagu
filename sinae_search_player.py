import os
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTableWidgetItem
from PyQt5.QtCore import Qt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# UI 파일 로드
root = os.path.dirname(os.path.abspath(__file__))
MainUI = uic.loadUiType(os.path.join(root, 'kbo_sinae.ui'))[0]

# ChromeDriver 자동 관리
service = Service(executable_path=ChromeDriverManager().install())

# 옵션 설정 예 (headless 모드)
options = webdriver.ChromeOptions()
options.headless = True

# 드라이버 초기화
driver = webdriver.Chrome(service=service, options=options)

# 웹 페이지 열기
driver.get('https://statiz.sporki.com/')

player_name = ""
current_url = ""

class MainDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.setWindowTitle("KBO")
        self.ui.searchbar.textChanged.connect(self.lineeditTextFunction)
        self.ui.searchbar.returnPressed.connect(self.printTextFunction)
        self.ui.searchButton.clicked.connect(self.click_search)


    def lineeditTextFunction(self):
        global player_name
        player_name = self.ui.searchbar.text()

    def printTextFunction(self):
        # self.lineedit이름.text()
        # Lineedit에 있는 글자를 가져오는 메서드
        global player_name

    def click_search(self):
        try:
            #driver.get('https://statiz.sporki.com/')
            # 검색 버튼을 클릭하여 검색 창을 나타내기
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[3]/div[1]/a'))
            )
            search_link.click()

            # 검색어 입력 창 찾기
            search_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="s"]'))
            )

            # 검색어 입력하고 엔터 누르기
            search_input.send_keys(player_name)
            search_input.send_keys(Keys.ENTER)
            #print(driver.page_source)

            current_url = driver.current_url
            print("현재 페이지 URL:", current_url)
        except Exception as e:
            #self.ui.label_playerinfo_2.setText("검색어를 다시 입력해주세요.")
            print("검색 창을 찾거나 입력할 수 없습니다:", e)

        # 검색 결과에서 가장 큰 값 클릭하기
        try:
            elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/section/div[3]/div/table/tbody/tr')
            if elements:
                max_value = max(elements, key=lambda x: x.find_element(By.XPATH, './td[3]').text)
                link_element = max_value.find_element(By.XPATH, './td[1]/a')
                link_element.click()
            #else:
                #print("값을 찾을 수 없습니다.")
        except Exception as e:
            print("값을 클릭할 수 없습니다:", e)


        topnews = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/section/div[3]/div[1]/div[3]/div')
        # topnews = "\n\n".join(["{} {}".format(topnews[i], topnews[i+1]) for i in range(0, len(topnews), 2)])
        topnews = [topnew.text for topnew in topnews]
        #self.ui.label_playername.setText("\n".join(topnews))
        # self.ui.label_playername.setText(topnews)
        #print(topnews)
        name = topnews[0]
        self.ui.label_playername.setText(name)
        cleaned_topnews = [item.replace('\n', ' | ') for item in topnews[1:]]
        # 공백으로 항목을 연결하여 문자열 생성
        rest_items = " ".join(cleaned_topnews)

        # QLabel에 설정
        self.ui.label_playerinfo.setText(rest_items)


        topnews1 = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/section/div[3]/div[1]/ul/li')
        topnews1 = [topnew.text for topnew in topnews1]
        cleaned_topnews1 = [item.replace('\n', ' ') for item in topnews1[1:]]
        self.ui.label_playerinfo_2.setText("\n".join(cleaned_topnews1))

        self.awards_list(rest_items)


    def awards_list(self, rest_items):

        if 'P' in rest_items:
        #driver.get(current_url)
        # topnews_elements 가져오기
            topnews_elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/section/div[7]/div[4]/div/div/div[2]/div/table/tbody/tr')
        else:
            topnews_elements = driver.find_elements(By.XPATH,
                                                    '/html/body/div[2]/div[3]/section/div[5]/div[4]/div/div/div[2]/div/table/tbody/tr')

        topnews = [topnews.text for topnews in topnews_elements]

        yearlist = []
        awardslist = []

        for item in topnews:
            # 공백으로 분리하여 year와 award로 나눔
            year, award = item.split(maxsplit=1)
            yearlist.append(year)
            awardslist.append(award)


        self.ui.tableWidget_2.setRowCount(len(topnews_elements))
        self.ui.tableWidget_2.setColumnCount(2)

        self.ui.tableWidget_2.setColumnWidth(0, 50)  # 첫 번째 열의 너비를 50으로 설정
        self.ui.tableWidget_2.setColumnWidth(1, 230)  # 두 번째 열의 너비를 150으로 설정

        self.ui.tableWidget_2.setShowGrid(False)
        header = self.ui.tableWidget_2.horizontalHeader()
        header.setVisible(False)
        vertical_header = self.ui.tableWidget_2.verticalHeader()
        vertical_header.setVisible(False)  # 수직 헤더 숨기기

        # 데이터를 tableWidget에 추가
        for i in range(len(yearlist)):
            item_year = QTableWidgetItem(yearlist[i])
            item_year.setTextAlignment(Qt.AlignCenter)
            item_awards = QTableWidgetItem(awardslist[i])
            item_awards.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(item_year))
            self.ui.tableWidget_2.setItem(i, 1, QTableWidgetItem(item_awards))

        self.war_list(rest_items)

    def war_list(self, rest_items):

        if 'P' in rest_items:
        #driver.get(current_url)
        # topnews_elements 가져오기
            topnews_elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/section/div[7]/div[3]/div/div/div[2]/div/table/tbody/tr')
        else:
            topnews_elements = driver.find_elements(By.XPATH,
                                                    '/html/body/div[2]/div[3]/section/div[5]/div[3]/div/div/div[2]/div/table/tbody/tr')

        yearlist = []
        war144list = []
        warlist = []
        ranklist = []
        for i in range(len(topnews_elements)):
            # 현재 요소의 텍스트를 가져와서 공백으로 분리한 후 첫 번째 요소를 ranklist에 추가
            text = topnews_elements[i].text.split()
            yearlist.append(text[0])
            war144list.append(text[1])
            warlist.append(text[2])
            ranklist.append(text[3])

        self.ui.tableWidget_3.setRowCount(len(topnews_elements))
        self.ui.tableWidget_3.setColumnCount(4)
        self.ui.tableWidget_3.setColumnWidth(0, 70)  # 첫 번째 열의 너비를 50으로 설정
        self.ui.tableWidget_3.setColumnWidth(1, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget_3.setColumnWidth(2, 70)
        self.ui.tableWidget_3.setColumnWidth(3, 70)

        self.ui.tableWidget_3.setShowGrid(False)
        header = self.ui.tableWidget_3.horizontalHeader()
        header.setVisible(False)
        vertical_header = self.ui.tableWidget_3.verticalHeader()
        vertical_header.setVisible(False)  # 수직 헤더 숨기기

        # 데이터를 tableWidget에 추가
        for i in range(len(yearlist)):
            item_year = QTableWidgetItem(yearlist[i])
            item_year.setTextAlignment(Qt.AlignCenter)
            item_war144 = QTableWidgetItem(war144list[i])
            item_war144.setTextAlignment(Qt.AlignCenter)
            item_war = QTableWidgetItem(warlist[i])
            item_war.setTextAlignment(Qt.AlignCenter)
            item_rank = QTableWidgetItem(ranklist[i])
            item_rank.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_3.setItem(i, 0, QTableWidgetItem(item_year))
            self.ui.tableWidget_3.setItem(i, 1, QTableWidgetItem(item_war144))
            self.ui.tableWidget_3.setItem(i, 2, QTableWidgetItem(item_war))
            self.ui.tableWidget_3.setItem(i, 3, QTableWidgetItem(item_rank))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainDialog()
    mainWindow.show()
    sys.exit(app.exec_())