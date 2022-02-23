# Dit bestand bevat alle functies die de basis-functies ondersteunen.  

from datetime import date, timedelta, datetime
import pandas as pd 
import os.path
from os import path

# Functie voor het omzetten van de data-input to een date-type, de teruggeven variabele d is de datum:
def correct_date(datum):
    if path.exists("date.txt") == False:
        try: 
            if datum == None:
                d = date.today()
                return d
            if datum == "today":
                d = date.today()
                return d
            if datum == "tomorrow":
                d = date.today() + timedelta(1)
                return d
            if datum == "yesterday":
                d = date.today() + timedelta(-1)
                return d
            # datum is string, maar moet een int zijn als +5 of bijv. -5 wordt gegeven.
            if len(str(datum)) < 3:
                di = int(datum)
                d = date.today() + timedelta(di)
                return d
            try:
                d = datetime.strptime(datum, "%Y-%m-%d").date()
                return d
            except:
                return "ERROR: date muste be 'today', 'tomorrow', 'yesterday', 'YYYY-MM-DD' or int (- or + from current date)"
        except: 
            return "ERROR: date muste be 'today', 'tomorrow', 'yesterday', 'YYYY-MM-DD' or int (- or + from current date)"
    elif path.exists("date.txt") == True:
        file = open("date.txt")
        line = file.read()
        file.close()
        d = datetime.strptime(line, "%Y-%m-%d").date()
        try: 
            if datum == "today":
                return d 
            elif datum == "tomorrow":
                dd = d + timedelta(1)
                return dd 
            elif datum == "yesterday":
                dd = d + timedelta(-1)
                return dd
            elif len(str(datum)) < 3:
                dd = d + timedelta(di)
                return dd
        except:
            return "ERROR: date muste be 'today', 'tomorrow', 'yesterday', 'YYYY-MM-DD' or int (- or + from current date)"




def advanced_time(inty):
    if inty == "reset":
        if os.path.exists("date.txt"):
        # removing the file using the os.remove() method
            os.remove("date.txt")
            return print(f"Reset completed; real date {date.today()} is used")
    else: 
        try: 
            di = int(inty)
            d = date.today() + timedelta(di)
            d = str(d)
            with open('date.txt', 'w') as file:
                file.write(d)
                file.close()
                return print(f"The new date has been set as {d}")
        except:
            return print("Error, please insert an int + or - from current date")

if __name__ == "__main__":
    print(correct_date("today"))

