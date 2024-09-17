import requests

def get_exchange_rate():
    # Используем ваш API ключ для Exchange Rate API
    api_key = 'b7260cebf25a0b552052653c'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    
    # Выполняем запрос к API для получения актуальных курсов
    response = requests.get(url)
    data = response.json()
    
    # Проверяем успешность запроса и наличие данных
    if response.status_code == 200 and 'conversion_rates' in data:
        # Получаем курс рубля к доллару
        rub_to_usd = data['conversion_rates']['RUB']
        return rub_to_usd
    else:
        print("Ошибка при получении курса валют")
        return None

print("Конвертер валют")

# Получаем актуальный курс рубля к доллару
ExRate = get_exchange_rate()

if ExRate:  # Проверяем, удалось ли получить курс валют
    print(f"Актуальный курс рубля к доллару: {ExRate}")
    
    # Запрашиваем сумму в рублях
    r = float(input("Введите сумму в рублях: "))
    ex = r / ExRate  # Расчет эквивалента в долларах
    
    # Округляем до 2 знаков после запятой
    ex = round(ex, 2)
    
    print("Эквивалент в USD: " + str(ex))
else:
    print("Не удалось получить курс валют.")