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
from urllib.parse import quote


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

# Descripciones elaboradas para combinaciones comunes de imports
IMPORT_COMBINATIONS = {
    frozenset(["pandas", "matplotlib"]): (
        "Análisis y visualización de datos utilizando Pandas para manipulación "
        "de DataFrames y Matplotlib para gráficos."
    ),
    frozenset(["pandas", "seaborn"]): (
        "Análisis exploratorio de datos con Pandas y visualización estadística "
        "avanzada con Seaborn."
    ),
    frozenset(["pandas", "numpy"]): (
        "Manipulación y análisis de datos tabulares con Pandas y operaciones "
        "numéricas eficientes con NumPy."
    ),
    frozenset(["pandas", "sklearn"]): (
        "Preparación de datos con Pandas y aplicación de algoritmos de Machine "
        "Learning con Scikit-learn."
    ),
    frozenset(["pyspark"]): (
        "Procesamiento de datos distribuidos con Apache Spark usando PySpark. "
        "Incluye operaciones de DataFrames, transformaciones y acciones."
    ),
    frozenset(["pandas", "matplotlib", "numpy"]): (
        "Análisis de datos completo con Pandas para manipulación, NumPy para "
        "cálculos numéricos y Matplotlib para visualización."
    ),
    frozenset(["pandas", "matplotlib", "seaborn"]): (
        "Análisis exploratorio de datos (EDA) con Pandas y visualización "
        "avanzada combinando Matplotlib y Seaborn."
    ),
}

# Constantes de configuración
MAX_DESCRIPTION_LENGTH = 450
MAX_SINGLE_DESCRIPTION_LENGTH = 180
SENTENCE_BOUNDARY_THRESHOLD = 0.6
TARGET_LINE_LENGTH = 80
MULTILINE_INDENT = "      "

# Categorías de prácticas
CATEGORIES = {
    "bigdata": {
        "title": "🔥 Prácticas de Big Data y Analytics",
        "anchor": "-prácticas-de-big-data-y-analytics",
        "range": (18, 21),
    },
    "python_advanced": {
        "title": "🐍 Prácticas de Python Avanzado",
        "anchor": "-prácticas-de-python-avanzado",
        "range": (15, 17),
    },
    "modularidad": {
        "title": "📦 Prácticas de Modularidad y Distribución",
        "anchor": "-prácticas-de-modularidad-y-distribución",
        "range": (12, 14),
    },
}

# Métodos y funciones comunes para formatear con backticks
METHODS_TO_FORMAT = [
    # Pandas methods
    r'\bgroupby\(\)',
    r'\bmerge\(\)',
    r'\bconcat\(\)',
    r'\bpivot\(\)',
    r'\bpivot_table\(\)',
    r'\bmelt\(\)',
    r'\brolling\(\)',
    r'\bresample\(\)',
    r'\bfillna\(\)',
    r'\bdropna\(\)',
    r'\bastype\(\)',
    r'\bapply\(\)',
    r'\bmap\(\)',
    r'\bloc\b',
    r'\biloc\b',
    # PySpark methods
    r'\bselect\(\)',
    r'\bfilter\(\)',
    r'\bwithColumn\(\)',
    r'\bjoin\(\)',
    r'\bagg\(\)',
    r'\bcollect\(\)',
    r'\bshow\(\)',
    r'\bprintSchema\(\)',
    # Python OOP
    r'\b__init__\b',
    r'\b__str__\b',
    r'\b__repr__\b',
    r'\bsuper\(\)',
    r'@classmethod\b',
    r'@staticmethod\b',
    r'@property\b',
    # Data types
    r'\bDataFrame\b',
    r'\bDataFrames\b',
    r'\bSeries\b',
    r'\bRDD\b',
]


def extract_number_from_folder(folder_name: str) -> int:
    """Extrae el número de práctica de un nombre de carpeta."""
    match = re.search(r"practica_(\d+)", folder_name)
    if match:
        return int(match.group(1))
    return 0


def encode_folder_url(folder_name: str) -> str:
    """Codifica el nombre de la carpeta para URLs (espacios → %20)."""
    return quote(folder_name, safe='')


