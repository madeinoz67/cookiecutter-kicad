

.PHONY: serve build install

install:
	poetry install

build:
	poetry run mkdocs build

serve: build
	poetry run mkdocs serve

clean:
	rm -rf site/
