include .env
export $(shell sed 's/=.*//' .env)

run:
	python3 stripe_statements.py

upload:
	open "https://go.xero.com/Bank/Import.aspx?accountID=67641283-C7E3-423F-835C-0ABA7C556F36"

clean:
	rm ./*.csv
