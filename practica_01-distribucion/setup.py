from setuptools import setup, find_packages

setup(
    name="paquete",
    version="0.1",
    packages=find_packages(),
    description="Este es un paquete de ejemplo",
    author="Mister Nobody",
    author_email="nobody@empty.com",
    url="http://www.mrnobody.net",
    scripts=['script.py']  # opcional
)