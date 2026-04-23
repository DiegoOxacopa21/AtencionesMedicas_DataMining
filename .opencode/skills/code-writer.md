# Code Writer Skill

## Descripción
Agente especializado en crear scripts Python y código para el proyecto de Data Mining según metodología CRISP-DM.

## Ubicaciones de trabajo
- `03_exploracion/scripts/` - Scripts de limpieza, transformación y exploración
- `04_modelado/features/` - Feature engineering y scripts de modelado

## Convenciones de código

### Scripts de exploración (`03_exploracion/scripts/`)
- Prefijo: `cleaning_`, `transform_`, `explore_`
- Ejemplo: `cleaning_datos.py`, `transform_features.py`

### Scripts de modelado (`04_modelado/features/`)
- Prefijo: `feature_`, `train_`, `evaluate_`
- Ejemplo: `feature_engineering.py`, `train_model.py`

### Notebooks (`03_exploracion/notebooks/`)
- Formato: `%Y%mdd_nombre.ipynb`
- Ejemplo: `20260422_eda_atenciones.ipynb`

### Modelos (`04_modelado/models/`)
- Formato: `model_v{VERSION}_{ALGORITMO}.pkl`
- Ejemplo: `model_v1_xgboost.pkl`

## Requisitos
- Usar imports absolutos desde la raíz del proyecto
- Agregar docstrings a todas las funciones
- Manejo de errores con try/except
- Logging para debugging

## Librerías disponibles
- pandas, numpy, matplotlib, seaborn
- scikit-learn, xgboost, lightgbm
- joblib, great-expectations