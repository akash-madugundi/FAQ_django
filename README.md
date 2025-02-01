# Multilingual FAQ System with Django, Redis, and Docker

This project is a **Multilingual FAQ System** built with Django and Django REST Framework. It supports dynamic translation of FAQs using **python googletrans**, content management with **django-ckeditor**, and caching with **Redis** for improved performance. The application is **containerized using Docker** for easy deployment and management of dependencies.

---

## Features
- **Multilingual Support**: Dynamic translation of FAQs based on the `lang` query parameter.
- **Rich Text Editing**: Integrated **django-ckeditor** for enhanced FAQ content formatting.
- **Caching with Redis**: Efficient caching using Redis to speed up API responses.
- **Dockerized**: Easy deployment using Docker for both Django and Redis.
- **PEP8**: Followed PEP8 compliance and modularity.

---

## Prerequisites
- Python 3.10+
- Docker & Docker Compose

---

## Installation

#### Clone the Repository
```bash
git clone <repository-url>
cd FAQ-django
```

#### Running the Project with Docker (Recommended)
```bash
docker-compose up --build
```
- Open Command Prompt to run API calls (specified in API examples).
- To stop the container, use:
```bash
docker-compose down
```

---

## API Examples
### 1. Retrieving FAQs
  #### Using Command Prompt
  - For English FAQs (default): 
    ```bash
    curl http://localhost:8000/api/faqs/
    ```
  - For Hindi FAQs: 
    ```bash
    curl http://localhost:8000/api/faqs/?lang=hi
    ```
  - For French FAQs:
    ```bash
    curl http://localhost:8000/api/faqs/?lang=fr
    ```
  - For Telugu FAQs: 
    ```bash
    curl http://localhost:8000/api/faqs/?lang=te
    ```
  - For Undefined Language (defaults to English): 
    ```bash
    curl http://localhost:8000/api/faqs/?lang=xyz
    ```
  #### Using Postman
  - GET Request for Telugu FAQs:  
    ```
    http://localhost:8000/api/faqs/?lang=te
    ```
    ##### NOTE:
    - **Predefined Languages:** `hi` (Hindi), `bn` (Bengali), `fr` (French)  
      *Retrieving FAQs in these languages is faster than others.*

### 2. Creating FAQs [extra feature]
  #### Using Command Prompt
  - Change `question` and `answer` in tags
    ```bash
    curl -X POST http://localhost:8000/api/faqs/create/ -H "Content-Type: application/json" -d "{\"question\": \"What is the capital of India?\", \"answer\": \"New Delhi\"}"
    ```
  #### Using Postman
  - Goto Body -> Select raw -> Attach question and answer using key-value in JSON format, then run this command-
    ```bash
    http://localhost:8000/api/faqs/create/
    ```

##### NOTE:
  - **Alternative URL:**  
      If `localhost` doesn’t work, use:  
      ```
      http://127.0.0.1:8000/api/faqs/
      ```
      
---

## Admin Interface
  - Access the Django admin panel at `http://localhost:8000/admin/` using the superuser credentials
    - Username: *akash*
    - Password: *12345*

---

## Running Tests
  - Goto *settings.py* in **faq** folder, update `CACHES` to- (since testing is done locally)
    ```bash
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': "redis://localhost:6379/1",       ## for testing tests folder locally
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
        }
    }
    ```
  - Then, run-
    ```bash
    pytest
    ```

---

## Technologies Used
  - **Backend**: Django, Django REST Framework
  - **Translation**: googletrans
  - **Database**: Uses SQLite by default
  - **Cache**: Redis
  - **Containerization**: Docker, Docker Compose

---

## License
  - This project is licensed under the MIT License
