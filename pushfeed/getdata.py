#!/usr/bin/env python
# -*- codign: utf-8

# import rethinkdn as r
from requests import get


URL_PROVINCIAS = "http://www.codigopostal.ec./js/ec/gob/anp/visor/server/GeometriasJson.php?metodo=getProvincias"


def getProvincias():
    data = get(URL_PROVINCIAS)
    print data.decode('unicode_escape')


if __name__=="__main__":
    getProvincias()
