import time
names = [1,2,3]
name_array_counter = 0

while name_array_counter < 3:
	print("Please enter name" , name_array_counter + 1)
	names[name_array_counter] = input()
	name_array_counter = name_array_counter + 1
	

print("Your class has these pupils:", names[0:100])

scores = [1,2,3]
score_array_counter = 0
total_score = 0
while score_array_counter < 3:
	print("Please enter ",names[score_array_counter],"'s result.")
	scores[score_array_counter] = input()
	total_score = int(total_score) + int(scores[score_array_counter])
	score_array_counter = score_array_counter + 1
print("Your class has these scores:", scores[0:100])
print("The total score for the class was:",total_score,"%")
total_score = int(total_score) / 3
print("The average percentage for this class was:",total_score)

