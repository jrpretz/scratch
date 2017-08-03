import numpy as np
import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute("drop table if exists xvy")
cur.execute("create table xvy (x float,y float)")

gx = np.random.normal(loc=0.0,scale=1.0,size=10000)
gy = np.random.normal(loc=0.0,scale=1.0,size=10000)

cur.execute("begin");
for i in range(0,10000):
  cur.execute("insert into xvy values (%s,%s)"%(gx[i],gy[i]))
conn.commit()
  
