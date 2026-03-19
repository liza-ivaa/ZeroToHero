"""
visualization.py

Замість збереження .png файлів — кожна функція повертає словник
з даними для побудови графіка на фронтенді (Chart.js, D3, Plotly тощо).

Структура відповіді кожної функції:
{
    "type":   тип графіка ("line" | "bar" | "step"),
    "title":  заголовок,
    "xlabel": підпис осі X,
    "ylabel": підпис осі Y,
    "datasets": [ { "label": ..., "data": [...] } ],
    ...  (додаткові поля залежно від типу)
}
"""


def get_frequency_polygon_data(frequencies: dict) -> dict:
    """
    Полігон частот.
    frequencies: { значення: кількість, ... }
    """
    values = list(frequencies.keys())
    freqs  = list(frequencies.values())

    return {
        "type":   "line",
        "title":  "Полігон частот",
        "xlabel": "Значення",
        "ylabel": "Частота",
        "datasets": [
            {
                "label": "Частоти",
                "data":  [{"x": x, "y": y} for x, y in zip(values, freqs)],
                "color": "#3b82f6",
            }
        ],
    }


def get_relative_frequency_polygon_data(relative_frequencies: dict) -> dict:
    """
    Полігон відносних частот.
    relative_frequencies: { значення: відносна_частота, ... }
    """
    values    = list(relative_frequencies.keys())
    rel_freqs = list(relative_frequencies.values())

    return {
        "type":   "line",
        "title":  "Полігон відносних частот",
        "xlabel": "Значення",
        "ylabel": "Відносна частота",
        "datasets": [
            {
                "label": "Відносні частоти",
                "data":  [{"x": x, "y": round(y, 6)} for x, y in zip(values, rel_freqs)],
                "color": "#22c55e",
            }
        ],
    }


def get_empirical_distribution_data(empirical_dist: list) -> dict:
    """
    Емпірична функція розподілу F*(x) — ступінчастий графік.
    empirical_dist: список кортежів (value, fx, interval_label)
    """
    points = [{"x": value, "y": round(fx, 6), "interval": interval}
              for value, fx, interval in empirical_dist]

    return {
        "type":   "step",
        "title":  "Емпірична функція розподілу F*(x)",
        "xlabel": "x",
        "ylabel": "F*(x)",
        "y_min":  0,
        "y_max":  1,
        "datasets": [
            {
                "label": "F*(x)",
                "data":  points,
                "color": "#ef4444",
            }
        ],
    }


def get_interval_histogram_data(intervals: list, frequencies: list) -> dict:
    """
    Гістограма інтервального розподілу.
    intervals:   список кортежів (start, end)
    frequencies: список частот для кожного інтервалу
    """
    bars = [
        {
            "label": f"[{start:.2f}, {end:.2f})",
            "x_start": round(start, 6),
            "x_end":   round(end, 6),
            "width":   round(end - start, 6),
            "midpoint": round((start + end) / 2, 6),
            "frequency": freq,
        }
        for (start, end), freq in zip(intervals, frequencies)
    ]

    return {
        "type":   "bar",
        "title":  "Гістограма інтервального розподілу",
        "xlabel": "Інтервали",
        "ylabel": "Частота",
        "datasets": [
            {
                "label": "Частоти",
                "data":  bars,
                "color": "#38bdf8",
            }
        ],
    }


def get_interval_empirical_distribution_data(interval_empirical_dist: list) -> dict:
    """
    Емпірична функція для інтервального розподілу — ступінчастий графік.
    interval_empirical_dist: список кортежів (end_value, fx, interval_label)
    """
    points = [
        {"x": round(end_value, 6), "y": round(fx, 6), "interval": interval}
        for end_value, fx, interval in interval_empirical_dist
    ]

    return {
        "type":   "step",
        "title":  "Емпірична функція розподілу для інтервального розподілу F*(x)",
        "xlabel": "x (межі інтервалів)",
        "ylabel": "F*(x)",
        "y_min":  0,
        "y_max":  1,
        "datasets": [
            {
                "label": "F*(x) для інтервалів",
                "data":  points,
                "color": "#a855f7",
            }
        ],
    }


def get_all_charts_data(
    frequencies: dict,
    relative_frequencies: dict,
    empirical_dist: list,
    intervals: list = None,
    interval_frequencies: list = None,
    interval_empirical_dist: list = None,
) -> dict:
    """
    Повертає всі графіки одним словником.
    Ключі відповідають назвам графіків — зручно передавати як JSON у відповіді API.
    """
    charts = {}

    if frequencies:
        charts["frequency_polygon"] = get_frequency_polygon_data(frequencies)

    if relative_frequencies:
        charts["relative_frequency_polygon"] = get_relative_frequency_polygon_data(
            relative_frequencies
        )

    if empirical_dist:
        charts["empirical_distribution"] = get_empirical_distribution_data(empirical_dist)

    if intervals and interval_frequencies:
        charts["interval_histogram"] = get_interval_histogram_data(
            intervals, interval_frequencies
        )

    if interval_empirical_dist:
        charts["interval_empirical_distribution"] = get_interval_empirical_distribution_data(
            interval_empirical_dist
        )

    return charts