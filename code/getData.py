#this is a module for pulling in raw data

#define function
def getRawData(dataset, stimuli):
	#make connection to the raw data file in the specified dataset with the specified stimuli
	f = open('../datasets/' + dataset + '/stimuliData/' + stimuli + '.txt', 'r')
	data=[]
	for line in f:
	    data.append(line)

	
	data=map(lambda x: 
			map(lambda y: 
				float(y.strip())
			,x.strip().split('\t'))
		,data)	

	
	return data

def getCurrentDataset():
	f=open('../currentDataset.txt','r')
	return f.read()

