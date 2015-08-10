import MySQLdb

class Node(object):

	def __init__(self,initialValues):
		self.valuesDict = initialValues

class Tree(object):

    def __init__(self):
        print "Initialising"
        self.attributes = {}
        self.tableName = ""
        self.db = MySQLdb.connect("localhost","root","","trial" )

    def getAttributes(self):
        for attributeName in self.attributes:
            print attributeName,
            print " : ",
            print self.attributes[attributeName]["dataType"]

    def addAttribute(self,newAttributeName,defaultValue,dataType,constraints):
    	newAttr = {}
    	newAttr["defaultValue"] = defaultValue
    	newAttr["dataType"] = dataType
    	newAttr["constraints"] = constraints
        self.attributes[newAttributeName] = newAttr
        setattr(self,newAttributeName,defaultValue)

    def createTable(self, newTableName, update = True):
        self.tableName = newTableName
        cursor = self.db.cursor()
        if not update:
        	if self.tableAlreadyExists():
        		return
        cursor.execute("DROP TABLE IF EXISTS " + self.tableName)
        columns = ""
        for attributeName,attributeDetails in self.attributes.iteritems():
            columns += attributeName + "  "
            columns += attributeDetails["dataType"]+ " "
            columns += " ".join(attributeDetails["constraints"])+","
        columns =  columns[:-1]
        sql = "CREATE TABLE " + self.tableName + " ("
        sql += columns
        sql += ")"
        print sql
        cursor.execute(sql)


    def tableAlreadyExists(self):
      	cursor = self.db.cursor()
        cursor.execute("SHOW TABLES LIKE '"+ self.tableName + "'")
    	result = cursor.fetchone()
    	if result:
    		return True
    	return False

    def addNode(self,valueDict):
        initialValues = {}
        for attributeName in valueDict:
            if(self.attributes.has_key(attributeName)):
                initialValues[attributeName] = valueDict[attributeName]
        
        insertQuery = "INSERT INTO "+self.tableName+ " ("
        insertQuery += ','.join(initialValues.keys())
        insertQuery += ") VALUES ("
        insertQuery += ",".join(["%s" for i in range(len(valueDict))])
        insertQuery += ")"
        print insertQuery

        cursor = self.db.cursor()
        print cursor.execute(insertQuery,valueDict.values())
        self.db.commit()
        


