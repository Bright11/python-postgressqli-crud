import psycopg2

dbname = "todo"
user = "postgres"
password = "chika"
host = "localhost"
port = "5589"

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    create_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id int PRIMARY KEY,
        task VARCHAR(255),
        ownner VARCHAR(255)
    )
    """
    cur.execute(create_table)
    
    # # insert data into database
    # insert_data="INSERT INTO tasks (id, task, ownner) VALUES (%s, %s, %s)"
    
    # add_value=(2,"Bincom task 2", "Chika E Nwazuo")
    # cur.execute(insert_data,add_value)
    conn.commit()
    # 
    print("Table 'tasks' created successfully.")

except psycopg2.Error as e:
    print("Error creating table:", e)

# finally:
#     if cur is not None:
#         cur.close()
#     if conn is not None:
#         conn.close()
