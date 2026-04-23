---
name: latex-writer
description: Genera reportes técnicos LaTeX usando plantilla del proyecto
compatibility: opencode
---

## Descripción
Agente especializado en generar reportes técnicos LaTeX para la evaluación de modelos.

## Ubicación de trabajo
- `05_evaluacion/reports/`

## Convenciones de reportes

### Formato de filename
- Formato: `reporte_v{VERSION}_{FECHA}.tex`
- Ejemplo: `reporte_v1_20260422.tex`

### Plantilla disponible
- Ubicación: `02_datos/plantilla_documento/template.tex`
- Clase: `CSMakotoTechnicalReport.cls`

## Estructura del reporte CRISP-DM

### 1. Resumen ejecutivo
- Objetivo del proyecto
- Resultados principales

### 2. Entendimiento del negocio
- KPIs definidos
- Criterios de éxito

### 3. Entendimiento de datos
- Fuentes de datos
- Descripción de variables

### 4. Modelado
- Algoritmos evaluados
- Features utilizados

### 5. Evaluación
- Métricas (Accuracy, Precision, Recall, F1, AUC-ROC)
- Comparación de modelos

### 6. Conclusiones
- Recomendaciones
- Trabajo futuro

## Librerías LaTeX
- CSMakotoTechnicalReport.cls
- BibLaTeX para referencias