from typing import List, Dict




def run() -> None:
    Score = 0
    Lives = 3

    Questions = [{"Question" : "Who is accused of the murder of Henry Clerval?", "Options" :" A. Alphonse Frankenstein \n B. Victor Frankenstein \n C. Justine Moritz \n D. Frankenstein’s monster", "Correct_answer": "C"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "Who is accused of the murder of Henry Clerval?", "Options" :" A. Victor Frankenstein \n B. Robert Walton \n C. Frankenstein’s monster \n D. Justine Moritz", "Correct_answer": "A"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "To whom is Victor taken after Henry is murdered?", "Options" :" A. M. Kempe \n B. His father \n C. Professor Waldman \n D. Mr. Kirwin", "Correct_answer": "D"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "What is the name of the professor at Ingolstadt who first teaches Victor the methods of modern science?", "Options" :" A. Krempe \n B. Clerval \n C. Waldman \n D. Beaufort ", "Correct_answer": "C"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "With what is Walton obsessed?", "Options" :" A. Creating life \n B. Reaching the North Pole \n C. Finding a passage to the East \n D. Discovering the source of the Earth’s magnetism", "Correct_answer": "B"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "Where does Victor first have a conversation with his monster?", "Options" :" A. In Victor’s apartment in Ingolstadt \n B. In a field outside of Geneva \n C. On a desolate island off Scotland \n D. In a hut on a glacier near Montanvert", "Correct_answer": "D"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "What does the monster want Victor to do to heal his loneliness?", "Options" :" A. Create a female monster to be his companion\n B. Accept him into his family\n C. Destroy him\n D. Work to make him appear less hideous", "Correct_answer": "A"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "How does Walton meet Victor?", "Options" :" A. They work in the same laboratory on an island off Scotland.\n B. Walton escorts Victor northward in pursuit of the monster.\n C. Walton finds Victor on the northern ice and nurses him back to health.\n D.They are students together at Ingolstadt", "Correct_answer": "C"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "How does Victor’s mother die?", "Options" :" A. She drowns in a river.\n B. The monster strangles her.\n C. She catches scarlet fever from Elizabeth.\n D. She is executed for murdering William", "Correct_answer": "C"},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},
                 {"Question" : "", "Options" :" A. \n B. \n C. \n D.", "Correct_answer": ""},

                 ]

    while  True == True :
        for i in range(20):
            if Lives > 0 :
                pass
            else:
                print("You lose")
                exit()
                
            print(" "*len(Questions[i]["Question"]),"Lives: ", Lives,"\n"," "*(len(Questions[i]["Question"])-1) ,"Score: ",Score)
            print(Questions[i]["Question"])
            print(Questions[i]["Options"])
            Election = input("Election: ").capitalize()
            if Election == "A" or Election =="B" or Election == "C" or Election == "D":
                if Election == Questions[i]["Correct_answer"] :
                    Score = Score + 1
                else :
                    Lives = Lives - 1
            else :
                print("You only can use A, B, C or D, please try again \n")
                



if __name__ == "__main__":
        
    run()