# Report SuperPy

## Design probleem 1 : de datum 

Om de functies te laten werken op een geselecteerde datum moest de string-input steeds worden omgezet naar een datum. 
Om de code van de basisfuncties niet te lang te maken heb ik besloten om een aparte module te maken met support-functies. 

Hiermee herkennen de functies de volgende inputs als waarde; "today", "tommorow", "yesterday", negatieve getallen, positieve getallen én een string geschreven als 'YYYY-MM-DD'. In het laatste stukje heb ik een try-except blok toegepast zodat ik een error kon geven als de input aan geen van de voorwaarden voldoet. 

    def correct_date(datum):
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



## Design probleem 2 : argparse functies (list)

De functies binnen deze code hebben en wisselend aantal argumenten nodig. `Variable number of arguments can be set with the * character.` 
Omdat deze argumenten in een list (als string) worden opgeslagen heb ik ze met indexing uit deze lijsten gevist; 

Dit zie je in het argparse code-block (index[0] als er maar 1 argument is) én in de blokken van de basiscode. 

    # Nargs "+" zorgt er voor dat de argumenten als een "list" worden opgeslagen, maar for de enkelvoudige argumenten moet ik daarom indexen. 
    if action == "inventory":
            basis.inventory(argument[0])
    elif action == "buy":
        basis.buy_product(argument) 
    elif action == "sell":
        basis.sell_product(argument)
    # elif action == "revenue":
    #     basis.revenue_report(argument[0])
    elif action == "profit": 
        extra.select_profit(argument)  
    elif action == "chart":
        extra.inventory_chart()  
    elif action == "excel":
        extra.CSV_to_Excel(argument[0])



## Design probleem 3 : het aanmaken, updaten printen en plotten van een CSV-file. 

Om de CSV files makkelijker te lezen en te exporteren heb ik gekozen voor de `pandas` module. 
Ook kan ik op die manier, voor het visualiseren, gemakkelijk de plot functie gebruiken. 
Hiervoor heb ik wel telkens de x.pop(0) moeten gebruiken bij het opnieuw lezen omdat er anders steeds dubbele indexen zouden komen bij elke keer dat het CSV-file opnieuw wordt ingelezen. 

    # Inventory given date
    def inventory(datum):
        expired_list = []
        d = correct_date(datum)
        open_bought = pd.read_csv("bought.csv")
        bought_list = open_bought.values.tolist()
        for x in bought_list:
            x.pop(0)
        for x in bought_list:
            l = datetime.datetime.strptime(x[4], "%Y-%m-%d")
            print(l)
            if l < datetime.datetime.strptime(str(d), "%Y-%m-%d"):
                bought_list.remove(x)
                expired_list.append(x)
                print("Expired product, removed from inventory")
