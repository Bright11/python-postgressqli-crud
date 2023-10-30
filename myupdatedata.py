import psycopg2
import connect  # Presuming this file contains the connection details

try:
    update_script = 'UPDATE tasks SET task = %s, ownner = %s WHERE id = %s'
    task_update = ("Bincom update", "Bright", 1)
    
    connect.cur.execute(update_script, task_update)
    connect.conn.commit()
    print("Updated")

except psycopg2.Error as e:
    print("Error:", e)

finally:
    if connect.cur is not None:
        connect.cur.close()
    if connect.conn is not None:
        connect.conn.close()
