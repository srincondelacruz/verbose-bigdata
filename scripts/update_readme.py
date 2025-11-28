#!/usr/bin/env python3
"""
Script para actualizar automáticamente el README.md principal del repositorio.

Escanea las carpetas de prácticas y proyectos personales, extrae o genera
descripciones, y actualiza el índice del README.md.
"""

import json
import os
import re
from pathlib import Path


# Mapeo de imports a temas
IMPORT_TOPICS = {
    "pandas": "Análisis de datos con Pandas",
    "pyspark": "Procesamiento con PySpark",
    "spark": "Procesamiento con Spark",
    "sklearn": "Machine Learning",
    "scikit-learn": "Machine Learning",
    "numpy": "Computación numérica",
    "tensorflow": "Deep Learning con TensorFlow",
    "keras": "Deep Learning con Keras",
    "torch": "Deep Learning con PyTorch",
    "matplotlib": "Visualización de datos",
    "seaborn": "Visualización estadística",
    "plotly": "Visualización interactiva",
    "requests": "Consumo de APIs",
    "flask": "Desarrollo web con Flask",
    "django": "Desarrollo web con Django",
    "fastapi": "Desarrollo de APIs con FastAPI",
    "sqlalchemy": "Bases de datos con SQLAlchemy",
    "pymongo": "Bases de datos MongoDB",
}


def extract_number_from_folder(folder_name: str) -> int:
    """Extrae el número de práctica de un nombre de carpeta."""
    match = re.search(r"practica_(\d+)", folder_name)
    if match:
        return int(match.group(1))
    return 0


def format_folder_name(folder_name: str) -> str:
    """Formatea el nombre de la carpeta para mostrar en el README."""
    if folder_name.startswith("practica_"):
        # Extraer número y nombre
        match = re.match(r"practica_(\d+)-(.+)", folder_name)
        if match:
            num = match.group(1)
            name = match.group(2).replace("_", " ").replace("-", " ")
            return f"Práctica {num}: {name.title()}"
        # Solo número
        match = re.match(r"practica_(\d+)", folder_name)
        if match:
            return f"Práctica {match.group(1)}"
    elif folder_name.startswith("ejercicios_personales-"):
        name = folder_name.replace("ejercicios_personales-", "")
        return f"Ejercicios Personales: {name.title()}"
    return folder_name


def read_readme_objective(readme_path: Path) -> str:
    """
    Lee un README.md y extrae el objetivo/descripción.
    
    Busca:
    - Líneas con "Objetivo:" o "## Objetivo"
    - El primer párrafo descriptivo después del título
    """
    try:
        content = readme_path.read_text(encoding="utf-8")
        lines = content.split("\n")
        
        # Buscar sección "Objetivo" (con o sin emoji)
        for i, line in enumerate(lines):
            stripped = line.strip()
            # Buscar encabezados de objetivo: "## Objetivo", "## 🎯 Objetivo", etc.
            if stripped.startswith("#") and "objetivo" in stripped.lower():
                # Tomar el siguiente párrafo no vacío
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if next_line and not next_line.startswith("#") and next_line != "---":
                        # Puede haber viñetas, tomar la primera o el párrafo
                        if next_line.startswith("*") or next_line.startswith("-"):
                            # Limpiar la viñeta
                            next_line = next_line.lstrip("*- ").strip()
                        return clean_description(next_line)
        
        # Buscar "Objetivo:" en una línea
        for line in lines:
            if "objetivo:" in line.lower():
                parts = line.split(":", 1)
                if len(parts) > 1 and parts[1].strip():
                    return clean_description(parts[1].strip())
        
        # Buscar primer párrafo descriptivo (después del título)
        found_title = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                found_title = True
                continue
            if found_title and stripped and not stripped.startswith("#"):
                # Ignorar líneas de separación y viñetas
                if stripped != "---" and not stripped.startswith("*") and not stripped.startswith("-"):
                    return clean_description(stripped)
        
        return ""
    except (OSError, UnicodeDecodeError):
        return ""


def clean_description(text: str) -> str:
    """Limpia y formatea una descripción."""
    # Eliminar markdown innecesario
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)  # Negritas
    text = re.sub(r"\*([^*]+)\*", r"\1", text)  # Itálicas
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # Enlaces
    text = text.strip()
    
    # Limitar longitud
    if len(text) > 200:
        text = text[:197] + "..."
    
    return text


