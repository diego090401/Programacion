from typing import List, Dict
Score = 0
Alive = True
Lives = 0
Questions = [{"Question" : "Question ", "Options" :"\n A. Diego \n B. Espinoza \n C. Quesada \n Alosno", "Correct_answer": "B"}, "Diego"]
Opt  = [i for i in range(20)]
Question_id: int = 0


def ask():
    print(Questions)
    print(Questions)
def run() -> None:
    Score = 0
    Alive = True
    Lives = 2
    Questions = [{"Question" : "Esto es un vergo de texto nada mas para ver si las preguntas si fucionan o no funciona o que verga jaja que loco xd xd xd xd xd", "Options" :" A. Diego \n B. Espinoza \n C. Quesada \n B. Quesada", "Correct_answer": "B"}, "Diego"]
    Opt  = [i for i in range(20)]
    Question_id: int = 0
    #print(Opt)
    while  Alive == True :
        if Lives > 0 :
            Alive == True
        else:
             Alive = False
        print(" "*len(Questions[0]["Question"]),"Lives: ", Lives,"\n"," "*(len(Questions[0]["Question"])-1) ,"Score: ",Score)
        print(Questions[0]["Question"])
        print(Questions[0]["Options"])
        Election = input("Election: ")


if __name__ == "__main__":
        
    run()