from selenium import webdriver

browser = webdriver.Firefox()

# Akute has heard about a cool new online to-do app. He goes
# to check out its homepage
browser.get('http://localhost:8000')

# He notices the page title and header mention to-do lists
assert 'To-Do' in browser.title, "Browser title was "+ browser.title

# He is invited to enter a to-do item straight away

# He types "Buy peacock feathers" into a text box (Akute's hobby
# is tying fly-fishing lures)

# When He hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. He
# enters "Use peacock feathers to make a fly" (Akute is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then He sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# He visits that URL - her to-do list is still there.

# Satisfied, He goes back to sleep
browser.quit()