def format_methods_with_backticks(text: str) -> str:
    """
    Formatea métodos y funciones con backticks en el texto.
    
    Busca patrones de métodos comunes y los envuelve en backticks.
    Evita duplicar backticks si ya están presentes.
    """
    result = text
    
    # Primero, manejar casos especiales de *args y **kwargs
    # Reemplazar *kwargs primero (más específico)
    result = re.sub(r'(?<!`)\*\*kwargs(?!`)', r'`**kwargs`', result)
    result = re.sub(r'(?<!`)\*args(?!`)', r'`*args`', result)
    
    for pattern in METHODS_TO_FORMAT:
        # Usar lookahead/lookbehind para evitar backticks
        safe_pattern = f'(?<!`)({pattern})(?!`)'
        result = re.sub(safe_pattern, r'`\1`', result)
    
    # Limpiar backticks duplicados
    result = re.sub(r'``+', '`', result)
    
    return result


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
    elif folder_name.startswith("ejercicios_personales_"):
        name = folder_name.replace("ejercicios_personales_", "")
        return f"Ejercicios Personales: {name.title()}"
    return folder_name


def read_readme_objective(readme_path: Path) -> str:
    """
    Lee un README.md y extrae el objetivo/descripción (hasta 3 oraciones).
    
    Busca:
    - Líneas con "Objetivo:" o "## Objetivo"
    - El primer párrafo descriptivo después del título
    - Combina múltiples líneas para un resumen más completo
    """
    try:
        content = readme_path.read_text(encoding="utf-8")
        lines = content.split("\n")
        
        # Buscar sección "Objetivo" (con o sin emoji)
        for i, line in enumerate(lines):
            stripped = line.strip()
            # Buscar encabezados de objetivo: "## Objetivo", "## 🎯 Objetivo", etc.
            if stripped.startswith("#") and "objetivo" in stripped.lower():
                # Recopilar múltiples líneas del objetivo (hasta 3 oraciones)
                collected_lines = []
                for j in range(i + 1, min(i + 10, len(lines))):
                    next_line = lines[j].strip()
                    # Detenerse si encontramos otro encabezado o separador
                    if next_line.startswith("#") or next_line == "---":
                        break
                    if not next_line:
                        # Línea vacía puede indicar fin de párrafo
                        if collected_lines:
                            break
                        continue
                    # Limpiar viñetas
                    if next_line.startswith("*") or next_line.startswith("-"):
                        next_line = next_line.lstrip("*- ").strip()
                    if next_line:
                        collected_lines.append(next_line)
                        # Limitar a 3 oraciones
                        full_text = " ".join(collected_lines)
                        sentences = re.split(r'(?<=[.!?])\s+', full_text)
                        if len(sentences) >= 3:
                            break
                
                if collected_lines:
                    full_text = " ".join(collected_lines)
                    return clean_description(full_text)
        
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


def clean_description(text: str, max_length: int = MAX_DESCRIPTION_LENGTH) -> str:
    """Limpia y formatea una descripción."""
    # Preservar *args y **kwargs antes de procesar markdown
    # Usar marcadores temporales para protegerlos
    text = re.sub(r'`\*\*kwargs`', '<<DOUBLE_STAR_KWARGS>>', text)
    text = re.sub(r'`\*args`', '<<STAR_ARGS>>', text)
    text = re.sub(r'\*\*kwargs', '<<DOUBLE_STAR_KWARGS>>', text)
    text = re.sub(r'\*args', '<<STAR_ARGS>>', text)
    
    # Eliminar markdown innecesario
    text = re.sub(r"`([^`]+)`", r"\1", text)  # Código inline
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)  # Negritas
    text = re.sub(r"\*([^*]+)\*", r"\1", text)  # Itálicas
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # Enlaces
    text = re.sub(r"\s+", " ", text)  # Normalizar espacios
    text = text.strip()
    
    # Restaurar *args y **kwargs
    text = text.replace('<<DOUBLE_STAR_KWARGS>>', '**kwargs')
    text = text.replace('<<STAR_ARGS>>', '*args')
    
    # Limitar longitud
    if len(text) > max_length:
        # Intentar cortar en un punto natural (fin de oración)
        truncated = text[:max_length]
        last_period = truncated.rfind(".")
        if last_period > max_length * SENTENCE_BOUNDARY_THRESHOLD:
            text = truncated[:last_period + 1]
        else:
            text = truncated[:max_length - 3] + "..."
    
    return text


