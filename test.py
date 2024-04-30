import os
import sys
import time
from selenium.webdriver.common.by import By
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QLabel

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

# UI 파일 로드
root = os.path.dirname(os.path.abspath(__file__))
MainUI = uic.loadUiType(os.path.join(root, 'kbo_ver04.ui'))[0]

# ChromeDriver 자동 관리
service = Service(executable_path=ChromeDriverManager().install())

# 옵션 설정 예 (headless 모드)
options = webdriver.ChromeOptions()

# 드라이버 초기화
driver = webdriver.Chrome(service=service, options=options)

# 웹 페이지 열기
driver.get('https://statiz.sporki.com/')
team_rank_url = 'https://statiz.sporki.com/'

news_url = 'https://sports.news.naver.com/kbaseball/index'


class KboApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.setWindowTitle("KBO")
        self.team_rank_widget()
        self.load_data()

#        self.update_game_info()  # 게임 정보 업데이트 추가

        # QTimer를 사용하여 일정 시간마다 게임 정보 업데이트
        self.timer = QtCore.QTimer(self)
#        self.timer.timeout.connect(self.update_game_info)
        self.timer.start(60000)  # 1분마다 업데이트

    """def update_game_info(self):
        game_info = self.get_game_info()
        game_labels = [self.ui.game_1, self.ui.game_2, self.ui.game_3, self.ui.game_4, self.ui.game_5]
        for i, info in enumerate(game_info):
            game_labels[i].setText(info)

    def get_game_info(self):
        try:
            html = requests.get("https://sports.news.naver.com/kbaseball/index")
            soup = BeautifulSoup(html.content, "html.parser")

            kboMatch = soup.find("div", id="_tab_box_kbo")
            if kboMatch:
                kboMatchItems = kboMatch.find("div", class_="hmb_list").find_all("li", class_="hmb_list_items")
                game_info_list = []

                for item in kboMatchItems:
                    leftItemBox = item.find(class_="vs_list vs_list1").find(class_="inner")
                    rightItemBox = item.find(class_="vs_list vs_list2").find(class_="inner")

                    leftScore_box = leftItemBox.find("div", class_="score")
                    rightScore_box = rightItemBox.find("div", class_="score")

                    leftName = leftItemBox.find("span", class_="name").text
                    leftPitcher = leftItemBox.find_all("span")[2].text

                    rightName = rightItemBox.find("span", class_="name").text
                    rightPitcher = rightItemBox.find_all("span")[2].text

                    game_info = "     " + leftName + "  vs  " + rightName + "\n" + "   "

                    if leftScore_box and rightScore_box:
                        leftScore = "".join(leftScore_box.stripped_strings)
                        rightScore = "".join(rightScore_box.stripped_strings)
                        game_info += leftScore + "        " + rightScore + "\n" "   "

                    game_info += leftPitcher + "   " + rightPitcher + "\n"
                    game_info_list.append(game_info)

                return game_info_list
            else:
                return ["No game information available"]

        except Exception as e:
            print("Error fetching game information:", e)
            return ["Error fetching game information"]"""


    def team_rank_widget(self):
        # 팀 순위 요소 가져오기
        team_rank_elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/main/div/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr')

        # 각 열의 데이터를 저장할 리스트 초기화
        rank_list = []
        name_list = []
        view_lists = [[] for _ in range(8)]  # 조회수 데이터를 저장할 리스트를 7개 생성

        # 텍스트 추출 및 저장
        for element in team_rank_elements:
            text = element.text.split()
            rank_list.append(text[0])
            name_list.append(text[1])
            for i in range(8):
                view_lists[i].append(text[i + 2])  # 조회수 데이터를 각 리스트에 저장

        # 테이블 위젯 설정
        row_count = len(rank_list)
        column_count = 10  # 열 개수를 10으로 설정
        self.ui.tableWidget.setRowCount(row_count)
        self.ui.tableWidget.setColumnCount(column_count)
        header = self.ui.tableWidget.horizontalHeader()
        header.setVisible(False)
        vertical_header = self.ui.tableWidget.verticalHeader()
        vertical_header.setVisible(False)  # 수직 헤더 숨기기
        self.ui.tableWidget.setShowGrid(False)  # 그리드 라인을 표시하지 않음

        # 열의 크기 조절
        self.ui.tableWidget.setColumnWidth(0, 50)  # 첫 번째 열의 너비를 50으로 설정
        self.ui.tableWidget.setColumnWidth(1, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget.setColumnWidth(2, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget.setColumnWidth(3, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget.setColumnWidth(4, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget.setColumnWidth(5, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget.setColumnWidth(6, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget.setColumnWidth(7, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget.setColumnWidth(8, 70)  # 두 번째 열의 너비를 150으로 설정
        self.ui.tableWidget.setColumnWidth(9, 70)  # 두 번째 열의 너비를 150으로 설정

        # 나머지 열의 크기를 조절하려면 필요한대로 추가하면 됩니다.

        # 데이터 추가
        for i in range(row_count):
            for j in range(column_count):
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # 가운데 정렬 설정
                if j == 0:
                    item.setText(rank_list[i])
                elif j == 1:
                    item.setText(name_list[i])
                else:
                    item.setText(view_lists[j - 2][i])
                self.ui.tableWidget.setItem(i, j, item)
    def load_data(self):
        self.load_team_rank()
        self.load_news()

    def load_team_rank(self):
        # 팀 순위 페이지 로드
        driver.get(team_rank_url)

        # 팀 순위 요소 가져오기
        team_rank_elements = driver.find_elements(By.XPATH,
                                                   '/html/body/div[2]/div[3]/main/div/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr')

        # 각 열의 데이터를 저장할 리스트 초기화
        rank_list = []
        name_list = []
        view_lists = [[] for _ in range(8)]  # 조회수 데이터를 저장할 리스트를 7개 생성

        # 텍스트 추출 및 저장
        for element in team_rank_elements:
            text = element.text.split()
            rank_list.append(text[0])
            name_list.append(text[1])
            for i in range(8):
                view_lists[i].append(text[i + 2])  # 조회수 데이터를 각 리스트에 저장

        # 테이블 위젯 설정
        row_count = len(rank_list)
        column_count = 10  # 열 개수를 10으로 설정
        self.ui.tableWidget.setRowCount(row_count)
        self.ui.tableWidget.setColumnCount(column_count)
        header = self.ui.tableWidget.horizontalHeader()
        header.setVisible(False)
        vertical_header = self.ui.tableWidget.verticalHeader()
        vertical_header.setVisible(False)  # 수직 헤더 숨기기
        self.ui.tableWidget.setShowGrid(False)  # 그리드 라인을 표시하지 않음

        # 열의 크기 조절
        for j in range(column_count):
            self.ui.tableWidget.setColumnWidth(j, 70)  # 열의 너비를 70으로 설정

        # 데이터 추가
        for i in range(row_count):
            for j in range(column_count):
                item = QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # 가운데 정렬 설정
                if j == 0:
                    item.setText(rank_list[i])
                elif j == 1:
                    item.setText(name_list[i])
                else:
                    item.setText(view_lists[j - 2][i])
                self.ui.tableWidget.setItem(i, j, item)

    def load_news(self):
        # 뉴스 페이지 로드
        driver.get(news_url)

        # 페이지 제목 가져오기
        # page_title_element = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/div[1]/h2')
        # page_title = page_title_element.text

        # 페이지 제목을 QLabel에 표시
        # self.ui.pageTitleLabel.setText(page_title)

        # 뉴스 항목 요소 가져오기
        news_elements = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/div[1]/ol/li')

        # 테이블 위젯 설정
        row_count = len(news_elements)
        column_count = 1
        self.ui.tableWidget_2.setRowCount(row_count)
        self.ui.tableWidget_2.setColumnCount(column_count)
        header = self.ui.tableWidget_2.horizontalHeader()
        header.setVisible(False)
        vertical_header = self.ui.tableWidget_2.verticalHeader()
        vertical_header.setVisible(False)  # 수직 헤더 숨기기
        self.ui.tableWidget_2.setShowGrid(False)  # 그리드 라인을 표시하지 않음

        # 열의 크기 조절
        self.ui.tableWidget_2.setColumnWidth(0, 300)  # 첫 번째 열의 너비를 조절

        # 라벨에 뉴스 제목 설정
        for i, element in enumerate(news_elements):
            if i < 8:
                label_name = f"new_list_item_{i + 1}"
                label = getattr(self.ui, label_name)
                link = element.find_element(By.TAG_NAME, "a")
                news_title = link.text[:33] + "..." if len(link.text) > 33 else link.text
                label.setText(f"{i + 1}. {news_title}")

                # 라벨에 클릭 이벤트 연결
                label.mousePressEvent = lambda event, link=link: self.on_news_label_clicked(link)

    def on_news_label_clicked(self, news_link):
        # 클릭한 라벨의 뉴스 링크를 콘솔에 출력
        print("Clicked News Link:", news_link.get_attribute("href"))
        # 해당 뉴스의 URL 가져오기
        news_url = news_link.get_attribute("href")
        # 웹 브라우저에서 뉴스 열기
        QDesktopServices.openUrl(QUrl(news_url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kbo = KboApp()
    kbo.show()
    sys.exit(app.exec_())