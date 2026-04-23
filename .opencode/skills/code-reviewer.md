# Code Reviewer Skill

## Descripción
Agente especializado en verificar convenciones de código, calidad y linting.

## Tareas
- Verificar nombres de archivos contra convenciones del proyecto
- Ejecutar linting con ruff/flake8
- Revisar calidad de código Python

## Convenciones del proyecto (AGENTS.md)

### Scripts
- snake_case con prefijo: `cleaning_`, `transform_`, `feature_`, `train_`, `evaluate_`
- Ejemplo: `cleaning_datos.py`, `transform_features.py`

### Notebooks
- Formato: `%Y%mdd_nombre.ipynb`
- Ejemplo: `20260422_eda_atenciones.ipynb`

### Modelos
- Formato: `model_v{VERSION}_{ALGORITMO}.pkl`
- Ejemplo: `model_v1_xgboost.pkl`

## Comandos de linting
```bash
# Python lint
ruff check .
flake8 .

# Type check
mypy .

# Formatter
ruff format .
```

## Reglas de calidad
- No agregar comentarios innecesarios
- Usar type hints cuando sea posible
- docstrings en funciones públicas
- Manejo de errores apropiado