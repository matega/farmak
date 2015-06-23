#!/usr/bin/python
import sys
def explodeline(line):
	return tuple([[d.strip() for d in p.split(",")] for p in line.split("\t")])

def serializedrug(drug):
	tmp=drug+"\t"
	tmp+=", ".join([alleffects[effect] for effect in database[drug]["effects"]])+"\t"
	tmp+=", ".join([allindications[indication] for indication in database[drug]["indications"]])
	return tmp
def byeffect(effect):
	try:
		return byeffectid(alleffects.index(effect))
	except ValueError:
		return []
def byindication(indication):
	try:
		return byindicationid(allindications.index(indication))
	except ValueError:
		return []

def byeffectid(effect):
	return [drug for drug in database.keys() if effect in database[drug]["effects"]]
def byindicationid(indication):
	return [drug for drug in database.keys() if indication in database[drug]["indications"]]


database={}
alleffects=[]
allindications=[]

with open(sys.argv[1]) as f:
	for l in f:
		drugs, effects, indications = explodeline(l)
		for drug in drugs:
			indications=[indication.capitalize() for indication in indications]
			if not drug in database:
				database[drug]={"effects":[], "indications":[]}
			drug = database[drug]
			for effect in effects:
				if effect and not effect in alleffects:
					alleffects.append(effect)
				if effect and not alleffects.index(effect) in drug["effects"]:
					drug["effects"].append(alleffects.index(effect))
			for indication in indications:
				if indication and not indication in allindications:
					allindications.append(indication)
				if indication and not allindications.index(indication) in drug["indications"]:
					drug["indications"].append(allindications.index(indication))
with open("drugsdatabase.csv", "w") as f:
	for drug in sorted(database.keys()):
		f.write(serializedrug(drug)+"\n")
print("{:d} drugs, {:d} effects and {:d} indications.".format(len(database), len(alleffects), len(allindications)))
with open("effects.txt", "w") as f:
	for effect in sorted(alleffects):
		f.write(effect+"\n")
with open("indications.txt", "w") as f:
	for indication in sorted(allindications):
		f.write(indication+"\n")
print(byeffect(raw_input("Effect? ")))
		
	
