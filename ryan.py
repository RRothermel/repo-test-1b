print("Hello Ryan")

score = "999,999"


scores = open("score.txt","a")
scores.write(score + "\n")
scores.close()