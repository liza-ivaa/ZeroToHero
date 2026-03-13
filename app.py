from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Отримуємо дані з форми
        data = request.form.get('numbers')
        # Перетворюємо рядок у список чисел
        nums = [float(x.strip()) for x in data.split(',')]

        # Рахуємо статистику
        result = {
            "mean": round(np.mean(nums), 2),
            "median": round(np.median(nums), 2),
            "var": round(np.var(nums), 2)
        }

    # render_template шукає файл у папці templates
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)