# Máquina Tragamonedas

Este programa es una simulación de una máquina tragamonedas, cuyos tiros se almacenarán para un posterior análisis de datos.

## Especificación

Se deberá crear un programa en Python que simule el comportamiento de una máquina tragamonedas con 3 slots, y valores aleatorios entre 1 y 6.
Al iniciar el programa, se deberán mostrar todos los slots en 0, con el texto `¡Haga su primer tiro!` en color azul claro, y un boton con el texto `Tirar`.
Al hacer click en tirar, se deben generar numeros aleatorios del 1 al 6 en cada slot, si todos coinciden el usuario ganó y se deberá mostrar el texto `¡Usted ganó!` en color verde claro; en su defecto, deberá mostrarse el texto `¡Siga participando!` en color azul claro.
Cada tiro, deberá almacenarse en un archivo en formato [CSV](https://es.wikipedia.org/wiki/Valores_separados_por_comas), localizado en el mismo directorio que el programa y con el nombre `shoots.csv`.

## Instalación

### Requisitos

- Git
- Python 3.9 o superior
- Tkinter (según el método de instalación de Python, puede ya estar incluido).

### Pasos

1. Clonar el repositorio.
2. Abrir una terminal en el directorio raíz del repositorio.
3. Ejecutar `python3 src/tragamonedas.py` o `python src/tragamonedas.py` (en caso de tener Python 3 instalado por defecto).

## Manual de Uso

### Leer datos recolectados

Los datos recolectados se almacenarán en el archivo `shoots.csv` (localizado en el mismo directorio que el programa). Éste se creará automáticamente cuando se realice el primer tiro.
Cada tiro se registra en una nueva linea, y cada valor separado por una coma (siguiendo el formato estándar de un archivo [CSV](https://es.wikipedia.org/wiki/Valores_separados_por_comas)).
