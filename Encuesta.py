class encuesta:
    def __init__(self,preguntas):
        self.preguntas=preguntas
        self.respuestas = []

    def agregar_respuesta(self, respuestas_persona):
        self.respuestas.append(respuestas_persona)

    def mostrar_resultados(self):
        print("\nResultados de la Encuesta")
        for i in range(10):
            print(f"\nPersona {i+1}")
            for j in range(4):
                if(j==1):
                    print("Idea de proyecto: ",la_encuesta.respuestas[i][j-1])
                elif(j==2):
                    print("Posibles beneficiarios del proyecto: ",la_encuesta.respuestas[i][j-1])
                elif(j==3):
                    print("Ambiciones despues de graduarse: ",la_encuesta.respuestas[i][j-1])


preguntas = [
    "¿Cual es su idea de proyecto?: ",
    "¿Sabes a quienes podria beneficiar tu proyecto?¿A quienes?: ",
    "¿Piensas seguir programando despues de la universidad?¿Que programas te gustaria realizar sin presion academica?: "
]

la_encuesta = encuesta(preguntas)

for i in range(10):
    print(f"\nPersona {i+1}:")
    respuestas = []
    for i in preguntas:
        respuesta = input(i + " ")
        respuestas.append(respuesta)
    la_encuesta.agregar_respuesta(respuestas)

la_encuesta.mostrar_resultados()