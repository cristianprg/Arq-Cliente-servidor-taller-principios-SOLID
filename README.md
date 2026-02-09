# Arq-Cliente-servidor-taller-principios-SOLID

📦 Sistemas Empresariales aplicando Principios SOLID


📚 Ejercicios Incluidos
1️⃣ Plataforma de Pagos con Múltiples Pasarelas

Sistema que permite procesar pagos mediante:

Tarjeta de crédito

PayPal

Transferencia bancaria

(Extensible a criptomonedas)

Principios aplicados:

Open/Closed

Liskov Substitution

Dependency Inversion



2️⃣ Sistema de Notificaciones Multicanal

Envío de notificaciones por:

Email

SMS

Push Notifications

Slack

Se diseñó una arquitectura desacoplada usando inyección de dependencias.

Principios aplicados:

Single Responsibility

Interface Segregation

Dependency Inversion



3️⃣ Sistema de Reportes Empresariales

Generación de reportes en:

PDF

CSV

(Extensible a Excel, HTML, etc.)

Se separó la lógica de cálculo de la lógica de presentación.

Principios aplicados:

Single Responsibility

Open/Closed

Liskov Substitution



4️⃣ Sistema de Gestión de Usuarios y Roles

Gestión de:

Administradores

Clientes

Invitados

(Extensible a nuevos roles)

Uso de polimorfismo e interfaces segregadas.

Principios aplicados:

Interface Segregation

Liskov Substitution

Open/Closed



5️⃣ Sistema de Facturación Electrónica

Sistema que:

Genera facturas en PDF

Envía facturas por distintos canales

Guarda facturas en base de datos

Arquitectura desacoplada que permite agregar nuevos canales sin modificar la lógica principal.

Principios aplicados:

Single Responsibility

Open/Closed

Dependency Inversion


🛠 Tecnologías

Python 3

abc (Abstract Base Classes)

Programación Orientada a Objetos


🚀 Cómo ejecutar

Clona el repositorio:

git clone <url-del-repo>


Ejecuta el archivo del ejercicio correspondiente:

python nombre_archivo.py
