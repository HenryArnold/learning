#coding=UTF-8
import optparse
import nmap

def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.PortScanner()
	results= nmScan.scan(tgtHost, tgtPort)
	state = results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
	print("[*]"+ tgtHost +"tcp/" +tgtPort +""+state)
def main():
	parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
	parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
	parser.add_option('-p',dest='tgtPort',type='int', help='specify target port ')
	(option,args) = parser.parse_args()
	tgtHost = option.tgtHost
	tgtPort = option.tgtPort
	args.append(tgtPort)
	if(tgtHost == None)|(tgtPort == None):
		print('[-]you must specify a target host and port[s]!')
		exit(0)
	for tgtport in args:
		nmapScan(tgtHost, tgtport)
if __name__ == '__main__':
	main()
	