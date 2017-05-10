.PHONY: clean
.PHONY: warn

%.pdf: %.tex $(DEPENDS)
	rubber --quiet --pdf --warn misc --warn refs --synctex $<

warn: main.tex $(DEPENDS)
	rubber --quiet --pdf --warn all --synctex $<

clean:
	rm -f *.aux *.bbl *.blg *.log *.toc *.snm *.out *.nav
