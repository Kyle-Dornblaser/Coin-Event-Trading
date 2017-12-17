#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Kyle Dornblaser"
__version__ = "0.1.0"
__license__ = "MIT"

from bs4 import BeautifulSoup
import datetime
from yattag import Doc
import json
import os
import sqlite3
import urllib.request

ID_INDEX = 0
COIN_INDEX = 1
EVENT_DATE_INDEX = 2
DESCRIPTION_INDEX = 3
POSTED_DATE_INDEX = 4
VALIDATION_INDEX = 5
EVENT_TYPE_INDEX = 6
BUY_LOW_INDEX = 7
BUY_AVG_INDEX = 8
BUY_HIGH_INDEX = 9
SELL_HIGH_INDEX = 10
SELL_DATE_INDEX = 11
HIGH_BTC_INDEX = 12
LATE_SELL_LOW_INDEX = 13
LATE_SELL_AVG_INDEX = 14
LATE_SELL_HIGH_INDEX = 15

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
             event_date integer,
             description text,
             posted_date integer,
             validation integer,
             event_type text,
             buy_low real,
             buy_avg real,
             buy_high real,
             sell_high real,
             sell_date integer,
             high_btc real,
             LATE_SELL_LOW_INDEX real,
             LATE_SELL_AVG_INDEX real,
             LATE_SELL_HIGH_INDEX real
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
            values = list(map(lambda x: "\'{0}\'".format(x), values))

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
        values = list(map(lambda x: "\'{0}\'".format(x), values))

        where_statement = []
        for i, val in enumerate(keys):
            where_statement.append("{0} = {1}".format(keys[i], values[i]))

        sql += ' AND '.join(where_statement) + ';'

        result = self.c.execute(sql)
        rows = self.c.fetchall()

        return len(rows) > 0

    def get_rows_without_prices(self):
        sql = 'SELECT * FROM events WHERE buy_low IS NULL;'
        result = self.c.execute(sql)
        rows = self.c.fetchall()
        return rows

    def get_all_rows(self):
        sql = 'SELECT * FROM events;'
        result = self.c.execute(sql)
        rows = self.c.fetchall()
        return rows

    def update(self, id, data):
        sql = 'UPDATE events SET '
        keys = list(data)
        values = list(data.values())
        set_statement = []
        for i, val in enumerate(keys):
            if (values[i]):
                set_statement.append("{0} = {1}".format(keys[i], values[i]))

        sql += ','.join(set_statement)
        sql += " WHERE id = {0};".format(id)
        if (len(set_statement) > 0):
            self.c.execute(sql)
            self.conn.commit()

    def __del__(self):
        """ Close the database when the object is destroyed """
        # TODO replace with https://en.wikibooks.org/wiki/Python_Programming/Context_Managers
        self.conn.close()



def main():
    """ Main entry point of the app """
    scrape()
    get_prices()
    generate_html()


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
                time_offset = 60 * 60 * 5
                event_date = datetime.datetime.strptime(item.h5.strong.get_text().replace('By ', '').strip(), '%d %B %Y').timestamp() - time_offset
                coin = item.h5.next_sibling.next_sibling.strong.get_text()
                description = item.h5.next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip()
                posted_date = datetime.datetime.strptime(item.find('p', class_='added-date').get_text().replace('[Added ','').replace(']','').strip(), '%d %B %Y').timestamp() - time_offset
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
    base_url = 'https://min-api.cryptocompare.com/data/histohour?tsym=USD&limit=2000&aggregate=24&fsym='
    db = DatabaseWorker()
    rows = db.get_rows_without_prices()

    current_date = datetime.datetime.utcnow()
    for row in rows:
        coin = row[COIN_INDEX]
        coin_symbol = coin[coin.find("(")+1:coin.find(")")] # https://stackoverflow.com/questions/4894069/regular-expression-to-return-text-between-parenthesis


        event_date = row[EVENT_DATE_INDEX]
        posted_date = row[POSTED_DATE_INDEX]

        response = urllib.request.urlopen(base_url + coin_symbol)
        data = response.read().decode("utf-8")
        record = {'buy_low': None,
                    'buy_high': None,
                    'sell_high': None,
                    'sell_date': None,
                    'high_btc': None,
                    'late_sell_low': None,
                    'late_sell_high': None}
        for day in json.loads(data)['Data']:

            if (day['time'] == posted_date):
                # initial buys
                record['buy_high'] = day['high']
                record['buy_low'] = day['low']
            elif (day['time'] > posted_date and day['time'] <= event_date):
                # find date with highest sell and add the date, and high for that day
                if (not record['sell_high'] or day['high'] > record['sell_high']):
                    record['sell_high'] = day['high']
                    record['sell_date'] = day['time']
            elif (day['time'] == event_date + 86400):
                # if you did not sell before the event, this is the price the day after
                record['late_sell_high'] = day['high']
                record['late_sell_low'] = day['low']
            elif (day['time'] > event_date + 86400):
                # break the loop since we are done with the days we need
                break

        db.update(row[ID_INDEX], record)



    #print(current_date)

