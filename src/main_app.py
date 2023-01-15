from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import mysql.connector as con

# 載入設計好的GUI介面檔案
ui,_=loadUiType('src/vet_hospital.ui')

def connect_to_database(sql_query):
    my_database = con.connect(host="localhost", user="root", password="", port=3306, db="veterinary_hospital")
    cursor = my_database.cursor()
    cursor.execute(sql_query)   # 執行指令
    result = cursor.fetchall()  # 取得結果
    my_database.commit()
    return cursor, result

def display_result(self, cursor, result):
    # 先計算會需要多少row和column
    row = 0
    column = 0
    for row_num, row_data in enumerate(result):
        row += 1
        column = 0
        for column_num, data in enumerate(row_data):
            column += 1
    
    self.result_display.clear() # 清除result_display裡面的內容
    self.result_display.setRowCount(0)  # 把row數量清空為0
    self.result_display.setColumnCount(column)

    for row_num, row_data in enumerate(result):
        self.result_display.insertRow(row_num)
        for column_num, data in enumerate(row_data):
            self.result_display.setItem(row_num, column_num, QTableWidgetItem(str(data)))
    
    # 取得每個column的名稱，並顯示
    self.result_display.setHorizontalHeaderLabels(cursor.column_names)

def show_text_browser(self, msg1, msg2):
    self.textBrowser.clear()
    self.textBrowser.append(msg1)
    self.textBrowser.append(msg2)

