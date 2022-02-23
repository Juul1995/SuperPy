import pandas as pd
from matplotlib import pyplot as plt
import csv
import datetime
from pandas.io.pytables import Selection
from basis import sell_product
import os
from support import correct_date

# Print the inventory as a bar-chart.
def inventory_chart():
    data = pd.read_csv("bought.csv")
    x_product = data["product_name"].tolist()
    y_count = data["count"].tolist()
    plt.grid(axis="y", color="Salmon", linestyle="--", linewidth=0.4)
    print(plt.bar(x_product, y_count, label="inventory", color="Teal"))
    plt.title("SuperPy Inventory")
    plt.show()


# export CSV as excel
def CSV_to_Excel(csv):
    csv_df = pd.read_csv(csv)
    # split .csv from name
    old_n = csv.split(".", 1)
    new_n = old_n[0]
    ex = pd.ExcelWriter(f"{new_n}.xlsx")
    csv_df.to_excel(ex, index=False)
    ex.save()


# Export selections of bought to CSV
def select_buy(datum_1, datum_2):
    d1 = correct_date(datum_1)
    d2 = correct_date(datum_2)
    data = pd.read_csv("bought.csv")
    data["buy_date"] = pd.to_datetime(
        data["buy_date"], format="%Y-%m-%d").dt.date

    for x in data["buy_date"]:
        if d1 <= x <= d2:
            item = (data[data["buy_date"] == x])
            if os.path.isfile(f"./bought_{d1}-{d2}.csv") == True:
                item.to_csv(f"bought_{d1}-{d2}.csv", mode="a", header=False)
                print(item)
            else:
                item.to_csv(f"bought_{d1}-{d2}.csv", mode="a")
                return print(item)


# Export selections of revenue to CSV
def select_revenue(list_2_dates):
    d1 = correct_date(list_2_dates[0])
    d2 = correct_date(list_2_dates[1])
    data = pd.read_csv("sold.csv")
    # convert str to date
    data["sell_date"] = pd.to_datetime(
        data["sell_date"], format="%Y-%m-%d").dt.date
    for x in data["sell_date"]:
        if d1 <= x <= d2:
            item = (data[data["sell_date"] == x])
            if os.path.isfile(f"./revenue_{d1}-{d2}.csv") == True:
                item.to_csv(f"revenue_{d1}-{d2}.csv", mode="a", header=False)
                print(item)
            else:
                item.to_csv(f"revenue_{d1}-{d2}.csv", mode="a")
                return print((f"revenue_{d1}-{d2}.csv"))
        else:
            print("There was no revenue during this period")


# Calculate the profit for a given period
def select_profit(list_2_dates):
    d1 = correct_date(list_2_dates[0])
    d2 = correct_date(list_2_dates[1])
    data = pd.read_csv("sold.csv")

    data["sell_date"] = pd.to_datetime(
        data["sell_date"], format="%Y-%m-%d").dt.date
    print(data)
    profit_total = []
    for x in data["sell_date"]:
        if d1 <= x <= d2:
            item = (data[data["sell_date"] == x])
            p = item["profit"]
            for x in p:
                profit_total.append(x)
        

    return print(sum(profit_total))


# if __name__ == "__main__":
#     pass
