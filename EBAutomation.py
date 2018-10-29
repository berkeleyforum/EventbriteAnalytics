from selenium import webdriver
import pyautogui
import time
import re
from selenium.webdriver.common.keys import Keys

trelloURL = "https://trello.com/c/BJT6bLBH/16-sean-miyashiro"
driver = webdriver.Chrome('/Users/avinash/Documents/Code/EventbriteAnalytics/chromedriver')

trelloData = """**Asians in Culture: The 88Rising Phenomenon | Sean Miyashiro at the Berkeley Forum**


November 2, 6:00 PM | Location TBA


**Event Description**
Join Sean Miyashiro, CEO, in a fireside chat as he speaks about 88rising, a hybrid media company and leading tastemaker for Asian youth culture. His talk will focus on the importance of making a place for Asians in hip-hop, how 88rising effortlessly bridges East to West while celebrating Asia's cultural vibrancy, and what it takes to succeed in the music industry. 


**Speaker Bio**
With an uncanny and extraordinary vision for brand strategy and creative direction, Sean Miyashiro has made a career out of creating innovative brands that push boundaries to the next level. An out-of-the-box thinker with a proven ability to bring ideas to life, Miyashiro’s background is in music as a former Vice creative. 88rising, then, fits right into the profile, as a vision of the future. Responsible for breaking Keith Ape, Higher Brothers, and Rich Brian into the US market - among the first Asian hip hop artists to truly crossover - Sean masterfully blends knowledge of online viral marketing strategies with constant creativity, ingenuity, and leadership. The result is revolutionary: a celebration of progressive, inclusive youth culture, with a distinct Asian panache. There is much to be discovered in the unique, vibrant, cultural landscape of Asia, across music, fashion, art, food, and more - and 88rising is there for all of it. A true pioneer in the media and entertainment industry where nothing else comes close, the company is trailblazing the way for never-before-seen, groundbreaking content and quickly becoming a leader in progressive music, and the apex of youth culture worldwide. Heralded by Forbes as the bridge between East and West, and the face of a new generation of Asian youth by CNN, 88rising is truly an authentic crossing of oceans and the architect of a new youth culture - with Sean Miyashiro at its helm.
"""
trelloImageURL = "forum.png"
eventData = [[s.replace('\n', '').replace('**', '') for s in trelloData.split("\n\n\n")][0]]
eventData.extend([re.sub("\*\*.+?\*\*", "", s.replace('\n', '')) for s in trelloData.split("\n\n\n")])
eventData = [s for s in eventData if len(s) > 1]

title = eventData[0]
date = eventData[1].split('|')[0]
date, eventTime = date.split(',')[0].strip().lower(), date.split(',')[1].strip()
m = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april':4,
         'may':5,
         'june':6,
         'july':7,
         'august':8,
         'september':9,
         'ocober':10,
         'november':11,
         'december':12
        }
date = str(m[date.split(" ")[0]]).strip()+"/"+date.split(" ")[1].strip()+"/2018"

location = eventData[1].split('|')[1]
description = title + "\n" + eventData[1] + "\n" + "Event Description\n" + eventData[2] + "\nSpeaker Bio \n" + eventData[3]

driver.get("https://www.eventbrite.com/create")
time.sleep(1)
pyautogui.typewrite("email")
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite("password")
pyautogui.press('enter')
time.sleep(1)


titleField = driver.find_element_by_name('group-details-name')
titleField.send_keys(title)
locationField = driver.find_element_by_id('location-name-input')
locationField.send_keys(location)

startTimeDate = driver.find_element_by_class_name('js-dtp-startdatetimepicker')
startDate = startTimeDate.find_element_by_class_name('js-dtp-datepicker-input')
pyautogui.click(startDate.location['x'], startDate.location['y'])
while len(startDate.get_attribute('value')) > 0:
    startDate.send_keys(Keys.BACK_SPACE)
startDate.send_keys(date)

startTime = startTimeDate.find_element_by_class_name('js-dtp-timepicker-input')
pyautogui.click(startTime.location['x'], startTime.location['y'])
while len(startTime.get_attribute('value')) > 0:
    startTime.send_keys(Keys.BACK_SPACE)
startTime.send_keys(eventTime)

endTimeDate = driver.find_element_by_class_name('js-dtp-enddatetimepicker')
startDate = endTimeDate.find_element_by_class_name('js-dtp-datepicker-input')
pyautogui.click(startDate.location['x'], startDate.location['y'])
while len(startDate.get_attribute('value')) > 0:
    startDate.send_keys(Keys.BACK_SPACE)
startDate.send_keys(date)

startTime = endTimeDate.find_element_by_class_name('js-dtp-timepicker-input')
pyautogui.click(startTime.location['x'], startTime.location['y'])
while len(startTime.get_attribute('value')) > 0:
    startTime.send_keys(Keys.BACK_SPACE)
startTime.send_keys(str(int(eventTime[:1])+1)+eventTime[1:])

descriptionBox = driver.find_element_by_id('event_details_details')
driver.execute_script("arguments[0].scrollIntoView();", descriptionBox)
time.sleep(1)
boxCoords = driver.find_element_by_id('event_details_details').location_once_scrolled_into_view
print(boxCoords)
pyautogui.click(boxCoords['x']+ 100, boxCoords['y'] + 250)
pyautogui.typewrite(description)

ticketHeader = driver.find_element_by_id('create_tickets_header')
freeTicketButton = driver.find_element_by_id('create-ticket-free-button')
driver.execute_script("arguments[0].scrollIntoView();", ticketHeader)
time.sleep(1)
freeTicketButton.click()
time.sleep(1)
berkeleyTickets = driver.find_element_by_name('group-tickets-0-ticket_type')
berkeleyTickets.send_keys('UC Berkeley Students, Staff, and Faculty')
berkeleyTicketsCount = driver.find_element_by_name('group-tickets-0-quantity_total')
berkeleyTicketsCount.send_keys('125')
ticketFooter = driver.find_element_by_class_name('js-ticket-summary-footer')
freeTicketButton = ticketFooter.find_element_by_class_name('js-create-ticket')
freeTicketButton.click()
time.sleep(1)
generalTickets = driver.find_element_by_name('group-tickets-1-ticket_type')
generalTickets.send_keys('General Admission')
pyautogui.press('tab')
pyautogui.typewrite('75')

makeLiveButton = driver.find_element_by_id('make-event-live-button-almost-done')
driver.execute_script("arguments[0].scrollIntoView();", makeLiveButton)
makeLiveButton.click()