import math

#мод
def calculate_mode(frequencies):

    max_freq = max(frequencies.values())
    modes = [value for value, freq in frequencies.items() if freq == max_freq]
    return modes


def calculate_median(variation_series):

    n = len(variation_series)

    if n % 2 == 1:
        return variation_series[n // 2]
    else:
        mid1 = variation_series[n // 2 - 1]
        mid2 = variation_series[n // 2]
        return (mid1 + mid2) / 2


def calculate_mean(sample): #середнє вибіркове

    n = len(sample)
    return sum(sample) / n


def calculate_range(variation_series): #розмах

    return variation_series[-1] - variation_series[0]


def calculate_variance(sample, mean): #вибіркова дисперсія

    n = len(sample)
    variance = sum((x - mean) ** 2 for x in sample) / n
    return variance


def calculate_sample_variance(sample, mean): #Виправлена дисперсія (S^2)

    n = len(sample)
    sample_var = sum((x - mean) ** 2 for x in sample) / (n - 1)
    return sample_var


def calculate_standard_deviation(sample_variance):#стандартне відхилення

    return math.sqrt(sample_variance)


def calculate_coefficient_of_variation(std_dev, mean): #коефіціент варіації

    if mean == 0:
        return 0
    return (std_dev / abs(mean)) * 100


def calculate_initial_moment(sample, mean, order): #початкові моменти

    n = len(sample)
    moment = sum(x ** order for x in sample) / n
    return moment


def calculate_central_moment(sample, mean, order): #центральні моменти

    n = len(sample)
    moment = sum((x - mean) ** order for x in sample) / n
    return moment


def calculate_skewness(mu3, variance): #асиметрія

    if variance == 0:
        return 0
    sigma = math.sqrt(variance)
    return mu3 / (sigma ** 3)


def calculate_kurtosis(mu4, variance): #ексцес

    if variance == 0:
        return 0
    sigma = math.sqrt(variance)
    return (mu4 / (sigma ** 4)) - 3