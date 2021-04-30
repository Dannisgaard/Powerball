# -*- coding: utf8 -*-
import datetime
from random import randint

color_series = []
number_of_items_in_serie = 99
number_of_series = 4
number_of_gains = 125

print "\n\n"
print "\n**************************************************************************************"
print "\n********************          POWERBALL GET THE WINNERS          *********************"
print "\n**************************************************************************************"
print "\n\n"

try:
    number_of_items_in_serie = raw_input("Enter number of tickets in serie: ")
    number_of_series = raw_input("Enter number of series you got: ")
    number_of_gains = raw_input("Enter the number of gains you want: ")

    number_of_items_in_serie = int(number_of_items_in_serie)
    number_of_series = int(number_of_series)
    number_of_gains = int(number_of_gains)

except Exception ,e:
    print "Must be numbers"
    exit()

for color_serie_number in range(1 ,number_of_series + 1):
    color_serie = raw_input("Enter color for serie " + str(color_serie_number) + " :")
    color_series.append(color_serie)


class LotteryTicket:
    color = "blank"
    number = 0


current_time = datetime.datetime.now()
color_serie_sets = [set() for _ in xrange(number_of_series)]
all_result_gains_list = []


print "\nDraw tickets in powerball\n"
print "We draw in {0} series of {1} numbers\n".format(number_of_series, number_of_items_in_serie)
print current_time.strftime("Ticket draw at %b %d. %Y  %H:%M\n")

while len(all_result_gains_list) < number_of_gains:
    for i in range(len(color_series)):
        x = randint(1, number_of_items_in_serie)

        while x in color_serie_sets[i]:
            x = randint(1, number_of_items_in_serie)

        color_serie_sets[i].add(x)
        ticket = LotteryTicket()
        ticket.color = color_series[i]
        ticket.number = x
        all_result_gains_list.append(ticket)

all_result_gains = set(all_result_gains_list)

gains_number = 1
space = " "
for gains in all_result_gains:
    sgains_number = str(gains_number)
    print sgains_number + "."+ space*(10 - len(sgains_number)),gains.color, gains.number
    gains_number += 1



