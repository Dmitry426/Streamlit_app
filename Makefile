isort:
	isort .

black:
	black ./streamlit_bert

lint: isort black



build:
	docker compose build


run:
	docker compose up -d

stop:
	docker compose down

