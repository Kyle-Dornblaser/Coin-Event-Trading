#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Kyle Dornblaser"
__version__ = "0.1.0"
__license__ = "MIT"

from bs4 import BeautifulSoup
import os
import sqlite3
import urllib.request

class DatabaseWorker:

    def __new__(cls):
        """ Signleton Pattern. Checks for existing instance before creating a
        new instance """
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseWorker, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        sqlite_file = os.path.join(os.path.dirname(__file__), 'db.sqlite')
        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()

        self.create_database()

    def create_database(self):
        """ Create the database if it does not already exist """

        print('Creating database if it does not already exist')
        create_table_statement = """
            CREATE TABLE
            IF NOT EXISTS events (
             id integer PRIMARY KEY,
             coin text NOT NULL,
             event_date text,
             description text,
             posted_date text,
             validation integer,
             event_type text,
             buy_low real,
             buy_avg real,
             buy_high real,
             sell_high real,
             sell_date text,
             high_btc real,
             late_sell_low real,
             late_sell_avg real,
             late_sell_high real
            );
        """
        self.c.execute(create_table_statement)

        self.conn.commit()


    def add_record(self, data):
        """ Add a new record to the database with supplied dictionary """

        if not self.already_exists(data, 'event_type'):
            sql = 'INSERT INTO events ('

            keys = list(data)
            values = list(data.values())
            values = list(map(lambda x: "\'" + x + "\'", values))

            sql += ', '.join(keys) + ') VALUES ('
            sql += ', '.join(values) + ');'
            self.c.execute(sql)
            self.conn.commit()

    def already_exists(self, data, exclude=None):
        """ Check to see if record already exists in the database. Optional
        param to exclude a passed key from the database query. """

        sql = 'SELECT * FROM events WHERE '

        keys = list(data)
        values = list(data.values())

        if exclude:
            exclude_index = keys.index(exclude)
            del keys[exclude_index]
            del values[exclude_index]

        values = list(map(lambda x: "\'" + x + "\'", values))

        where_statement = []
        for i, val in enumerate(keys):
            where_statement.append("{0} = {1}".format(keys[i], values[i]))

        sql += ' AND '.join(where_statement) + ';'

        result = self.c.execute(sql)
        rows = self.c.fetchall()

        return len(rows) > 0

    def __del__(self):
        """ Close the database when the object is destroyed """
        # TODO replace with https://en.wikibooks.org/wiki/Python_Programming/Context_Managers
        self.conn.close()



def main():
    """ Main entry point of the app """

    scrape()


def scrape():
    """ Scrapes the event data and adds it to the database """
    print('Scraping events')

    base_url = 'http://coinmarketcal.com'

    categories = {0: 'Release',
                    1: 'Rebranding',
                    2: 'Coin Supply',
                    3: 'Exchange',
                    4: 'Conference',
                    5: 'Community Event',
                    6: 'Other'}

    db = DatabaseWorker()

    for key, value in categories.items():
        print ("{0}:{1}".format(key, value))

        html_doc = urllib.request.urlopen("{0}/pastevents?form%5bcategories%5d%5b%5d={1}".format(base_url, key))
        scraper = BeautifulSoup(html_doc, 'html.parser')

        # emulate do while
        up_to_date = False
        while not up_to_date:
            for item in scraper.find_all('div', class_='content-box-general'):
                event_date = item.h5.strong.get_text()
                coin = item.h5.next_sibling.next_sibling.strong.get_text()
                description = item.h5.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
                posted_date = item.find('p', class_='added-date').get_text()
                validation = item.find('div', class_='progress-bar').get('aria-valuenow')
                data = {'event_date': event_date,
                        'coin': coin,
                        'description': description,
                        'posted_date': posted_date,
                        'validation': validation,
                        'event_type': value}
                if (db.already_exists(data, 'validation')):
                    # up to date, move on to next category
                    print("{0}: up to date".format(value))
                    up_to_date = True
                    break;
                else:
                    print("{0}: adding record for {1}".format(value, coin))
                    db.add_record(data)

            next_page = scraper.find('i', class_='fa fa-angle-right')
            if (next_page):
                next_page = next_page.parent.get('href')
                html_doc = urllib.request.urlopen("{0}{1}".format(base_url, next_page))
                scraper = BeautifulSoup(html_doc, 'html.parser')
            else:
                up_to_date = True;

def get_prices():
    """ Get prices for all past events """
    # TODO

def generate_html():
    """ Generate HTML document with all the data from the database """
    # TODO

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
