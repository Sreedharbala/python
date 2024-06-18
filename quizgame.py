# print("welcome to my quiz")
#
#
# playing = input("do you want to play? ")
# score = 0
#
# if playing.lower()!= "yes" :
#     quit()
# print("okay let\'s play :)")
# print("use small alphabets")
#
# answer = input("what is meant by sql? ").lower()
# if answer == "structure query language":
#     print("correct!")
#     score += 1
# else:
#     print("incorrect!")
#
# answer = input("what is meant by DBMS? ")
# if answer.lower() == "database management system":
#     print("correct!")
#     score += 1
# else:
#     print("incorrect!")
#
# answer = input("what is meant by RDBMS? ")
# if answer.lower() == "relational database management system":
#     print("correct!")
#     score += 1
# else:
#     print("incorrect!")
#
# answer = input("what is meant by ERD diagram? ")
# if answer.lower() == "entity relationship diagram":
#     print("correct!")
#     score += 1
# else:
#     print("incorrect!")
#
# print("you got"  + str(score) +  "correct answers!")
# print("you got"  + str((score/4)*100) +  "%.")


print("welcome to my quiz!")


playing = input("do you want to play? ")
score = 0


if playing.lower() != "yes":
    quit()

print("ok let\'s play")
print("use small alphabets")

answer = input("what is meant by MLA? ")
if answer.lower() == "member of legislative assembly":
    print("correct!")
    score +=1
else:
    print("incorrect!")

print("you got" + str(score) + "correct answers")
print("you got" + str((score/1)*100) + "%.")
