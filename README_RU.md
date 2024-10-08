# traffic-generator
 
Этот проект создает Docker-контейнер, который отправляет HTTP-запросы каждые несколько секунд на заданный URL с телом запроса фиксированного размера. Контейнер деплоится как сервис в Kubernetes.

## Функционал

- Отправка HTTP-запросов методом POST на указанный URL.
- Настраиваемый интервал между запросами.
- Настраиваемый размер тела запроса (по умолчанию 100 Кб).
- Возможность задания параметров через переменные окружения.
- Тайм-аут запросов: 5 секунд.

## Переменные окружения

Вы можете настроить поведение контейнера через следующие переменные окружения:

- `REQUEST_URL` — URL, на который отправляются запросы. По умолчанию: `http://example.com`.
- `REQUEST_INTERVAL` — Интервал между запросами в секундах. По умолчанию: `5`.
- `REQUEST_PAYLOAD_SIZE` — Размер тела запроса в байтах. По умолчанию: `102400` (100 Кб).

## Как запустить

```sh
kubectl apply -f Deployment.yaml -n <namespace>
```

Или

```sh
kubectl apply -f https://raw.githubusercontent.com/karpulixdocker/traffic-generator/main/Deployment.yaml -n <namespace>
```
