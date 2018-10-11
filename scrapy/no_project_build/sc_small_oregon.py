# python2.7
# Franco Gil, from a uthopic latin country :)

import scrapy
import pandas
from pandas import DataFrame
from scrapy.spiders import Rule
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess

class to_excel(scrapy.Spider):
  """
  A very small spider to grab data on a small table and send it on a excel file
  with almost 2 columns on in.
  
  PD: This unfinished version for a upwork project.
  """
	name='excel'
  # ugly url x:x'
	start_urls=['https://ltclicensing.oregon.gov/Facilities?GeoLocationString=&RangeValue=50&LocationSearchString=&FacilitySearchString=&AFH=true&AFH=false&ALF=true&ALF=false&NF=true&NF=false&RCF=true&RCF=false&Medicaid=true&Medicaid=false&Medicare=true&Medicare=false&PrivatePay=true&PrivatePay=false&OpenOnly=false']

	def parse(self, response): #parse2
		w=[]; names=[]; city=[]
		for i in range(10):
			j=i+2
			path='//tr[%s]' %str(j)
			data=response.xpath(path).extract_first()
			w_in=[]
			for k in range(6):
				l=k+1
				path2=path+'/td[%s]/text()' %str(l)
				d_in=response.xpath(path2).extract_first()
				if type(d_in) != None:
					d_in=str(d_in)
					d_in=d_in.replace('\n', '')
					d_in=d_in.replace('  ', '')
					if l==1: #names
						names.append(d_in)
					elif l==2:
						city.append(d_in)
					w_in.append(d_in)
					w.append(w_in); w_in=[]
		print len(names), len(city)
		df=DataFrame({'Name':names, 'City':city})
		df.reindex(['Names', 'City'], axis=1)
		df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
		

		

process = CrawlerProcess({
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, ''like Gecko) Chrome/45.0.2454.85 Safari/537.36'
})

process.crawl(to_excel)
process.start() # the script will block here until the crawling is finished
