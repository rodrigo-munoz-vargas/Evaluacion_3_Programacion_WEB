from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# Almacen temp de registros
registros = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    # Variables para los valores ingresados
    nota1 = nota2 = nota3 = asistencia = None

    if request.method == 'POST':
        try:
            # Obteener notas y asistencia desde el formulario
            nota1 = request.form['nota1']
            nota2 = request.form['nota2']
            nota3 = request.form['nota3']
            asistencia = request.form['asistencia']

            # Convertir valores a float para cálculo con decimales
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
            # Manejar valores no validos
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


@app.route('/redirigir')
def redirigir():
    # Redirigir a la pagina principal
    return redirect(url_for('index'))


@app.route('/error404')
def error404():
    # Devuelve un error 404
    abort(404)


@app.errorhandler(404)
def page_not_found(e):
    # Página para error 404
    return render_template('404.html'), 404


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    global registros
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')

        # Agregar registro a la lista
        if nombre and edad:
            registros.append({'nombre': nombre, 'edad': int(edad)})

    # Mostrar registros almacenados
    return render_template('registro.html', registros=registros)


@app.route('/borrar_registros')
def borrar_registros():
    global registros
    registros = []  # Limpiar lista de registros
    return redirect(url_for('registro'))


if __name__ == '__main__':
    app.run(debug=True)