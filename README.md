Stripe-Xero
=================

This is a simple script to create statements from your Stripe account that you can import into [Xero](http://www.xero.com/). These statements will probably work with other accounting software with minimal tweaking.

Transfer transactions from this tool should match the transactions in your bank account, so reconciliation is simpler. The tool also creates separate transactions for Stripe processing fees.

This tool saves the timestamp of the last balance transfer it found in Stripe, so successive runs will only include new transactions since the last run.

Dependencies
------------

Stripe's Python library

    pip install stripe

How to Use It
------------

Copy the example environment file:
```
cp .env.example .env
```

You'll need to set the `STRIPE_API_KEY` environment variable in `.env` with your Stripe account's secret key.

Run the script:
```
make run
```

This task will grab all of your balance transactions and create a CSV file suitable for importing into Xero. The next time it runs, it will only grab new transactions since the last run.

To get the data into Xero, you'll first need a bank account in Xero that represents your Stripe account.

Import the CSV file "statement" into your Stripe bank account in Xero, confirm that the fields match up the way you expect, and start reconciling.

Enjoy!

Other Notes
-------

We use this script for quick-and-dirty reconciliation at [Retention Hero](http://www.retentionhero.com/). Bug reports and pull requests welcome.
