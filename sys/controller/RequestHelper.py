import mysql.connector
from DatabaseAdapter import *
import sys
import json

class RequestHelper:

    dbAdapter = None
    def __init__(self,dbAdapter):
        self.dbAdapter = dbAdapter
    '''
    add a new request sent by user
    '''
    def addNewRequest(self,recipientId,senderId):

        query ="INSERT INTO request VALUES(CURRENT_TIMESTAMP,'%s','%s');"%(recipientId,senderId)

        cur = self.dbAdapter.getcursor()
        try:
          cur.execute(query)
        except mysql.connector.Error as err:

          print("****************************************")
          print("SQLException from addNewRequest():")
          print("Error code:", err.errno)
          print("SQLSTATE value:", err.sqlstate)
          print("Error message:", err.msg)
          print("Might be query issue:",query)
          print("****************************************")
          return False
        return cur.rowcount>0

    """
    Delete a request based on recipientId and senderId

    """
        
    def deleteRequest(self,recipientId,senderId):

        cur = self.dbAdapter.getcursor()
        query =("DELETE FROM request "
                "WHERE recipient_id = '%s' AND sender_id = '%s'")%(recipientId,senderId)
        try:
          cur.execute(query)
          
        except mysql.connector.Error as err:

          print("****************************************")
          print("SQLException from deleteRequest():")
          print("Error code:", err.errno)
          print("SQLSTATE value:", err.sqlstate)
          print("Error message:", err.msg)
          print("Might be query issue:",query)
          print("****************************************")
          return False
          
        return cur.rowcount>0

    '''
    get a list of message of a same recipient
    '''
    
    def getRequestListByAid(self,recipientId):

        cur = self.dbAdapter.getcursor()

        query =("SELECT sender_id,time,author.name,nick_name,servers.name "
               "FROM request,author,servers WHERE servers.sid = author.sid AND aid = sender_id and recipient_id = '%s'")%(recipientId)

        try:
            cur.execute(query)
          
        except mysql.connector.Error as err:

            print("****************************************")
            print("SQLException from getMessageListByAuthorName():")
            print("Error code:", err.errno)
            print("SQLSTATE value:", err.sqlstate)
            print("Error message:", err.msg)
            print("Might be query issue:",query)
            print("****************************************")
            return None

        return cur.fetchall()

    def getSentRequestByAid(self,aid):
        """
        To get list of authors, who is the author followed 
        """
        cur = self.dbAdapter.getcursor()
        query =("SELECT recipient_id,time,name "
               "FROM request,author WHERE aid = recipient_id and sender_id = '%s'")%(aid)
        try:
            cur.execute(query)
        except mysql.connector.Error as err:

            print("****************************************")
            print("SQLException from getMessageListByAuthorName():")
            print("Error code:", err.errno)
            print("SQLSTATE value:", err.sqlstate)
            print("Error message:", err.msg)
            print("Might be query issue:",query)
            print("****************************************")
            return None

        return cur.fetchall()
    '''
    To get the number of requests
    '''
    def getRequestCountByAid(self,recipientId):

        cur = self.dbAdapter.getcursor()

        query = ("SELECT count(*) FROM request "
                 "WHERE recipient_id = '%s'")%(recipientId)
        try:
            cur.execute(query)
            result = cur.fetchone()
        except mysql.connector.Error as err:

            print("****************************************")
            print("SQLException from getRequestCountByAid():")
            print("Error code:", err.errno)
            print("SQLSTATE value:", err.sqlstate)
            print("Error message:", err.msg)
            print("Might be query issue:",query)
            print("****************************************")
            return None

        return result[0]

    ''' 
    delete all message by author id
    '''
    def deleteAllRequestByAid(self,recipient_id):
        
        cur = self.dbAdapter.getcursor()
        query = "DELETE FROM request WHERE recipient_id ='%s'"%(recipient_id)

        try:
          cur.execute(query)

        except mysql.connector.Error as err:

          print("****************************************")
          print("SQLException from deleteAllRequestByAid():")
          print("Error code:", err.errno)
          print("SQLSTATE value:", err.sqlstate)
          print("Error message:", err.msg)
          print("Might be query issue:",query)
          print("****************************************")
          return False

        return cur.rowcount>0

