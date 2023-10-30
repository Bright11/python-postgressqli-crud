import psycopg2

import connect 


try:
    connect.cur.execute("SELECT * FROM tasks")
    
    #print(connect.cur.fetchall())
    for record in connect.cur.fetchall():
        print(record)

except Exception as e:
    print("error",e)
    
    
finally:
    if connect.cur is not None:
        connect.cur.close()
    if connect.conn is not None:
        connect.conn.close()
