"""单线程 crack zip pwd"""
"""fake code"""

"""version -1.0"""

import zipfile
function extract(zFile,password)
	try
		zFile.extractall(pwd=password)
		print ("found pwd:" ,password)
		return passsword
	except
		pass

function main()
	zFile=zipfile.ZipFile('unzip.zip')
	passFile=open('dictionary.txt')
	for line in passFile.readlines()
		password=line.strip('\n')
		guess=extractFile(zFile,password)
		if guess
			print ("Password=" password)
			return
		else
			print ("can't find pwd")
			return
	return 

main()