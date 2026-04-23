#-----------------------------------
#     DETERMINAR EL PORCENTAJE DE VALORES FALTANTES EN EL DATASET
#----------------------------------
import pandas as pd
from typing import Dict

CHUNK_SIZE = 1_000_000
FILE = "02_datos/raw/dataset_unido.csv"
OUTPUT = "03_exploracion/valores_faltantes_resultado.csv"


def analizar(filepath: str, chunk_size: int = CHUNK_SIZE) -> Dict[str, float]:
    """Analiza porcentaje de valores faltantes con chunks."""
    total_rows = 0
    missing_counts = {}

    print(f"Archivo: {filepath}")
    print(f"Chunk size: {chunk_size:,}\n")

    for chunk_num, chunk in enumerate(pd.read_csv(filepath, chunksize=chunk_size, low_memory=False), 1):
        total_rows += len(chunk)
        print(f"Chunk {chunk_num}: {total_rows:,} filas procesadas")

        for col in chunk.columns:
            if col not in missing_counts:
                missing_counts[col] = 0
            missing_counts[col] += chunk[col].isna().sum()

    missing_percent = {col: (count / total_rows) * 100 for col, count in missing_counts.items()}

    results = pd.DataFrame({
        'columna': list(missing_percent.keys()),
        'nulos': [missing_counts[c] for c in missing_percent],
        'porcentaje': list(missing_percent.values()),
        'total': total_rows
    }).sort_values('porcentaje', ascending=False)

    results.to_csv(OUTPUT, index=False)
    return missing_percent


if __name__ == "__main__":
    result = analizar(FILE)

    print("\n" + "=" * 50)
    print("RESUMEN")
    print("=" * 50)
    for col, pct in result.items():
        if pct > 0:
            print(f"  {col}: {pct:.2f}%")