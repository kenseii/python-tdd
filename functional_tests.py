from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() 

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Akute has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # He types "Buy peacock feathers" into a text box (Akute's hobby
        # is tying fly-fishing lures)
        input_box.send_keys('Buy peacock feathers')

        # When He hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows)
        )

        # There is still a text box inviting her to add another item. He
        # enters "Use peacock feathers to make a fly" (Akute is very methodical)
        self.fail('Finish the test!')
        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember his list. Then He sees
        # that the site has generated a unique URL for his -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, He goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
