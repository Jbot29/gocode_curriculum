#Stack Challenge 2: Build an html validator using a stack data structure

test_html = '''<html><body><div><h1>Test Html</h1><p></p></div></body></html>'''
test_bad_html = '''<html><body><div><h1>Test Html</h1><p></div></body></html>'''
test_bad_html2 = "</div>"
test_bad_html3 = "<div>"

#Tip: You can consider using regex, but it is not recommended at this point because we have not taught it.  It is not necessary to solve this problem.
import re

#Here are some methods to help guide the structure of your program, you do NOT have to use these.

def get_tokens(html):
    """Converts a string of html into an array of tokens"""
    pass

def open_tag(token):
    """takes a string token, checks it matches <*> if so return the tag name"""
    pass
        
def close_tag(token):
    """takes string token, checks if matches </*> if so return tag name"""
    pass

def valid_html(tokens):
    """takes an array of tokens parsed from html, and validates correct ordering of open/close"""
    pass


assert valid_html(get_tokens(test_html)) == True
assert valid_html(get_tokens(test_bad_html)) == False

        
    


