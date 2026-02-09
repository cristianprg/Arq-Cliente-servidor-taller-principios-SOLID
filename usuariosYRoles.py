"""
Ejercicio 5: Sistema de Gestión de Usuarios y Roles

Objetivo: Extender roles sin romper el sistema.

Un sistema tiene:
- Usuarios administradores
- Usuarios clientes
- Usuarios invitados

Cada uno tiene permisos distintos.


Tarea diseñar un sistema que:
- Permita extender nuevos roles sin romper los existentes.
- Evite clases gigantes con métodos que algunos roles no usan.

Actividades:
- Interfaz UserRole.
- Implementar Admin, Cliente, Invitado.
- Usar polimorfismo

Principios aplicados:
- I – Interface Segregation
- L – Liskov Substitution
- O – Open/Closed

"""

from abc import ABC, abstractmethod #El uso de ABS para las clases abstratas obliga a implementar lso metodos definidos en ellas


class PermisoVisualizacion(ABC):
    @abstractmethod
    def ver_contenido(self):
        pass

class PermisoCompra(ABC):
    @abstractmethod
    def comprar(self):
        pass

class PermisoAdministrativo(ABC):
    @abstractmethod
    def crear_usuario(self):
        pass

    @abstractmethod
    def eliminar_usuario(self):
        pass

class UserRole(ABC):
    @abstractmethod
    def descripcion(self):
        pass

#Implementaciones de roles
#Admin
class Admin(UserRole, PermisoVisualizacion, PermisoAdministrativo):
    
    contenidos_admin = [
        "Dashboard principal",
        "Reportes de ventas",
        "Configuración del sistema",
        "Gestión de usuarios"
    ]
    
    nuevo_usuario = {
        "username": "juan.perez",
        "rol": "Cliente",
        "email": "juan.perez@empresa.com"
    }
    
    usuario_a_eliminar = {
        "username": "usuario.inactivo",
        "motivo": "Cuenta inactiva por más de 6 meses"
    }

    def descripcion(self):
        return "Administrador del sistema"

    def ver_contenido(self):
        print(f"Admin viendo contenido: {', '.join(self.contenidos_admin)}")

    def crear_usuario(self):
        print(f"Admin creando usuario: Nuevo usuario '{self.nuevo_usuario['username']}', Rol: {self.nuevo_usuario['rol']}, Email: {self.nuevo_usuario['email']}")

    def eliminar_usuario(self):
        print(f"Admin eliminando usuario: Usuario '{self.usuario_a_eliminar['username']}' ha sido eliminado del sistema - {self.usuario_a_eliminar['motivo']}")


#Cliente
class Cliente(UserRole, PermisoVisualizacion, PermisoCompra):
    
    contenidos_cliente = [
        "Catálogo de productos",
        "Historial de compras",
        "Ofertas especiales",
        "Mi perfil"
    ]
    
    compra_actual = {
        "producto": "Laptop HP 15",
        "cantidad": 1,
        "total": 850.00,
        "metodo_pago": "Tarjeta de crédito"
    }

    def descripcion(self):
        return "Cliente del sistema"

    def ver_contenido(self):
        print(f"Cliente viendo contenido: {', '.join(self.contenidos_cliente)}")

    def comprar(self):
        print(f"Cliente realizando compra: Producto '{self.compra_actual['producto']}', Cantidad: {self.compra_actual['cantidad']}, Total: ${self.compra_actual['total']:.2f}, Método de pago: {self.compra_actual['metodo_pago']}")

#Invitado
class Invitado(UserRole, PermisoVisualizacion):
    
    contenidos_invitado = [
        "Página de inicio",
        "Productos destacados (sin precios)",
        "Sobre nosotros"
    ]

    def descripcion(self):
        return "Usuario invitado"

    def ver_contenido(self):
        print(f"Invitado viendo contenido limitado: {', '.join(self.contenidos_invitado)}")

#Ejemplo polimorfismo
def mostrar_contenido(usuario: PermisoVisualizacion):
    usuario.ver_contenido()

admin = Admin()
cliente = Cliente()
invitado = Invitado()

usuarios = [admin, cliente, invitado]

for u in usuarios:
    print(u.descripcion())
    u.ver_contenido()
