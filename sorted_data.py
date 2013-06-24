from sys import argv

script, filename = argv

file_text = open(filename)

rest_list = {}

#read each line, split on the colon, put pairs into a list of tuples
for line in file_text:
	restaurant, score = line.split(':')
	score = score.strip('\n')
	rest_list[restaurant] = score

sorted_rest_list = sorted(rest_list.iteritems())

for restaurant in sorted_rest_list:
	print "Restaurant %s has a score of %s." %  (restaurant[0], float(restaurant[1])) 