def analyze_notebook(notebook_path: Path) -> dict:
    """
    Analiza un notebook Jupyter y extrae información de múltiples celdas.
    
    Busca en las primeras 5 celdas markdown para obtener más contexto.
    Detecta patrones como "Objetivo:", "En esta práctica...", "Aprenderemos..."
    Filtra ejercicios numerados y enfoca en títulos/descripciones principales.
    
    Returns:
        dict con 'description', 'imports' y 'topics'
    """
    result = {"description": "", "imports": set(), "topics": set()}
    
    try:
        content = notebook_path.read_text(encoding="utf-8")
        notebook = json.loads(content)
        cells = notebook.get("cells", [])
        
        # Patrones de texto descriptivo a buscar (prioridad alta)
        descriptive_patterns = [
            r"(?:objetivo|propósito|meta)[\s:]+(.+)",
            r"(?:en esta práctica|en este notebook)[\s,]+(.+)",
            r"(?:aprenderemos|veremos|estudiaremos)[\s]+(.+)",
            r"(?:introducción a|tutorial de|guía de)[\s]+(.+)",
        ]
        
        # Patrones a ignorar (ejercicios, pasos numerados)
        ignore_patterns = [
            r"^(?:Ejercicio|Ejemplo|Paso|Tarea)\s*\d+",
            r"^\d+\.\s*(?:Calcular|Crear|Usar|Buscar|Mostrar)",
            r"^(?:Crea|Escribe|Define|Implementa)\s+(?:un|una|el|la)",
        ]
        
        main_title = ""
        priority_descriptions = []  # Descripciones de patrones específicos
        title_descriptions = []     # Títulos markdown
        
        markdown_cells_checked = 0
        max_markdown_cells = 5
        
        for cell in cells:
            cell_type = cell.get("cell_type", "")
            source = cell.get("source", [])
            if isinstance(source, list):
                source = "".join(source)
            
            if cell_type == "markdown":
                markdown_cells_checked += 1
                lines = source.split("\n")
                
                for line in lines:
                    stripped = line.strip()
                    # Ignorar líneas vacías, blockquotes y líneas muy cortas
                    if not stripped or stripped.startswith(">") or len(stripped) < 5:
                        continue
                    
                    # Verificar si es un patrón a ignorar
                    should_ignore = False
                    for ignore_pattern in ignore_patterns:
                        if re.match(ignore_pattern, stripped, re.IGNORECASE):
                            should_ignore = True
                            break
                    if should_ignore:
                        continue
                    
                    # Buscar patrones descriptivos (alta prioridad)
                    for pattern in descriptive_patterns:
                        match = re.search(pattern, stripped, re.IGNORECASE)
                        if match:
                            desc = match.group(1).strip()
                            if desc and len(desc) > 10:
                                priority_descriptions.append(desc)
                                break
                    
                    # Buscar títulos con # (## Título, ### Título, etc.)
                    if stripped.startswith("#"):
                        title = stripped.lstrip("#").strip()
                        # Ignorar títulos que parecen ejercicios
                        if title and len(title) > 5:
                            if not re.match(r"^(?:Ejemplo|Ejercicio|Paso|Tarea)\s*\d+", title, re.IGNORECASE):
                                # El primer título principal es especial
                                if not main_title and stripped.startswith("# "):
                                    main_title = title
                                else:
                                    title_descriptions.append(title)
                
                if markdown_cells_checked >= max_markdown_cells:
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
        
        # Construir descripción final
        descriptions = []
        
        # Prioridad 1: Descripciones de patrones específicos (objetivo, etc.)
        if priority_descriptions:
            descriptions.extend(priority_descriptions[:2])
        
        # Prioridad 2: Título principal
        if main_title and len(descriptions) < 2:
            descriptions.insert(0, main_title)
        
        # Prioridad 3: Otros títulos relevantes
        if title_descriptions and len(descriptions) < 2:
            for title in title_descriptions[:2]:
                if title not in descriptions:
                    descriptions.append(title)
                    if len(descriptions) >= 2:
                        break
        
        # Combinar descripciones únicas
        if descriptions:
            seen = set()
            unique = []
            for desc in descriptions:
                clean = clean_description(desc, max_length=MAX_SINGLE_DESCRIPTION_LENGTH)
                if clean and clean.lower() not in seen:
                    seen.add(clean.lower())
                    unique.append(clean)
            result["description"] = " ".join(unique[:2])
    
    except (OSError, json.JSONDecodeError, UnicodeDecodeError, KeyError):
        pass
    
    return result


