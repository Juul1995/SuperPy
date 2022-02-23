import csv
from datetime import date, time, timedelta
import argparse
import datetime
from numpy import prod

import pandas as pd
from support import correct_date
import os

# re-stock inventory
def buy_product(prod_list):
        prod_list[2] = str(correct_date(prod_list[2]))
        prod_list[4] = str(correct_date (prod_list[4]))
    # see if csv exists
        if os.path.isfile("./bought.csv") == False:
            bought_list = []
            bought_list.append(prod_list)
            bought = pd.DataFrame(bought_list, columns=[
                "id", "product_name", "buy_date", "buy_price", "expiration_date", "count"])
            bought.to_csv("bought.csv")
            return print(f"{prod_list[1]} added to inventory")
        elif os.path.isfile("./bought.csv") == True:
            open_bought = pd.read_csv("bought.csv", index_col=0)
            # To ensure code keeps running when df is empty;
            if open_bought.empty == True:
                bought_list = []
                
            elif open_bought.empty == False:
                bought_list = open_bought.values.tolist()
                # Add to inventory, or add to existing stock.
                for x in bought_list:
                    if prod_list[1] in x:
                        print(f"old stock {(x[5])}, added {prod_list[5]}")
                        for x in bought_list:
                            if prod_list[1] == x[1]:
                                x[5] = int(prod_list[5]) + int(x[5])
                                bought = pd.DataFrame(bought_list, columns=[
                                    "id", "product_name", "buy_date", "buy_price", "expiration_date", "count"])
                                bought.to_csv("bought.csv")
                                print(
                                    f"{prod_list[1]} added to existing stock in inventory")
                                return (bought)
                else:
            
                    bought_list.append(prod_list)
                    bought = pd.DataFrame(bought_list, columns=[
                        "id", "product_name", "buy_date", "buy_price", "expiration_date", "count"])
                    bought.to_csv("bought.csv")
                    return print(f"{prod_list[1]} added to inventory")


# Inventory given date
def inventory(datum):
    expired_list = []
    d = correct_date(datum)
    open_bought = pd.read_csv("bought.csv", index_col=0)
    bought_list = open_bought.values.tolist()
    for x in bought_list:
        l = datetime.datetime.strptime(x[4], "%Y-%m-%d")
        print(l)
        if l < datetime.datetime.strptime(str(d), "%Y-%m-%d"):
            bought_list.remove(x)
            expired_list.append(x)
            print("Expired product, removed from inventory")

        bought = pd.DataFrame(bought_list, columns=[
            "id", "product_name", "buy_date", "buy_price", "expiration_date", "count"])
        expired = pd.DataFrame(expired_list, columns=[
            "id", "product_name", "buy_date", "buy_price", "expiration_date", "count"])
        bought.to_csv("bought.csv")
        expired.to_csv("expired.csv")
        return print(bought)

# def sell_product
def sell_product(prod):
    sold_product = []
    id = prod[0]
    product = prod[1]
    sell_price = prod[3]
    amount = prod[2]
    try:
        sell_date = prod[4]
    except IndexError:
        sell_date = "today"
    d = correct_date(sell_date)
    open_bought = pd.read_csv("bought.csv", index_col=0)
    bought_list = open_bought.values.tolist()
    # check of de value bestaat in bought.csv 
    if product not in open_bought.values:
        return print(f"ERROR:{product} not in stock.")
    # de value bestaat; 
    for x in bought_list:
        if product == x[1]:
            new_amount = int(x[5]) - int(amount)
            if new_amount <= 0:
                bought_list.remove(x)
                bought = pd.DataFrame(bought_list, columns=[
                    "id", "product_name", "buy_date", "buy_price", "expiration_date", "count"])
                bought.to_csv("bought.csv")
                return print(f"ERROR:{product} not in stock.")
            if new_amount > 0:
                x[5] = new_amount
                id = x[0]
                # update new row to bought.csv
                bought = pd.DataFrame(bought_list, columns=[
                    "id", "product_name", "buy_date", "buy_price", "expiration_date", "count"])
                bought.to_csv("bought.csv")
                print(f"{product} in stock")
                # add to sold_list & create 'sold.csv"
                sold_product.append(id)
                sold_product.append(product)
                sold_product.append(amount)
                sold_product.append(sell_price)
                cost = float(x[3]) * float(amount)
                round_up = round((float(sell_price) - cost), 2)
                # add the profit, to prepare for profit function
                sold_product.append(round_up)
                sold_product.append(d)
                # List containing row of product is created in sold_product
                # see if CSV with sold items exists;

                if os.path.isfile("./sold.csv") == False:
                    sold_list = []
                    sold = pd.DataFrame([sold_product], columns=[
                        "id", "product", "amount", "sell_price", "profit", "sell_date"])
                    sold.to_csv("sold.csv")

                    return print(f"{product} is sold")

                if os.path.isfile("./sold.csv") == True:
                    open_sold = pd.read_csv("sold.csv", index_col=0)
                    sold_list = open_sold.values.tolist()

                for x in sold_list:
                    if open_sold.empty == True:
                        sold_list = []
                        sold_list.append(sold_product)
                        sold = pd.DataFrame(sold_list, columns=[
                            "id", "product", "amount", "sell_price", "profit", "sell_date"])
                        sold.to_csv("sold.csv")
                        return print(f"{product} is sold")

                    else:
                        sold = pd.DataFrame([sold_product], columns=[
                            "id", "product", "amount", "sell_price", "profit", "sell_date"])
                        sold.to_csv("sold.csv", mode="a",
                                    header=False)
                        return print(f"{product} is sold")
            

                
             


# report revenue
def revenue_report(datum):
    if datum == int:
        d = correct_date(datum)
    else:
        d = correct_date(datum)

    if os.path.isfile("./sold.csv") == False:
        return "No products have been sold, no revenue yet"
    revenue_sum = []
    df = pd.read_csv("sold.csv")
    lf = df.values.tolist()
    for item in lf:
        if item[3] == str(d):
            revenue_sum.append(item[4])
    return print(f"The revenue of {d} is EUR {sum(revenue_sum)}")


# report profit
def report_profit(datum):
    profit_list = []
    d = correct_date(datum)
    if os.path.isfile("./sold.csv") == False:
        return "No products have been sold, no profit yet"

    df = pd.read_csv("sold.csv")
    data = df.values.tolist()
    for item in data:
        if item[3] == str(d):
            profit_list.append(item[6])

    # Extract expired goods from profit.
    df_2 = pd.read_csv("expired.csv")
    data_2 = df_2.values.tolist()
    for item_2 in data_2:
        if item_2[5] == str(d):
            minus_expired = -(item_2[4])
            profit_list.append(minus_expired)
    return print(f"The profit of {d} is EUR {sum(profit_list)}")



# # test commands
# if __name__ == '__main__':
#     pass