def analyze_notebook(notebook_path: Path) -> dict:
    """
    Analiza un notebook Jupyter y extrae información.
    
    Returns:
        dict con 'description', 'imports' y 'topics'
    """
    result = {"description": "", "imports": set(), "topics": set()}
    
    try:
        content = notebook_path.read_text(encoding="utf-8")
        notebook = json.loads(content)
        cells = notebook.get("cells", [])
        
        for cell in cells:
            cell_type = cell.get("cell_type", "")
            source = cell.get("source", [])
            if isinstance(source, list):
                source = "".join(source)
            
            if cell_type == "markdown":
                # Buscar títulos o descripciones
                if not result["description"]:
                    lines = source.split("\n")
                    for line in lines:
                        stripped = line.strip()
                        # Ignorar líneas vacías y blockquotes
                        if not stripped or stripped.startswith(">"):
                            continue
                        # Buscar títulos con # (## Título, ### Título, etc.)
                        if stripped.startswith("#"):
                            title = stripped.lstrip("#").strip()
                            # Ignorar títulos que son solo números o muy cortos
                            if title and len(title) > 3:
                                # Ignorar títulos que parecen ejemplos numerados
                                if not re.match(r"^Ejemplo\s*\d+", title, re.IGNORECASE):
                                    result["description"] = clean_description(title)
                                    break
                        # Si no empieza con #, podría ser texto descriptivo
                        elif stripped and not stripped.startswith("!") and not stripped.startswith("*"):
                            # Verificar si es una oración descriptiva (más de 10 caracteres)
                            if len(stripped) > 10:
                                result["description"] = clean_description(stripped)
                                break
            
            elif cell_type == "code":
                # Extraer imports
                for line in source.split("\n"):
                    line = line.strip()
                    if line.startswith("import ") or line.startswith("from "):
                        match = re.match(r"(?:from|import)\s+(\w+)", line)
                        if match:
                            module = match.group(1).lower()
                            result["imports"].add(module)
                            if module in IMPORT_TOPICS:
                                result["topics"].add(IMPORT_TOPICS[module])
    except (OSError, json.JSONDecodeError, UnicodeDecodeError, KeyError):
        pass
    
    return result


def analyze_python_file(py_path: Path) -> dict:
    """
    Analiza un archivo Python y extrae información.
    
    Returns:
        dict con 'description', 'imports' y 'topics'
    """
    result = {"description": "", "imports": set(), "topics": set()}
    
    try:
        content = py_path.read_text(encoding="utf-8")
        lines = content.split("\n")
        
        # Buscar docstring del módulo
        in_docstring = False
        docstring_lines = []
        for line in lines:
            stripped = line.strip()
            if not in_docstring:
                if stripped.startswith('"""') or stripped.startswith("'''"):
                    in_docstring = True
                    # Docstring de una línea
                    if stripped.count('"""') == 2 or stripped.count("'''") == 2:
                        docstring_lines.append(stripped[3:-3])
                        break
                    docstring_lines.append(stripped[3:])
                elif stripped.startswith("#"):
                    # Comentario inicial
                    comment = stripped.lstrip("#").strip()
                    if comment and not result["description"]:
                        result["description"] = comment
                elif stripped and not stripped.startswith("import") and not stripped.startswith("from"):
                    break
            else:
                if stripped.endswith('"""') or stripped.endswith("'''"):
                    docstring_lines.append(stripped[:-3])
                    break
                docstring_lines.append(stripped)
        
        if docstring_lines:
            result["description"] = clean_description(" ".join(docstring_lines).strip())
        
        # Extraer imports
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("import ") or stripped.startswith("from "):
                match = re.match(r"(?:from|import)\s+(\w+)", stripped)
                if match:
                    module = match.group(1).lower()
                    result["imports"].add(module)
                    if module in IMPORT_TOPICS:
                        result["topics"].add(IMPORT_TOPICS[module])
    except (OSError, UnicodeDecodeError):
        pass
    
    return result


