PREFIX = /usr/local
MANPREFIX = ${PREFIX}/share/man

install:
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp -f clpimg ${DESTDIR}${PREFIX}/bin
	chmod 755 ${DESTDIR}${PREFIX}/bin/clpimg

uninstall:
	rm -f ${DESTDIR}${PREFIX}/bin/clpimg

.PHONY: install uninstall
