"""
Stage : Development -01
 @author : Abdel Rahman Abdin , 120200128
 @author : Hamza Sallam , 120200013

"""
from bs4 import BeautifulSoup
import urllib.request
import sys
# we take arguments in the form "2022 12 2 climate"
arguments = sys.argv


def getCategory(category):
    # returns the html file of category as a string
    return urllib.request.urlopen("https://www.nytimes.com/section/"+ category).read()

def parseDate(html, date):
    soup = BeautifulSoup(html, 'html.parser')
    
def main(args):
    # takes a date and category as command line arguments and return an array of headlines
    html = getCategory(args[-1])
    date = args[0] + "/" + args[1] + "/" + args[2]
    return parseDate(html, date)
