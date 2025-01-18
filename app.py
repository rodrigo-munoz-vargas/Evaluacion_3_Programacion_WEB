from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    # Variables para almacenar los valores ingresados
    nota1 = nota2 = nota3 = asistencia = None

    if request.method == 'POST':
        try:
            # Obtener las notas y asistencia desde el formulario
            nota1 = request.form['nota1']
            nota2 = request.form['nota2']
            nota3 = request.form['nota3']
            asistencia = request.form['asistencia']

            # Convertir los valores a float para cálculo con decimales
            nota1_float = float(nota1)
            nota2_float = float(nota2)
            nota3_float = float(nota3)
            asistencia_float = float(asistencia)

            # Calcular el promedio
            promedio = (nota1_float + nota2_float + nota3_float) / 3

            # Determinar si aprueba
            if promedio >= 40 and asistencia_float >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

            # Mostrar plantilla con el promedio y estado
            return render_template(
                'ejercicio1.html',
                nota1=nota1,
                nota2=nota2,
                nota3=nota3,
                asistencia=asistencia,
                promedio=promedio,
                estado=estado
            )
        except ValueError:
            # Manejar valores no válidos
            return render_template(
                'ejercicio1.html',
                nota1=nota1,
                nota2=nota2,
                nota3=nota3,
                asistencia=asistencia,
                error="Por favor, ingrese valores numéricos válidos."
            )
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # Inicializar variables para los nombres
    nombre1 = nombre2 = nombre3 = None
    nombre_mas_largo = None
    longitud = None

    if request.method == 'POST':
        # Obtener los nombres desde el formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Buscar el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

    # Mostrar plantilla con los resultados
    return render_template(
        'ejercicio2.html',
        nombre1=nombre1,
        nombre2=nombre2,
        nombre3=nombre3,
        nombre_mas_largo=nombre_mas_largo,
        longitud=longitud
    )


if __name__ == '__main__':
    app.run(debug=True)
