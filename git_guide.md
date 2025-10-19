## Структура веток
# В проекте используются следующие долгоживущие ветки:

1. 🌟 Main Branch    
Название: main     
Назначение: Основная стабильная ветка. Содержит только проверенный, готовый к продакшену код.    
Правила работы:   
✅ Прямые коммиты ЗАПРЕЩЕНЫ   
✅ Только слияние через Pull Request после ревью    
✅ Всегда должна быть стабильной и рабочей   
✅ Теги версий проставляются только здесь    

2. 🗃️ DB Branch    
Название: db    
Назначение: Работа с миграциями базы данных, изменения схемы, скрипты обновления    
Правила работы:   
✅ Создавать feature-ветки от db для конкретных миграций   
✅ Названия: feature/db/add-user-table, fix/db/foreign-key-constraint   
✅ После готовности - Pull Request в db   
✅ Тестировать миграции на тестовой базе   
✅ Не мержить в main напрямую, только через общий PR  

3. 🧪 Tests Branch  
Название: tests  
Назначение: Разработка и модификация тестов (unit, integration, e2e)  
Правила работы:  
✅ Создавать feature-ветки от tests для новых тест-кейсов   
✅ Названия: feature/tests/user-auth-spec, fix/tests/flaky-test  
✅ Pull Request в tests после готовности  
✅ Убедиться, что все тесты проходят   
✅ Не ломать существующие тест  

4. 🏗️ Layer Branch  
Название:   
Назначение: Разработка слоев приложения (controller, service, repository)   
Правила работы:  
✅ Создавать feature-ветки от Layer для конкретных компонентов  
✅ Названия: feature/layer/user-controller, fix/layer/service-logic  
✅ Следовать принципам слоистой архитектуры   
✅ Pull Request в Layer после готовности  

5. ⚡ Service Branch  
Название: Service    
Назначение: Бизнес-логика, сервисный слой, интеграции с внешними API   
Правила работы:     
✅ Создавать feature-ветки от Service для конкретных сервисов   
✅ Названия: feature/service/payment-processing, fix/service/email-notification   
✅ Pull Request в Service после готовности   
✅ Тестировать бизнес-логику   

# 🚀 Стандартный процесс разработки

1. Начало работы над задачей      
- Переключиться на соответствующую ветку и обновить её   
git checkout [branch-name]  # db/tests/Layer/Service   
git pull origin [branch-name]   

- Создать feature-ветку    
git checkout -b feature/[component]/[short-description]   
Пример: git checkout -b feature/db/add-user-profile-table   

2. Ежедневная работа
- Делать коммиты   
git add .   
git commit -m "feat: add user profile table migration"   
git commit -m "fix: resolve foreign key constraint issue"   

- Регулярно пушить   
git push origin feature/[branch-name]   

3. Завершение задачи
Создать Pull Request из своей feature-ветки в соответствующую родительскую ветку
Пройти код-ревью
Исправить замечания (дополнительные коммиты)
После апрува - выполнить merge

4. После мержа  
- Удалить локальную feature-ветку    
git branch -d feature/[branch-name]   

- Удалить ветку на remote   
git push origin --delete feature/[branch-name]   

- Вернуться к родительской ветке и обновиться   
git checkout [parent-branch]   
git pull origin [parent-branch]   

🔄 Процесс интеграции в Main   
Когда функциональность в одной из веток (db, tests, Layer, Service) готова к выпуску:    
Провести интеграционное тестирование    
Получить approve от тимлида    
Выполнить мерж в main    
Создать тег версии    

📝 Convention Commits   
Используйте понятные сообщения коммитов:   
feat: - новая функциональность   
fix: - исправление ошибки   
docs: - изменения в документации   
test: - добавление или исправление тестов   
refactor: - рефакторинг кода   
style: - исправление форматирования   

Пример:   
git commit -m "feat(db): add user profile table with indexes"   
git commit -m "fix(service): handle null values in payment processing"   

После того, как вы сделали push, перейдите в github, 
❗ Важные правила   
Не коммитить напрямую в основные ветки   
Всегда создавать feature-ветки для новой работы   
Перед созданием PR обновлять свою ветку из родительской   
Не забывать удалять отработанные feature-ветки   
Перед мержем в main убедиться, что все тесты проходят   
Этот workflow обеспечит порядок в разработке и минимизирует конфликты! 🎯   