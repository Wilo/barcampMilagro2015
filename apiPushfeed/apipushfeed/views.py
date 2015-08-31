""" Cornice services.
"""
import rethinkdb as r
from cornice import Service
from pushfeed import daoApi

hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    dao = daoApi()
    data = dao.getData()
    items = []
    for d in data:
      items.append(d)
    return items
