import os
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def visualizar_datos(
    fuente: str = "data/raw/bank-additional-full.csv",
    salida: str = "docs/figures",
):
    # Crear directorio de salida
    Path(salida).mkdir(parents=True, exist_ok=True)

    # Leer datos
    df = pd.read_csv(fuente, sep=";")

    # Gráfico 1: Distribución de la variable objetivo (y)
    ax = df["y"].value_counts().plot(kind="bar")
    ax.set_title("Distribución de la variable objetivo (y)")
    ax.set_xlabel("y")
    ax.set_ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(os.path.join(salida, "distribucion_target.png"))
    plt.close()

    # Gráfico 2: Distribución de educación (education)
    ax = df["education"].value_counts().plot(kind="barh")
    ax.set_title("Distribución de education")
    ax.set_xlabel("Cantidad")
    ax.set_ylabel("education")
    plt.tight_layout()
    plt.savefig(os.path.join(salida, "distribucion_education.png"))
    plt.close()

    print(f"OK: gráficos guardados en {salida}")


if __name__ == "__main__":
    visualizar_datos()