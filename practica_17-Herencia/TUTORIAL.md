# Práctica 17: Herencia y Tipos de Métodos (OOP Avanzado)

Esta práctica profundiza en la Programación Orientada a Objetos, introduciendo la **Herencia**, la **Sobrescritura de métodos** y la distinción entre métodos de instancia, de clase y estáticos.

---

## Ejercicio 4: Creando tu Primera Clase con Métodos de Instancia

Estás desarrollando un sistema para una tienda de videojuegos que necesita gestionar su inventario. Crea una clase llamada `Videojuego`.

**Atributos de instancia:**
* `titulo`: Nombre del videojuegos.
* `plataforma`: Consola o sistema (PS5, Xbox, PC, etc.).
* `precio`: Precio en euros.
* `unidades`: Cantidad disponible en stock.

**Métodos de instancia:**
* `mostrar_detalle()`: Muestra toda la información del videojuego.
* `aplicar_descuento(porcentaje)`: Reduce el precio según el porcentaje dado.
* `vender(cantidad)`: Reduce las unidades disponibles. Si no hay suficientes, muestra error.

---

## Ejercicio 5: Métodos de Instancia, Clase y Estáticos

Una academia de idiomas necesita un sistema para gestionar sus estudiantes. Crea una clase `Estudiante`.

**Atributos:**
* **De Clase:**
    * `total_estudiantes`: Contador que se incrementa al crear un estudiante.
    * `cuota_mensual`: Precio fijo de 120€ para todos.
* **De Instancia:**
    * `nombre`, `idioma`, `nivel` (A1, A2, B1, B2, C1, C2).

**Métodos:**
1.  **Instancia:** `mostrar_perfil()`: Muestra la info del estudiante.
2.  **Clase (`@classmethod`):** `mostrar_estadisticas()`: Muestra el total de estudiantes y la cuota actual.
3.  **Clase (`@classmethod`):** `cambiar_cuota(nueva_cuota)`: Modifica la cuota para todos.
4.  **Estático (`@staticmethod`):** `validar_nivel(nivel)`: Verifica si el nivel es válido (A1-C2). Retorna `True`/`False`.

> **Nota:** Recuerda que los métodos de clase reciben `cls` y los estáticos no reciben ni `self` ni `cls`.

---

## Ejercicio 6: Herencia Simple - Creando Jerarquías

Una empresa de logística necesita gestionar paquetes. Crea una jerarquía de clases.



[Image of diagram of inheritance in object oriented programming]


### Clase Padre: `Paquete`
* **Atributos:** `id_seguimiento`, `peso_kg`, `origen`, `destino`.
* **Métodos:**
    * `mostrar_info()`: Muestra información básica.
    * `calcular_costo_base()`: Retorna `peso_kg * 2.5`.

### Clase Hija: `PaqueteFragil` (Hereda de `Paquete`)
* **Atributo adicional:** `seguro` (booleano).
* **Constructor:** Usa `super().__init__()` para inicializar al padre.
* **Sobrescritura:** `calcular_costo_base()`: Añade 10€ extra si tiene seguro.
* **Método propio:** `mostrar_advertencia()`: Imprime "⚠️ FRÁGIL - MANEJAR CON CUIDADO".

### Clase Hija: `PaqueteExpress` (Hereda de `Paquete`)
* **Atributo adicional:** `fecha_limite`.
* **Sobrescritura:** `calcular_costo_base()`: Multiplica el costo base por 2.
* **Método propio:** `tiempo_restante(fecha_actual)`: Calcula días restantes.

---

## Ejercicio 7: Sobrescritura de Métodos (Polimorfismo)

Un sistema de streaming necesita calcular suscripciones.

### Clase Padre: `PlanSuscripcion`
* **Atributos:** `nombre_usuario`, `meses_contratados`.
* **Métodos:**
    * `calcular_precio()`: Retorna 0 (base).
    * `mostrar_resumen()`: Muestra usuario y precio total.

### Clases Hijas:

**1. `PlanBasico`**
* Precio: 7.99€/mes.
* Características: 720p, 1 pantalla.
* Sobrescribe `calcular_precio()`.
* Añade `mostrar_caracteristicas()`.

**2. `PlanEstandar`**
* Precio: 12.99€/mes.
* Características: 1080p, 2 pantallas.
* Sobrescribe `calcular_precio()`: Aplica **15% descuento** si contrata 12 meses o más.

**3. `PlanPremium`**
* Precio: 17.99€/mes.
* Características: 4K, 4 pantallas, descargas.
* Sobrescribe `calcular_precio()`: Aplica **20% descuento** si contrata 12 meses o más.

> **Requisito:** En cada hija, sobrescribe `mostrar_resumen()` llamando primero al padre con `super().mostrar_resumen()` y luego imprimiendo las características específicas.