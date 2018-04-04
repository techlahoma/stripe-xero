import os
import pickle
import time
import calendar
import csv
import datetime
import stripe

last_txn_filename = 'last_txn_time.pkl'

def process_new_transactions():
    last_txn_time = None
    try:
        with open(last_txn_filename, 'rb') as last_txn_file:
            last_txn_time = pickle.load(last_txn_file)
    except IOError:
        print("No previous transaction found. Getting all available transactions.")
        pass

    utcnow_timestamp = calendar.timegm(time.gmtime())

    page_size = 2
    filter_params = {
        'limit': page_size,
    }
    if last_txn_time:
        filter_params['created'] = {'gt': last_txn_time}

    have_more_data = True
    balance_transactions = []
    while have_more_data:
        page = stripe.BalanceTransaction.all(**filter_params)
        balance_transactions.extend(page['data'])

        have_more_data = page['has_more']
        if have_more_data:
            filter_params['starting_after'] = page['data'][-1]['id']

    print("Found %d new transactions" % len(balance_transactions))
    if len(balance_transactions) == 0:
        print("Not creating csv file.")
        return

    balance_transactions.sort(key=lambda b: b['created'])
    statement_filename = 'stripe_%s.csv' % utcnow_timestamp
    with open(statement_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'source', 'amount', 'currency', 'type', 'date', 'description'])
        for tr in balance_transactions:
            created_date = datetime.datetime.fromtimestamp(tr['created']).strftime('%Y-%m-%d')
            writer.writerow([tr['id'], tr['source'], "%.2f" % (tr['amount'] / 100.), tr['currency'], tr['type'], created_date, tr['description']])
            for fee in tr['fee_details']:
                writer.writerow([tr['id'], tr['source'], "%.2f" % (-1*fee['amount'] / 100.), fee['currency'], fee['type'], created_date, fee['description']])

    print("Created %s" % statement_filename)

    if balance_transactions:
        last_txn_time = max([b['created'] for b in balance_transactions])
        with open(last_txn_filename, 'wb') as last_txn_file:
            pickle.dump(last_txn_time, last_txn_file)


if __name__ == '__main__':
    stripe.api_key = os.environ['STRIPE_API_KEY']
    process_new_transactions()
