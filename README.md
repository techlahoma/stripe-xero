## Stripe-Xero

This is a simple script to create statements from your Stripe account that you can import into [Xero](http://www.xero.com/).

Transfer transactions from this tool should match the transactions in your bank account, so reconciliation is simpler. The tool also creates separate transactions for Stripe processing fees.

This tool saves the timestamp of the last balance transfer it found in Stripe, so successive runs will only include new transactions since the last run. This file needs to be committed and pushed up to github.

### Dependencies

 * Python 3
 * Stripe's Python library


### Instructions


#### First time only:
```
git clone https://github.com/techlahoma/stripe-xero/
pip install stripe
```
Copy the example environment file:

```
cp .env.example .env
```

You'll need to set the `STRIPE_API_KEY` environment variable in `.env` with your Stripe account's secret key. If you don't have one of these, get an account from the Treasurer or Infrastructure Chair.


#### Run the script:
If someone else has run the script since the last time you did, you will want to pull from github again:
```
git pull
```
Run the script:
```
make run
```

This task will grab all of your balance transactions and create a CSV file suitable for importing into Xero. The next time it runs, it will only grab new transactions since the last run.

#### Import the CSV file "statement" into our Stripe bank account in Xero: 

On OSX: run the following make command to open the Xero web page:
```
make upload
```
Other OSes: 
Import the newly created csv file to xero under the stripe account in Xero
(https://go.xero.com/Bank/Import.aspx?accountID=67641283-C7E3-423F-835C-0ABA7C556F36 )

Commit changes (new pickle file) and push back up to github:
```
git commit -a -m "pkl updates"
```


The *.pkl file saves the last date and time transactions were pulled. If you don’t push the *.pkl file up to github, the next person will pull all the transactions you pulled as well as any new. This is fine, though, because Xero detects duplicate entries and automatically removes them. It’s not perfect, though, so you will need to check the reconciliation report (as is standard).
