"""
Ejercicio 4: Sistema de Reportes Empresariales
Objetivo: Separar cálculo y formato.

Una empresa genera reportes en:
- PDF
- Excel
- CSV
- HTML


Tarea crear un diseño que:
- Permita agregar nuevos formatos sin modificar el generador principal.
- Separe el cálculo de datos del formato de salida.


Actividades:
- Clase que genera datos.
- Interfaces para formatos.

Implementaciones:
- PDF
- CSV

Principios aplicados:
- S – Single Responsibility
- O – Open/Closed
- L – Liskov Substitution

"""

from abc import ABC, abstractmethod
import random


class ReporteDatos:

    def obtener_datos(self):
        # Simular cálculos empresariales con valores aleatorios
        ventas_producto_a = random.randint(5000, 15000)
        ventas_producto_b = random.randint(3000, 10000)
        ventas_producto_c = random.randint(2000, 8000)
        ventas_totales = ventas_producto_a + ventas_producto_b + ventas_producto_c
        
        costos_operativos = random.randint(2000, 5000)
        costos_marketing = random.randint(1000, 3000)
        costos_logistica = random.randint(800, 2500)
        gastos_totales = costos_operativos + costos_marketing + costos_logistica
        
        utilidad_bruta = ventas_totales - gastos_totales
        impuestos = int(utilidad_bruta * 0.15)
        utilidad_neta = utilidad_bruta - impuestos
        
        clientes_nuevos = random.randint(50, 200)
        clientes_recurrentes = random.randint(100, 500)
        clientes_totales = clientes_nuevos + clientes_recurrentes
        
        return {
            "ventas_producto_a": ventas_producto_a,
            "ventas_producto_b": ventas_producto_b,
            "ventas_producto_c": ventas_producto_c,
            "ventas_totales": ventas_totales,
            "costos_operativos": costos_operativos,
            "costos_marketing": costos_marketing,
            "costos_logistica": costos_logistica,
            "gastos_totales": gastos_totales,
            "utilidad_bruta": utilidad_bruta,
            "impuestos": impuestos,
            "utilidad_neta": utilidad_neta,
            "clientes_nuevos": clientes_nuevos,
            "clientes_recurrentes": clientes_recurrentes,
            "clientes_totales": clientes_totales
        }

class ReporteFormatter(ABC):

    @abstractmethod
    def formatear(self, datos: dict):
        pass

class ReportePDF(ReporteFormatter):

    def formatear(self, datos):
        print("Generando reporte en PDF")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")

class ReporteCSV(ReporteFormatter):

    def formatear(self, datos):
        print("Generando reporte en CSV")
        print(",".join(datos.keys()))
        print(",".join(str(v) for v in datos.values()))

#Clase principal
class GeneradorReporte:

    def __init__(self, proveedor_datos: ReporteDatos, formatter: ReporteFormatter):
        self.proveedor_datos = proveedor_datos
        self.formatter = formatter

    def generar(self):
        datos = self.proveedor_datos.obtener_datos()
        self.formatter.formatear(datos)


datos = ReporteDatos()

reporte = GeneradorReporte(
    proveedor_datos=datos,
    formatter=ReportePDF()
)

reporte.generar()
