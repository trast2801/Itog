import os
import json


class PriceMachine():

    def __init__(self):
        self.data = []
        ''' здесь хранятся данные из прайс листов
            это набор коретежей
            (номер пп, название, цена, фасовка, файл, цена за кг)
            цена за кг - вычисляемое поле (фасовка * цена)  
        '''

        self.result = ''  # пока не придумал
        self.name_length = 0

    def load_prices(self, file_path):
        files = os.listdir(file_path)
        result = []
        for i in files:
            if 'price' in i:
                result.append(i)
            else:
                continue
        files= [] #освобождаю память
        print(result)



        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''

    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''

    def find_text(self, text):
        pass



print("          Анализатор прайс-листов")
while True:
    print()
    file_path = input('Введите путь для импорта данных, по умолчанию используем текущую папку /data ('
                      'для выхода нажимите /) :')
    if file_path == "/":
        break
    if len(file_path) == 0 :
        file_path = 'data' # путь по умолчанию в папке проекта
    if os.path.exists(file_path) == False:
        input("Такой каталог не доступен, нажмите Enter для продолжения")
        print()
    else:
        print(f"Данные берем из этого каталога : {file_path}")
        pm = PriceMachine()
        print(pm.load_prices(file_path))




#    Логика работы программы
'''
print('the end')
print(pm.export_to_html())

'''
