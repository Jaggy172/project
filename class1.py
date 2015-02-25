#!usr/bin/python
import MySQLdb


class DBHandler():
    '''Static database connection, this prevents excessive use of resources'''
    connection=None
    dbname='teve'
    dbuser='teve'
    dbpassword='9txVy3mz'

    def __init__(self):
        '''This initialises the database'''
        if DBHandler.connection == None:
            DBHandler.connection=MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)
       
    def cursor(self):
        return DBHandler.connection.cursor()

class Gene():
    '''A class to describe a specific gene'''
    Gene_symbol=''
    Gene_title=''
    Gene_ID=''
    probelist=[] #Each gene can have more than one probe_id
   
    def __init__(self,gene_ID):
        '''Initialisation method for Gene Class'''
        db=DBHandler()
        self.Gene_ID=Gene_ID
        cursor=db.cursor()
        sql='SELECT Gene_Title, Gene_Symbol from Genes where Genes=%s'
        cursor.execute(sql,(Gene_ID,))#Queries the database for result then populates Classfield.
        result=cursor.fetchone()
        self.Gene_Title =result[0]
        self.Gene_Symbol=result[1]

        probesql='SELECT Gene_ID from Probes where Gene_ID=%s'
        cursor.execute(probesql,(Gene_ID,))
        #'''fetches the probes'''
       
        for result in cursor.fetchall():
           self.probelist.append(result[0])

    def get_expression(self, Sample_ID):
        '''Retrieves gene expression values for any given experiment'''
        db=DBHandler()
        cursor=db.cursor()
        sql='SELECT Expression_value where ID_REF=%s AND Sample_ID=%s'
	cursor.execute(sql,(ID_REF, Sample_ID))
	#fetch value from cursor and return it.

print("Mission Complete!")

        
 


 
