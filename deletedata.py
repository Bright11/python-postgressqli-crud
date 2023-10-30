import psycopg2
import connect


try:
    deletedata="DELETE FROM tasks WHERE id=%s"
    deleteid=('1')
    connect.cur.execute(deletedata,deleteid)
    print("deleted")
    connect.conn.commit()

except Exception as e:
    print("error",e)
    

finally:
    if connect.cur is not None:
        connect.cur.close()
    if connect.conn is not None:
        connect.conn.close()