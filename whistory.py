#!/usr/bin/python -u
import requests, subprocess, sys
from lxml import html

headers = {'Accept':'text/css,*/*;q=0.1',
        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'en-US,en;q=0.8',
        'User-Agent':'Mozilla/5 (Solaris 10) Gecko'}

def wh(url):
	page = requests.get('http://who.is/domain-history/' + url, headers=headers)
	tree = html.fromstring(page.text)
	dati = tree.xpath('//span[@data-bind-domain="raw_registrar_lookup"]/text()')
	#print dati[1].encode('utf-8') #esempio stampa il nome
	#for item in dati:
		#print item.encode('utf-8')
	subprocess.call(["mkdir .out"], shell=True)
	output= open('.out/out.txt','a')
	lunghezza = len(dati)
	i = 0
	while i < lunghezza:
		print >> output, dati[i].encode('utf-8')
		i = i+1
	output.close()
	subprocess.call(["awk '{$1=$1}{print }' .out/out.txt > .out/final.txt"], shell=True)
	final_output = subprocess.call(["cat .out/final.txt"], shell=True)
	subprocess.call(["rm -r .out"], shell=True)
	print final_output

if __name__ == "__main__":

	try:
		url = (str(sys.argv[1]))
	except IndexError:
		print ("Usage: " +sys.argv[0] + " " + "domain name")
		sys.exit(2)
	wh(url)