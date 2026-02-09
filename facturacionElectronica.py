"""
Ejercicio 1: Sistema de Facturación Electrónica

- Genere facturas en PDF.
- Envíe facturas por correo.
- Guarde facturas en base de datos.
- Permita cambiar el medio de envío (email, WhatsApp, API).

Diseñar una solución que:
- Separe la generación de la factura del envío y del almacenamiento.
- Permita agregar nuevos métodos de envío sin modificar el código existente.

Actividades Diseñar clases para:
- Generar factura
- Enviar factura
- Guardar factura

Usar interfaces/abstracciones.
Inyectar dependencias.

Principios aplicados:
- S – Single Responsibility
- O – Open/Closed
- D – Dependency Inversion

"""
from abc import ABC, abstractmethod

class Factura:
    def __init__(self, cliente, monto):
        self.cliente = cliente
        self.monto = monto

class GeneradorFactura(ABC):
    @abstractmethod
    def generar(self, factura: Factura):
        pass
    
class GeneradorPDF(GeneradorFactura):
    def generar(self, factura):
        print(f"Generando PDF para {factura.cliente} por ${factura.monto}")
        return "factura.pdf"

class RepositorioFactura(ABC):
    @abstractmethod
    def guardar(self, factura: Factura):
        pass

class RepositorioSQL(RepositorioFactura):
    def guardar(self, factura):
        print(f"Guardando factura de {factura.cliente} en BD")

class CanalEnvio(ABC):
    @abstractmethod
    def enviar(self, archivo, factura: Factura):
        pass

class EnvioEmail(CanalEnvio):
    def enviar(self, archivo, factura):
        print(f"Enviando {archivo} por EMAIL a {factura.cliente}")

class EnvioWhatsApp(CanalEnvio):
    def enviar(self, archivo, factura):
        print(f"Enviando {archivo} por WHATSAPP a {factura.cliente}")

class EnvioAPI(CanalEnvio):
    def enviar(self, archivo, factura):
        print(f"Enviando {archivo} por API externa")

class ServicioFacturacion:
    def __init__(
        self,
        generador: GeneradorFactura,
        repositorio: RepositorioFactura,
        canal_envio: CanalEnvio
    ):
        self.generador = generador
        self.repositorio = repositorio
        self.canal_envio = canal_envio

    def procesar(self, factura: Factura):
        archivo = self.generador.generar(factura)
        self.repositorio.guardar(factura)
        self.canal_envio.enviar(archivo, factura)

factura = Factura("Juan Pérez", 250000)

servicio = ServicioFacturacion(
    generador=GeneradorPDF(),
    repositorio=RepositorioSQL(),
    canal_envio=EnvioWhatsApp()  # Cambia aquí el canal
)

servicio.procesar(factura)

