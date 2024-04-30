from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import QFile
from PyQt5.uic import loadUi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KBOApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # UI 파일 불러오기
        ui_file = QFile("kisun1.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loadUi(ui_file)
        ui_file.close()

        # 버튼 클릭 시그널에 슬롯 함수 연결
        self.ui.pushButton.clicked.connect(self.handle_button_click)
        self.ui.pushButton_1.clicked.connect(self.handle_button_1_click)
        self.ui.pushButton_2.clicked.connect(self.handle_button_2_click)
        self.ui.pushButton_3.clicked.connect(self.handle_button_3_click)  # 새로운 버튼에 슬롯 함수 연결
        self.ui.pushButton_4.clicked.connect(self.handle_button_4_click)
        self.ui.pushButton_5.clicked.connect(self.handle_button_5_click)
        # 웹 드라이버 설정
        self.driver = webdriver.Chrome()
        self.tableWidget_week_2 = self.ui.findChild(QTableWidget, "tableWidget_week_2")
        self.tableWidget_week_3 = self.ui.findChild(QTableWidget, "tableWidget_week_3")  # 새로운 테이블 위젯 찾기

        # 창 표시
        self.ui.show()

    def get_column_values(self, column_index, table_xpath):
        column_values = []
        # 테이블의 행 수 가져오기
        row_count = len(self.driver.find_elements(By.XPATH, f'{table_xpath}/table[1]/tbody/tr'))
        for i in range(1, row_count + 1):
            xpath = f'{table_xpath}/table[1]/tbody/tr[{i}]/td[{column_index}]'
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            column_values.append(element.text)
        return column_values

    def handle_button_click(self):
        self.fetch_data(
            'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024&type=pitcher&playerOrder=era')

    def handle_button_1_click(self):
        self.fetch_data(
            'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024&type=pitcher&playerOrder=w')

    def handle_button_2_click(self):
        self.fetch_data(
            'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024&type=pitcher&playerOrder=sv')

    def handle_button_3_click(self):
        self.fetch_batter_data(
            'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024&type=batter&playerOrder=hra')
    def handle_button_4_click(self):
        self.fetch_batter_data(
            'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024&type=batter&playerOrder=hr')

    def handle_button_5_click(self):
        self.fetch_batter_data(
            'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024&type=batter&playerOrder=sb')
    def fetch_data(self, url):
        try:
            # 웹 페이지 열기
            self.driver.get(url)

            # 데이터 가져오기
            names = self.get_column_values(1, '//*[@id="_pitcherRecord"]')
            jachaek = self.get_column_values(2, '//*[@id="_pitcherRecord"]')
            wins = self.get_column_values(5, '//*[@id="_pitcherRecord"]')
            save = self.get_column_values(7, '//*[@id="_pitcherRecord"]')

            num_rows = len(names)
            num_columns = 4
            self.tableWidget_week_2.setRowCount(num_rows)
            self.tableWidget_week_2.setColumnCount(num_columns)
            headers = ['이름', '평균자책', '승리', '세이브']
            self.tableWidget_week_2.setHorizontalHeaderLabels(headers)
            for i, (name, era, win, sv) in enumerate(zip(names, jachaek, wins, save)):
                self.tableWidget_week_2.setItem(i, 0, QTableWidgetItem(name))
                self.tableWidget_week_2.setItem(i, 1, QTableWidgetItem(era))
                self.tableWidget_week_2.setItem(i, 2, QTableWidgetItem(win))
                self.tableWidget_week_2.setItem(i, 3, QTableWidgetItem(sv))

            # 테이블 크기 조정
            self.tableWidget_week_2.resizeColumnsToContents()
            self.tableWidget_week_2.resizeRowsToContents()

        except Exception as e:
            print("Error occurred:", e)

    def fetch_batter_data(self, url):
        try:
            # 웹 페이지 열기
            self.driver.get(url)

            # 데이터 가져오기
            names = self.get_column_values(1, '//*[@id="_batterRecord"]')
            tauls = self.get_column_values(2, '//*[@id="_batterRecord"]')
            hrs = self.get_column_values(8, '//*[@id="_batterRecord"]')
            dorus = self.get_column_values(11, '//*[@id="_batterRecord"]')

            num_rows = len(names)
            num_columns = 4
            self.tableWidget_week_3.setRowCount(num_rows)
            self.tableWidget_week_3.setColumnCount(num_columns)
            headers = ['이름', '타율', '홈런', '도루']
            self.tableWidget_week_3.setHorizontalHeaderLabels(headers)
            for i, (name, taul, hr, doru) in enumerate(zip(names, tauls, hrs, dorus)):
                self.tableWidget_week_3.setItem(i, 0, QTableWidgetItem(name))
                self.tableWidget_week_3.setItem(i, 1, QTableWidgetItem(taul))
                self.tableWidget_week_3.setItem(i, 2, QTableWidgetItem(hr))
                self.tableWidget_week_3.setItem(i, 3, QTableWidgetItem(doru))

            # 테이블 크기 조정
            self.tableWidget_week_3.resizeColumnsToContents()
            self.tableWidget_week_3.resizeRowsToContents()

        except Exception as e:
            print("Error occurred:", e)


# PyQt 애플리케이션 초기화
app = QApplication([])
window = KBOApp()
app.exec_()
