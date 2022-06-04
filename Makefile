all: grammar code2node.zip

antlr-4.10.1-complete.jar:
	wget https://www.antlr.org/download/antlr-4.10.1-complete.jar

.PHONY: grammar
grammar: antlr-4.10.1-complete.jar
	java -cp "${PWD}/antlr-4.10.1-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 NodeCode.g4 -no-listener -visitor -o grammar

clean:
	rm antlr-4.10.1-complete.jar
	rm -rf grammar

.PHONY: code2node.zip
code2node.zip: *.py LICENSE README.md antlr4 grammar
	rm -f $@
	mkdir -p code2node
	cp -a $^ code2node/
	$(shell find -name __pycache__ | xargs rm -rf )
	zip -r $@ code2node/
	rm -rf code2node
