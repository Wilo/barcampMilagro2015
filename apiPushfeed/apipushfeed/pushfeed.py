import rethinkdb as r

class daoApi:

  def __init__(self):
     r.connect('localhost',28015).repl()
     self.db = r.db('pushfeed').table('news')

  def getData(self):
      return self.db.run()
