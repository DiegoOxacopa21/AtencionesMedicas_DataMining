import pandas as pd
import os
from datetime import datetime

INPUT_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\dataset_sin_columnas.csv'
OUTPUT_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\dataset_limpio.csv'
REPORT_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\reportes\1_reporte_eliminar_filas_y_columnas.txt'

print('=' * 50)
print('ELIMINAR REGISTROS CON NULOS')
print('=' * 50)

print('\n[1] Contando registros totales y con nulos...')
total = 0
con_nulos = 0

for chunk in pd.read_csv(INPUT_FILE, chunksize=2000000, low_memory=False):
    total += len(chunk)
    con_nulos += chunk.isnull().any(axis=1).sum()
    print(f'  {total:,} regs | Nulos: {con_nulos:,}')

print(f'\n  Total: {total:,} | Con nulos: {con_nulos:,} ({con_nulos/total*100:.2f}%)')

print('\n[2] Eliminando registros con nulos...')
guardados = 0

for idx, chunk in enumerate(pd.read_csv(INPUT_FILE, chunksize=2000000, low_memory=False)):
    limpio = chunk.dropna()
    guardados += len(limpio)
    mode = 'w' if idx == 0 else 'a'
    header = idx == 0
    limpio.to_csv(OUTPUT_FILE, index=False, mode=mode, header=header)
    print(f'  Chunk {idx+1}: {guardados:,} regs')

print(f'\n  Finales: {guardados:,}')

print('\n[3] Validando...')
nulos_val = 0
for chunk in pd.read_csv(OUTPUT_FILE, chunksize=2000000, low_memory=False):
    nulos_val += chunk.isnull().any(axis=1).sum()

print(f'  Nulos restantes: {nulos_val}')

print('\n[4] Generando reporte...')
reporte = f"""================================================================================
REPORTE DE ELIMINACION - VALORES FALTANTES Y COLUMNAS INNECESARIAS
================================================================================
Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Archivo origen: {INPUT_FILE}
Archivo destino: {OUTPUT_FILE}

--------------------------------------------------------------------------------
ANTES DE LA LIMPIEZA
--------------------------------------------------------------------------------
- Total de registros: {total:,}
- Registros con valores nulos: {con_nulos:,}
- Porcentaje de registros con nulos: {con_nulos/total*100:.2f}%

--------------------------------------------------------------------------------
COLUMNAS ELIMINADAS (7)
--------------------------------------------------------------------------------
- DESC_UNIDAD_EJECUTORA
- IPRESS
- PLAN_SEGURO
- COD_SERVICIO
- DESC_SERVICIO
- SEXO
- GRUPO_EDAD

--------------------------------------------------------------------------------
DESPUES DE LA LIMPIEZA
--------------------------------------------------------------------------------
- Total de registros finales: {guardados:,}
- Registros eliminados: {total - guardados:,}
- Porcentaje de registros eliminados: {(total - guardados)/total*100:.2f}%

--------------------------------------------------------------------------------
VALIDACION
--------------------------------------------------------------------------------
- Nulos encontrados en dataset limpio: {nulos_val}
- Estado: {'APROBADO - Sin valores nulos' if nulos_val == 0 else 'FALLADO'}

================================================================================
"""

with open(REPORT_FILE, 'w', encoding='utf-8') as f:
    f.write(reporte)

print(f'Reporte: {REPORT_FILE}')
print('>>> COMPLETADO <<<')