import sys
import requests
import json
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#description_label{
                font-size: 40px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)


    def get_weather(self):
        api_key = "weather api key "
        city=self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response=requests.get(url)
        data=response.json() 
        # print(data)

        if data["cod"] ==200:
            self.display_weather(data)
        else:
            self.display_error("you live on pluto ???")
        
    def display_error(self,message):
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet("font-size :30px;")
        self.description_label.setStyleSheet("font-size :25px;")
        self.description_label.setText("idk :) ")
    def display_weather(self,data):
        temperature=data["main"]["temp"]
        description=data["weather"][0]["description"]
        self.temperature_label.setText(f"{temperature}* C")
        self.description_label.setText(description)
if __name__=="__main__":
    # main()
    app=QApplication(sys.argv)
    window=WeatherApp()
    window.show()
    sys.exit(app.exec_())