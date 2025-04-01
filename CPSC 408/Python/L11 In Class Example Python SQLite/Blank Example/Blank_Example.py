#import library
import sqlite3
print('import')

#add path to chinook.db to connect to it
connection = sqlite3.connect("chinook.db")
print('connection: ', connection)

#cursor object that executes SQL commands
cur_obj = connection.cursor()
print('init cursor: ', cur_obj)

#function definitions

#create tweet table
def createQuery():
    create_query = '''  
    CREATE TABLE tweet(
      tweetID INT NOT NULL PRIMARY KEY,
      Text VARCHAR(280),
      creationDate DATETIME,
      User VARCHAR(20),
      Likes INT,
      Retweets INT,
      Comments INT
    );
    '''
    #queues up query to run
    cur_obj.execute(create_query)
    #commit changes so that they persist
    #cursor execute, connection commit
    connection.commit()
    print('Tweet Table Successfully Created')

#insert a tweet
def insertQueryHardCode():
    insert_query = '''
    INSERT INTO tweet
    VALUES(1, 'This is a tweet', '2025-01-01', '@Vaysman', 1, 2, 3);
    '''
    cur_obj.execute(insert_query)
    connection.commit()
    print ('Inserted hard coded values successfully')

def insertQueryQmark():
    record  = (2, 'This is not a tweet', '2025-01-02', '@Alice')

    insert_query = '''
    INSERT INTO tweet(tweetID, Text, creationDate, User)
    VALUES(?,?,?,?);
    '''

    cur_obj.execute(insert_query, record)
    connection.commit()
    print ('Inserted Qmark values successfully')

def insertManyQuery():
    records = [
        (3, 'hello world', '2021-01-03', '@Eve'),
        (4, 'hello universe', '2021-01-04', '@Bob'),
        (5, 'this is patrick', '2021-01-05', '@pStar')
    ]

    insert_query = '''
    INSERT INTO tweet(tweetID, Text, creationDate, User)
    VALUES(?,?,?,?);
    '''

    cur_obj.executemany(insert_query, records)
    connection.commit()

def updateQuery():
    update_query = '''
    UPDATE tweet
    SET Likes = ?, Comments = ?, Retweets = ?
    WHERE tweetID = ?;
    '''

    new_data = [
        (4, 5, 10, 2),
        (10, 15, 20, 3),
        (500, 0, 1, 5)
    ]
    cur_obj.executemany(update_query, new_data)
    connection.commit()

def insertExecuteScriptQuery():
    insert_queries = '''
    INSERT INTO tweet(tweetID, Text, creationDate, User)
    VALUES (6,'squilliam fancyson sucks eggs', '2021-01-06','@squidwurd');
    INSERT INTO tweet(tweetID, Text, creationDate, User)
    VALUES (7,'squidward needs ibuprofen', '2021-01-06','@skwillz');
    '''

    cur_obj.executescript(insert_queries)
    connection.commit

def selectQuery():
    select_query = '''
    SELECT *
    FROM tweet;
    '''

    results = cur_obj.execute(select_query)
    
    #print(results.fetchall())
    print(results.fetchone())
    print(results.fetchone())
    print(results.fetchone())

def selectQueryNamedPlaceholder():
    name = '@Vaysman'
    id = 1

    select_query = '''
    SELECT *
    FROM tweet
    WHERE User = :username
    AND tweetID = :tID;
    '''

    result = cur_obj.execute(select_query, {'username': name, 'tID': id})
    
    for row in result:
        print(row)

def insertQueryInnocentTweet():
    text = 'Another Tweet'

    insert_query = '''
    INSERT INTO tweet(tweedID, Text)
    Values(20, '%s')
    '''% text

    cur_obj.executescript(insert_query)
    connection.commit()

#main method
#createQuery()
#insertQueryHardCode()
#insertQueryQmark()
#insertManyQuery()
#updateQuery()
#insertExecuteScriptQuery()
#selectQuery()
selectQueryNamedPlaceholder()

#always close connections when exiting
cur_obj.close()
connection.close()
print('connection closed')