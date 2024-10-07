from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '09102020'
app.config['MYSQL_DB'] = 'basededatos_vamar'

mysql = MySQL(app)

# Obtener todos los pacientes
@app.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()
        return jsonify(pacientes)
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener paciente activo", "error": str(e)})
    finally:
        cursor.close()

# Obtener un paciente por ID
@app.route('/pacientes/<int:id>', methods=['GET'])
def obtener_paciente(id):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM pacientes WHERE id = %s", (id,))
        paciente = cursor.fetchone()
        if paciente is None:
            return jsonify({"No existe paciente con ese ID"})
        return jsonify(paciente)
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener paciente"})
    finally:
        cursor.close()

# Crear un nuevo paciente
@app.route('/pacientes', methods=['POST'])
def crear_paciente():
    datos = request.get_json()
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("INSERT INTO pacientes (nombre_completo, apellido_completo, tipo_identidad, numero_identidad, correo_electronico, celular, telefono, sexo, edad, alergias, eps) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (datos['nombre_completo'], datos['apellido_completo'], datos['tipo_identidad'], datos['numero_identidad'], datos['correo_electronico'], datos['celular'], datos['telefono'], datos['sexo'], datos['edad'], datos['alergias'], datos['eps']))
        mysql.connection.commit()
        return jsonify({"mensaje": "Paciente creado con éxito"})
    except Exception as e:
        return jsonify({"mensaje": "Error al crear paciente", "error": str(e)})
    finally:
        cursor.close()

# Actualizar un paciente existente
@app.route('/pacientes/<int:id>', methods=['PUT'])
def actualizar_paciente(id):
    datos = request.get_json()
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("UPDATE pacientes SET nombre_completo = %s, apellido_completo = %s, tipo_identidad = %s, numero_identidad = %s, correo_electronico = %s, celular = %s, telefono = %s, sexo = %s, edad = %s, alergias = %s, eps = %s WHERE id = %s", 
                       (datos['nombre_completo'], datos['apellido_completo'], datos['tipo_identidad'], datos['numero_identidad'], datos['correo_electronico'], datos['celular'], datos['telefono'], datos['sexo'], datos['edad'], datos['alergias'], datos['eps'], id))
        mysql.connection.commit()
        return jsonify({"mensaje": "Paciente actualizado con éxito"})
    except Exception as e:
        return jsonify({"mensaje": "Error al actualizar paciente", "error": str(e)})
    finally:
        cursor.close()

# Eliminar un paciente
@app.route('/pacientes/<int:id>', methods=['DELETE'])
def eliminar_paciente(id):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM pacientes WHERE id = %s", (id,))
        mysql.connection.commit()
        return jsonify({"mensaje": "Paciente eliminado con éxito"})
    except Exception as e:
        return jsonify({"mensaje": "Error al eliminar paciente", "error": str(e)})
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
    