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