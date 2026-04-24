# -------------------------------------------------------
# Limpieza de Inconsistencias (Data Cleansing Lógico)
# ----------------------------------------------------
# Planteamiento: 
#       Detectar y corregir valores erróneos o fuera de rango producto de errores de registro
# 
# Ejecución/Estrategia:
#       Un hospital no puede tener un NIVEL_EESS que sea una letra inválida (solo I, II, III), ni puede haber ATENCIONES negativas. Crearemos filtros lógicos.
# OBJETIVOS: 
#       1. NIVEL_EESS: Solo se mantienen valores I, II o III
#       2. ATENCIONES: Solo se mantienen valores > 0
# #



import pandas as pd
import os
from datetime import datetime

INPUT_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\3_dataset_limpio.csv'
OUTPUT_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\4_dataset_inconsistencias.csv'
TEMP_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\temp_inconsistencias.csv'
REPORT_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\reportes\2_reporte_limpieza_inconsistencias.txt'

NIVEL_VALIDOS = {'I', 'II', 'III'}

print('=' * 60)
print('LIMPIEZA DE INCONSISTENCIAS')
print('=' * 60)

print('\n[1] Contando registros iniciales y anomalias...')
total = 0
nivel_invalidos = 0
atenciones_invalidos = 0

for chunk in pd.read_csv(INPUT_FILE, chunksize=2000000, low_memory=False):
    total += len(chunk)
    nivel_invalidos += (~chunk['NIVEL_EESS'].isin(NIVEL_VALIDOS)).sum()
    atenciones_invalidos += (chunk['ATENCIONES'] <= 0).sum()
    print(f'  {total:,} regs | NIVEL invalidos: {nivel_invalidos:,} | ATENCIONES <=0: {atenciones_invalidos:,}')

print(f'\n  Total inicial: {total:,}')
print(f'  NIVEL_EESS no I/II/III: {nivel_invalidos:,}')
print(f'  ATENCIONES <= 0: {atenciones_invalidos:,}')

print('\n[2] Aplicando filtros...')

guardados = 0
for idx, chunk in enumerate(pd.read_csv(INPUT_FILE, chunksize=2000000, low_memory=False)):
    mask_nivel = chunk['NIVEL_EESS'].isin(NIVEL_VALIDOS)
    mask_aten = chunk['ATENCIONES'] > 0
    chunk_limpio = chunk[mask_nivel & mask_aten]
    guardados += len(chunk_limpio)
    
    mode = 'w' if idx == 0 else 'a'
    header = idx == 0
    chunk_limpio.to_csv(OUTPUT_FILE, index=False, mode=mode, header=header)
    print(f'  Chunk {idx+1}: {len(chunk_limpio):,} guardados')

print(f'\n  Registros finales: {guardados:,}')
print(f'  Archivo creado: {OUTPUT_FILE}')

total_eliminados = total - guardados
pct_eliminado = (total_eliminados / total * 100) if total > 0 else 0

reporte = f"""================================================================================
REPORTE DE LIMPIEZA DE INCONSISTENCIAS
================================================================================
Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Archivo: {INPUT_FILE}

--------------------------------------------------------------------------------
RESUMEN ANTES
--------------------------------------------------------------------------------
- Total de registros: {total:,}

--------------------------------------------------------------------------------
FILTROS APLICADOS
--------------------------------------------------------------------------------
1. NIVEL_EESS: Solo se mantienen valores I, II o III
2. ATENCIONES: Solo se mantienen valores > 0

--------------------------------------------------------------------------------
RESULTADOS
--------------------------------------------------------------------------------
- Registros eliminados por NIVEL_EESS invalido: {nivel_invalidos:,}
- Registros eliminados por ATENCIONES <= 0: {atenciones_invalidos:,}
- Total registros eliminados: {total_eliminados:,}
- Porcentaje eliminado: {pct_eliminado:.2f}%

--------------------------------------------------------------------------------
RESUMEN DESPUES
--------------------------------------------------------------------------------
- Total de registros finales: {guardados:,}
- Estado: {'LIMPIO - Sin cambios' if total_eliminados == 0 else f'LIMPIO - Eliminados {total_eliminados:,} registros'}

================================================================================
"""

with open(REPORT_FILE, 'w', encoding='utf-8') as f:
    f.write(reporte)

print(f'Reporte: {REPORT_FILE}')
print('>>> COMPLETADO <<<')