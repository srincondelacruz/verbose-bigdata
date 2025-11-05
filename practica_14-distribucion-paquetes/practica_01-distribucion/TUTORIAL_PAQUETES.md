# Parte 01 - Distribución

Para crear un paquete distribuible (que se pueda ejecutar desde cualquier ubicación) tenemos que crear un fichero `setup.py` fuera de la raíz, indicando una información básica.

## 🧱 1. Crear la estructura del proyecto

En PowerShell:

```powershell
mkdir distribucion
cd distribucion
code .
Estructura dentro de VS Code:

distribucion/
├── paquete/
│   ├── __init__.py
│   ├── hola/
│   │   ├── __init__.py
│   │   └── saludos.py
│   └── adios/
│       ├── __init__.py
│       └── despedidas.py
├── script.py
└── setup.py
Cada carpeta debe tener un archivo __init__.py para que Python la reconozca como paquete o subpaquete.

🧩 2. Crear el código del paquete
🗂 paquete/hola/saludos.py
Python

def saludar():
    print("👋 Hola, te estoy saludando desde la función saludar() del módulo saludos")

class Saludo:
    def __init__(self):
        print("👋 Hola, te estoy saludando desde el __init__ de la clase Saludo")
🗂 paquete/adios/despedidas.py
Python

def despedir():
    print("👋 Adiós, esto viene del subpaquete adios")
🗂 paquete/init.py
Python

__all__ = ["hola", "adios"]
🧰 3. Crear un entorno virtual
En la raíz del proyecto:

PowerShell

python -m venv .venv
Activa el entorno virtual:

PowerShell

.\\.venv\\Scripts\\Activate.ps1
Si aparece un error de permisos:

PowerShell

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
⚙️ 4. Crear el archivo setup.py
Python

from setuptools import setup, find_packages

setup(
    name="paquete",
    version="0.1",
    packages=find_packages(),
    description="Este es un paquete de ejemplo",
    author="Mister Nobody",
    author_email="nobody@empty.com",
    url="[http://www.mrnobody.net](http://www.mrnobody.net)",
    scripts=['script.py']  # opcional
)
📒 find_packages() busca automáticamente todos los subpaquetes. scripts te permite incluir archivos ejecutables. Los metadatos (author, url, etc.) se muestran con pip show paquete.

⚡ 5. Instalar el paquete en modo editable
Desde la raíz del proyecto:

PowerShell

python -m pip install -e .
Verifica la instalación:

PowerShell

python -m pip show paquete
🧩 En este punto ya puedes importar el paquete desde cualquier ubicación en tu sistema.

🧪 6. Probar el paquete desde cualquier ubicación
PowerShell

cd C:\\Users\\tuusuario
python
Dentro de Python:

Python

>>> from paquete.hola.saludos import saludar
>>> saludar()
✅ Resultado esperado: 👋 Hola, te estoy saludando desde la función saludar() del módulo saludos

📦 7. Crear una distribución real
🧰 7.1 Instalar herramientas necesarias
PowerShell

python -m pip install --upgrade setuptools wheel twine
📦 7.2 Generar los archivos de distribución
PowerShell

python setup.py sdist bdist_wheel
Esto crea la carpeta dist/ con:

dist/
├── paquete-0.1.tar.gz
└── paquete-0.1-py3-none-any.whl
💡 .tar.gz: distribución fuente (incluye el código). .whl: distribución binaria (instalación rápida).

Ahora, si utilizamos el comando pip list, podremos consultar todos los paquetes instalados en nuestro Python, y podremos ver también el nuestro.

🚀 8. Instalar desde la distribución local (para simular otro usuario que instala)
Primero, desinstala la versión editable (opcional):

PowerShell

python -m pip uninstall paquete -y
Instala desde el .tar.gz:

PowerShell

python -m pip install dist\\paquete-0.1.tar.gz
Y prueba:

Python

from paquete.adios.despedidas import despedir
despedir()
✅ Resultado: 👋 Adiós, esto viene del subpaquete adios

🌐 9. Publicar el paquete en TestPyPI
⚠️ Esta parte es opcional, pero muy útil para enseñar distribución real sin usar el PyPI oficial.

9.1 Crear cuenta en TestPyPI
Ir a https://test.pypi.org/

Crear una cuenta o iniciar sesión.

En tu perfil → Account settings → API tokens → Create API token

Copia el token (empieza por pypi-...)

9.2 Subir el paquete con Twine
Ejecuta:

PowerShell

python -m twine upload --repository testpypi dist/*
Cuando aparezca: Enter your API token: Pega el token completo y presiona Enter.

Actualizar el proyecto (Ejemplo v0.2)
Supongamos que quiero actualizar mi proyecto, añadiendo una función mas al archivo saludos.py:

Python

def prueba():
    print("Esto es una prueba de la nueva version del módulo saludos")
Ya hemos terminado de hacer los cambios en “nuestro proyecto” y ahora vamos al archivo setup.py y actualizamos la versión cambiándola por la versión 0.2.

Guardamos, luego volvemos a la terminal desde el fichero raiz y ejecutamos de nuevo el paso 7.2:

PowerShell

python setup.py sdist bdist_wheel
Esto creará la nueva versión, como se puede ver en el directorio dist.

Actualizamos el paquete escribiendo:

PowerShell

pip install paquete-0.2.tar.gz --upgrade
Si vuelo a ejecutar: pip list, se podrá observar la nueva versión.

Verifiquemos que se ha actualizado probando desde fuera del directorio.

Si queremos borrar el paquete instalado desde la terminal escribimos:

PowerShell

pip uninstall paquete
Parte 02 - PIP y paquetes externos
Ejecutar desde un notebook de Jupyter. GitHub - pandas-dev/pandas: Flexible and powerful data analysis / manipulation library for Python...

Creación del entorno
PowerShell

python -m venv venv
venv\\Scripts\\activate     # Windows
source venv/bin/activate  # Linux/Mac
Comandos PIP
Verificar instalación de pip: python -m ensurepip --default-pip

Verificar su versión: pip --version

Instala un paquete desde PyPI: pip install nombre_paquete # pip install pandas

Desinstala un paquete: pip uninstall nombre_paquete # pip uninstall pandas

Muestra los paquetes instalados: pip list

Muestra información detallada de un paquete: pip show nombre_paquete

Muestra los paquetes y sus versiones (para requirements.txt): # pip freeze pip freeze > requirements.txt

Instala paquetes desde un archivo: pip install -r requirements.txt

Actualiza un paquete: pip install --upgrade nombre_paquete

Verifica dependencias rotas o incompatibles: pip check

Instalar un paquete localmente: pip install .

O, en modo editable (para desarrollo): pip install -e .

Instalar un paquete desde GitHub: pip install git+https://github.com/pallets/flask.git

Instalar una versión específica: pip install numpy==1.26.0

O versiones más nuevas: pip install "pandas>=2.0.0"


---