# wiki word cloud generator
# github: rafaelwi

""" Imports """
import sys
import wcfuncts as wc 

""" Main Program """
# Get URL
url = wc.get_args(sys.argv)

# Get filename
filename = wc.get_filename(url)

# Get page text
page_text = wc.get_page_text(url)

# Generate and save word cloud
wc.generate_word_cloud(page_text, filename)

### end of script cloud.py ###
