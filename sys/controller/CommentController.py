from CommentHelper import *
import sys
sys.path.append("sys/model")
from comment import *

class CommentController:

    def __init__(self,dbAdapter):
        self.commentHelper = CommentHelper(dbAdapter)
    '''
    Get all comments for a specific author by aid
    '''
    def getCommentsForAuthor(self,aid):

        result = self.commentHelper.getCommentsForAuthor(aid)
        if result != None:
            commentsArray = []
            for item in result:
                comment = Comment(item[0],item[1],item[2],item[3],item[4].strftime("%Y-%m-%d %H:%M:%S"),item[5])
                commentsArray.append(comment.tojson())
            print(commentsArray)
            return json.dumps(commentsArray)
        return None
    '''
    Get all comments for a specific post by pid
    @param String Post ID
    @return String/None Returns a JSON formatted dictionary of comments if getting successfully, else None
    '''
    def getCommentsForPost(self,pid):
        
        result = self.commentHelper.getCommentsForPost(pid)
        if result != None:
            commentDict = {}
            for item in result:
                comment = Comment(item[0],item[1],item[2],item[3],item[4].strftime("%Y-%m-%d %H:%M:%S"),pid)
                commentDict[comment.getCid()] = comment.tojson()
            return json.dumps(commentDict)
        return None

    '''
    For Public API Only
    Get all the comments for public posts
    @return Array commentsArray [{'comment':{},'pid':''}],else None
    '''
    def getCommentsForPublicPosts(self):

        result = self.commentHelper.getCommentsForPublicPosts()

        if result != None:
            commentsArray = []
            for row in result:
                comment = {}
                author = {}
                author['id'] = row[1]
                author['host'] = row[5]
                author['displayname'] = row[2]

                comment['author'] = author
                comment['comment'] = row[3]
                comment['pubDate'] = row[4].strftime("%Y-%m-%d %H:%M:%S")
                comment['guid'] = row[0]
                comment['pid'] = row[6]
                commentsArray.append(comment)
            return commentsArray
        return None

    '''
    Add comment for a specific post 
    @param String Author ID
    @param String Post ID
    @param String Content
    @return String/Boolean Returns Aid if adding successfully, else False
    '''
    def addCommentForPost(self,aid,pid,content):

        return self.commentHelper.addCommentForPost(aid,pid,content)

    '''
    Delete comment for a specific post
    @param String Comment ID
    @return Boolean Returns True if deleted successfully, else False
    '''
    def deleteCommentForPost(self,cid):

        return self.commentHelper.deleteCommentForPost(cid)
    '''
    Count number of comments for a specific post
    @param String Post ID
    @return Integer Returns the rowcount 
    '''
    def countCommentsForPost(self,pid):

        return self.commentHelper.countCommentsForPost(pid)