# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 10:10:34 2025

@author: OPMIKE
"""

import time

# Definimos los estados
estados = ["rojo", "verde", "amarillo"]
tiempos = {"rojo": 5, "verde": 5, "amarillo": 2}

estado_actual = "rojo"

while True:
    print(f"Semáforo en {estado_actual}")
    time.sleep(tiempos[estado_actual])  # Espera según el estado
    
    # Cambiar al siguiente estado
    if estado_actual == "rojo":
        estado_actual = "verde"
    elif estado_actual == "verde":
        estado_actual = "amarillo"
    elif estado_actual == "amarillo":
        estado_actual = "rojo"