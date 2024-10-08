import csv
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
        temp_data = []
        files = os.listdir(file_path)  # получить список файлов в целевой директории
        result = []

        # добавить проверку что это csv файл ??

        for i in files:
            if 'price' in i:
                temp = file_path + i
                result.append(temp)
            else:
                continue
        # files = []  # освобождаю память
        print(result)
        count_files = 0
        # stroka = "Номер,Название,Цена,Фасовка,Файл,Цена за кг"
        # self.data.append(stroka)
        for file in result:
            with open(file, encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count_inner = 0  # счетчик первых строк в каждом файле (имя столбцов)
                for row in file_reader:
                    if count_inner == 0:
                        dict_ = self._search_product_price_weight(row)
                        # Вывод строки, содержащей заголовки для столбцов
                        # print(f'Файл содержит столбцы: {", ".join(row)}')
                    else:
                        # Вывод строк
                        row_tovar = (dict_.get("товар"))
                        row_cena = (dict_.get("цена"))
                        row_ves = (dict_.get("вес"))
                        cena_za_edinicy = round(int(row[row_cena]) / int(row[row_ves]), 2)
                        stroka = (f' {row[row_tovar]}, {row[row_cena]}, {row[row_ves]}, {files[count_files]},'
                                  f' {cena_za_edinicy:}')
                        temp_data.append([row[row_tovar], row[row_cena], row[row_ves], files[count_files],cena_za_edinicy]) # заполнение массива из прайсов
                    count_inner += 1
            count_files += 1  # использую для ввода имени файла
        #self._enum(temp_data)
        self.data = sorted(temp_data, key=lambda x: float(x[4]))
        count = 1
        for i in self.data:
            print(count, i[0], i[1], i[2], i[3], i[4])
            count += 1

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
        row = {}
        count = 0
        for temp in headers:
            if 'название' in temp or 'наименование' in temp or 'продукт' in temp or 'товар' in temp:
                row['товар'] = count
            if 'розница' in temp or 'цена' in temp:
                row['цена'] = count
            if 'вес' in temp or 'масса' in temp or 'фасовка' in temp:
                row['вес'] = count
            count += 1
        # print (row)
        '''
            Возвращает номера столбцов
        '''

        return row

    def _enum(self, data : []):  # возвращает и сортированный нумерованный список
        count = 1
        target = []
        data = sorted(data, key=lambda x: float(x[4]))
        '''for i in target1:
            source = str(count) + ',' +  data[count-1]
            target.append(source)
            count += 1
        #self.data = target #продумать как сделать без буферного списка
        #target1 = sorted(target, key=lambda x: float(x[6]))
        self.data = target.copy()

        '''
        for i in data:
            print(count, i[0], i[1], i[2], i[3], i[4])
            count += 1


    # def export_to_html(self, fname='output.html'):
    #     result = '''
    #     <!DOCTYPE html>
    #     <html>
    #     <head>
    #         <title>Позиции продуктов</title>
    #     </head>
    #     <body>
    #         <table>
    #             <tr>
    #                 <th>Номер</th>
    #                 <th>Название</th>
    #                 <th>Цена</th>
    #                 <th>Фасовка</th>
    #                 <th>Файл</th>
    #                 <th>Цена за кг.</th>
    #             </tr>
    #     '''

    def export_to_html(self, output_file_path=r'output.html'):
        if self.data:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write('''
                <!DOCTYPE html>
                <html lang='ru'>
                <head>
                    <meta charset='UTF-8'>
                    <title>Список продуктов</title>
                </head>
                <body>
                    <table>
                        <tr>
                            <th>№</th>
                            <th>Наименование</th>
                            <th>Цена </th>
                            <th>Вес </th>
                            <th>Файл </th>
                            <th>Цена за кг. </th>
                        </tr>
                ''')

                count = 1
                for i in self.data:
                    name = i[0]
                    price = i[1]
                    price_per_kg = str(i[4])
                    ves = i[2]
                    file_name = i[3]
                    file.write(
                        f"<tr>"
                            f"<td>{count}</td>"
                            f"<td>{name}</td>"
                            f"<td>{price}</td>"
                            f"<td>{ves}</td>"
                            f"<td>{file_name}</td>"
                            f"<td>{price_per_kg}</td>"
                        f"</tr>"
                    )
                    count += 1
                file.write('''
                    </table>
                </body>
                </html>
                ''')
            print(f"HTML файл успешно создан: {output_file_path}")
        else:
            print("Нет данных для экспорта в HTML файл.")


    def find_text(self, text):
        pass


print("          Анализатор прайс-листов")
while True:
    print()
    file_path = input('Введите путь для импорта данных, по умолчанию используем текущую папку /data ('
                      'для выхода нажимите /) :')
    if file_path == "/":
        break
    if len(file_path) == 0:
        file_path = os.getcwd() + '\data\\'  # путь по умолчанию в папке проекта
    if os.path.exists(file_path) == False:
        input("Такой каталог не доступен, нажмите Enter для продолжения")
        print()
    else:
        print(f"Данные берем из этого каталога : {file_path}")
        pm = PriceMachine()
        print(pm.load_prices(file_path))
        pm.export_to_html()

#    Логика работы программы
'''
print('the end')
print(pm.export_to_html())

'''
