import json
from PostPermissionHelper import *
class PostPermissionController:
    def __init__(self,dbAdapter):
        self.postPermissionHelper = PostPermissionHelper(dbAdapter)

    def addPostPermission(self,pid,aidList):
    '''add post permission to post'''
        return self.postPermissionHelper.addPostPermission(pid,aidList)
