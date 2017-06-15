from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get('http://www.baseballamerica.com/draftdb/index.php')

#Set this later
#driver.implicitly_wait(10)

#Lets grab the title
title = driver.get_element_by_tag_name('title')
title.text

# We want to switch to the 2016 year and notice that
# this field carries the "SELECT" tagname and is named 'year'

selectYear = Select(driver.find_element_by_name('year'))

# Three ways to pick 2016
selectYear.select_by_index(1)
selectYear.select_by_visible_text("text")
selectYear.select_by_value('2016')


# We also want all rounds
# do something similiear to how we selected rounds

selectRound = Select(driver.find_element_by_name('round'))

selectRound.select_by_index(0)


# Now we are ready to execute the search.
# Locate the search button

search = driver.find_element_by_id('search500')
# it is an input so the search object has an function we to click it
search.click()

# notice that it might take a while for the page to load,
# Waits our useful, lets set one above.

#Now try to locate the table

table = driver.find_elements_by_tag_name('table')

#Check to see how many we got
len(table)

#Try to find a way to isolate the table we want
tableDiv = driver.find_elements_by_class_name('column-one')
len(tableDiv)

#Good!, just one element so it must be what we are looking for
#Now do the same to find table

table = tableDiv.find_elements.by_tag_name("table")
len(table)

#Good!  Now, try to print out each item from the first row
