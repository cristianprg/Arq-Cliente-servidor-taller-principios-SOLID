"""
Ejercicio 2: Plataforma de Pagos con Múltiples Pasarelas Contexto
Objetivo: Permitir múltiples pasarelas sin cambiar la lógica principal.

Un e-commerce debe permitir pagos con:
- Tarjeta de crédito
- PayPal
- Transferencia bancaria
- Criptomonedas (futuro)

Tarea Implementa un diseño que:
- Permita agregar nuevas pasarelas sin tocar la lógica principal.
- Use abstracciones para manejar los pagos.

Actividades:
- Crear una interfaz PaymentMethod.
- Implementar varios métodos.
- Usar una clase PaymentProcessor.

Principios aplicados:
- O – Open/Closed
- L – Liskov Substitution
- D – Dependency Inversion

"""

from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Procesando pago de ${amount} con tarjeta de crédito")

class PayPalPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Procesando pago de ${amount} con PayPal")

class BankTransferPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Procesando transferencia bancaria por ${amount}")

class CryptoPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Procesando pago en criptomonedas por ${amount}")

#logica principal
class PaymentProcessor:

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount: float):
        print("Iniciando proceso de pago...")
        self.payment_method.pay(amount)
        print("Pago finalizado.")

processor = PaymentProcessor(CreditCardPayment())
processor.process(200)
