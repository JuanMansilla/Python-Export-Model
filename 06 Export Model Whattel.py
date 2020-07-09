# Quitar Comillas "" a todo lo que tenga el simbolo $()
#################################
# Initialize Script
#################################
# Variables generales:
# Nombre del archivo
NameFile = "$(GV_File)"+".mod"
mf = open(NameFile, 'w')
# Items Generales
Vol = 5*5*5.0  # Tamano del bloque
MCAF = 1.0      # Item Requerido por Whattel
PCAF = 1.0      # Item Requerido por Whattel
Parcel = 1      # Item Requerido por Whattel

#################################
# Main Script
#################################
Ton = 0.0
b = ""
# Nombre de la variable de mineral
Otype = ""
# Ubicacion:
# X --> i --> Col // Y --> j --> Row // Z --> k --> Level
ijk = str(int("$(col)")) + ',' + str(int("$(row)")) + ',' + \
    str(int(111-"$(level)"))  # Numero de bloques totales


def OtypeEval():
    if "$(TYPE)" == 11:
        Otype = "Ox1"
    elif "$(TYPE)" == 12:
        Otype = "OxA"
    elif "$(TYPE)" == 16:
        Otype = "Sulf"
    elif "$(TYPE)" == 19:
        Otype = "OxAL"
    elif "$(TYPE)" == 17:
        Otype = "SulA"
    elif "$(TYPE)" == 20 or "$(TYPE)" == 18:
        Otype = "CAB"
    elif "$(TYPE)" == 21 or "$(TYPE)" == 22:
        Otype = "CAB"
    elif "$(TYPE)" == 23:
        Otype = "CAB"
    else:
        Otype = "DES"
    return Otype


if (100.1 >= "$(TOPO%)" and "$(TOPO%)" >= 10):
    Ton = round((("$(TOPO%)"/100)*Vol*"$(DENS)"), 3)
    # ',1,1.0,1.0,' --> Parcel: Solo una linea, MCAF = 1.0, PCAF = 1.0
    Linea1 = ijk + ',1,1.0,1.0,' + str(Ton) + ',' + str("$(DGEO)")
    if ("$(AUREC)" > 5 and "$(AGREC)" > 5):
        Linea = ijk + ',' + OtypeEval() + ',' + str(Ton) + ',' + str(round("$(AU)"*"$(AUREC)", 3)
                                                                     * Ton/100) + ',' + str(round("$(AG)"*"$(AGREC)", 3)*Ton/100)
        Linea2 = Linea + ',' + str("$(CATE)"*Ton)
    else:
        Linea = ijk + ',' + OtypeEval() + ',' + str(Ton) + ',' + str(round("$(AU)"*0, 3)
                                                                     * Ton/100) + ',' + str(round("$(AG)"*0, 3)*Ton/100)
        Linea2 = Linea + ',' + str("$(CATE)"*Ton)
    b = str(Linea1 + "\n" + Linea2)
else:
    Linea1 = ijk + ',0,0.0,0.0,0.0,0'
    b = str(Linea1)

data = b + "\n"
mf.write(data)

###########################
# Final Script
###########################
mf.close
