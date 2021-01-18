# Súlyozott vizsgaátlag, súlyozott vizsga pontszám átlaga / weighted exam score average

# Entering how many exams you have done
number_of_exams = int(input('Enter number of exams: '))

# Entering how many credit these exams cover / Annak megadása, hogy ezek a vizsgák hány kreditet fedeznek
total_credits = int(input('Entering how many credit these exams cover: '))

# Begin with average of 0 and then add up percentages from each exam
# Kezdd 0-s átlaggal, majd add össze az egyes vizsgák százalékát
average = 0
for exam in range(number_of_exams):
    score = int(input('Enter exam score: '))
    exam_credits = int(input('Enter how many credits this exam covered: '))
    average = average + exam_credits/total_credits
print('Your average is', average)