def analyze_python_file(py_path: Path) -> dict:
    """
    Analiza un archivo Python y extrae información completa.
    
    Lee docstrings completos (no solo la primera línea), combina comentarios
    iniciales, y busca definiciones de funciones/clases para inferir el tema.
    
    Returns:
        dict con 'description', 'imports' y 'topics'
    """
    result = {"description": "", "imports": set(), "topics": set()}
    
    try:
        content = py_path.read_text(encoding="utf-8")
        lines = content.split("\n")
        
        # Buscar docstring del módulo (leer completo)
        in_docstring = False
        docstring_lines = []
        initial_comments = []
        docstring_quote = None
        
        for line in lines:
            stripped = line.strip()
            if not in_docstring:
                # Detectar inicio de docstring
                if stripped.startswith('"""') or stripped.startswith("'''"):
                    docstring_quote = stripped[:3]
                    in_docstring = True
                    # Docstring de una línea
                    if stripped.count(docstring_quote) == 2:
                        docstring_lines.append(stripped[3:-3])
                        break
                    docstring_lines.append(stripped[3:])
                elif stripped.startswith("#"):
                    # Recopilar comentarios iniciales
                    comment = stripped.lstrip("#").strip()
                    if comment and not comment.startswith("-"):
                        initial_comments.append(comment)
                elif stripped and not stripped.startswith("import") and not stripped.startswith("from"):
                    # Fin del preámbulo
                    break
            else:
                if docstring_quote and stripped.endswith(docstring_quote):
                    docstring_lines.append(stripped[:-3])
                    break
                docstring_lines.append(stripped)
        
        # Usar docstring si existe, sino combinar comentarios iniciales
        if docstring_lines:
            full_docstring = " ".join(docstring_lines).strip()
            result["description"] = clean_description(full_docstring)
        elif initial_comments:
            # Combinar los primeros comentarios (hasta 3)
            combined = " ".join(initial_comments[:3])
            result["description"] = clean_description(combined)
        
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
        
        # Buscar definiciones de clases/funciones para inferir tema
        class_names = []
        for line in lines:
            class_match = re.match(r"class\s+(\w+)", line)
            if class_match:
                class_names.append(class_match.group(1))
        
        # Si hay clases definidas y no hay descripción, mencionarlas
        if class_names and not result["description"]:
            if len(class_names) == 1:
                result["description"] = f"Implementación de la clase {class_names[0]}."
            else:
                result["description"] = f"Implementación de clases: {', '.join(class_names[:3])}."
    
    except (OSError, UnicodeDecodeError):
        pass
    
    return result


def generate_description_from_imports(imports: set, topics: set, folder_name: str) -> str:
    """
    Genera una descripción elaborada basada en los imports y temas detectados.
    
    Utiliza combinaciones de imports conocidas para generar descripciones
    más completas y contextuales.
    """
    # Primero, buscar combinaciones conocidas de imports
    known_imports = {imp for imp in imports if imp in IMPORT_TOPICS}
    
    if known_imports:
        # Buscar la mejor combinación que coincida
        best_match = None
        best_match_size = 0
        
        for combo, description in IMPORT_COMBINATIONS.items():
            if combo.issubset(known_imports) and len(combo) > best_match_size:
                best_match = description
                best_match_size = len(combo)
        
        if best_match:
            return best_match
        
        # Si no hay combinación conocida, generar descripción compuesta
        topics_list = sorted({IMPORT_TOPICS[imp] for imp in known_imports})
        
        if len(topics_list) == 1:
            return f"Práctica de {topics_list[0]}."
        elif len(topics_list) == 2:
            return f"Práctica que combina {topics_list[0]} y {topics_list[1]}."
        else:
            main_topics = ", ".join(topics_list[:-1])
            return f"Práctica que combina {main_topics} y {topics_list[-1]}."
    
    if topics:
        topics_list = sorted(topics)
        if len(topics_list) == 1:
            return f"Práctica de {topics_list[0]}."
        else:
            return f"Práctica de {', '.join(topics_list)}."
    
    # Generar descripción basada en el nombre de la carpeta
    name = folder_name.split("-", 1)[-1] if "-" in folder_name else folder_name
    name = name.replace("_", " ").replace("-", " ").title()
    return f"Práctica sobre {name}."


