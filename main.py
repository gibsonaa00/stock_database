from database import DataBase as db
from webscraper import yahoo_finance as yf
from declared_enums import ScrapeMethod,Columns
import pandas as pd
import os
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-s", "--stockname", dest="stock_name",help="Stock name")
parser.add_argument("-sd", "--startdate", dest="start_date", help="Start date", default=None)
parser.add_argument("-ed", "--enddate", dest="end_date", help="End Date", default=None)
args = parser.parse_args()


def main():
    stock_db =db(f"stocks.db")
    scrape = yf(database=stock_db,db_symbol=args.stock_name)

    if stock_db.check(table=args.stock_name):
        max_date = stock_db.get_latest_date(table=args.stock_name)
        scrape(stock=args.stock_name,start_date=max_date,method=ScrapeMethod.FROM)
    else:
        scrape(stock=args.stock_name,method=ScrapeMethod.ALL)
    
    df = pd.DataFrame(stock_db.get(table=args.stock_name))
    df.sort_values(Columns.DATE.name.lower(), inplace=True)
    df.to_csv(f"{os.environ['HOME']}/Downloads/{args.stock_name}.csv")

if __name__ == "__main__":
    main()