Outputs =["lunes", "martes", "miercoles", "jueves", "viernes", "Sabado", "Domingo", "Otro dia", "Otro dia"]
def i_want_to_sort(Cedula):
    Cedula = [ int(i) for i in list(Cedula) if i != "-"]
    return max(Cedula)
def i_want_options(Mayor):
    return Outputs[Mayor-1]
print(i_want_options(i_want_to_sort(input("Ingrese su cedula con formato x-xxxx-xxx: "))))