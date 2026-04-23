# 04_modelado - Modelado

## Propósito
Feature engineering, entrenamiento y almacenamiento de modelos ML.

## Subcarpetas
- `features/`: Scripts de ingeniería de features
- `models/`: Modelos entrenados (.pkl, .joblib)

## Contenido esperado
- Scripts de feature engineering
- Modelos entrenados versionados
- Métricas de training

## Convenciones de versionado
- Formato: `model_v{VERSION}_{ALGORITMO}.pkl`
- Ejemplo: `model_v1_xgboost.pkl`, `model_v2_random_forest.joblib`
- Siempre guardar también hiperparámetros (JSON)

## Archivos relevantes
- `README.md` (este archivo)