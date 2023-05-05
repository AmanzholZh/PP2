import psycopg2 as ps
from configparser import ConfigParser

# Function to configure database
<<<<<<< HEAD
<<<<<<< HEAD
def config(filename='database.ini', section='postgresql'):
=======
def config(filename='credentials.ini', section='postgresql'):
>>>>>>> 7ea8f7e... Final commit
=======
def config(filename='credentials.ini', section='postgresql'):
>>>>>>> 1f284975c03986ee3845dd5c4a50f0eb6ec17a30
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

# Function to connect to the server
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = ps.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# Function to insert the data into the table
def InsertData(name, score= 0, level= 1, table= 'snake'):
    
    comand = f"""INSERT INTO {table} (name, score, level)
                VALUES ('{name}', '{score}', {level}); """
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(comand)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        
        # Print success
        print(f"Successfully inserted {name} user with {score} score and {level} level into the {table} table")
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Function to Change the data
def ChangeData(name, score, level, table= 'snake'):
    
    # Commands
    change_score = f"""UPDATE {table} 
                SET score = {score}, level = {level} WHERE name = '{name}'"""
                
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the CHANGE statement
        cur.execute(change_score)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        
        # Print success
        print(f"Successfully changed {name} score to {score} and level to {level}")
        
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
# Function to show the contents of a table            
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def view(name, show= '*', table= 'snake'):
=======
def view(name, show, table= 'snake'):
>>>>>>> 7ea8f7e... Final commit
=======
def view(name, show= '*', table= 'snake'):
>>>>>>> 4474a2e... commit
=======
def view(name, show= '*', table= 'snake'):
>>>>>>> 1f284975c03986ee3845dd5c4a50f0eb6ec17a30
    
    comand = f""" SELECT {show} FROM {table} WHERE name = '{name}'"""
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = ps.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute(comand)
        
        # return  the contents
        return cur.fetchall()
            
    except:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return 0
        
    finally:
        if conn is not None:
            conn.close()
            
if __name__ == '__main__':
    print(view('beka'))
    print(view('tegfv'))
=======
        return []
=======
        return 0
>>>>>>> 4474a2e... commit
=======
        return 0
>>>>>>> 1f284975c03986ee3845dd5c4a50f0eb6ec17a30
        
    finally:
        if conn is not None:
            conn.close()
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ea8f7e... Final commit
=======
            
if __name__ == '__main__':
    print(view('beka'))
    print(view('tegfv'))
>>>>>>> 4474a2e... commit
=======
            
if __name__ == '__main__':
    print(view('beka'))
    print(view('tegfv'))
>>>>>>> 1f284975c03986ee3845dd5c4a50f0eb6ec17a30