def analyze_folder(folder_path: Path) -> str:
    """
    Analiza una carpeta de práctica y genera una descripción completa.
    
    Combina información de múltiples fuentes:
    1. Si existe README.md o TUTORIAL.md, extrae hasta 3 oraciones del objetivo
    2. Si no, combina información de notebooks, archivos Python e imports
    3. Utiliza el nombre de la carpeta como contexto adicional
    """
    # Caso 1: Existe README.md - usar como fuente principal
    readme_path = folder_path / "README.md"
    if readme_path.exists():
        objective = read_readme_objective(readme_path)
        if objective:
            return objective
    
    # Caso 1b: Existe TUTORIAL.md - usar como fuente secundaria
    tutorial_path = folder_path / "TUTORIAL.md"
    if tutorial_path.exists():
        objective = read_readme_objective(tutorial_path)
        if objective:
            return objective
    
    # Caso 2: Analizar archivos y combinar información
    all_imports = set()
    all_topics = set()
    notebook_descriptions = []
    python_descriptions = []
    
    # Analizar notebooks
    for notebook in folder_path.glob("*.ipynb"):
        info = analyze_notebook(notebook)
        all_imports.update(info["imports"])
        all_topics.update(info["topics"])
        if info["description"]:
            notebook_descriptions.append(info["description"])
    
    # Analizar archivos Python
    for py_file in folder_path.glob("*.py"):
        info = analyze_python_file(py_file)
        all_imports.update(info["imports"])
        all_topics.update(info["topics"])
        if info["description"]:
            python_descriptions.append(info["description"])
    
    # Construir descripción final
    final_description = ""
    
    # Priorizar descripciones de notebooks (suelen ser más descriptivas)
    if notebook_descriptions:
        final_description = notebook_descriptions[0]
    elif python_descriptions:
        final_description = python_descriptions[0]
    
    # Si tenemos una descripción, opcionalmente añadir contexto tecnológico
    if final_description:
        # Solo añadir info de imports si la descripción es corta
        if all_imports and len(final_description) < 200:
            tech_desc = generate_description_from_imports(all_imports, all_topics, folder_path.name)
            # Evitar redundancia con descripciones genéricas
            if tech_desc and "Práctica sobre" not in tech_desc:
                final_description = f"{final_description} {tech_desc}"
        return clean_description(final_description)
    
    # Generar descripción desde imports si no hay otras fuentes
    return generate_description_from_imports(all_imports, all_topics, folder_path.name)


def scan_folders(base_path: Path) -> tuple[list, list, list]:
    """
    Escanea el directorio base y encuentra carpetas de prácticas, ejercicios y cheatsheets.
    
    Returns:
        Tuple de (prácticas, ejercicios_personales, cheatsheets) ordenados
    """
    practicas = []
    ejercicios = []
    cheatsheets = []
    
    for item in base_path.iterdir():
        if not item.is_dir():
            continue
        
        name = item.name
        if name.startswith("practica_"):
            practicas.append(item)
        elif name.startswith("ejercicios_personales"):
            ejercicios.append(item)
        elif name == "cheatsheets":
            cheatsheets.append(item)
    
    # Ordenar prácticas por número (descendente)
    practicas.sort(key=lambda p: extract_number_from_folder(p.name), reverse=True)
    
    # Ordenar ejercicios alfabéticamente
    ejercicios.sort(key=lambda e: e.name)
    
    return practicas, ejercicios, cheatsheets


