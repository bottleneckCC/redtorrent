

def IsItDownloaded(self, movietitle=None):





    cur.execute("SELECT * FROM dlmovies WHERE title = ?", (movietitle))
    check1=cur.fetchone()

    if check1 is not None:
        print "Already downloaded!"
 
    else:
        print "Good to go!" 
