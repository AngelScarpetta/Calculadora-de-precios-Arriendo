# Calculadora de Precios de Arriendo

Este proyecto es una calculadora desarrollada en **Python** que permite a los usuarios calcular el precio de arriendo incluyendo componentes como el **4x1000**, el **IVA** y otros costos adicionales. Es ideal para gestionar costos financieros y simplificar cálculos relacionados con el arriendo de bienes o servicios.

---

## Características

- **Descuento inicial:** Aplica automáticamente un descuento del 5% al precio base del arriendo.
- **Cálculo del IVA:** Calcula automáticamente el IVA (19% por defecto) a partir del precio base ajustado y los costos adicionales.
- **Cálculo del 4x1000:** Incluye opcionalmente el cálculo del impuesto financiero del 4x1000.
- **Costos adicionales:** Permite agregar otros costos o tarifas personalizadas.
- **Resumen detallado:** Muestra un desglose claro del cálculo total.
- **Interfaz de usuario simple:** Ejecutable desde la terminal o línea de comandos.

---

## Requisitos

Para ejecutar este proyecto necesitas:

- **Python 3.7 o superior**
- Biblioteca estándar de Python (no se necesitan paquetes externos)

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/AngelScarpetta2004/Calculadora-de-precios-Arriendo.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd Calculadora-de-precios-Arriendo
   ```

3. Ejecuta el script:
   ```bash
   python calculadora.py
   ```

---

## Uso

1. Ingresa el precio base de la casa o propiedad.
2. Agrega los costos adicionales cuando se solicite (puedes especificar múltiples costos).
3. Obtén el cálculo total, con un desglose que incluye el precio base con descuento, IVA, 4x1000 (si aplica) y los costos adicionales.

### Ejemplo de uso interactivo:

Al ejecutar el script, el programa solicitará la siguiente información:

- **Precio base de la casa:** Ingresa el valor inicial del arriendo.
- **Costos adicionales:** Especifica los costos extra, como mantenimiento o servicios. Ingresa "fin" cuando termines de agregar costos.

### Salida esperada:

Si el precio base es **$1,000,000**, con costos adicionales de **$50,000**, el cálculo será:

- Precio base con descuento (5%): $950,000
- Costo de adicionales: $50,000
- Valor imponible: $1,000,000
- IVA (19%): $190,000
- Precio total sin 4x1000: $1,190,000
- 4x1000 (0.4%): $4,000
- **Precio total con 4x1000:** $1,194,000

---

## Código Principal

El archivo principal es [`calculadora.py`](https://github.com/AngelScarpetta2004/Calculadora-de-precios-Arriendo/blob/main/calculadora.py), que incluye las funciones necesarias para realizar los cálculos. Puedes personalizar las tasas y agregar nuevos componentes según tus necesidades.

---

## Contribución

Si deseas contribuir:

1. Realiza un fork del repositorio.
2. Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Envía un pull request con tus mejoras.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.

---

## Autor

Desarrollado por [Angel Scarpetta](https://github.com/AngelScarpetta2004).

---

## Futuras Mejoras

- Integración con una interfaz gráfica (GUI).
- Cálculo automatizado para múltiples monedas.
- Generación de reportes en PDF o Excel.