def format_multiline_description(description: str, indent: str = MULTILINE_INDENT) -> str:
    """
    Formatea una descripción larga en múltiples líneas.
    
    Divide el texto en oraciones y las distribuye en 2-3 líneas
    para mejor legibilidad en el README.
    """
    # Dividir en oraciones
    sentences = re.split(r'(?<=[.!?])\s+', description)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if len(sentences) <= 1:
        return description
    
    # Distribuir en líneas (objetivo: 2-3 líneas)
    lines = []
    current_line = []
    current_length = 0
    
    for sentence in sentences:
        if current_length + len(sentence) > TARGET_LINE_LENGTH and current_line:
            lines.append(" ".join(current_line))
            current_line = [sentence]
            current_length = len(sentence)
        else:
            current_line.append(sentence)
            current_length += len(sentence) + 1
    
    if current_line:
        lines.append(" ".join(current_line))
    
    # Limitar a 3 líneas
    lines = lines[:3]
    
    # Formatear con saltos de línea e indentación
    if len(lines) == 1:
        return lines[0]
    
    return f"\n{indent}".join(lines)


def get_practice_theme(folder_name: str) -> str:
    """
    Extrae el tema de una práctica del nombre de la carpeta.
    
    Ejemplo: practica_21-pySpark_basico → PySpark Básico
    """
    match = re.match(r"practica_\d+-(.+)", folder_name)
    if match:
        name = match.group(1)
        # Reemplazar separadores y capitalizar
        name = name.replace("_", " ").replace("-", " ")
        return name.title()
    return ""


def categorize_practices(practicas: list) -> dict:
    """
    Organiza las prácticas en categorías según su número.
    
    Returns:
        Dict con categorías como claves y listas de prácticas como valores
    """
    categorized = {key: [] for key in CATEGORIES}
    
    for practica in practicas:
        num = extract_number_from_folder(practica.name)
        for cat_key, cat_info in CATEGORIES.items():
            range_start, range_end = cat_info["range"]
            if range_start <= num <= range_end:
                categorized[cat_key].append(practica)
                break
    
    return categorized


def get_cheatsheet_files(cheatsheets_path: Path) -> list:
    """
    Obtiene la lista de archivos markdown en la carpeta cheatsheets.
    
    Returns:
        Lista de tuples (nombre_archivo, nombre_display)
    """
    files = []
    if cheatsheets_path.exists():
        for f in cheatsheets_path.glob("*.md"):
            name = f.stem
            display_name = name.replace("_", " ").title()
            files.append((f.name, display_name))
    return sorted(files)


def generate_table_of_contents(categorized: dict, has_cheatsheets: bool, has_ejercicios: bool) -> list:
    """
    Genera la tabla de contenidos con enlaces internos.
    """
    lines = [
        "## 📋 Tabla de Contenidos",
        "",
    ]
    
    # Añadir enlaces a categorías
    for cat_key in ["bigdata", "python_advanced", "modularidad"]:
        if categorized.get(cat_key):
            cat_info = CATEGORIES[cat_key]
            lines.append(f"- [{cat_info['title']}](#{cat_info['anchor']})")
    
    if has_cheatsheets:
        lines.append("- [📚 Material de Referencia](#-material-de-referencia)")
    
    if has_ejercicios:
        lines.append("- [🏆 Proyectos Personales](#-proyectos-personales)")
    
    lines.append("")
    return lines


def generate_category_table(practicas: list, base_path: Path) -> list:
    """
    Genera una tabla markdown para una lista de prácticas.
    
    Formato:
    | Práctica | Tema | Descripción |
    |:--------:|:-----|:------------|
    | [**21**](./practica_21/) | PySpark Básico | Descripción... |
    """
    lines = [
        "| Práctica | Tema | Descripción |",
        "|:--------:|:-----|:------------|",
    ]
    
    # Ordenar por número descendente
    sorted_practicas = sorted(
        practicas, 
        key=lambda p: extract_number_from_folder(p.name), 
        reverse=True
    )
    
    for practica in sorted_practicas:
        folder_name = practica.name
        encoded_url = encode_folder_url(folder_name)
        num = extract_number_from_folder(folder_name)
        theme = get_practice_theme(folder_name)
        
        description = analyze_folder(practica)
        # Formatear métodos con backticks
        description = format_methods_with_backticks(description)
        # Limpiar descripción para tabla (eliminar saltos de línea)
        description = description.replace("\n", " ").strip()
        
        lines.append(f"| [**{num}**](./{encoded_url}/) | {theme} | {description} |")
    
    lines.append("")
    return lines


