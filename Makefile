include .env
export $(shell sed 's/=.*//' .env)

run:
	python3 stripe_statements.py

clean:
	rm ./*.csv
