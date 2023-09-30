from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Robot
from orders.models import Order
from django.conf import settings

@receiver(post_save, sender=Robot)
def notify_customer_when_robot_available(sender, instance, created, **kwargs):
    if created:
        # Робот был создан, проверяем наличие заказов на эту модель и версию робота
        orders = Order.objects.filter(robot_serial=instance.model)

        if orders:
            for order in orders:
                customer = order.customer
                subject = 'Робот доступен'
                message = f'Добрый день!\nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.'
                from_email = 'nikitaI7@yandex.ru'
                recipient_list = [customer.email]

                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
