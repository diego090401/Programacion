from typing import List, Dict

def run() -> None:
    Score = 0
    Lives = 3

    Questions = [{"Question" : "Who is accused of the murder of Henry Clerval?", "Options" :" A. Alphonse Frankenstein \n B. Victor Frankenstein \n C. Justine Moritz \n D. Frankenstein’s monster", "Correct_answer": "C"},
                 {"Question" : "Who is writing all of the letters?", "Options" :" A. the monster \n B. Elmo \n C. Dr Framkenstein brother \n D. Robert Walton", "Correct_answer": "D"},
                 {"Question" : "Who is accused of the murder of Henry Clerval?", "Options" :" A. Victor Frankenstein \n B. Robert Walton \n C. Frankenstein’s monster \n D. Justine Moritz", "Correct_answer": "A"},
                 {"Question" : "Where was Victor Frankenstein born?", "Options" :" A. Paris \n B. Ingolstadt \n C. Naples \n D.", "Correct_answer": "Belize"},
                 {"Question" : "To whom is Victor taken after Henry is murdered?", "Options" :" A. M. Kempe \n B. His father \n C. Professor Waldman \n D. Mr. Kirwin", "Correct_answer": "D"},
                 {"Question" : "What does Victor tell Robert Walton that he feels a slave of", "Options" :" A. His dog \n B.His creature \n C. His profession \n D. His passions", "Correct_answer": "B"},
                 {"Question" : "What is the name of the professor at Ingolstadt who first teaches Victor the methods of modern science?", "Options" :" A. Krempe \n B. Clerval \n C. Waldman \n D. Beaufort ", "Correct_answer": "C"},
                 {"Question" : "Who is the first victim to be killed by the Creature?", "Options" :" A. Justine \n B. William \n C. Caroline \n D. Walton", "Correct_answer": "B"},
                 {"Question" : "With what is Walton obsessed?", "Options" :" A. Creating life \n B. Reaching the North Pole \n C. Finding a passage to the East \n D. Discovering the source of the Earth’s magnetism", "Correct_answer": "B"},
                 {"Question" : "What is the name of Walton’s sister?", "Options" :" A. Catherine Beaufort \n B. Elizabeth Saville\n C. Margaret Lavenza \n D.Margaret Saville", "Correct_answer": "D"},
                 {"Question" : "Where does Victor first have a conversation with his monster?", "Options" :" A. In Victor’s apartment in Ingolstadt \n B. In a field outside of Geneva \n C. On a desolate island off Scotland \n D. In a hut on a glacier near Montanvert", "Correct_answer": "D"},
                 {"Question" : "Where does Victor follow the Monster?", "Options" :" A. Into Russia and the polar regions \n B. On a deserted island in Scotland \n C. Through Europe\n D. To Africa", "Correct_answer": "A"},
                 {"Question" : "What does the monster want Victor to do to heal his loneliness?", "Options" :" A. Create a female monster to be his companion\n B. Accept him into his family\n C. Destroy him\n D. Work to make him appear less hideous", "Correct_answer": "A"},
                 {"Question" : "Where does Victor go to school?", "Options" :" A. England \n B.France \n C. Germany \n D.Switzerland", "Correct_answer": "C"},
                 {"Question" : "How does Walton meet Victor?", "Options" :" A. They work in the same laboratory on an island off Scotland.\n B. Walton escorts Victor northward in pursuit of the monster.\n C. Walton finds Victor on the northern ice and nurses him back to health.\n D.They are students together at Ingolstadt", "Correct_answer": "C"},
                 {"Question" : "Who says the following: “But it is true that I am a wretch. I have murdered the lovely and the helpless; I have strangled the innocent as they slept, and grasped to death his throat who never injured me or any other living thing.", "Options" :" A. Clerval \n B. The Monster \n C. Victor \n D. Walton", "Correct_answer": "B"},
                 {"Question" : "How does Victor’s mother die?", "Options" :" A. She drowns in a river.\n B. The monster strangles her.\n C. She catches scarlet fever from Elizabeth.\n D. She is executed for murdering William", "Correct_answer": "C"},

                 ]

    while  True == True :
            
        print("______                      _                       _          _                        _      ")
        print("|  ___|                    | |                     | |        (_)                      (_)     ")
        print("| |_    _ __   __ _  _ __  | | __  ___  _ __   ___ | |_   ___  _  _ __     __ _  _   _  _  ____")
        print("|  _|  | '__| / _` || '_ \ | |/ / / _ \| '_ \ / __|| __| / _ \| || '_ \   / _` || | | || ||_  /")
        print("| |    | |   | (_| || | | ||   < |  __/| | | |\__ \| |_ |  __/| || | | | | (_| || |_| || | / / ")
        print("\_|    |_|    \__,_||_| |_||_|\_\ \___||_| |_||___/ \__| \___||_||_| |_|  \__, | \__,_||_|/___|")
        print("                                                                             | |               ")
        print("                                                                             |_|               ")
        print("                                                By Diego Alonso Espinoza                                            ")

        for i in range(20):
            if Lives > 0 :
                pass
            else:   
                print(" __          __                _                _   ")
                print(" \ \        / /               | |              | |")
                print("  \ \  /\  / /    __ _   ___  | |_    ___    __| |")
                print("   \ \/  \/ /    / _` | / __| | __|  / _ \  / _` |")  
                print("    \  /\  /    | (_| | \__ \ | |_  |  __/ | (_| |")  
                print("     \/  \/      \__,_| |___/  \__|  \___|  \__,_|")  
                             
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