def generate_html():
    """ Generate HTML document with all the data from the database """
    print('Generating HTML')
    db = DatabaseWorker()
    rows = db.get_all_rows()
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('head'):
            doc.stag('link', href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css', type='text/css', rel='stylesheet')
            doc.stag('link', href='https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css', type='text/css', rel='stylesheet')
            with tag('script', src='https://code.jquery.com/jquery-2.2.4.min.js', type='text/javascript'):
                text()
            with tag('script', src='https://cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js', type='text/javascript'):
                text()
            with tag ('script', type='text/javascript'):
                text("""

                    $(document).ready(function(){
                    $('#table').DataTable();
                    });

                 """)

        with tag('body'):
            with tag('div', klass='container-fluid'):
                with tag('table', klass='table-striped', id='table'):
                    with tag('tr'):
                        with tag('th'):
                            text('Coin')
                        with tag('th'):
                            text('Event Type')
                        with tag('th'):
                            text('Description')
                        with tag('th'):
                            text('Low Buy')
                        with tag('th'):
                            text('High Buy')
                        with tag('th'):
                            text('High Sell')
                        with tag('th'):
                            text('Low Multiple')
                        with tag('th'):
                            text('High Multiple')
                        with tag('th'):
                            text('Sell Late Low')
                        with tag('th'):
                            text('Sell Late High')
                        with tag('th'):
                            text('Late Low Multiple')
                        with tag('th'):
                            text('Late High Multiple')
                        with tag('th'):
                            text('Sell Date')
                        with tag('th'):
                            text('Num Days')
                    for row in rows:
                        row = list(map(lambda x: '' if x is None else x, row))
                        with tag('tr'):
                            with tag('td'):
                                text(row[COIN_INDEX])
                            with tag('td'):
                                text(row[EVENT_TYPE_INDEX])
                            with tag('td'):
                                text(row[DESCRIPTION_INDEX])
                            with tag('td'):
                                text(row[BUY_LOW_INDEX])
                            with tag('td'):
                                text(row[BUY_HIGH_INDEX])
                            with tag('td'):
                                text(row[SELL_HIGH_INDEX])
                            with tag('td'):
                                if (row[SELL_HIGH_INDEX] == '' or row[BUY_HIGH_INDEX] == ''):
                                    text('')
                                else:
                                    text("{0:.2f}".format(row[SELL_HIGH_INDEX]/row[BUY_HIGH_INDEX]))
                            with tag('td'):
                                if (row[SELL_HIGH_INDEX] == '' or row[BUY_LOW_INDEX] == ''):
                                    text('')
                                else:
                                    text("{0:.2f}".format(row[SELL_HIGH_INDEX]/row[BUY_LOW_INDEX]))
                            with tag('td'):
                                text(row[LATE_SELL_LOW_INDEX])
                            with tag('td'):
                                text(row[LATE_SELL_HIGH_INDEX])
                            with tag('td'):
                                if (row[LATE_SELL_HIGH_INDEX] == '' or row[BUY_HIGH_INDEX] == ''):
                                    text('')
                                else:
                                    text("{0:.2f}".format(row[LATE_SELL_HIGH_INDEX]/row[BUY_HIGH_INDEX]))
                            with tag('td'):
                                if (row[LATE_SELL_HIGH_INDEX] == '' or row[BUY_LOW_INDEX] == ''):
                                    text('')
                                else:
                                    text("{0:.2f}".format(row[LATE_SELL_HIGH_INDEX]/row[BUY_LOW_INDEX]))
                            with tag('td'):
                                if (row[SELL_DATE_INDEX] == ''):
                                    text('')
                                else:
                                    text(datetime.datetime.fromtimestamp(row[SELL_DATE_INDEX]).strftime('%Y-%m-%d'))
                            with tag('td'):
                                text(round((row[EVENT_DATE_INDEX] - row[POSTED_DATE_INDEX]) / 86400))

    file = open(os.path.join(os.path.dirname(__file__), 'index.html'),'w',  encoding='utf-8')
    file.write(doc.getvalue())
    file.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
