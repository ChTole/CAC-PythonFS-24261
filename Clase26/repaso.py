# Repaso condicionales

# Ejemplo con factor sanguineo
# Rh+ o Rh-
factor = "Rh-"
# if - elif - else
if factor == "Rh+":
    print("Sos factor Rh+")
elif factor == "Rh-":
    print("Sos factor Rh-")
else:
    print("No reconozco el factor.")

# Match - case // Python 3.10
# Python NO ES RETROCOMPATIBLE - Cuidado!
match factor:
    case "Rh+":
        print("Sos factor Rh+")
    case "Rh-":
        print("Sos factor Rh-")
    case _:
        print("No reconozco el factor.")