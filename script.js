document.getElementById('calculateBtn').addEventListener('click', function () {
    let input = document.getElementById('dataInput').value;
    if (input === "") {
        alert("Будь ласка, введіть числа!");
    } else {
        console.log("Дані отримано: " + input);
        // Функція парсингу рядка в масив чисел
        function parseInput(inputString) {
            let numbers = [];
            let parts = inputString.split(",");

            for (let i = 0; i < parts.length; i++) {
                let num = parseFloat(parts[i].trim());
                if (!isNaN(num)) {
                    numbers.push(num);
                }
            }
            return numbers;
        }

        // Функція створення варіаційного ряду
        function getSortedSeries(arr) {
            let sorted = [...arr];
            return sorted.sort((a, b) => a - b);
        }

        // Перевірка в консолі
        let testInput = "10, 5, 8, 1, 3";
        let parsedData = parseInput(testInput);
        console.log("Варіаційний ряд:", getSortedSeries(parsedData));

        // Знаходимо середнє значення
        function getMean(arr) {
            let sum = 0;
            for (let i = 0; i < arr.length; i++) {
                sum += arr[i];
            }
            return sum / arr.length;
        }

        // Знаходимо медіану (використовуємо вже відсортований масив)
        function getMedian(sortedArr) {
            let middle = Math.floor(sortedArr.length / 2);

            if (sortedArr.length % 2 !== 0) {
                return sortedArr[middle]; // Якщо кількість непарна — беремо число посередині
            } else {
                return (sortedArr[middle - 1] + sortedArr[middle]) / 2; // Якщо парна — середнє двох чисел
            }
        }

        // Знаходимо моду (число, що зустрічається найчастіше)
        function getMode(arr) {
            let counts = {};
            let maxCount = 0;
            let modes = [];

            for (let i = 0; i < arr.length; i++) {
                let num = arr[i];
                counts[num] = (counts[num] || 0) + 1;
                if (counts[num] > maxCount) {
                    maxCount = counts[num];
                }
            }

            for (let num in counts) {
                if (counts[num] === maxCount) {
                    modes.push(Number(num));
                }
            }
            return modes;
        }

        // Дисперсія
        function getVariance(arr) {
            let mean = getMean(arr);
            let sumOfSquares = 0;

            for (let i = 0; i < arr.length; i++) {
                sumOfSquares += Math.pow(arr[i] - mean, 2);
            }
            return sumOfSquares / arr.length;
        }

        // Середнє квадратичне відхилення
        function getStandardDeviation(arr) {
            return Math.sqrt(getVariance(arr));
        }

        function getFrequencyTable(arr) {
            let frequency = {};
            for (let i = 0; i < arr.length; i++) {
                let num = arr[i];
                frequency[num] = (frequency[num] || 0) + 1;
            }
            return frequency;
        }

        let finalData = parseInput("10, 5, 8, 1, 3, 5"); // Тестові дані
        let sorted = getSortedSeries(finalData);

        console.log("--- Результати розрахунків ---");
        console.log("Варіаційний ряд:", sorted);
        console.log("Середнє арифметичне:", getMean(finalData));
        console.log("Медіана:", getMedian(sorted));
        console.log("Мода:", getMode(finalData));
        console.log("Дисперсія:", getVariance(finalData));
        console.log("Квадратичне відхилення:", getStandardDeviation(finalData));
        console.log("Частотна таблиця:", getFrequencyTable(finalData));
    }
});