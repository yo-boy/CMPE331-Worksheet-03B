"""
Stage : Development -01
 @author : Abdel Rahman Abdin , 120200128
 @author : Hamza Sallam , 120200013

"""

import urllib.request
import sys
# we take arguments in the form "2022 12 2 climate"
arguments = sys.argv


def getCategory(category):
    # returns the html file of category as a string
    return urllib.request.urlopen("https://www.nytimes.com/section/"+ category).read()

