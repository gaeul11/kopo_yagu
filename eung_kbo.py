import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot, QDateTime
from bs4 import BeautifulSoup

root = os.path.dirname(os.path.abspath(__file__))
ui_path = os.path.join(root, 'kbo.ui')


class KboApp(QMainWindow):
    current_date_time = QDateTime.currentDateTime()

    def __init__(self):
        super().__init__()
        uic.loadUi(ui_path, self)  # UI 로드
        self.setWindowTitle("kbo")  # 창 제목 설정

        # 버튼 클릭 시 동작 설정
        self._3.clicked.connect(self.show_info_3)
        self._4.clicked.connect(self.show_info_4)
        self._5.clicked.connect(self.show_info_5)
        self._6.clicked.connect(self.show_info_6)
        self._7.clicked.connect(self.show_info_7)
        self._8.clicked.connect(self.show_info_8)

    @pyqtSlot()
    def show_info(self, button_num):
        self.month.setText(f"{button_num}월")  # 클릭된 버튼에 해당하는 월 표시

    def show_info_3(self):
        for i in range(1, 36):
            getattr(self, f"d_{i}").setText("")

        self.show_info('3')
        html_content_1 = """
        <td><span class="day">1</span> <div class="inner"></div></td>
        """
        html_content_2 = """
        <td><span class="day">2</span> <div class="inner"></div></td>
        """
        html_content_3 = """
        <td><span class="day">3</span> <div class="inner"></div></td>
        """
        html_content_4 = """
        <td><span class="day">4</span> <div class="inner"></div></td>
        """
        html_content_5 = """
        <td><span class="day">5</span> <div class="inner"></div></td>
                """
        html_content_6 = """
        <td><span class="day">6</span> <div class="inner"></div></td>
                """
        html_content_7 = """
        <td><span class="day">7</span> <div class="inner"></div></td>
                """
        html_content_8 = """
        <td><span class="day">8</span> <div class="inner"></div></td>
                """
        html_content_9 = """
        <td><span class="day">9</span> <div class="inner"></div></td>
                """
        html_content_10 = """
        <td><span class="day">10</span> <div class="inner"></div></td>
                """
        html_content_11 = """
        <td><span class="day">11</span> <div class="inner"></div></td>
                """
        html_content_12 = """
        <td><span class="day">12</span> <div class="inner"></div></td>
                """
        html_content_13 = """
        <td><span class="day">13</span> <div class="inner"></div></td>
                """
        html_content_14 = """
        <td><span class="day">14</span> <div class="inner"></div></td>
                """
        html_content_15 = """
        <td><span class="day">15</span> <div class="inner"></div></td>
                """
        html_content_16 = """
        <td><span class="day">16</span> <div class="inner"></div></td>
                """
        html_content_17 = """
        <td><span class="day">17</span> <div class="inner"></div></td>
                """
        html_content_18 = """
        <td><span class="day">18</span> <div class="inner"></div></td>
                """
        html_content_19 = """
        <td><span class="day">19</span> <div class="inner"></div></td>
                """
        html_content_20 = """
        <td><span class="day">20</span> <div class="inner"></div></td>
                """
        html_content_21 = """
        <td><span class="day">21</span> <div class="inner"></div></td>
                """
        html_content_22 = """
        <td><span class="day">22</span> <div class="inner"></div></td>
                """
        html_content_23 = """
        <td><span class="day">23</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240001"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">2</span><span class="score lead">8</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240002"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">3</span><span class="score lead">5</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240003"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">6</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240004"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="score">5</span><span class="score lead">7</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240005"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">3</span><span class="score lead">4</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li></ul></div></div></td>
        """

        html_content_24 = """
        <td><span class="day">24</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240010"><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span><span class="score lead">6</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240009"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240008"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">11</span><span class="score">8</span><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240007"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">6</span><span class="score lead">7</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240006"><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span><span class="score lead">8</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span></a></li></ul></div></div></td>
        """

        html_content_25 = """
        <td><span class="day">25</span> <div class="inner"></div></td>"""

        html_content_26 = """
        <td><span class="day">26</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240015"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="score">5</span><span class="score lead">10</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240014"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">1</span><span class="score lead">2</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240013"><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span><span class="score lead">8</span><span class="score">5</span><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240012"><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span><span class="score lead">6</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240011"><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span><span class="score">3</span><span class="score lead">4</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li></ul></div></div></td>"""

        html_content_27 = """
        <td><span class="day">27</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240016"><span class="team" style="background-color:#FFFFFF;color:#0061AA;">삼성</span><span class="score">2</span><span class="score">2</span><span class="team" style="background-color:#FFFFFF;color:#fc1cad;">LG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240017"><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span><span class="score lead">3</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240018"><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span><span class="score lead">11</span><span class="score">8</span><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240019"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">2</span><span class="score lead">8</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240020"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="score">2</span><span class="score lead">6</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li></ul></div></div></td>
        """

        html_content_28 = """
        <td><span class="day">28</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=preview&amp;s_no=20240025"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240024"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240023"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">7</span><span class="score lead">8</span><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240022"><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span><span class="score lead">10</span><span class="score">6</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240021"><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span><span class="score">1</span><span class="score lead">18</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li></ul></div></div></td>
        """

        html_content_29 = """
        <td><span class="day">29</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240030"><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span><span class="score">1</span><span class="score lead">3</span><span class="team" style="background-color:#888888;color:#FFFFFF;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240029"><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span><span class="score lead">6</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240028"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">2</span><span class="score lead">3</span><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240027"><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span><span class="score lead">3</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240026"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">4</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span></a></li></ul></div></div></td>
        """

        html_content_30 = """
        <td><span class="day">30</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240033"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">5</span><span class="score lead">8</span><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240035"><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span><span class="score lead">8</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240034"><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span><span class="score lead">9</span><span class="score">6</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240032"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">3</span><span class="score lead">8</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240031"><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span><span class="score">0</span><span class="score lead">8</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li></ul></div></div></td>
        """

        html_content_31 = """
        <td><span class="day">31</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240036"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">9</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240037"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">4</span><span class="score lead">8</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240038"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">3</span><span class="score lead">14</span><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240039"><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span><span class="score lead">4</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240040"><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span><span class="score lead">8</span><span class="score">7</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li></ul></div></div></td>
        """

        def parse_schedule(html_content, target_day):
            soup = BeautifulSoup(html_content, 'html.parser')
            day = soup.find('span', class_='day').text
            print(day)

            # Check if the current day matches the target day
            if day != target_day:
                return ""  # Return empty string if it's not the target day

            games = soup.find_all('li')
            result = f"{day}\n"
            for game in games:
                teams = game.find_all('span', class_='team')
                if len(teams) != 2:
                    continue  # Skip if teams are not found
                team1 = teams[0].text
                team2 = teams[1].text
                scores = game.find_all('span', class_='score')
                score1 = scores[0].text if scores else '우취'
                score2 = scores[1].text if len(scores) > 1 else ''
                result += f"{team1} {score1} {score2} {team2}\n"

            return result

        html_content_1 = [html_content_1]
        html_content_2 = [html_content_2]
        html_content_3 = [html_content_3]
        html_content_4 = [html_content_4]
        html_content_5 = [html_content_5]
        html_content_6 = [html_content_6]
        html_content_7 = [html_content_7]
        html_content_8 = [html_content_8]
        html_content_9 = [html_content_9]
        html_content_10 = [html_content_10]
        html_content_11 = [html_content_11]
        html_content_12 = [html_content_12]
        html_content_13 = [html_content_13]
        html_content_14 = [html_content_14]
        html_content_15 = [html_content_15]
        html_content_16 = [html_content_16]
        html_content_17 = [html_content_17]
        html_content_18 = [html_content_18]
        html_content_19 = [html_content_19]
        html_content_20 = [html_content_20]
        html_content_21 = [html_content_21]
        html_content_22 = [html_content_22]
        html_contents23 = [html_content_23]
        html_contents24 = [html_content_24]
        html_contents25 = [html_content_25]
        html_contents26 = [html_content_26]
        html_contents27 = [html_content_27]
        html_contents28 = [html_content_28]
        html_contents29 = [html_content_29]
        html_contents30 = [html_content_30]
        html_contents31 = [html_content_31]

        full_schedule1 = ""
        target_days1 = "1"
        for html_content in html_content_1:
            full_schedule1 += parse_schedule(html_content, target_days1)

        full_schedule2 = ""
        target_days2 = "2"
        for html_content in html_content_2:
            full_schedule2 += parse_schedule(html_content, target_days2)

        full_schedule3 = ""
        target_days3 = "3"
        for html_content in html_content_3:
            full_schedule3 += parse_schedule(html_content, target_days3)

        full_schedule4 = ""
        target_days4 = "4"
        for html_content in html_content_4:
            full_schedule4 += parse_schedule(html_content, target_days4)

        full_schedule5 = ""
        target_days5 = "5"
        for html_content in html_content_5:
            full_schedule5 += parse_schedule(html_content, target_days5)

        full_schedule6 = ""
        target_days6 = "6"
        for html_content in html_content_6:
            full_schedule6 += parse_schedule(html_content, target_days6)

        full_schedule7 = ""
        target_days7 = "7"
        for html_content in html_content_7:
            full_schedule7 += parse_schedule(html_content, target_days7)

        full_schedule8 = ""
        target_days8 = "8"
        for html_content in html_content_8:
            full_schedule8 += parse_schedule(html_content, target_days8)

        full_schedule9 = ""
        target_days9 = "9"
        for html_content in html_content_9:
            full_schedule9 += parse_schedule(html_content, target_days9)

        full_schedule10 = ""
        target_days10 = "10"
        for html_content in html_content_10:
            full_schedule10 += parse_schedule(html_content, target_days10)

        full_schedule11 = ""
        target_days11 = "11"
        for html_content in html_content_11:
            full_schedule11 += parse_schedule(html_content, target_days11)

        full_schedule12 = ""
        target_days12 = "12"
        for html_content in html_content_12:
            full_schedule12 += parse_schedule(html_content, target_days12)

        full_schedule13 = ""
        target_days13 = "13"
        for html_content in html_content_13:
            full_schedule13 += parse_schedule(html_content, target_days13)

        full_schedule14 = ""
        target_days14 = "14"
        for html_content in html_content_14:
            full_schedule14 += parse_schedule(html_content, target_days14)

        full_schedule15 = ""
        target_days15 = "15"
        for html_content in html_content_15:
            full_schedule15 += parse_schedule(html_content, target_days15)

        full_schedule16 = ""
        target_days16 = "16"
        for html_content in html_content_16:
            full_schedule16 += parse_schedule(html_content, target_days16)

        full_schedule17 = ""
        target_days17 = "17"
        for html_content in html_content_17:
            full_schedule17 += parse_schedule(html_content, target_days17)

        full_schedule18 = ""
        target_days18 = "18"
        for html_content in html_content_18:
            full_schedule18 += parse_schedule(html_content, target_days18)

        full_schedule19 = ""
        target_days19 = "19"
        for html_content in html_content_19:
            full_schedule19 += parse_schedule(html_content, target_days19)

        full_schedule20 = ""
        target_days20 = "20"
        for html_content in html_content_20:
            full_schedule20 += parse_schedule(html_content, target_days20)

        full_schedule21 = ""
        target_days21 = "21"
        for html_content in html_content_21:
            full_schedule21 += parse_schedule(html_content, target_days21)

        full_schedule22 = ""
        target_days22 = "22"
        for html_content in html_content_22:
            full_schedule22 += parse_schedule(html_content, target_days22)

        full_schedule23 = ""
        target_day23 = "23"
        for html_content in html_contents23:
            full_schedule23 += parse_schedule(html_content, target_day23)

        full_schedule24 = ""
        target_day24 = "24"
        for html_content in html_contents24:
            full_schedule24 += parse_schedule(html_content, target_day24)

        full_schedule25 = ""
        target_day25 = "25"
        for html_content in html_contents25:
            full_schedule25 += parse_schedule(html_content, target_day25)

        full_schedule26 = ""
        target_day26 = "26"
        for html_content in html_contents26:
            full_schedule26 += parse_schedule(html_content, target_day26)

        full_schedule27 = ""
        target_day27 = "27"
        for html_content in html_contents27:
            full_schedule27 += parse_schedule(html_content, target_day27)

        full_schedule28 = ""
        target_day28 = "28"
        for html_content in html_contents28:
            full_schedule28 += parse_schedule(html_content, target_day28)

        full_schedule29 = ""
        target_day29 = "29"
        for html_content in html_contents29:
            full_schedule29 += parse_schedule(html_content, target_day29)

        full_schedule30 = ""
        target_day30 = "30"
        for html_content in html_contents30:
            full_schedule30 += parse_schedule(html_content, target_day30)

        full_schedule31 = ""
        target_day31 = "31"
        for html_content in html_contents31:
            full_schedule31 += parse_schedule(html_content, target_day31)

        self.d_5.setText(full_schedule1)
        self.d_6.setText(full_schedule2)
        self.d_7.setText(full_schedule3)
        self.d_8.setText(full_schedule4)
        self.d_9.setText(full_schedule5)
        self.d_10.setText(full_schedule6)
        self.d_11.setText(full_schedule7)
        self.d_12.setText(full_schedule8)
        self.d_13.setText(full_schedule9)
        self.d_14.setText(full_schedule10)
        self.d_15.setText(full_schedule11)
        self.d_16.setText(full_schedule12)
        self.d_17.setText(full_schedule13)
        self.d_18.setText(full_schedule14)
        self.d_19.setText(full_schedule15)
        self.d_20.setText(full_schedule16)
        self.d_21.setText(full_schedule17)
        self.d_22.setText(full_schedule18)
        self.d_23.setText(full_schedule19)
        self.d_24.setText(full_schedule20)
        self.d_25.setText(full_schedule21)
        self.d_26.setText(full_schedule22)
        self.d_27.setText(full_schedule23)
        self.d_28.setText(full_schedule24)
        self.d_29.setText(full_schedule25)
        self.d_30.setText(full_schedule26)
        self.d_31.setText(full_schedule27)
        self.d_32.setText(full_schedule28)
        self.d_33.setText(full_schedule29)
        self.d_34.setText(full_schedule30)
        self.d_35.setText(full_schedule31)

    def show_info_4(self):
        for i in range(1, 36):
            getattr(self, f"d_{i}").setText("")

        self.show_info('4')
        html_content_1 = """
                    <td><span class="day">1</span> <div class="inner"></div></td>
                    """
        html_content_2 = """
                    <td><span class="day">2</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240041"><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span><span class="score lead">7</span><span class="score">5</span><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240042"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">6</span><span class="score lead">13</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240043"><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span><span class="score">6</span><span class="score lead">10</span><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240044"><span class="team" style="background-color:#888888;color:#FFFFFF;">롯데</span><span class="score lead">1</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240045"><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span><span class="score lead">8</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li></ul></div></div></td>        """
        html_content_3 = """
            	    <td><span class="day">3</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=preview&amp;s_no=20240050"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240049"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240048"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">5</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240047"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">3</span><span class="score lead">5</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240046"><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span><span class="score">0</span><span class="score lead">5</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li></ul></div></div></td>        """
        html_content_4 = """
                    <td><span class="day">4</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240051"><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span><span class="score">7</span><span class="score lead">8</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240052"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">2</span><span class="score lead">3</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240053"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">6</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240054"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">5</span><span class="score lead">6</span><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240055"><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span><span class="score lead">10</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li></ul></div></div></td>
                    """
        html_content_5 = """
                    <td><span class="day">5</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240060"><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span><span class="score">0</span><span class="score lead">5</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240059"><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span><span class="score lead">4</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240058"><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span><span class="score">2</span><span class="score lead">5</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240057"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">7</span><span class="score lead">11</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240056"><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span><span class="score lead">8</span><span class="score">7</span><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span></a></li></ul></div></div></td>                """
        html_content_6 = """
                    <td><span class="day">6</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240061"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">4</span><span class="score lead">8</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240062"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">6</span><span class="score lead">7</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240063"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">7</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240064"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">1</span><span class="score lead">8</span><span class="team" style="background-color:#888888;color:#FFFFFF;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240065"><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span><span class="score">3</span><span class="score lead">16</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li></ul></div></div></td>                """
        html_content_7 = """
                    <td><span class="day">7</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240070"><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span><span class="score">1</span><span class="score lead">10</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240069"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">6</span><span class="score lead">7</span><span class="team" style="background-color:#888888;color:#FFFFFF;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240068"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">7</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240067"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">3</span><span class="score lead">4</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240066"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">7</span><span class="score lead">16</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li></ul></div></div></td>                """
        html_content_8 = """
                    <td><span class="day">8</span> <div class="inner"></div></td>                """
        html_content_9 = """
                    <td><span class="day">9</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240075"><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span><span class="score lead">6</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240074"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">8</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240073"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">2</span><span class="score lead">7</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240072"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="score">5</span><span class="score lead">8</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240071"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">3</span><span class="score lead">5</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li></ul></div></div></td>                """
        html_content_10 = """
                    <td><span class="day">10</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240076"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">4</span><span class="score lead">7</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240077"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="score">4</span><span class="score lead">8</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240078"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">4</span><span class="score lead">5</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240079"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">10</span><span class="score">7</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240080"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">2</span><span class="score lead">3</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li></ul></div></div></td>                """
        html_content_11 = """
                    <td><span class="day">11</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240085"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">7</span><span class="score lead">8</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240084"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">4</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240083"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">4</span><span class="score lead">8</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240082"><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span><span class="score lead">5</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240081"><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span><span class="score lead">3</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span></a></li></ul></div></div></td>                            """
        html_content_12 = """
                    <td><span class="day">12</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240090"><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span><span class="score lead">8</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240089"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">8</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240088"><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span><span class="score">3</span><span class="score lead">8</span><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240087"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">4</span><span class="score lead">9</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240086"><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span><span class="score lead">2</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span></a></li></ul></div></div></td>                """
        html_content_13 = """
                    <td><span class="day">13</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240094"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">11</span><span class="score">9</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240091"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">2</span><span class="score lead">5</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240092"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">1</span><span class="score lead">8</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240093"><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span><span class="score lead">11</span><span class="score">8</span><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240095"><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span><span class="score lead">4</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li></ul></div></div></td>                """
        html_content_14 = """
                    <td><span class="day">14</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240100"><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span><span class="score">5</span><span class="score lead">12</span><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240099"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">5</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240098"><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span><span class="score lead">8</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240097"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">5</span><span class="score lead">7</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240096"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">5</span><span class="score lead">9</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li></ul></div></div></td>                """
        html_content_15 = """<td><span class="day">15</span> <div class="inner"></div></td>
                            """
        html_content_16 = """<td><span class="day">16</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240105"><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span><span class="score lead">7</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240104"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">5</span><span class="score lead">7</span><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240103"><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span><span class="score">4</span><span class="score lead">6</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240102"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">3</span><span class="score lead">6</span><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240101"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">2</span><span class="score lead">7</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li></ul></div></div></td>                """
        html_content_17 = """<td><span class="day">17</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240106"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">5</span><span class="score lead">6</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240107"><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span><span class="score lead">6</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240108"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">11</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240109"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">2</span><span class="score lead">9</span><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240110"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">3</span><span class="score lead">4</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li></ul></div></div></td>
                            """
        html_content_18 = """
                    <td><span class="day">18</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=preview&amp;s_no=20240115"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240114"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">2</span><span class="score lead">5</span><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240113"><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span><span class="score">5</span><span class="score lead">7</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240112"><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span><span class="score lead">3</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240111"><span class="team" style="background-color:#888888;color:#FFFFFF;">롯데</span><span class="score lead">9</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span></a></li></ul></div></div></td>                """
        html_content_19 = """
                    <td><span class="day">19</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240120"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">3</span><span class="score lead">4</span><span class="team" style="background-color:#888888;color:#FFFFFF;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240119"><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span><span class="score">3</span><span class="score lead">4</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240118"><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span><span class="score">1</span><span class="score lead">6</span><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240117"><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span><span class="score lead">4</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240116"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="score">8</span><span class="score lead">19</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li></ul></div></div></td>                """
        html_content_20 = """<td><span class="day">20</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=preview&amp;s_no=20240121"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240122"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240123"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">1</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240124"><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span><span class="score">2</span><span class="score lead">9</span><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240125"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li></ul></div></div></td>
                            """
        html_content_21 = """
                    <td><span class="day">21</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240130"><span class="team" style="background-color:#FFFFFF;color:#000000;">KT</span><span class="score">9</span><span class="score">9</span><span class="team" style="background-color:#FFFFFF;color:#888888;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240129"><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span><span class="score lead">15</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240128"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">5</span><span class="score">3</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240127"><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span><span class="score lead">10</span><span class="score">8</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240126"><span class="team" style="background-color:#86001f;color:#FFFFFF;">키움</span><span class="score lead">8</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20241399"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">5</span><span class="score lead">7</span><span class="team" style="background-color:#888888;color:#FFFFFF;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20241400"><span class="team" style="background-color:#FFFFFF;color:#fc1cad;">LG</span><span class="score">5</span><span class="score">5</span><span class="team" style="background-color:#FFFFFF;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20241401"><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span><span class="score">1</span><span class="score lead">2</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li></ul></div></div></td>                """
        html_content_22 = """
                    <td><span class="day">22</span> <div class="inner"></div></td>                """
        html_content_23 = """
                   <td><span class="day">23</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=preview&amp;s_no=20240135"><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span><span class="weather rain">우천취소</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240134"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">3</span><span class="score lead">7</span><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240133"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">6</span><span class="score lead">9</span><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240132"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">5</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240131"><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span><span class="score">3</span><span class="score lead">4</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li></ul></div></div></td>
                    """

        html_content_24 = """
                    <td><span class="day">24</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240136"><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span><span class="score lead">3</span><span class="score">1</span><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240137"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">6</span><span class="score">4</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240138"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">1</span><span class="score lead">7</span><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240139"><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span><span class="score">0</span><span class="score lead">6</span><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240140"><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span><span class="score lead">12</span><span class="score">7</span><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span></a></li></ul></div></div></td>
                    """

        html_content_25 = """
                    <td><span class="day">25</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240145"><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span><span class="score">3</span><span class="score lead">6</span><span class="team" style="background-color:#888888;color:#FFFFFF;">롯데</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240144"><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span><span class="score lead">8</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#0061AA;">삼성</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240143"><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span><span class="score">0</span><span class="score lead">9</span><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240142"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">13</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240141"><span class="team" style="background-color:#EEEEEE;color:#002b69;">NC</span><span class="score">3</span><span class="score lead">7</span><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span></a></li></ul></div></div></td>
                    """
        html_content_26 = """
                    <td><span class="day">26</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240150"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">0</span><span class="score lead">4</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240149"><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span><span class="score lead">10</span><span class="score">5</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240148"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">2</span><span class="score lead">5</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240147"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">3</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240146"><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span><span class="score">6</span><span class="score lead">7</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li></ul></div></div></td>
                    """
        html_content_27 = """
                   <td><span class="day">27</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240151"><span class="team" style="background-color:#EEEEEE;color:#ed1c24;">KIA</span><span class="score">3</span><span class="score lead">6</span><span class="team" style="background-color:#fc1cad;color:#FFFFFF;">LG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240152"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">11</span><span class="score">0</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240153"><span class="team" style="background-color:#000000;color:#FFFFFF;">KT</span><span class="score lead">5</span><span class="score">2</span><span class="team" style="background-color:#EEEEEE;color:#cf152d;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240154"><span class="team" style="background-color:#EEEEEE;color:#042071;">두산</span><span class="score">5</span><span class="score lead">10</span><span class="team" style="background-color:#f37321;color:#FFFFFF;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240155"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">0</span><span class="score lead">2</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li></ul></div></div></td>
                    """

        html_content_28 = """
                    <td><span class="day">28</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=summary&amp;s_no=20240160"><span class="team" style="background-color:#EEEEEE;color:#888888;">롯데</span><span class="score">3</span><span class="score lead">5</span><span class="team" style="background-color:#002b69;color:#FFFFFF;">NC</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240159"><span class="team" style="background-color:#042071;color:#FFFFFF;">두산</span><span class="score lead">17</span><span class="score">8</span><span class="team" style="background-color:#EEEEEE;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240158"><span class="team" style="background-color:#EEEEEE;color:#000000;">KT</span><span class="score">6</span><span class="score lead">11</span><span class="team" style="background-color:#cf152d;color:#FFFFFF;">SSG</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240157"><span class="team" style="background-color:#0061AA;color:#FFFFFF;">삼성</span><span class="score lead">11</span><span class="score">6</span><span class="team" style="background-color:#EEEEEE;color:#86001f;">키움</span></a></li><li><a href="/schedule/?m=summary&amp;s_no=20240156"><span class="team" style="background-color:#ed1c24;color:#FFFFFF;">KIA</span><span class="score lead">10</span><span class="score">7</span><span class="team" style="background-color:#EEEEEE;color:#fc1cad;">LG</span></a></li></ul></div></div></td>
                    """

        html_content_29 = """
                    <td style="background-color:#FCE2EA;"><span class="day">29</span> <div class="inner"></div></td>
                    """

        html_content_30 = """
                    <td><span class="day">30</span> <div class="inner"><div class="game_schedule_m">경기스케줄</div><div class="games"><ul><li><a href="/schedule/?m=preview&amp;s_no=20240161"><span class="team" style="background-color:#FFFFFF;color:#0061AA;">삼성</span><span class="stadium">잠실</span><span class="team" style="background-color:#FFFFFF;color:#042071;">두산</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240162"><span class="team" style="background-color:#FFFFFF;color:#cf152d;">SSG</span><span class="stadium">대전</span><span class="team" style="background-color:#FFFFFF;color:#f37321;">한화</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240163"><span class="team" style="background-color:#FFFFFF;color:#000000;">KT</span><span class="stadium">광주</span><span class="team" style="background-color:#FFFFFF;color:#ed1c24;">KIA</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240164"><span class="team" style="background-color:#FFFFFF;color:#86001f;">키움</span><span class="stadium">사직</span><span class="team" style="background-color:#FFFFFF;color:#888888;">롯데</span></a></li><li><a href="/schedule/?m=preview&amp;s_no=20240165"><span class="team" style="background-color:#FFFFFF;color:#fc1cad;">LG</span><span class="stadium">창원</span><span class="team" style="background-color:#FFFFFF;color:#002b69;">NC</span></a></li></ul></div></div></td>
                    """

        def parse_schedule(html_content, target_day):
            soup = BeautifulSoup(html_content, 'html.parser')
            day = soup.find('span', class_='day').text
            print(day)

            # Check if the current day matches the target day
            if day != target_day:
                return ""  # Return empty string if it's not the target day

            games = soup.find_all('li')
            result = f"{day}\n"
            for game in games:
                teams = game.find_all('span', class_='team')
                if len(teams) != 2:
                    continue  # Skip if teams are not found
                team1 = teams[0].text
                team2 = teams[1].text
                scores = game.find_all('span', class_='score')
                score1 = scores[0].text if scores else '우취'
                score2 = scores[1].text if len(scores) > 1 else ''
                result += f"{team1} {score1} {score2} {team2}\n"

            return result

        html_content_1 = [html_content_1]
        html_content_2 = [html_content_2]
        html_content_3 = [html_content_3]
        html_content_4 = [html_content_4]
        html_content_5 = [html_content_5]
        html_content_6 = [html_content_6]
        html_content_7 = [html_content_7]
        html_content_8 = [html_content_8]
        html_content_9 = [html_content_9]
        html_content_10 = [html_content_10]
        html_content_11 = [html_content_11]
        html_content_12 = [html_content_12]
        html_content_13 = [html_content_13]
        html_content_14 = [html_content_14]
        html_content_15 = [html_content_15]
        html_content_16 = [html_content_16]
        html_content_17 = [html_content_17]
        html_content_18 = [html_content_18]
        html_content_19 = [html_content_19]
        html_content_20 = [html_content_20]
        html_content_21 = [html_content_21]
        html_content_22 = [html_content_22]
        html_contents23 = [html_content_23]
        html_contents24 = [html_content_24]
        html_contents25 = [html_content_25]
        html_contents26 = [html_content_26]
        html_contents27 = [html_content_27]
        html_contents28 = [html_content_28]
        html_contents29 = [html_content_29]
        html_contents30 = [html_content_30]

        full_schedule1 = ""
        target_days1 = "1"
        for html_content in html_content_1:
            full_schedule1 += parse_schedule(html_content, target_days1)

        full_schedule2 = ""
        target_days2 = "2"
        for html_content in html_content_2:
            full_schedule2 += parse_schedule(html_content, target_days2)

        full_schedule3 = ""
        target_days3 = "3"
        for html_content in html_content_3:
            full_schedule3 += parse_schedule(html_content, target_days3)

        full_schedule4 = ""
        target_days4 = "4"
        for html_content in html_content_4:
            full_schedule4 += parse_schedule(html_content, target_days4)

        full_schedule5 = ""
        target_days5 = "5"
        for html_content in html_content_5:
            full_schedule5 += parse_schedule(html_content, target_days5)

        full_schedule6 = ""
        target_days6 = "6"
        for html_content in html_content_6:
            full_schedule6 += parse_schedule(html_content, target_days6)

        full_schedule7 = ""
        target_days7 = "7"
        for html_content in html_content_7:
            full_schedule7 += parse_schedule(html_content, target_days7)

        full_schedule8 = ""
        target_days8 = "8"
        for html_content in html_content_8:
            full_schedule8 += parse_schedule(html_content, target_days8)

        full_schedule9 = ""
        target_days9 = "9"
        for html_content in html_content_9:
            full_schedule9 += parse_schedule(html_content, target_days9)

        full_schedule10 = ""
        target_days10 = "10"
        for html_content in html_content_10:
            full_schedule10 += parse_schedule(html_content, target_days10)

        full_schedule11 = ""
        target_days11 = "11"
        for html_content in html_content_11:
            full_schedule11 += parse_schedule(html_content, target_days11)

        full_schedule12 = ""
        target_days12 = "12"
        for html_content in html_content_12:
            full_schedule12 += parse_schedule(html_content, target_days12)

        full_schedule13 = ""
        target_days13 = "13"
        for html_content in html_content_13:
            full_schedule13 += parse_schedule(html_content, target_days13)

        full_schedule14 = ""
        target_days14 = "14"
        for html_content in html_content_14:
            full_schedule14 += parse_schedule(html_content, target_days14)

        full_schedule15 = ""
        target_days15 = "15"
        for html_content in html_content_15:
            full_schedule15 += parse_schedule(html_content, target_days15)

        full_schedule16 = ""
        target_days16 = "16"
        for html_content in html_content_16:
            full_schedule16 += parse_schedule(html_content, target_days16)

        full_schedule17 = ""
        target_days17 = "17"
        for html_content in html_content_17:
            full_schedule17 += parse_schedule(html_content, target_days17)

        full_schedule18 = ""
        target_days18 = "18"
        for html_content in html_content_18:
            full_schedule18 += parse_schedule(html_content, target_days18)

        full_schedule19 = ""
        target_days19 = "19"
        for html_content in html_content_19:
            full_schedule19 += parse_schedule(html_content, target_days19)

        full_schedule20 = ""
        target_days20 = "20"
        for html_content in html_content_20:
            full_schedule20 += parse_schedule(html_content, target_days20)

        full_schedule21 = ""
        target_days21 = "21"
        for html_content in html_content_21:
            full_schedule21 += parse_schedule(html_content, target_days21)

        full_schedule22 = ""
        target_days22 = "22"
        for html_content in html_content_22:
            full_schedule22 += parse_schedule(html_content, target_days22)

        full_schedule23 = ""
        target_day23 = "23"
        for html_content in html_contents23:
            full_schedule23 += parse_schedule(html_content, target_day23)

        full_schedule24 = ""
        target_day24 = "24"
        for html_content in html_contents24:
            full_schedule24 += parse_schedule(html_content, target_day24)

        full_schedule25 = ""
        target_day25 = "25"
        for html_content in html_contents25:
            full_schedule25 += parse_schedule(html_content, target_day25)

        full_schedule26 = ""
        target_day26 = "26"
        for html_content in html_contents26:
            full_schedule26 += parse_schedule(html_content, target_day26)

        full_schedule27 = ""
        target_day27 = "27"
        for html_content in html_contents27:
            full_schedule27 += parse_schedule(html_content, target_day27)

        full_schedule28 = ""
        target_day28 = "28"
        for html_content in html_contents28:
            full_schedule28 += parse_schedule(html_content, target_day28)

        full_schedule29 = ""
        target_day29 = "29"
        for html_content in html_contents29:
            full_schedule29 += parse_schedule(html_content, target_day29)

        full_schedule30 = ""
        target_day30 = "30"
        for html_content in html_contents30:
            full_schedule30 += parse_schedule(html_content, target_day30)

        self.d_1.setText(full_schedule1)
        self.d_2.setText(full_schedule2)
        self.d_3.setText(full_schedule3)
        self.d_4.setText(full_schedule4)
        self.d_5.setText(full_schedule5)
        self.d_6.setText(full_schedule6)
        self.d_7.setText(full_schedule7)
        self.d_8.setText(full_schedule8)
        self.d_9.setText(full_schedule9)
        self.d_10.setText(full_schedule10)
        self.d_11.setText(full_schedule11)
        self.d_12.setText(full_schedule12)
        self.d_13.setText(full_schedule13)
        self.d_14.setText(full_schedule14)
        self.d_15.setText(full_schedule15)
        self.d_16.setText(full_schedule16)
        self.d_17.setText(full_schedule17)
        self.d_18.setText(full_schedule18)
        self.d_19.setText(full_schedule19)
        self.d_20.setText(full_schedule20)
        self.d_21.setText(full_schedule21)
        self.d_22.setText(full_schedule22)
        self.d_23.setText(full_schedule23)
        self.d_24.setText(full_schedule24)
        self.d_25.setText(full_schedule25)
        self.d_26.setText(full_schedule26)
        self.d_27.setText(full_schedule27)
        self.d_28.setText(full_schedule28)
        self.d_29.setText(full_schedule29)
        self.d_30.setText(full_schedule30)

    def show_info_5(self):
        for i in range(1, 36):
            getattr(self, f"d_{i}").setText("")

        self.show_info('5')
        import requests
        from lxml import html

        url = "https://statiz.sporki.com/schedule/?year=2024&month=5"

        response = requests.get(url)
        html_content = response.text

        parsed_html = html.fromstring(html_content)

        # Function to set text for each day
        def set_day_text(day_widget, text):
            day_widget.setText(text)

        # Dictionary to store XPath expressions for each day
        days = {
            day: (
                "/html/body/div[2]/div[3]/section/div[3]/div/div/div/div[2]/div/table/tbody/tr[{}]/td[{}]/span".format(
                    day // 7 + 1, (day % 7) + 1),
                [
                    "/html/body/div[2]/div[3]/section/div[3]/div/div/div/div[2]/div/table/tbody/tr[{}]/td[{}]/div/div[2]/ul/li[{}]/a/span[{}]".format(
                        day // 7 + 1, (day % 7) + 1, i, j) for i in range(1, 6) for j in range(1, 4)])
            for day in range(3, 33)
        }

        # Counter for setting text to corresponding widget
        widget_counter = 4

        # Loop through each day's XPath expressions
        for day, (day_xpath, day_xpath_g) in days.items():
            game_result = parsed_html.xpath(day_xpath)
            if game_result:
                set_day_text(getattr(self, f"d_{widget_counter}"), game_result[0].text_content().strip())
            else:
                set_day_text(getattr(self, f"d_{widget_counter}"), "경기 결과를 찾을 수 없습니다.")

            # Set game schedule text
            count = 0
            day_text = ""
            for xpath_expression in day_xpath_g:
                data = parsed_html.xpath(xpath_expression)
                if data:
                    for item in data:
                        day_text += item.text_content().strip() + ' '
                        count += 1
                        if count % 3 == 0:
                            day_text += "\n"
            set_day_text(getattr(self, f"d_{widget_counter}"), day_text)
            widget_counter += 1

    def show_info_6(self):
        for i in range(1, 36):
            getattr(self, f"d_{i}").setText("")

        self.show_info('6')
        import requests
        from lxml import html

        url = "https://statiz.sporki.com/schedule/?year=2024&month=6"

        response = requests.get(url)
        html_content = response.text

        parsed_html = html.fromstring(html_content)

        def set_day_text(day_widget, text):
            day_widget.setText(text)

        days = {
            day: (
                "/html/body/div[2]/div[3]/section/div[3]/div/div/div/div[2]/div/table/tbody/tr[{}]/td[{}]/span".format(
                    day // 7 + 1, (day % 7) + 1),
                [
                    "/html/body/div[2]/div[3]/section/div[3]/div/div/div/div[2]/div/table/tbody/tr[{}]/td[{}]/div/div[2]/ul/li[{}]/a/span[{}]".format(
                        day // 7 + 1, (day % 7) + 1, i, j) for i in range(1, 6) for j in range(1, 4)])
            for day in range(3, 35)
        }

        widget_counter = 4

        for day, (day_xpath, day_xpath_g) in days.items():
            game_result = parsed_html.xpath(day_xpath)
            if game_result:
                set_day_text(getattr(self, f"d_{widget_counter}"), game_result[0].text_content().strip())
            else:
                set_day_text(getattr(self, f"d_{widget_counter}"), "경기 결과를 찾을 수 없습니다.")

            count = 0
            day_text = ""
            for xpath_expression in day_xpath_g:
                data = parsed_html.xpath(xpath_expression)
                if data:
                    for item in data:
                        day_text += item.text_content().strip() + ' '
                        count += 1
                        if count % 3 == 0:
                            day_text += "\n"
            set_day_text(getattr(self, f"d_{widget_counter}"), day_text)
            widget_counter += 1
            if widget_counter > 35:
                break

    def show_info_7(self):
        for i in range(1, 36):
            getattr(self, f"d_{i}").setText("")

        self.show_info('7')
        import requests
        from lxml import html

        url = "https://statiz.sporki.com/schedule/?year=2024&month=7"

        response = requests.get(url)
        html_content = response.text

        parsed_html = html.fromstring(html_content)

        # Function to set text for each day
        def set_day_text(day_widget, text):
            day_widget.setText(text)

        # Dictionary to store XPath expressions for each day
        days = {
            day: (
                "/html/body/div[2]/div[3]/section/div[3]/div/div/div/div[2]/div/table/tbody/tr[{}]/td[{}]/span".format(
                    day // 7 + 1, (day % 7) + 1),
                [
                    "/html/body/div[2]/div[3]/section/div[3]/div/div/div/div[2]/div/table/tbody/tr[{}]/td[{}]/div/div[2]/ul/li[{}]/a/span[{}]".format(
                        day // 7 + 1, (day % 7) + 1, i, j) for i in range(1, 6) for j in range(1, 4)])
            for day in range(1, 33)
        }

        # Counter for setting text to corresponding widget
        widget_counter = 2

        # Loop through each day's XPath expressions
        for day, (day_xpath, day_xpath_g) in days.items():
            game_result = parsed_html.xpath(day_xpath)
            if game_result:
                set_day_text(getattr(self, f"d_{widget_counter}"), game_result[0].text_content().strip())
            else:
                set_day_text(getattr(self, f"d_{widget_counter}"), "경기 결과를 찾을 수 없습니다.")

            # Set game schedule text
            count = 0
            day_text = ""
            for xpath_expression in day_xpath_g:
                data = parsed_html.xpath(xpath_expression)
                if data:
                    for item in data:
                        day_text += item.text_content().strip() + ' '
                        count += 1
                        if count % 3 == 0:
                            day_text += "\n"
            set_day_text(getattr(self, f"d_{widget_counter}"), day_text)
            widget_counter += 1
            if widget_counter > 33:
                break  # Stop the loop if widget_counter exceeds 33

    def show_info_8(self):
        for i in range(1, 36):
            getattr(self, f"d_{i}").setText("")

        self.show_info('8')
        import requests
        from lxml import html

        url = "https://statiz.sporki.com/schedule/?year=2024&month=8"

        response = requests.get(url)
        html_content = response.text

        parsed_html = html.fromstring(html_content)

        # Function to set text for each day
        def set_day_text(day_widget, text):
            day_widget.setText(text)

        # Dictionary to store XPath expressions for each day
        days = {
            day: (
                "/html/body/div[2]/div[3]/section/div[3]/div/div/div/div[2]/div/table/tbody/tr[{}]/td[{}]/span".format(
                    day // 7 + 1, (day % 7) + 1),
                [
                    "/html/body/div[2]/div[3]/section/div[3]/div/div/div/div[2]/div/table/tbody/tr[{}]/td[{}]/div/div[2]/ul/li[{}]/a/span[{}]".format(
                        day // 7 + 1, (day % 7) + 1, i, j) for i in range(1, 6) for j in range(1, 4)])
            for day in range(1, 33)
        }

        # Counter for setting text to corresponding widget
        widget_counter = 2

        # Loop through each day's XPath expressions
        for day, (day_xpath, day_xpath_g) in days.items():
            game_result = parsed_html.xpath(day_xpath)
            if game_result:
                set_day_text(getattr(self, f"d_{widget_counter}"), game_result[0].text_content().strip())
            else:
                set_day_text(getattr(self, f"d_{widget_counter}"), "경기 결과를 찾을 수 없습니다.")

            # Set game schedule text
            count = 0
            day_text = ""
            for xpath_expression in day_xpath_g:
                data = parsed_html.xpath(xpath_expression)
                if data:
                    for item in data:
                        day_text += item.text_content().strip() + ' '
                        count += 1
                        if count % 3 == 0:
                            day_text += "\n"
            set_day_text(getattr(self, f"d_{widget_counter}"), day_text)
            widget_counter += 1
            if widget_counter > 33:
                break  # Stop the loop if widget_counter exceeds 33


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kbo = KboApp()
    kbo.show()
    sys.exit(app.exec_())
