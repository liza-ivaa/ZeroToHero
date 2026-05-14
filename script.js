document.getElementById('calculateBtn').addEventListener('click', function () {
    let input = document.getElementById('dataInput').value;
    if (input === "") {
        alert("Будь ласка, введіть числа!");
    } else {
        console.log("Дані отримано: " + input);

    }
});