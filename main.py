import math

from data_generation import (
    build_variation_series, calculate_frequencies,
    calculate_relative_frequencies, calculate_empirical_distribution
)
from numeric_characteristics import (
    calculate_mode, calculate_median, calculate_mean, calculate_range,
    calculate_variance, calculate_sample_variance, calculate_standard_deviation,
    calculate_coefficient_of_variation, calculate_initial_moment,
    calculate_central_moment, calculate_skewness, calculate_kurtosis
)
from interval_distribution import (
    calculate_intervals, calculate_interval_midpoints, calculate_grouped_mean,
    calculate_grouped_variance, calculate_grouped_mode, calculate_grouped_median,
    calculate_grouped_moments, calculate_interval_empirical_distribution,
    calculate_grouped_initial_moments
)


def parse_sample(raw_input: str) -> list[float]:
    """
    Приймає рядок із числами (через пробіл, кому, таб або новий рядок).
    Повертає список float.
    Кидає ValueError якщо немає жодного числа.
    """
    content = raw_input.replace(',', ' ').replace('\t', ' ').replace('\n', ' ')
    values = content.split()

    sample = []
    for value in values:
        try:
            sample.append(round(float(value), 2))
        except ValueError:
            pass

    if not sample:
        raise ValueError("Введені дані не містять числових значень")

    return sample


# ── Варіаційний ряд і частоти ────────────────────────────────────────────────

def get_variation_series(sample: list) -> list:
    return build_variation_series(sample)


def get_frequencies(sample: list) -> dict:
    return calculate_frequencies(sample)


def get_relative_frequencies(sample: list) -> tuple[dict, float]:
    freq = calculate_frequencies(sample)
    return calculate_relative_frequencies(freq, len(sample))


def get_empirical_distribution(sample: list) -> list:
    variation_series = build_variation_series(sample)
    return calculate_empirical_distribution(variation_series)


# ── Числові характеристики ────────────────────────────────────────────────────

def get_mode(sample: list) -> list:
    freq = calculate_frequencies(sample)
    return calculate_mode(freq)


def get_median(sample: list) -> float:
    var_series = build_variation_series(sample)
    return calculate_median(var_series)


def get_mean(sample: list) -> float:
    return calculate_mean(sample)


def get_range(sample: list) -> float:
    var_series = build_variation_series(sample)
    return calculate_range(var_series)


def get_variance(sample: list) -> float:
    mean = calculate_mean(sample)
    return calculate_variance(sample, mean)


def get_sample_variance(sample: list) -> float:
    mean = calculate_mean(sample)
    return calculate_sample_variance(sample, mean)


def get_standard_deviation(sample: list) -> float:
    mean = calculate_mean(sample)
    sample_var = calculate_sample_variance(sample, mean)
    return calculate_standard_deviation(sample_var)


def get_coefficient_of_variation(sample: list) -> float:
    mean = calculate_mean(sample)
    sample_var = calculate_sample_variance(sample, mean)
    std_dev = calculate_standard_deviation(sample_var)
    return calculate_coefficient_of_variation(std_dev, mean)


def get_initial_moments(sample: list) -> dict:
    mean = calculate_mean(sample)
    return {
        'm1': calculate_initial_moment(sample, mean, 1),
        'm2': calculate_initial_moment(sample, mean, 2),
        'm3': calculate_initial_moment(sample, mean, 3),
        'm4': calculate_initial_moment(sample, mean, 4),
    }


def get_central_moments(sample: list) -> dict:
    mean = calculate_mean(sample)
    return {
        'mu2': calculate_central_moment(sample, mean, 2),
        'mu3': calculate_central_moment(sample, mean, 3),
        'mu4': calculate_central_moment(sample, mean, 4),
    }


def get_skewness(sample: list) -> float:
    mean = calculate_mean(sample)
    variance = calculate_variance(sample, mean)
    mu3 = calculate_central_moment(sample, mean, 3)
    return calculate_skewness(mu3, variance)


def get_kurtosis(sample: list) -> float:
    mean = calculate_mean(sample)
    variance = calculate_variance(sample, mean)
    mu4 = calculate_central_moment(sample, mean, 4)
    return calculate_kurtosis(mu4, variance)


