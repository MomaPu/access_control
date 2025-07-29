# Система управления доступом (RBAC)

## Структура проекта

access_control/
├── accounts/ # Приложение для работы с пользователями
│ ├── models.py # Кастомная модель пользователя
│ ├── serializers.py # Сериализаторы для регистрации/авторизации
│ ├── views.py # ViewSet для работы с пользователями
│ └── ...
│
├── rbac/ # Ядро RBAC системы
│ ├── models.py # Модели: Role, ResourceType, Permission
│ ├── serializers.py # Сериализаторы для моделей RBAC
│ ├── views.py # ViewSet для управления RBAC
│ ├── middleware.py # Middleware для проверки прав
│ └── decorators.py # Декораторы для контроля доступа
│
├── resources/ # Пример защищенного ресурса
│ ├── models.py # Модель Document с кастомными правами
│ ├── serializers.py # Сериализаторы документов
│ └── views.py # ViewSet с проверкой прав доступа
│
├── access_control/ # Основные настройки
│ ├── settings.py # Конфигурация Django
│ ├── urls.py # Главные URL-маршруты
│ └── ...
│
└── manage.py # Скрипт управления Django



## Ключевые компоненты

### 1. Модели данных
- **Пользователи**: Кастомная модель `CustomUser` (наследуется от `AbstractUser`)
- **Роли**: Модель `Role` с набором разрешений
- **Ресурсы**: Модели `ResourceType` и `Document` с системой прав доступа
- **Разрешения**: Модель `AccessPermission` (связь ролей и ресурсов)

### 2. API Endpoints
- **Аутентификация**:
  - `POST /api/auth/register/` - регистрация
  - `POST /api/auth/login/` - авторизация
  - `POST /api/auth/logout/` - выход

- **RBAC управление** (только для админов):
  - `GET /api/rbac/roles/` - список ролей
  - `POST /api/rbac/roles/` - создание роли
  - `GET /api/rbac/permissions/` - список разрешений

- **Документы**:
  - `GET /api/documents/` - список документов (требуется право `document.read`)
  - `POST /api/documents/` - создание (требуется `document.create`)
  - `DELETE /api/documents/{id}/` - удаление (требуется `document.delete`)

### 3. Система проверки прав
1. **Middleware**: Глобальная проверка доступа
2. **Декораторы**: Точечная проверка в ViewSet

