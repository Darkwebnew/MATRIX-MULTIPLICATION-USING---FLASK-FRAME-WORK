from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Matrix multiplication route
@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        # Get matrices from the form
        matrix_a = request.form.get('matrix_a')
        matrix_b = request.form.get('matrix_b')

        # Convert string input to 2D integer arrays
        matrix_a = [[int(num) for num in row.split()] for row in matrix_a.strip().split('\n')]
        matrix_b = [[int(num) for num in row.split()] for row in matrix_b.strip().split('\n')]

        # Validate matrix dimensions
        if len(matrix_a[0]) != len(matrix_b):
            return "Matrix A's column count must match Matrix B's row count."

        # Perform matrix multiplication
        result = [
            [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)]
            for row_a in matrix_a
        ]

        return render_template('mainfile.html', result=result)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
