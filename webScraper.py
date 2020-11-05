#!/usr/bin/env python3
# import docx
import requests
from bs4 import BeautifulSoup
# from docx.enum.section import WD_SECTION_START


def printJobs(input):
	r = requests.get(input)
	soup = BeautifulSoup(r.text, features='html.parser')
	for match in soup.find_all('div', id='jobDescriptionText'):
		print(match.get_text())


def htmlRequest(input): #function that parses URL for input from Indeed Listing
	r = requests.get(input) 
	soup = BeautifulSoup(r.text, features='html.parser')
	print(soup.title.string)
	list = []
	for link in soup.find_all('h2', {'class': 'title'}):
		links = link.a.get('href')
		completeLink = 'https://indeed.com' + links
		list.append(completeLink)
	for i in list:
		printJobs(i)
    


def main(): #main function to loop to write to docx file for output
	while input != '-1':
		x = input('Enter the URL here or 0 to quit: ')
		if x == 0:
			break
		else:
			htmlRequest(x)


if __name__ == '__main__': main()
