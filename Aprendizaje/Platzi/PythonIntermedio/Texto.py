Text = []
with open("Aprendizaje\Platzi\PythonIntermedio\Archivo.txt", 'r', encoding="utf-8") as f :
    for line in f :
            Text.append(line)

print(Text, end = "\n")