class MainApp(QWidget, ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        # 以下是每個按鈕被點擊時，其所觸發的function
        self.show_vet_b.clicked.connect(self.show_vet)
        # ex. 當show_vet_b這個按鈕被點擊時，就觸發show_vet這個function
        self.show_dept_b.clicked.connect(self.show_department)
        self.show_pat_b.clicked.connect(self.show_patient)
        self.show_record_b.clicked.connect(self.show_record)
        self.show_owner_b.clicked.connect(self.show_owner)
        self.show_check_b.clicked.connect(self.show_check)
        self.sfw_b.clicked.connect(self.select_from_where)
        self.delete_b.clicked.connect(self.delete)
        self.insert_b.clicked.connect(self.insert)
        self.update_b.clicked.connect(self.update)
        self.in_b.clicked.connect(self.in_query)
        self.not_in_b.clicked.connect(self.not_in_query)
        self.exists_b.clicked.connect(self.exists_query)
        self.not_exists_b.clicked.connect(self.not_exists_query)
        self.count_b.clicked.connect(self.count_query)
        self.sum_b.clicked.connect(self.sum_query)
        self.max_b.clicked.connect(self.max_query)
        self.min_b.clicked.connect(self.min_query)
        self.avg_b.clicked.connect(self.avg_query)
        self.having_b.clicked.connect(self.having_query)
        self.enter_b.clicked.connect(self.sql_query)

    # 以下是各按鈕所觸發的各個function
    def show_vet(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT * FROM 獸醫")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("顯示獸醫的資料")
            msg2 = ("SQL指令：\nSELECT * FROM 獸醫")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")
    
    def show_department(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT * FROM 科別")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)

            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("顯示科別資訊")
            msg2 = ("SQL指令：\nSELECT * FROM 科別")
            show_text_browser(self, msg1, msg2)
            
        except con.Error as error:
            print(f"Database error: {error}")
        
    def show_patient(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT * FROM 病患")
            
            # 把query結果顯示在result_display
            display_result(self, cursor, result)

            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("顯示病患資料")
            msg2 = ("SQL指令：\nSELECT * FROM 病患")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")
    
    def show_record(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT * FROM 來診紀錄")
            
            # 把query結果顯示在result_display
            display_result(self, cursor, result)

            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("顯示來診紀錄")
            msg2 = ("SQL指令：\nSELECT * FROM 來診紀錄")
            show_text_browser(self, msg1, msg2)
            
        except con.Error as error:
            print(f"Database error: {error}")

    def show_owner(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT * FROM 飼主")
            
            # 把query結果顯示在result_display
            display_result(self, cursor, result)

            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("顯示飼主資料")
            msg2 = ("SQL指令：\nSELECT * FROM 飼主")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def show_check(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT * FROM 看診")
            
            # 把query結果顯示在result_display
            display_result(self, cursor, result)

            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("顯示看診紀錄")
            msg2 = ("SQL指令：\nSELECT * FROM 看診")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def select_from_where(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT P.姓名 AS 病患姓名, O.姓名 AS 飼主姓名, O.電話 AS 飼主電話 FROM 病患 AS P, 飼主 AS O WHERE P.飼主身分證字號 = O.身分證字號;")
            
            # 把query結果顯示在result_display
            display_result(self, cursor, result)

            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("顯示每個病患姓名，以及其飼主名稱和電話")
            msg2 = ("SQL指令：\nSELECT P.姓名 AS 病患姓名, O.姓名 AS 飼主姓名, O.電話 AS 飼主電話 \nFROM 病患 AS P, 飼主 AS O \nWHERE P.飼主身分證字號 = O.身分證字號;")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")
    
    def delete(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("DELETE FROM 獸醫 WHERE 姓名 = 'John';")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)

            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("獸醫John離職了，刪掉他的資訊")
            msg2 = ("SQL指令：\nDELETE FROM 獸醫 \nWHERE 姓名 = 'John';")
            show_text_browser(self, msg1, msg2)

            QMessageBox.information(self, "Delete Vet John", "成功刪除獸醫John的資料")
        except con.Error as error:
            print(f"Database error: {error}")
    
    def insert(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("INSERT INTO 獸醫 VALUES('Z777777777', 'John', '1999-08-11', '男', '2021-12-01', '0977-777-777', '台南市gg路27號', '013', '23000');")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("獸醫John離職後又回鍋了，新增他的資訊")
            msg2 = ("SQL指令：\nINSERT INTO 獸醫\nVALUES('Z777777777', 'John', '1999-08-11', '男', '2021-12-01', '0977-777-777', '台南市gg路27號', '013', '23000');")
            show_text_browser(self, msg1, msg2)

            QMessageBox.information(self, "Insert Vet John", "成功新增獸醫John的資料")
        except con.Error as error:
            print(f"Database error: {error}")
    
    def update(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("UPDATE 獸醫 SET 薪水 = 22000 WHERE 科別ID = '013';")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("整容科業績太差，整容科全員薪水降為22k以示懲處")
            msg2 = ("SQL指令：\nUPDATE 獸醫\nSET 薪水 = 22000\nWHERE 科別ID = '013';")
            show_text_browser(self, msg1, msg2)

            QMessageBox.information(self, "Update Vet Salary", "成功將整容科獸醫降薪至22k")
        except con.Error as error:
            print(f"Database error: {error}")
    
    def in_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT D.科別名稱 AS 科別名稱, V.姓名 AS 獸醫姓名 FROM 獸醫 AS V, 科別 AS D WHERE D.科別ID IN (SELECT V.科別ID FROM 獸醫 WHERE V.科別ID = D.科別ID) ORDER BY D.科別ID;")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("顯示每個獸醫及其科別/專科")
            msg2 = ("SQL指令：\nSELECT D.科別名稱 AS 科別名稱, V.姓名 AS 獸醫姓名 \nFROM 獸醫 AS V, 科別 AS D \nWHERE D.科別ID IN (SELECT V.科別ID FROM 獸醫 WHERE V.科別ID = D.科別ID)\nORDER BY D.科別ID;")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")
    
    def not_in_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT V.姓名, V.薪水, DEPT.科別名稱 FROM 獸醫 AS V, 科別 AS DEPT WHERE V.科別ID NOT IN (SELECT D.科別ID FROM 科別 AS D WHERE D.科別名稱 = '一般內科' OR D.科別名稱 = '一般外科') AND V.科別ID = DEPT.科別ID;")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢非一般內科，也不是一般外科獸醫的姓名、科別、以及薪水")
            msg2 = ("SQL指令：\nSELECT V.姓名, V.薪水, DEPT.科別名稱 \nFROM 獸醫 AS V, 科別 AS DEPT \nWHERE V.科別ID NOT IN (SELECT D.科別ID FROM 科別 AS D WHERE D.科別名稱 = '一般內科' OR D.科別名稱 = '一般外科') AND V.科別ID = DEPT.科別ID;")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {eerror}")
    
    def exists_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT 姓名 AS 病患姓名 FROM 病患 AS P WHERE EXISTS (SELECT * FROM 看診 AS V, 來診紀錄 AS R WHERE R.日期 = '2022-10-03' AND V.來診紀錄編號 = R.來診紀錄編號 AND V.病患病歷ID = P.病歷ID);")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢2022-10-03來診的病患姓名")
            msg2 = ("SQL指令：\nSELECT 姓名 AS 病患姓名 \nFROM 病患 AS P \nWHERE EXISTS (SELECT * FROM 看診 AS V, 來診紀錄 AS R WHERE R.日期 = '2022-10-03' AND V.來診紀錄編號 = R.來診紀錄編號 AND V.病患病歷ID = P.病歷ID);")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def not_exists_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT V.姓名, V.薪水 FROM 獸醫 AS V WHERE NOT EXISTS (SELECT * FROM 獸醫 WHERE V.薪水 >= 40000);")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢薪水低於40000的獸醫姓名與薪水")
            msg2 = ("SQL指令：\nSELECT V.姓名, V.薪水 \nFROM 獸醫 AS V \nWHERE NOT EXISTS (SELECT * FROM 獸醫 WHERE V.薪水 >= 40000);")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")
    
    def count_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT COUNT(V.身分證字號) AS 低薪獸醫數量 FROM 獸醫 AS V WHERE V.薪水 < 40000;")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢有多少獸醫薪水低於40000")
            msg2 = ("SQL指令：\nSELECT COUNT(V.身分證字號) AS 低薪獸醫數量 \nFROM 獸醫 AS V \nWHERE V.薪水 < 40000;")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def sum_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT SUM(掛號費) + SUM(診療費) AS 當日營業額 FROM 來診紀錄 WHERE 日期 = '2022-10-06';")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢2022-10-06之營業額")
            msg2 = ("SQL指令：\nSELECT SUM(掛號費) + SUM(診療費) AS 當日營業額 FROM 來診紀錄 WHERE 日期 = '2022-10-06';")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def max_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT A.姓名, A.薪水 FROM 獸醫 AS A WHERE A.薪水 IN (SELECT MAX(B.薪水) FROM 獸醫 AS B);")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢薪水最高的獸醫的姓名和薪水")
            msg2 = ("SQL指令：\nSELECT A.姓名, A.薪水 \nFROM 獸醫 AS A \nWHERE A.薪水 IN (SELECT MAX(B.薪水) FROM 獸醫 AS B);")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def min_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT A.姓名, A.薪水 FROM 獸醫 AS A WHERE A.薪水 IN (SELECT MIN(B.薪水) FROM 獸醫 AS B);")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢薪水最低的獸醫的姓名和薪水")
            msg2 = ("SQL指令：\nSELECT A.姓名, A.薪水 \nFROM 獸醫 AS A \nWHERE A.薪水 IN (SELECT MIN(B.薪水) FROM 獸醫 AS B);")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def avg_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT AVG(薪水) AS 平均薪資 FROM 獸醫;")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢獸醫的平均薪資")
            msg2 = ("SQL指令：\nSELECT AVG(薪水) AS 平均薪資 \nFROM 獸醫;")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def having_query(self):
        try:
            # 連線至database
            cursor, result = connect_to_database("SELECT SUM(掛號費) + SUM(診療費) AS 日營業額, 日期 FROM 來診紀錄 GROUP BY 日期 HAVING 日營業額 >= 5000;")

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            # 在textBrower顯示此按鈕的說明與SQL指令
            msg1 = ("查詢日營業額超過5000的日期和日營業額")
            msg2 = ("SQL指令：\nSELECT SUM(掛號費) + SUM(診療費) AS 日營業額, 日期 \nFROM 來診紀錄 \nGROUP BY 日期 \nHAVING 日營業額 >= 5000;")
            show_text_browser(self, msg1, msg2)

        except con.Error as error:
            print(f"Database error: {error}")

    def sql_query(self):
        try:
            # 取得輸入的SQL指令
            query = self.enter_sql_cmd.toPlainText()

            # 連線至database
            cursor, result = connect_to_database(query)

            # 把query結果顯示在result_display
            display_result(self, cursor, result)
            
            self.textBrowser.clear()
            QMessageBox.information(self, "SQL Query", "SQL query sent successfully")
        except Exception as error:
            print(error)
            QMessageBox.information(self, "SQL Query", "Error in sending SQL query")
