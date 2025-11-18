# Práctica 17: Herencia y Tipos de Métodos (OOP Avanzado)

Este directorio contiene la Práctica 17, enfocada en profundizar en los conceptos de Programación Orientada a Objetos (OOP), específicamente en la **Herencia** y los diferentes tipos de métodos en Python.

## 🎯 Objetivos

* Distinguir y aplicar **Métodos de Instancia** (`self`), **Métodos de Clase** (`@classmethod`) y **Métodos Estáticos** (`@staticmethod`).
* Implementar **Herencia Simple** para crear jerarquías de clases lógicas.
* Utilizar `super()` para extender la funcionalidad de las clases padre.
* Aplicar **Polimorfismo** mediante la sobrescritura de métodos.

## 🗂️ Contenido

* **[TUTORIAL.md](./TUTORIAL.md)**: Guion con los enunciados de los ejercicios (Videojuegos, Academia, Logística, Streaming).
* **[practica_17.py](./practica_17.py)**: Código fuente con la solución a todos los ejercicios.

## 🧠 Conceptos Clave Implementados

### 1. Tipos de Métodos (Ej. 5 - Academia)
* **Instancia:** Acceden a datos del objeto individual (ej. `mostrar_perfil`).
* **Clase:** Acceden a variables compartidas por toda la clase (ej. `cambiar_cuota`).
* **Estáticos:** Funciones utilitarias que no dependen ni de la instancia ni de la clase (ej. `validar_nivel`).

### 2. Herencia y `super()` (Ej. 6 - Logística)
Se creó una clase base `Paquete` y clases hijas `PaqueteFragil` y `PaqueteExpress`.
* Se utilizó `super().__init__(...)` para reutilizar el constructor del padre.
* Se sobrescribió el método `calcular_costo_base()` para alterar el comportamiento según el tipo de paquete.

### 3. Polimorfismo (Ej. 7 - Streaming)
Diferentes clases (`PlanBasico`, `PlanPremium`) responden al mismo método (`calcular_precio`) de manera diferente, permitiendo tratar a todos los planes de forma uniforme pero con lógica específica.