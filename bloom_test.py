from bloomfilter import BloomFilter 
from random import shuffle 
import numpy as np

# plotting the result of the test
import matplotlib.pyplot as plt

n = 3000 #no of items to add 
p = 0.5 #false positive probability 
A = np.zeros((99,50))
f = open('mat.txt',"w")

for i in np.arange(0.01,1,0.01):
	for j in np.arange(1000,11000,200):
		bloomf = BloomFilter(float(j),float(i))
	#	print("Inserted Elements : ", n) 
	#	print("Size of bit array:{}  m ".format(bloomf.size)) 
	#	print("False positive Probability:{}".format(bloomf.fp_prob)) 
	#	print("Number of hash functions:{}  k ".format(bloomf.hash_count)) 
		
		tmp = 0
		word_present = []
		with open('dict_present.txt') as my_file:
			for line in my_file:
				tmp += 1
				if tmp==j:
					break
				word_present.append(line.rstrip('\n'))

		tmp = 0
		word_absent = []
		with open('dict_absent.txt') as my_file:
			for line in my_file:
				tmp += 1
				if tmp==j:
					break
				word_absent.append(line.rstrip('\n'))

		shuffle(word_present) 

		for item in word_present: 
			bloomf.add(item) 

		shuffle(word_present) 
		shuffle(word_absent) 

		test_words = word_present[:int(j/2)] + word_absent 

		shuffle(test_words)

		fp = 0
		pp = 0
		dnp = 0
		 
		for word in test_words: 
			if bloomf.check(word): 
				if word in word_absent: 
		#			print("'{}' is a false positive!".format(word)) 
					fp+=1
				else:
		#			print("'{}' is probably present!".format(word)) 
					pp+=1
			else: 
		#		print("'{}' is definitely not present!".format(word)) 
				dnp+=1
		'''		
		print('fp: ', fp)
		print('pp: ', pp)
		print('dnp: ', dnp)
		'''
		A[int(i*100)-1][int(j/200)-5] = int(fp)/int(fp+pp+dnp)

		if j == 49500:
			f.write(str(A[int(i*100)-1][int(j/200)-5]))
		else:
			f.write(str(A[int(i*100)-1][int(j/200)-5])+',')
		print('j',j/200-5)
	print('i',int(i*100))

f.close()

#plt.plot(np.arange(0.01,1,0.01),A, 'ro')
#plt.ylim((0,0.001))
#plt.show()

