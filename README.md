# Máquina Tragamonedas

Este programa es una simulación de una máquina tragamonedas, cuyos tiros se almacenarán para un posterior análisis de datos.

## Índice

- [Máquina Tragamonedas](#máquina-tragamonedas)
  - [Índice](#índice)
  - [Especificación](#especificación)
  - [Instalación](#instalación)
    - [Requisitos](#requisitos)
    - [Pasos](#pasos)
  - [Manual de Uso](#manual-de-uso)
    - [Leer datos recolectados](#leer-datos-recolectados)

## Especificación

Se deberá crear un programa en Python que simule el comportamiento de una máquina tragamonedas con 3 slots, y valores aleatorios entre 1 y 6.
Al iniciar el programa, se deberán mostrar todos los slots en 0, con el texto `¡Haga su primer tiro!` en color azul claro, y un boton con el texto `Tirar`.
El usuario podrá visualizar un sistema de apuesta, con el cual deberá interactuar.
En primer lugar, contaremos con una casilla donde el usuario indicará el monto a ingresar, para así luego introducirlo presionando el botón `depositar`.
Una vez depositado, el usuario será capaz de ver la cantidad de dinero disponible en el apartado de `balance`. A la hora de apostar, abrá otro casillero donde el usuario deberá ingresar un monto con el cual poder apostar.
Este tendrá que ser mayor que 0 y que no supere lo disponible en el balance.
Al hacer click en tirar, se deben generar numeros aleatorios del 1 al 6 en cada slot. En caso de que todos coincidan, se mostrará el texto `¡Usted ganó!` en color verde claro; El usuario será el ganador, por ende, será recompensado con un multiplicador de x5 hacia la apuesta anteriormente introducida. En su defecto, deberá mostrarse el texto `¡Siga participando!` en color azul claro, y el usuario perderá su apuesta.
Cada tiro, deberá almacenarse en un archivo en formato [CSV](https://es.wikipedia.org/wiki/Valores_separados_por_comas), localizado en el mismo directorio que el programa y con el nombre `shoots.csv`.

## Instalación

### Requisitos

- Git
- Python 3.9 o superior
- Tkinter (según el método de instalación de Python, puede ya estar incluido).

### Pasos

1. Clonar el repositorio.
2. Abrir una terminal en el directorio raíz del repositorio.
3. Ejecutar `python3 tragamonedas.py` o `python tragamonedas.py` (en caso de tener Python 3 instalado por defecto).

## Manual de Uso

1. Una vez ejecutado el programa, escoja un monto a ingresar y presione el botón "depositar".
2. Luego de haber depositado, podra empezar a jugar, eligiendo la cantidad de dinero que se pondrá a juego.
3. En caso de que no desee continuar, el usuario podrá retirar el total de su balance dándole click a "retirar".

### Leer datos recolectados

Los datos recolectados se almacenarán en el archivo `shoots.csv` (localizado en el mismo directorio que el programa). Éste se creará automáticamente cuando se realice el primer tiro.
Cada tiro se registra en una nueva linea, y cada valor separado por una coma (siguiendo el formato estándar de un archivo [CSV](https://es.wikipedia.org/wiki/Valores_separados_por_comas)).