def get_all_characteristics(sample: list) -> dict:
    """Повертає всі числові характеристики одним словником."""
    var_series = build_variation_series(sample)
    freq = calculate_frequencies(sample)
    mean = calculate_mean(sample)

    variance = calculate_variance(sample, mean)
    sample_var = calculate_sample_variance(sample, mean)
    std_dev = calculate_standard_deviation(sample_var)

    mu2 = calculate_central_moment(sample, mean, 2)
    mu3 = calculate_central_moment(sample, mean, 3)
    mu4 = calculate_central_moment(sample, mean, 4)

    return {
        'mean':       mean,
        'mode':       calculate_mode(freq),
        'median':     calculate_median(var_series),
        'range':      calculate_range(var_series),
        'variance':   variance,
        'sample_var': sample_var,
        'std_dev':    std_dev,
        'coef_var':   calculate_coefficient_of_variation(std_dev, mean),
        'm1':         calculate_initial_moment(sample, mean, 1),
        'm2':         calculate_initial_moment(sample, mean, 2),
        'm3':         calculate_initial_moment(sample, mean, 3),
        'm4':         calculate_initial_moment(sample, mean, 4),
        'mu2':        mu2,
        'mu3':        mu3,
        'mu4':        mu4,
        'skewness':   calculate_skewness(mu3, variance),
        'kurtosis':   calculate_kurtosis(mu4, variance),
    }


# ── Інтервальний розподіл ─────────────────────────────────────────────────────

def get_interval_distribution(sample: list, num_intervals: int = None) -> dict:
    """
    Повертає словник з усіма даними інтервального розподілу:
      intervals, h, frequencies, midpoints
    """
    intervals, h, freq = calculate_intervals(sample, num_intervals)
    midpoints = calculate_interval_midpoints(intervals)
    return {
        'intervals':   intervals,
        'h':           h,
        'frequencies': freq,
        'midpoints':   midpoints,
    }


def get_interval_empirical_distribution(sample: list, num_intervals: int = None) -> list:
    data = get_interval_distribution(sample, num_intervals)
    return calculate_interval_empirical_distribution(
        data['intervals'], data['frequencies']
    )


def get_grouped_characteristics(sample: list, num_intervals: int = None) -> dict:
    """Числові характеристики для згрупованих (інтервальних) даних."""
    data = get_interval_distribution(sample, num_intervals)
    midpoints  = data['midpoints']
    freq       = data['frequencies']
    intervals  = data['intervals']
    h          = data['h']

    mean   = calculate_grouped_mean(midpoints, freq)
    var    = calculate_grouped_variance(midpoints, freq, mean)
    std    = math.sqrt(var)
    coef_v = (std / abs(mean)) * 100 if mean != 0 else 0

    mu2 = calculate_grouped_moments(midpoints, freq, mean, 2)
    mu3 = calculate_grouped_moments(midpoints, freq, mean, 3)
    mu4 = calculate_grouped_moments(midpoints, freq, mean, 4)

    return {
        'mean':     mean,
        'mode':     calculate_grouped_mode(intervals, freq, h),
        'median':   calculate_grouped_median(intervals, freq),
        'variance': var,
        'std_dev':  std,
        'coef_var': coef_v,
        'mu2':      mu2,
        'mu3':      mu3,
        'mu4':      mu4,
        'skewness': calculate_skewness(mu3, var),
        'kurtosis': calculate_kurtosis(mu4, var),
    }


def get_grouped_initial_moments(sample: list, num_intervals: int = None) -> dict:
    data = get_interval_distribution(sample, num_intervals)
    midpoints = data['midpoints']
    freq      = data['frequencies']
    return {
        'm1': calculate_grouped_initial_moments(midpoints, freq, 1),
        'm2': calculate_grouped_initial_moments(midpoints, freq, 2),
        'm3': calculate_grouped_initial_moments(midpoints, freq, 3),
        'm4': calculate_grouped_initial_moments(midpoints, freq, 4),
    }