def generate_readme(base_path: Path, practicas: list, ejercicios: list, cheatsheets: list) -> str:
    """
    Genera el contenido del README.md principal con formato profesional.
    
    Incluye:
    - Header con título y descripción
    - Tabla de contenidos con navegación
    - Secciones categorizadas con tablas markdown
    - Métodos formateados con backticks
    - URLs correctamente codificadas
    """
    lines = [
        "# 🎓 Prácticas del Módulo Big Data (Curso 2025)",
        "",
        "> Repositorio con todas las prácticas de la asignatura de Big Data.",
        "",
        "---",
        "",
    ]
    
    # Categorizar prácticas
    categorized = categorize_practices(practicas)
    
    has_cheatsheets = bool(cheatsheets)
    has_ejercicios = bool(ejercicios)
    
    # Tabla de contenidos
    lines.extend(generate_table_of_contents(categorized, has_cheatsheets, has_ejercicios))
    lines.append("---")
    lines.append("")
    
    # Sección de Big Data y Analytics (18-21)
    if categorized["bigdata"]:
        lines.append(f"## {CATEGORIES['bigdata']['title']}")
        lines.append("")
        lines.extend(generate_category_table(categorized["bigdata"], base_path))
    
    # Sección de Python Avanzado (15-17)
    if categorized["python_advanced"]:
        lines.append(f"## {CATEGORIES['python_advanced']['title']}")
        lines.append("")
        lines.extend(generate_category_table(categorized["python_advanced"], base_path))
    
    # Sección de Modularidad y Distribución (12-14)
    if categorized["modularidad"]:
        lines.append(f"## {CATEGORIES['modularidad']['title']}")
        lines.append("")
        lines.extend(generate_category_table(categorized["modularidad"], base_path))
    
    # Sección de Material de Referencia (cheatsheets)
    if cheatsheets:
        lines.append("## 📚 Material de Referencia")
        lines.append("")
        lines.append("| Recurso | Descripción |")
        lines.append("|:--------|:------------|")
        
        cheatsheet_path = cheatsheets[0]  # Solo hay una carpeta cheatsheets
        cheatsheet_files = get_cheatsheet_files(cheatsheet_path)
        
        for filename, display_name in cheatsheet_files:
            encoded_path = f"./cheatsheets/{quote(filename, safe='')}"
            lines.append(f"| [**{display_name}**]({encoded_path}) | Guía de referencia rápida |")
        
        lines.append("")
    
    # Sección de Proyectos Personales
    if ejercicios:
        lines.append("## 🏆 Proyectos Personales")
        lines.append("")
        lines.append("| Proyecto | Descripción |")
        lines.append("|:---------|:------------|")
        
        for ejercicio in ejercicios:
            folder_name = ejercicio.name
            encoded_url = encode_folder_url(folder_name)
            display_name = format_folder_name(folder_name)
            
            description = analyze_folder(ejercicio)
            description = format_methods_with_backticks(description)
            description = description.replace("\n", " ").strip()
            
            lines.append(f"| [**{display_name}**](./{encoded_url}/) | {description} |")
        
        lines.append("")
    
    return "\n".join(lines)


def main():
    """Punto de entrada principal del script."""
    # Determinar la ruta base del repositorio
    script_path = Path(__file__).resolve()
    base_path = script_path.parent.parent
    
    print(f"Escaneando repositorio en: {base_path}")
    
    # Escanear carpetas
    practicas, ejercicios, cheatsheets = scan_folders(base_path)
    
    print(f"Encontradas {len(practicas)} prácticas, {len(ejercicios)} proyectos personales y {len(cheatsheets)} carpetas de referencia")
    
    # Generar README
    readme_content = generate_readme(base_path, practicas, ejercicios, cheatsheets)
    
    # Escribir README
    readme_path = base_path / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")
    
    print(f"README.md actualizado exitosamente")


if __name__ == "__main__":
    main()
