install:
	pip install -r requirements.txt -r test-requirements.txt
	pip install -e .

run:
	yoink

test:
	mypy yoink
	pylint -f colorized yoink
