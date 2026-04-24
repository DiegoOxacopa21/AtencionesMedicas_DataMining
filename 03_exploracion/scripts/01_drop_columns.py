import pandas as pd
import os
from datetime import datetime

INPUT_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\raw\dataset_unido.csv'
OUTPUT_FILE = r'C:\Users\diego\dev\projects\AtencionesMedicas_DataMining\02_datos\dataset_sin_columnas.csv'

COLS_TO_DROP = [
    'DESC_UNIDAD_EJECUTORA',
    'IPRESS',
    'PLAN_SEGURO',
    'COD_SERVICIO',
    'DESC_SERVICIO',
    'SEXO',
    'GRUPO_EDAD'
]

print('=' * 50)
print('ELIMINAR COLUMNAS')
print('=' * 50)

for idx, chunk in enumerate(pd.read_csv(INPUT_FILE, chunksize=2000000, low_memory=False)):
    chunk = chunk.drop(columns=COLS_TO_DROP, errors='ignore')
    mode = 'w' if idx == 0 else 'a'
    header = idx == 0
    chunk.to_csv(OUTPUT_FILE, index=False, mode=mode, header=header)
    print(f'Chunk {idx+1}: OK')

print(f'\nArchivo guardado: {OUTPUT_FILE}')
print('>>> COMPLETADO <<<')