# Practice for postgres and python 
# Mahdi Abbasi

import psycopg2
import psycopg2.extras


host_name = 'localhost'
database = 'test'
username = 'postgres'
pw2 = 'miai09362092181'
port_id = 5432

conn = None

#------------- CONNECT WITH POSTGRES DATABASE -------------#

try:
    conn = psycopg2.connect(
        host = host_name,
        database = database,
        user = username,
        password = pw2,
        port = port_id,)
    print('Connection Successfully🔥')
    
#------------- CREATE TABLE IN POSTGRES DATABASE -------------#
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DROP TABLE IF EXISTS table_python')
    create_script = '''
                CREATE TABLE IF NOT EXISTS table_python (
                    id int PRIMARY KEY,
                    name varchar(100) NOT NULL,
                    followers int,
                    post_num int
                )
    '''
    cur.execute(create_script)
    conn.commit()

#------------- INSERT DATA IN TABLE table_python -------------#
    insert_scripts = 'INSERT INTO table_python (id, name, followers, post_num) values(%s, %s, %s, %s)'
    insert_values = [(1,'Mahdi_Abbasi', 1710, 3), (2,'Jadi_Mirmirani', 9900, 898)]
    for insert_value in insert_values:
        cur.execute(insert_scripts, insert_value)
#------------- SELECT DATA FROM table_python TABLE -------------#
    cur.execute('select * from table_python')
    records = cur.fetchall()
    print('select data is : \n',)
    for record in records:
        print(record)
    print()
    conn.commit()
#------------- UPDATE DATE IN table_python TABLE -------------#
    update_scripts = 'UPDATE table_python SET followers = followers * 2.5'
    cur.execute(update_scripts)
    conn.commit
##### select data after update
    cur.execute('select * from table_python')
    records = cur.fetchall()
    print('select after update date in table : ',end= '\n',)
    for record in records:
        print(record)
    print()
    conn.commit()
#------------- DELETE SOME DATE FROM table_python TABLE -------------#
    delete_script = 'DELETE FROM table_python where name = %s'
    delete_id = ('Jadi_Mirmirani',)
    cur.execute(delete_script,delete_id)
#### select data after delete
    cur.execute('select * from table_python')
    records = cur.fetchall()
    print('select after delete date in table : ',end= '\n',)
    for record in records:
        print(record)
    print()


except Exception as error :
    print('Error Message: ', error)

finally:
    if conn is not None:
        conn.close()
        cur.close()