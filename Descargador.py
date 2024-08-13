import mysql.connector
import csv

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="Isidro3213.mysql.pythonanywhere-services.com",
    user="Isidro3213",
    password="",
    database="Isidro3213$base1"
)

cursor = conn.cursor()

# Ejecutar la consulta SQL
cursor.execute("SELECT * FROM auth_user")

# Obtener todos los resultados de la consulta
rows = cursor.fetchall()

# Especificar el nombre del archivo donde se guardarán los datos
with open('datos.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Escribir los nombres de las columnas (opcional)
    column_names = [i[0] for i in cursor.description]
    writer.writerow(column_names)

    # Escribir los datos
    writer.writerows(rows)

# Cerrar la conexión a la base de datos
conn.close()
