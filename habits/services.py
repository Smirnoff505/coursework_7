import requests

from config import settings


class MyTelegramBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    def send_message(self, telega_chat_id, text):
        """Метод отправки сообщения в телеграмм"""

        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'telega_chat_id': telega_chat_id,
                'text': text,
            }
        )


def my_bot_send_message(telega_chat_id, text):
    """Метод отправки сообщения в телеграмм"""

    url = 'https://api.telegram.org/bot'
    token = settings.TELEGRAM_TOKEN

    requests.post(
        url=f'{url}{token}/sendMessage',
        data={
            'chat_id': telega_chat_id,
            'text': f'Через 10 минут не забудьте выполнить {text}',
        }
    )
