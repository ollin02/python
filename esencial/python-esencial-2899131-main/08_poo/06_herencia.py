class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz Cumpleaños #{self.edad}")


class Empleado(Persona):

    def __init__(self, horas_totales, nombre, edad):
        super(Empleado,self).__init__(nombre, edad)
        self.horas_totales= horas_totales

    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"{self.nombre} ha trabajado {horas_trabajadas} horas")
        print(f"Horas totales: {self.horas_totales}")


paco = Empleado(nombre="Paco", edad=20, horas_totales=30)
paco.trabajar(horas_trabajadas= 16)
paco.cumplir_anios()

