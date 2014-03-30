#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras
import sys

con = None

try:
     
    con = psycopg2.connect(database='scrape', user='postgres', password='password')  
    
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)    
    cur.execute("SELECT * FROM newmovies limit 5")

    rows = cur.fetchall()

    #for row in rows:
    #    print "%s %s" % (row["id"], row["title"])
  
    row1 = rows[1] 
    moviename0 = row1["title"]
    moviename = moviename0.replace(" ", "%20")
    print "%s" % moviename 

    cur.execute("SELECT * FROM dlmovies WHERE title = '%s'" % moviename0)
    check1=cur.fetchone()

    if check1 is not None:
        print "Already downloaded!"

    else:
        print "Good to go!"


except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

