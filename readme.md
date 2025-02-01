# **Footer test elements**

Автотест проверяет наличие футера и нескольких элементов в нем на сайте  https://only.digital/.
А именно:
- Футер на странице.
- Логотип
- Социальные сети
- Telegram для связи
- Кнопки

## Стек

- Python 3
- WebDriver Manager
- Selenium WebDriver
- unittest

## Установка
1. Клонируйте репозиторий:
`git clone https://github.com/helloGalina/only_tests_footer.git
cd footer-elements-test`

2. Установите необходимые зависимости:
`pip install -r requirements.txt`

3. Запуск теста:
`python -m unittest test_footer.py`
Тест откроет браузер с помощью ChromeDriver, проверит элементы футера и выведет результаты в консоль.

## Описание теста

### Инициализация драйвера:

В методе setUp инициализируется драйвер Chrome с помощью webdriver.Chrome() и менеджера драйверов ChromeDriverManager.

### Поиск элементов:

#### Футер: Поиск по тегу footer.

#### _Логотип_: Поиск по классу Footer_logo__2QEhf.

#### _Социальные сети:_ Поиск по классу Socials_socialsWrap__DPtp_.

#### _Telegram для связи:_ Поиск по классу TelegramAlternative_root__7q06_.

#### _Кнопки_: Находятся все элементы с тегом button. Тест выводит количество найденных кнопок и текст каждой из них.

#### _Закрытие драйвера:_ После выполнения теста браузер закрывается методом tearDown.

##### _Пример вывода_

При успешном прохождении теста в консоли будет выведен следующий вывод:
``Футер найден!
Логотип найден!
Социальные сети найдены!
Telegram для связи найден!
Найдено 10 кнопок в футере:
Кнопка 1: Название кнопки 1
Кнопка 2: Название кнопки 2
...```
...