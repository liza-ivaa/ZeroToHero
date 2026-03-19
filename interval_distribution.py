import math

#розраховує інтервали
def calculate_intervals(sample, num_intervals=None):
    n = len(sample)
    x_min = min(sample)
    x_max = max(sample)

    if num_intervals is None:
        num_intervals = round(1 + 3.322 * math.log10(n))

    h = (x_max - x_min) / num_intervals

    intervals = []
    interval_frequencies = []

    for i in range(num_intervals):
        start = x_min + i * h
        end = start + h

        if i == num_intervals - 1:
            count = sum(1 for x in sample if start <= x <= x_max)
            end = x_max
        else:
            count = sum(1 for x in sample if start <= x < end)

        intervals.append((start, end))
        interval_frequencies.append(count)

    return intervals, h, interval_frequencies


#розраховує средини інтервалів
def calculate_interval_midpoints(intervals):

    return [(start + end) / 2 for start, end in intervals]

#середнє вибіркове
def calculate_grouped_mean(midpoints, frequencies): #середнє вибіркова

    n = sum(frequencies)
    weighted_sum = sum(mid * freq for mid, freq in zip(midpoints, frequencies))
    return weighted_sum / n

# розр варіацію
def calculate_grouped_variance(midpoints, frequencies, mean): #дисперсія

    n = sum(frequencies)
    weighted_sum = sum(((mid - mean) ** 2) * freq
                      for mid, freq in zip(midpoints, frequencies))
    return weighted_sum / n

#мода
def calculate_grouped_mode(intervals, frequencies, h):
    """
     Mo = x_Mo + h * (n_Mo - n_{Mo-1}) / ((n_Mo - n_{Mo-1}) + (n_Mo - n_{Mo+1}))
    де x_Mo - початок модального інтервалу,
       h - ширина інтервалу,
       n_Mo - частота модального інтервалу,
       n_{Mo-1} - частота попереднього інтервалу,
       n_{Mo+1} - частота наступного інтервалу
    """
    #   модальний інтервал (з максимальною частотою)
    max_freq_idx = frequencies.index(max(frequencies))

    x_mo = intervals[max_freq_idx][0]
    n_mo = frequencies[max_freq_idx]

    # частота попереднього інтервалу
    n_prev = frequencies[max_freq_idx - 1] if max_freq_idx > 0 else 0

    # частота наступного інтервалу
    n_next = frequencies[max_freq_idx + 1] if max_freq_idx < len(frequencies) - 1 else 0

    denominator = (n_mo - n_prev) + (n_mo - n_next)
    if denominator == 0:
        return x_mo + h / 2

    mode = x_mo + h * (n_mo - n_prev) / denominator
    return mode

#медіана
def calculate_grouped_median(intervals, frequencies):
    """
     Me = x_Me + h * ((n/2 - S_{Me-1}) / n_Me)
    де x_Me - початок медіанного інтервалу,
       h - ширина інтервалу,
       n - обсяг вибірки,
       S_{Me-1} - сума частот до медіанного інтервалу,
       n_Me - частота медіанного інтервалу
    """
    n = sum(frequencies)
    half_n = n / 2

    #  медіанний інтервал
    cumulative = 0
    median_idx = 0

    for i, freq in enumerate(frequencies):
        cumulative += freq
        if cumulative >= half_n:
            median_idx = i
            break

    x_me = intervals[median_idx][0]
    x_me_end = intervals[median_idx][1]
    h = x_me_end - x_me
    n_me = frequencies[median_idx]

    # Сума частот до медіанного інтервалу
    s_prev = sum(frequencies[:median_idx])

    # Обчислюємо медіану
    if n_me == 0:
        return (x_me + x_me_end) / 2

    median = x_me + h * ((half_n - s_prev) / n_me)
    return median

def calculate_grouped_initial_moments(midpoints, frequencies, order): #початкові моменти
    """
     m_k = Σ(x_i^k * n_i) / n
    де x_i - середина i-го інтервалу,
        n_i - частота i-го інтервалу,
        n - загальний обсяг вибірки
    """
    n = sum(frequencies)
    weighted_sum = sum((mid ** order) * freq for mid, freq in zip(midpoints, frequencies))
    return weighted_sum / n

def calculate_grouped_moments(midpoints, frequencies, mean, order): #центральні моменти
    """
    μ_k = Σ(x_i - x̅)^k * n_i / n
    """
    n = sum(frequencies)
    weighted_sum = sum(((mid - mean) ** order) * freq
                      for mid, freq in zip(midpoints, frequencies))
    return weighted_sum / n

#емпірична функція розподілу
def calculate_interval_empirical_distribution(intervals, frequencies):
    """
    Формула: F*(x) = S_i / n
    де S_i - сума частот всіх інтервалів до i-го включно,
       n - загальний обсяг вибірки
    """
    n = sum(frequencies)
    cumulative = 0
    empirical_dist = []

    for i, (start, end) in enumerate(intervals):
        cumulative += frequencies[i]
        fx = cumulative / n
        empirical_dist.append((end, fx, f"[{start:.2f}, {end:.2f})"))

    return empirical_dist