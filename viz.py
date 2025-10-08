"""Petite librairie utilitaire pour les visualisations réutilisables.

Contient :
- visualization(data, column, lower_limit=None, upper_limit=None)

Usage dans un notebook :
from viz import visualization
visualization(dataset, 'Glucose', lower_limit=..., upper_limit=...)
"""

import matplotlib.pyplot as plt
import seaborn as sbn


def visualization(data, column, lower_limit=None, upper_limit=None):
    """Affiche un boxplot et un histogramme KDE pour la colonne donnée.

    Args:
        data (pd.DataFrame): le DataFrame contenant la colonne.
        column (str): nom de la colonne à tracer.
        lower_limit (float|None): ligne horizontale inférieure (optionnelle).
        upper_limit (float|None): ligne horizontale supérieure (optionnelle).
    """
    fig, axes = plt.subplots(1, 2, figsize=(18, 5))

    # BoxPlot (avec des limites si définies)
    sbn.boxplot(data=data, y=column, ax=axes[0], color="skyblue")

    if upper_limit is not None:
        axes[0].axhline(y=upper_limit, color="red", linestyle="--", linewidth=1, label=f"Limit sup:{upper_limit:.2f}")
    if lower_limit is not None:
        axes[0].axhline(y=lower_limit, color="red", linestyle="--", linewidth=1, label=f"Limit inf:{lower_limit:.2f}")

    axes[0].set_title(f"Boxplot de {column}")
    try:
        axes[0].legend()
    except Exception:
        pass

    # Histogramme avec KDE (et Limites si définies)
    sbn.histplot(data[column], kde=True, ax=axes[1], color="orange")

    if upper_limit is not None:
        axes[1].axvline(x=upper_limit, color="red", linestyle="--", linewidth=1, label=f"Limit sup:{upper_limit:.2f}")
    if lower_limit is not None:
        axes[1].axvline(x=lower_limit, color="red", linestyle="--", linewidth=1, label=f"Limit inf:{lower_limit:.2f}")

    axes[1].set_title(f"Distribution de {column}")
    try:
        axes[1].legend()
    except Exception:
        pass

    plt.title(f"{column}")
    plt.tight_layout()
    plt.show()
