PREFIX = /usr/local
MANPREFIX = ${PREFIX}/share/man

install:
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp -f clpimg*.py ${DESTDIR}${PREFIX}/bin
	chmod 755 ${DESTDIR}${PREFIX}/bin/clpimg*.py

uninstall:
	rm -f ${DESTDIR}${PREFIX}/bin/clpimg*.py

.PHONY: install uninstall
