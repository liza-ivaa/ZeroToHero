document.getElementById('calculateBtn').addEventListener('click', function () {
    let input = document.getElementById('dataInput').value;

    if (input.trim() === "") {
        alert("Будь ласка, введіть числа!");
        return;
    }

    // 1. Парсинг
    let numbers = input.split(",").map(n => parseFloat(n.trim())).filter(n => !isNaN(n));

    if (numbers.length === 0) {
        alert("Введіть коректні числа через кому!");
        return;
    }

    // 2. Розрахунки
    let sorted = [...numbers].sort((a, b) => a - b);

    // Середнє
    let sum = numbers.reduce((a, b) => a + b, 0);
    let mean = sum / numbers.length;

    // Медіана
    let mid = Math.floor(sorted.length / 2);
    let median = sorted.length % 2 !== 0 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;

    // Мода
    let counts = {};
    let maxFreq = 0;
    numbers.forEach(n => {
        counts[n] = (counts[n] || 0) + 1;
        if (counts[n] > maxFreq) maxFreq = counts[n];
    });
    let modes = Object.keys(counts).filter(n => counts[n] === maxFreq);

    // Дисперсія та відхилення
    let variance = numbers.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / numbers.length;
    let stdDev = Math.sqrt(variance);

    // 3. Вивід на екран
    document.getElementById('sortedRow').innerText = sorted.join(", ");
    document.getElementById('meanVal').innerText = mean.toFixed(2);
    document.getElementById('medianVal').innerText = median;
    document.getElementById('modeVal').innerText = modes.join(", ");
    document.getElementById('varianceVal').innerText = variance.toFixed(2);
    document.getElementById('stdDevVal').innerText = stdDev.toFixed(2);

    // Частотна таблиця
    let tableHTML = "<table><tr><th>Число</th><th>Частота</th></tr>";
    for (let num in counts) {
        tableHTML += `<tr><td>${num}</td><td>${counts[num]}</td></tr>`;
    }
    tableHTML += "</table>";
    document.getElementById('frequencyTable').innerHTML = tableHTML;
});

// Очистка
document.getElementById('clearBtn').addEventListener('click', function () {
    document.getElementById('dataInput').value = "";
    location.reload();
});