#Uses requests and html parser Beautifulsoup
import requests 
from bs4 import BeautifulSoup
#Takes in the url for walletexplorer and creates soup object
#Change site variable to the website
url = "https://www.walletexplorer.com"
site = "BTCCPool"   #change
r = requests.get(url)
soup = BeautifulSoup(r.content)
#finds the address tag, list
links = soup.find_all("a")
#goes through list only taking in websites in main table
for link in links:
	if(link.text != "Huobi.com"):  #Do not change
		continue
	elif ((link.text.find('.') != -1) and (link.text!="WalletExplorer.com")):
		print(site)
		#creates new Url for requests with website name
		newUrl = ("https://www.walletexplorer.com/wallet/" + site + "/addresses")
		newR = requests.get(newUrl)
		
		newSoup = BeautifulSoup(newR.content)
		newLinks = newSoup.find_all("a")
		count = 1
		#loop prints the first page of addresses
		for newLink in newLinks:
			if(len(newLink.text)>=25):
				print(newLink.text)
		#finds amount of pages for the url
		pageNum = newSoup.find_all("div", {"class": "paging"})
		for item in pageNum:
			s = int((item.contents[0])[10:])
		#range for all pages to have address starting with page 2
		for i in range(1, s):
			count+=1
			print(count)
			pageUrl =  ("https://www.walletexplorer.com/wallet/" + site + "/addresses?page=" + str(count))
			pageR = requests.get(pageUrl)
			pageSoup = BeautifulSoup(pageR.content)
			pageLinks = pageSoup.find_all("a")
			#loop to print text of each page
			for ad in pageLinks:
				if(len(ad.text)>=25):
					print(ad.text)