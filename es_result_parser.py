import sys
import json
def parse_es_raw_result(raw_result):
	result_list = []
	c = 1
	for single_result in json.loads(raw_result)['results']:
		print "--- {0} ---".format(c)
		c += 1
		result_list.append(parse_one_result(single_result))
	return result_list
	
def parse_one_result(single_result):
	print single_result['name']
	print single_result['phone']
	print single_result['location']
	parse_score_explanation(single_result['explanation'])
	print '\n'

def parse_score_explanation(explanation):
	print "final score: {0}".format(explanation['value'])
	score_sum = explanation['details'][0]['details'][0]
	if len(score_sum['details'])>0:
		score_name = score_sum['details'][0]['details'][0]['details'][0]
		parse_name_score(score_name)
	else:
		print "No name score"
	if len(score_sum['details'])>1:
		score_location = score_sum['details'][1]['details'][0]['details'][0]['details'][0]
		parse_location_score(score_location)
	else:
		print "No location score"

def parse_name_score(score_name):
	print "Scaled Score for Name: {0}".format(score_name['value']) # what's max?
	print "Raw Score for Name: {0}".format(score_name['details'][0]['details'][0]['value'])

def parse_location_score(score_location):
	print "Scaled Score for Location: {0}".format(score_location['value'])
	print "Raw Score for Location: {0}".format(score_location['details'][0]['value']) # sum of address1,2,3, postal code and city (if any)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit
	myfile = open (sys.argv[1], "r") 
	parse_es_raw_result(myfile.read())