import requests

'''
Выведите в консоль категории товаров, представленных на https://fakestoreapi.com.
Запросите у пользователя, товары какой категории он желает просмотреть.
Выведите информацию о соответствующих товарах в отформатированном для чтения виде в консоль.
'''
#Выведем имеющиеся категории
print('На сайте представлены следующие категории товаров:')
url_category='https://fakestoreapi.com/products/categories'
category_info=requests.get(url_category).json()
for i in range(0,len(category_info)):
    print(category_info[i])
#Запрашиваем у пользователя категорию
user_input=input('Товары какой категории вы желаете просмотреть: ')
#Формируем URL для запроса
url_prodacts='https://fakestoreapi.com/products'
# Отправляем GET-запрос
# Получаем ответ в формате JSON
prodacts_info=requests.get(url_prodacts).json()
found=False
for i in prodacts_info:
    if i["category"]==user_input:
        found=True
        # Выводим информацию в удобном виде
        print(f'Идентификатор: {i["id"]}')
        print(f'Категория: {i["category"]}')
        print(f'Название: {i["title"]}')
        print(f'Цена: {i["price"]}')
        print(f'Описание {i["description"]}')
        print(f'Изображение: {i["image"]}')
        print(f'Рейтинг: {i["rating"]["rate"]}, Количество оценок: {i["rating"]["count"]}\n')

if not found:
    print('Такой категории нет')