def build_variation_series(sample): #варіаційний ряд
    return sorted(sample)


def calculate_frequencies(sample):  # поява кожного значення у вибірці
    frequencies = {}
    for value in sample:
        frequencies[value] = frequencies.get(value, 0) + 1
    return dict(sorted(frequencies.items()))


def calculate_relative_frequencies(frequencies, total):  # відносні частоти
    relative_freq = {}
    for value, freq in frequencies.items():
        relative_freq[value] = freq / total

    total_sum = sum(relative_freq.values())
    return relative_freq, total_sum

def calculate_empirical_distribution(sample):  # емпірична функція
    n = len(sample)
    unique_values = sorted(set(sample))

    empirical_dist = []

    for i, value in enumerate(unique_values):
        count = sum(1 for x in sample if x < value)
        fx = count / n

        if i == 0:
            interval = f"(-∞, {value})"
        else:
            interval = f"[{unique_values[i - 1]}, {value})"

        empirical_dist.append((value, fx, interval))

    last_value = unique_values[-1]
    empirical_dist.append((last_value, 1.0, f"[{last_value}, +∞)"))

    return empirical_dist