#!/usr/bin/env python
# coding: utf-8
import subprocess
import unittest
import mysql.connector
import json
import sys,os
sys.path.append("sys/controller")
sys.path.append("sys/model")
# Adapter
from DatabaseAdapter import *
# helpers
from AuthorHelper import *
from CircleHelper import *
from PostHelper import *
from RequestHelper import *
# Controllers 
from AuthorController import *
from RequestController import *
from CommentController import *
from CircleController import *
from PostController import *
from PostPermissionController import *
from ServiceController import *
# models
import author
import post
import time
import Utility
DEBUG = True

'''PLEASE rebuild the database everytime before run all the tests'''
class TestController(unittest.TestCase):
    
    def setUp(self):


        self.cid = None
        self.aid = None
        # DO NOT CHANGE HERE
        dbAdapter = DatabaseAdapter()
        dbAdapter.connect()
        dbAdapter.setAutoCommit()
        # helpers
        self.authorHelper = AuthorHelper(dbAdapter)
        self.circleHelper = CircleHelper(dbAdapter)
        self.postHelper = PostHelper(dbAdapter)
        self.requestHelper = RequestHelper(dbAdapter)
        # controllers
        self.commentController = CommentController(dbAdapter)
        self.postController = PostController(dbAdapter)
        self.requestController = RequestController(dbAdapter)
        self.circleController = CircleController(dbAdapter)
        self.authorController = AuthorController(dbAdapter)
        self.postPermissionController = PostPermissionController(dbAdapter)
        self.serviceController = ServiceController(dbAdapter)
    '''
     ====================   PostController & Helper =======================
    '''
    def test_getLocalPublicPosts(self):
        result = self.postController.getLocalPublicPosts()
        self.assertTrue(result != None,"Failed to get local public posts")
    '''
     ===================== ServiceController =============================
    '''
    def test_sendPublicPostsToRemoteServer(self):
        result = self.serviceController.sendPublicPostsToRemoteServer()
        self.assertTrue(result != None,"Failed to send public posts to remote server")

    '''
     ====================   AuthorController & Helper  ====================
     PLEASE rebuild the database before run all the tests
    '''
    def test_addAuthor(self):
        result = self.authorController.addAuthor('test','','')
        self.assertTrue(result != None,"Failed to add author")


    def test_addRemoteAuthor(self):
        result = self.authorController.addRemoteAuthor('remote_test_aid','','cs410.cs.ualberta.ca:41068')
        self.assertTrue(result != None,"Failed to add an remote author")

    def test_getAllAuthorObjectsForRemoteServer(self):
        result = self.authorHelper.getAllAuthorObjectsForRemoteServer()
        self.assertTrue(result != None,"Failed to get all author objects for remote server")

    def test_isRemoteAuthor(self):
        result = self.authorController.isRemoteAuthor('100000')
        self.assertTrue(result == True,"Failed to check isRemoteAuthor")

        result = self.authorController.isRemoteAuthor('333333')
        self.assertTrue(result == False,"Failed to check isRemoteAuthor")
    
    def test_getGlobalAuthors(self):

        result = self.authorController.getGlobalAuthors()
        self.assertTrue(result != None,"Failed to get global authors")

    def test_doesAuthorExists(self):

        result = self.authorController.doesAuthorExists('111111')
        self.assertTrue(result == True,"Failed to check the existence of author")
        
    '''
     ====================   Request ControllerHelper  ====================
     PLEASE rebuild the database before run all the tests
    '''
    def test_sendRequest(self):
        # Tested By : Guanqi
        result = self.requestController.sendRequest('111111','222222')
        self.assertTrue(result == True,"Failed to sent a request")
    
    
    def test_accpetRequestFromSender(self):
        result = self.requestController.acceptRequestFromSender('111111','222222')
        self.assertTrue(result == True,"Failed to accept a request from sender")
    
   
    '''
    Cannot delete request by far
    def test_deleteRequest(self):
        result = self.requestController.deleteRequest('222222','111111')
        self.assertTrue(result == True,"Failed to delete a request")
    '''
    def test_getAllRequestByAid(self):
        result = self.requestController.getAllRequestByAid('111111')
        self.assertTrue(result != None,"Failed to get all request by aid")

    def test_getRequestCountByAid(self):
        result = self.requestController.getRequestCountByAid('111111')
        self.assertTrue(result != None,"Failed to get request count by aid")
        result = self.requestController.getRequestCountByAid('3123213213')
        self.assertTrue(result != None,"The count should be zero")

    def test_deleteAllRequestByAid(self):
        result = self.requestController.deleteAllRequestByAid('111111')
        self.assertTrue(result == True,"Failed to delete all request by aid")
        
    '''
     ====================   CommentController  ====================
     PLEASE rebuild the database before run all the tests!!!
    '''

    def test_getCommentsForPost(self):
    # Tested By : Guanqi
        result = self.commentController.getCommentsForPost('1')
        self.assertTrue(result != None,"Failed to get all comments for post")

    def test_addCommentForPost(self):
    # Tested By : Guanqi
        cid = self.commentController.addCommentForPost('111111','1','Hello')

        self.assertTrue(cid != None,"Failed to add comment for post")

    def test_deleteCommentForPost(self):

        result = self.commentController.deleteCommentForPost('1')
        self.assertTrue(result == True,"Failed to delete comment for post")

    def test_getCommentsForPublicPosts(self):
        result = self.commentController.getCommentsForPublicPosts()
        self.assertTrue(result != None,"Faild to get comments for public posts")

    '''
    ===================  CircleController ===========================
    '''

    def test_areFriends(self):
        result = self.circleController.areFriends('111111','333333')
        self.assertTrue(result == True,"Failed to determine the relationship between the two aids")

        result = self.circleController.areFriends('555555','111111')
        self.assertTrue(result == False,"Failed to determine the relationship between the two aids")

    def test_areFriendsOfAuthor(self):
        author = "111111"
        authorsList = ["222222","333333"]

        result = self.circleController.areFriendsOfAuthor(author,authorsList)
        self.assertTrue(result != None,"Failed to check areFriends of Author ")

    def test_addFriendForAuthor(self):
        result = self.circleController.addFriendForAuthor('111111','999999')
        self.assertTrue(result == True,"Failed to add friend for author")

    def test_deleteFriendOfAuthor(self):
        result = self.circleController.deleteFriendOfAuthor('111111','999999')
        self.assertTrue(result == True,"Failed to delete friend of author")
    
    '''
    =================== PostPermission Controller ====================
    '''

    def test_addPostPermission(self):
        pid = '7'
        aidsList = ['444444','111111','333333']
        result = self.postPermissionController.addPostPermission(pid,aidsList)
        self.assertTrue(result == True,"Failed to add post permission")

        aidsList = []
        result = self.postPermissionController.addPostPermission(pid,aidsList)
        self.assertTrue(result == False,"Failed to add post permission")

if __name__ == '__main__':
    print("**************************** Script Starts ****************************")
    subprocess.call(["./install.sh", "-rebuild_all"])
    print("**************************** Script Ends *********************************")
    print("**************************** Test Starts *********************************")
    unittest.main()
        