def generate_description_from_imports(imports: set, topics: set, folder_name: str) -> str:
    """Genera una descripción basada en los imports y temas detectados."""
    if topics:
        return f"Práctica de {', '.join(sorted(topics))}."
    
    if imports:
        known_imports = [imp for imp in imports if imp in IMPORT_TOPICS]
        if known_imports:
            topics_from_imports = [IMPORT_TOPICS[imp] for imp in known_imports]
            return f"Práctica de {', '.join(sorted(set(topics_from_imports)))}."
    
    # Generar descripción genérica basada en el nombre de la carpeta
    name = folder_name.split("-", 1)[-1] if "-" in folder_name else folder_name
    name = name.replace("_", " ").replace("-", " ").title()
    return f"Práctica sobre {name}."


def analyze_folder(folder_path: Path) -> str:
    """
    Analiza una carpeta de práctica y genera una descripción.
    
    1. Si existe README.md, extrae el objetivo
    2. Si no, analiza los archivos .py y .ipynb
    3. Si no puede inferir nada, genera descripción genérica
    """
    readme_path = folder_path / "README.md"
    
    # Caso 1: Existe README.md
    if readme_path.exists():
        objective = read_readme_objective(readme_path)
        if objective:
            return objective
    
    # Caso 2: Analizar archivos
    all_imports = set()
    all_topics = set()
    descriptions = []
    
    # Analizar notebooks
    for notebook in folder_path.glob("*.ipynb"):
        info = analyze_notebook(notebook)
        all_imports.update(info["imports"])
        all_topics.update(info["topics"])
        if info["description"]:
            descriptions.append(info["description"])
    
    # Analizar archivos Python
    for py_file in folder_path.glob("*.py"):
        info = analyze_python_file(py_file)
        all_imports.update(info["imports"])
        all_topics.update(info["topics"])
        if info["description"]:
            descriptions.append(info["description"])
    
    # Usar primera descripción encontrada
    if descriptions:
        return descriptions[0]
    
    # Generar descripción desde imports
    return generate_description_from_imports(all_imports, all_topics, folder_path.name)


def scan_folders(base_path: Path) -> tuple[list, list]:
    """
    Escanea el directorio base y encuentra carpetas de prácticas y ejercicios.
    
    Returns:
        Tuple de (prácticas, ejercicios_personales) ordenados
    """
    practicas = []
    ejercicios = []
    
    for item in base_path.iterdir():
        if not item.is_dir():
            continue
        
        name = item.name
        if name.startswith("practica_"):
            practicas.append(item)
        elif name.startswith("ejercicios_personales"):
            ejercicios.append(item)
    
    # Ordenar prácticas por número (descendente)
    practicas.sort(key=lambda p: extract_number_from_folder(p.name), reverse=True)
    
    # Ordenar ejercicios alfabéticamente
    ejercicios.sort(key=lambda e: e.name)
    
    return practicas, ejercicios


def generate_readme(base_path: Path, practicas: list, ejercicios: list) -> str:
    """Genera el contenido del README.md principal."""
    lines = [
        "# Prácticas del Módulo Big Data (Curso 2025)",
        "",
        "Repositorio con todas las prácticas de la asignatura.",
        "",
        "---",
        "## 📂 Índice de Prácticas",
        "",
    ]
    
    for practica in practicas:
        folder_name = practica.name
        display_name = format_folder_name(folder_name)
        description = analyze_folder(practica)
        
        lines.append(f"* **[{display_name}](./{folder_name}/)**")
        lines.append(f"    * *Objetivo: {description}*")
        lines.append("")
    
    if ejercicios:
        lines.append("## 📂 Índice de Proyectos Personales")
        lines.append("")
        
        for ejercicio in ejercicios:
            folder_name = ejercicio.name
            display_name = format_folder_name(folder_name)
            description = analyze_folder(ejercicio)
            
            lines.append(f"* **[{display_name}](./{folder_name}/)**")
            lines.append(f"    * *Objetivo: {description}*")
    
    return "\n".join(lines)


def main():
    """Punto de entrada principal del script."""
    # Determinar la ruta base del repositorio
    script_path = Path(__file__).resolve()
    base_path = script_path.parent.parent
    
    print(f"Escaneando repositorio en: {base_path}")
    
    # Escanear carpetas
    practicas, ejercicios = scan_folders(base_path)
    
    print(f"Encontradas {len(practicas)} prácticas y {len(ejercicios)} proyectos personales")
    
    # Generar README
    readme_content = generate_readme(base_path, practicas, ejercicios)
    
    # Escribir README
    readme_path = base_path / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")
    
    print(f"README.md actualizado exitosamente")


if __name__ == "__main__":
    main()
