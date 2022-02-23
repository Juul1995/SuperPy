# Imports
import argparse
import csv
from datetime import date

from numpy import require
import basis
import extra
import support

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# https://levelup.gitconnected.com/the-easy-guide-to-python-command-line-arguments-96b4607baea1?gi=7be7cd88f467
# PS C:\Users\Administrator\Winc-BE\SuperPy> python main.py --action buy --argument 9, "hagelslag", "2021-12-30", 3.00, "2031-01-01", 3        
# python main.py --action inventory --input "today" 
# nargs="+", action="extend",
parser = argparse.ArgumentParser(
        description="The SuperPy system")

# create the inventory argument 
parser.add_argument("--action", choices= ["inventory" ,"buy" ,"sell" ,"revenue" ,"profit" ,"chart" ,"excel", "advanced_time"], help= "choose : inventory,buy,sell,revenue,profit,chart,excel", required= True)
parser.add_argument("--argument", action= "extend", nargs = '+', required=False, 
help=
"""(1) inventory: Date muste be 'today', 'tommorow', 'yesterday', 'YYYY-MM-DD' or int (- or + from current date).
(2) buy: Give: 'id', 'product_name', 'buy_date', 'buy_price', 'expiration_date', 'count'. expiration date must be 'YYYY-MM-DD'.
(3) sell: Give: id, product, amount, sell_price, sell_date (Date muste be 'today', 'tommorow', 'yesterday', 'YYYY-MM-DD' or    
                        int (- or + from current date).
(4) profit: write 2 dates, Date muste be 'today', 'tommorow', 'yesterday', 'YYYY-MM-DD' or int (- or + from current date).
(5) chart: No arguments. Gives the current inventory. 
(6) excel: choose; 'bought.csv', 'expired.csv' or 'sold.csv
(7) advanced_time : 
""")


args = parser.parse_args()

action = args.action 
argument = args.argument

# Nargs "+" zorgt er voor dat de argumenten als een "list" worden opgeslagen, maar for de enkelvoudige argumenten moet ik daarom indexen. 
if action == "inventory":
    basis.inventory(argument[0])
elif action == "buy":
    # buy : 'id', 'product_name', 'buy_date', 'buy_price', 'expiration_date', 'count'.
    basis.buy_product(argument)
    value = argument
elif action == "sell":
    basis.sell_product(argument)
    value = argument
# elif action == "revenue":
#     basis.revenue_report(argument[0])
elif action == "profit": 
    extra.select_profit(argument)
    value = argument  
elif action == "chart":
    extra.inventory_chart()
elif action == "excel":
    extra.CSV_to_Excel(argument[0])
elif action == "advanced_time":
    support.advanced_time(argument[0])






    

    









