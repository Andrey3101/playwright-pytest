# Автотесты 7pay

## Структура проекта
    .
    ├── components          # объектные модели компонентов, использующихся на страницах
    ├── fixtures            # фикстуры
    ├── pages               # объектные модели страниц
    ├── tests               # тесты                  
    |
    ├── reports             # файлы с отчётами о результатах
    └── traces              # трэйсы неуспешных тестов

> просмотреть трейсы можно командой `playwright show-trace ./traces/xxx.zip` или в браузере [trace.playwright.dev](https://trace.playwright.dev)
## Запуск локально

1. Перейти в корневую директорию проекта 
1. Установить зависимости
```pip install --no-cache-dir -r requirements.txt```
1. Запустить тесты
```pytest ./tests --stage=dev```

### запуск одного теста
```pytest ./tests/merchantinvoice.py --stage=dev```

### запуск с генерацией отчёта в формате JUnit
```pytest ./tests/merchantinvoice.py --stage=dev --junitxml=./reports/test-report.xml```
отчёт будет помещён в директорию `./reports`