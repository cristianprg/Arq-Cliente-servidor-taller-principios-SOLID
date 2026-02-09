"""
Ejercicio 3: Sistema de Notificaciones Multicanal
Objetivo: Hacer intercambiables los canales de notificación.

Una app debe enviar notificaciones por:
- Email
- SMS
- Push notifications
- Slack

Tarea diseñar una arquitectura donde:
- Cada tipo de notificación sea intercambiable.
- El sistema central no dependa de clases concretas.

Actividades:
- Crear interfaz Notifier.
- Implementar Email, SMS, Push.
- Usar inyección de dependencias.

Principios aplicados
- I – Interface Segregation
- D – Dependency Inversion
- S – Single Responsibility

"""

from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):

    def send(self, message: str):
        print(f"Enviando EMAIL: {message}")

class SMSNotifier(Notifier):

    def send(self, message: str):
        print(f"Enviando SMS: {message}")

class PushNotifier(Notifier):

    def send(self, message: str):
        print(f"Enviando PUSH: {message}")

class SlackNotifier(Notifier):

    def send(self, message: str):
        print(f"Enviando SLACK: {message}")

# Servicio de notificaciones que usa inyección de dependencias
class NotificationService:

    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)


service = NotificationService(EmailNotifier())
service.notify("Bienvenido al sistema")
