from __future__ import unicode_literals
##from django.db import models
from django import forms
import os

def get_variables_choices():
	base_path = os.path.dirname(__file__)
	file_path = os.path.abspath(os.path.join(base_path, "..", "..", "Analysis/Data/city_health_stats.csv" ))

	with open(file_path) as f:
		variables = f.readline().strip().split(",")[2:]

	print(variables)
	temp = [(x,x) for x in variables]
	return temp

class Variable(forms.Form):
	variable_choices = get_variables_choices()
	variable_1 = forms.ChoiceField(label = "Variable 1", choices = variable_choices)
	variable_choices.append(("None", "None"))
	variable_2 = forms.ChoiceField(label = "Variable 2", choices = variable_choices)
	##= forms.CharField(max_length = 64)


'''
class Neighborhood(models.Model):
	pass
	##name = models.CharField(max_length = 200)
'''