print 'take noRuns'
import random
import numpy as np
import os
import ConfigParser
import sys
sys.path.insert(0, '../../code/')
import getData
Config = ConfigParser.ConfigParser()
Config.read('analysis.config')
NUMSHUFFLES = int(Config.get("analysis","number_of_shuffles"))

def listdir_nohidden(path):
	for f in os.listdir(path):
         if not f.startswith('.'):
			if not f.endswith('p'):
				yield f


files = map(lambda x: x.rpartition('.')[0], listdir_nohidden('stimuliData'))
exportFolder = os.getcwd().split('/')[-1] + '_norun'

def getNoRuns(file):
	f = open("noRuns/" + file + '.txt', 'r')
	data=[]
	for line in f:
	    data.append(line.strip())

	return data

numberOfFramesPerTrial=int(Config.get("analysis","total_number_of_frames_in_trial")) #It is 401 instead of 400 because the middle frame must be ignored.
NUMFRAMESBEFORE=int(Config.get("analysis","number_of_frames_before"))
NUMFRAMESAFTER=int(Config.get("analysis","number_of_frames_after"))

	

def analyzeStimulus(fileName):
	data = getData.getOriginalData('stimuliData/' + fileName)
	noRuns = getNoRuns(file)
	trialNum = len(data[0]) / numberOfFramesPerTrial
	noRunTrials = []
	noRunTrialsReal = []
	for x in range(trialNum):
		if noRuns[x] == '1':
			noRunTrials.append(map(lambda neuron: neuron[x * numberOfFramesPerTrial: (x+1) * numberOfFramesPerTrial], data))
			noRunTrialsReal += np.array(map(lambda neuron: neuron[x * numberOfFramesPerTrial: (x+1) * numberOfFramesPerTrial], data)).transpose().tolist()
	
	noRunTrialsReal = np.array(noRunTrialsReal).transpose().tolist()
	
	f = open('../' + exportFolder + '/stimuliData/' + fileName + '.txt', 'w')
	for line in noRunTrialsReal:
		f.write('\t'.join(map(str,line)) + '\n')
	f.close()



for file in files:
	analyzeStimulus(file)

	