# =====================================================
# Problema 5 - Fase 5 Evaluación Final POA
# Curso: Fundamentos de Programación
# Autor: Johan Sebastian Corzo Torres
# =====================================================

# Matriz con nombre del recurso y horas trabajadas

recursos = [
    ["Carlos", 8, 8, 9, 8, 8],
    ["Ana", 7, 8, 7, 8, 7],
    ["Luis", 9, 9, 9, 9, 9],
    ["Maria", 8, 8, 8, 8, 8]
]

# Función para calcular horas y clasificación

def calcular_jornada(horas):

    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total_horas, clasificacion


# Encabezado del cuadro

print("=" * 110)
print("              REPORTE SEMANAL DE HORAS TRABAJADAS")
print("=" * 110)

print(f"{'Nombre':<12}"
      f"{'Lunes':<10}"
      f"{'Martes':<10}"
      f"{'Miércoles':<12}"
      f"{'Jueves':<10}"
      f"{'Viernes':<10}"
      f"{'Total':<10}"
      f"{'Clasificación':<20}")

print("-" * 110)

# Mostrar datos

for recurso in recursos:

    nombre = recurso[0]
    lunes = recurso[1]
    martes = recurso[2]
    miercoles = recurso[3]
    jueves = recurso[4]
    viernes = recurso[5]

    horas = recurso[1:]

    total, clasificacion = calcular_jornada(horas)

    print(f"{nombre:<12}"
          f"{lunes:<10}"
          f"{martes:<10}"
          f"{miercoles:<12}"
          f"{jueves:<10}"
          f"{viernes:<10}"
          f"{total:<10}"
          f"{clasificacion:<20}")

print("=" * 110)