MODULES=librarian

all: flakes test

test:: clear_coverage run_tests test_report

analysis:: flakes

flakes:
	@echo Searching for static errors...
	@flake8 --statistics ${MODULES}

coveralls::
	coveralls

publish: run_publish run_tag

run_publish::
	@python setup.py sdist --formats zip,gztar upload

run_tag::
	python -m releaseme --git

run_tests:
	@echo Running Tests...
	@coverage run --source=librarian -- manage.py test -v 2 librarian

test_report:
	@coverage report -m

clear_coverage:
	@echo Cleaning previous coverage...
	@coverage erase