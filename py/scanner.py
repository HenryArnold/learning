#code = UTF-8
import optparse
import socket
import threading

screenLock = threading.Semaphore(value=1)
#tcp socket connect sen recv  
def connScan(tgtHost,tgtPort):

	try:
		connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		connSkt.send('ViolentPython\r\n')
		results = connSkt.recv(100)
		print('[+]%d/tcp open' %tgtPort)
		print('[+]'+str(results))
		connSkt.close()
	except:
		print('[-]%d/tcp closed' %tgtPort)
		
def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = socket.gethostbyname(tgtHost)
	except:
		print("[-]Cannot resolve '%s':Unknown host" %tgtHost)
		return
	try:
		tgtName = socket.gethostbyaddr(tgtIP)
		print('\n[+]Scan Result for:' +tgtName[0])
	except:
		print('\n[+]Scan Reault fot:' +tgtIP)
	socket.setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		print('Scanning port'+str(tgtPort))
		connScan(tgtHost,int(tgtPort))
		
def main ():
	parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost',type='string',help='specify target host')
	parser.add_option('-p',dest='tgtPort',type='int',help='specify target port')
	(options,args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPort = options.tgtPort
	args.append(tgtPort)
	if (tgtHost == None)|(tgtPort == None):
		print('[-]you must specifiy a target host and port[s]!')
		exit(0)
	portScan(tgtHost, args)
	
if __name__=='__main__':
	main()
		
	
