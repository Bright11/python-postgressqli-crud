import psycopg2
import connect 
 
 
 
 
try:
      # insert data into database
    insert_data="INSERT INTO tasks (id, task, ownner) VALUES (%s, %s, %s)"
    
    add_value=(3,"Bincom task 3", "ChikaGod Nwazuo")
    connect.cur.execute(insert_data,add_value)
    
    connect.conn.commit()
    print("good")

except Exception as e:
    print(e)
    
    
finally:
    if connect.cur is not None:
        connect.cur.close()
    if connect.conn is not None:
        connect.conn.close()
