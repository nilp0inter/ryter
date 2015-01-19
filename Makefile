# Makefile for Python package
#

.PHONY: clean test

BEHAVE=$(shell which behave)

clean:
	find . -name "__pycache__" -type d | xargs rm -rf
	find . -name "*.pyc" -type f | xargs rm -f

test:
	$(MAKE) clean
	$(BEHAVE) --tags ~@wip tests/spells
