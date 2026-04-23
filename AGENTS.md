# AGENTS.md - Proyecto AtencionesMedicas_DataMining

## Configuración del entorno

- **Lenguaje**: Python (via Anaconda3)
- **Gestor de paquetes**: Conda/pip
- **Activar entorno**: `conda activate <nombre_entorno>`

## Estructura del proyecto (CRISP-DM)

```
atenciones_medicas_mining/
├── 01_negocio/          # Entendimiento del negocio
│   └── README.md
├── 02_datos/           # Entendimiento de datos
│   ├── raw/             # Datos crudos (NO modificar)
│   └── README.md
├── 03_exploracion/     # Preparación de datos
│   ├── notebooks/      # Jupyter EDA
│   ├── scripts/       # Scripts Python
│   └── README.md
├── 04_modelado/        # Modelado
│   ├── features/       # Feature engineering
│   ├── models/        # Modelos (.pkl, .joblib)
│   └── README.md
├── 05_evaluacion/      # Evaluación
│   ├── reports/       # Reportes LaTeX/PDF
│   └── README.md
├── 06_despliegue/      # Despliegue (si aplica)
├── tests/             # Pytest
└── data/              # Datos procesados
```

## Comandos esenciales

```bash
# Crear ambiente conda
conda create -n atenciones python=3.11 pandas numpy matplotlib scikit-learn seaborn jupyter
conda activate atenciones

# Instalar librerías adicionales
conda install -c conda-forge xgboost lightgbm joblib great-expectations

# Jupyter
jupyter notebook

# Exportar entorno
conda env export > environment.yml
```

## Convenciones

- **Notebooks**: `%Y%mdd_nombre.ipynb` (ej: 20260422_eda_atenciones.ipynb)
- **Modelos**: `model_v{VERSION}_{ALGORITMO}.pkl` (ej: model_v1_xgboost.pkl)
- **Scripts**: snake_case con prefijo (ej: cleaning_datos.py, transform_features.py)
- **Reportes LaTeX**: `reporte_v{VERSION}_{FECHA}.tex`
- **Datos crudos**: NUNCA modificar en `02_datos/raw/`

## Flujo CRISP-DM

1. **01_negocio/**: Definir objetivos, KPIs, éxito
2. **02_datos/**: Recopilar datos crudos,documentar fuentes
3. **03_exploracion/**: EDA, limpieza, transformación
4. **04_modelado/**: Features, entrenamiento
5. **05_evaluacion/**: Métricas, reportes
6. **06_despliegue/**: Pipeline producción

## Agentes

- **Code writer**: Crear scripts en `03_exploracion/scripts/` y `04_modelado/features/`
- **Code reviewer**: Verificar convenciones, lint (ruff/flake8)
- **LaTeX writer**: Generar reportes en `05_evaluacion/reports/`

## Referencias

- Metodología CRISP-DM: https://www.datascience-pm.com/crisp-dm-2/