# coding=utf-8

from django.http import JsonResponse


from project.settings import  QINIU_accessKey, QINIU_secretKey,QINIU_videoBucketName, \
      QINIU_imgBucketName, \
    QINIU_textBucketName, USER_TYPE
from qiniu import  Auth,BucketManager,put_data

import logging

util_logger =  logging.getLogger("util")


qiniuAuth = Auth(QINIU_accessKey,QINIU_secretKey)
bucketMgr = BucketManager(qiniuAuth)

token_expire_time =  3600
check_expire_time =  3500

import string,time

class Handler():
    RES_VIDEO = 'video'
    RES_IMG   = 'img'
    RES_TEXT  = 'text'

    def __init__(self):

        self.random_seeds = string.lowercase + string.digits
        self.lastGetTokenTimeTab = {self.RES_VIDEO:0, self.RES_IMG : 0, self.RES_TEXT : 0}
        self.tokenTab = {self.RES_VIDEO:None, self.RES_IMG : None, self.RES_TEXT : None}
        self.bucketTab = {
                             self.RES_VIDEO:QINIU_videoBucketName,
                             self.RES_IMG : QINIU_imgBucketName,
                             self.RES_TEXT : QINIU_textBucketName
        }





    def get_upload_token(self,resource_type,policy=None):

        curTime = time.time()
        if self.tokenTab[resource_type]:
            passedTime = curTime - self.lastGetTokenTimeTab[resource_type]
            # 没有过1小时，用缓存的token， 过了就重新生成token， 确保每次获取的token至少可以用24小时
            if passedTime < check_expire_time:
                util_logger.debug('passtime: %s, reuse saved token' % passedTime)
                return self.tokenTab[resource_type]


        #randomString = ''.join(random.choice(self.random_seeds) for i in range(6))
        self.tokenTab[resource_type] = qiniuAuth.upload_token(self.bucketTab[resource_type],
                                               key=None,
                                               expires=token_expire_time,
                                               policy=policy)
        # print self.tokenTab[resource_type]

        self.lastGetTokenTimeTab[resource_type] = curTime

        return self.tokenTab[resource_type]

    def get_key_by_url(self,resourceUrl):

        splitPos = resourceUrl.find('/',8) # jump to the end of leading http://
        if splitPos <0:
            err ='unknow resource url format :%s' % resourceUrl
            util_logger.error(err)
            return 417,err

        splitPos += 1 # jump to the part behind the /

        return 0, resourceUrl[splitPos:]

    def delete_qiniu_file(self,resourceUrl,file_type):

        util_logger.critical( 'request to delete qiniu %s file %s' % (file_type,resourceUrl))

        if file_type == 'video':
            bucketName = QINIU_videoBucketName
        elif file_type == 'text':
            bucketName = QINIU_textBucketName
        else:
            return 417,"upsupported file type:%s"%file_type

        ret, key_or_err = self.get_key_by_url(resourceUrl)
        if ret != 0:
            return ret, key_or_err

        ret,info =  bucketMgr.delete(bucketName,key_or_err)

        return ret,info





    def add_qiniu_text_file(self,fileContent,urlPath):
        util_logger.debug( 'request to add qiniu text file ')

        token = self.get_upload_token(self.RES_TEXT)

        ret, info = put_data(token,
                             key= urlPath,
                             data= fileContent,
                             mime_type="text/html")

        if  not ret or ('key'not in ret):
            return False, info.error
        else:
            return True, ret["key"]




    def modify_qiniu_text_file(self,url,fileContent):
        util_logger.debug( 'request to modify qiniu text file ')

        ret, key_or_err = self.get_key_by_url(url)
        if ret != 0:
            return ret, key_or_err

        key = key_or_err

        token = qiniuAuth.upload_token(QINIU_textBucketName,
                                               key=key,
                                               expires=token_expire_time,
                                               )

        ret, info = put_data(token,
                             key= key,
                             data= fileContent,
                             mime_type="text/html")


        if  not ret or ('key'not in ret):
            return False, info.error
        else:
            return True, ret["key"]




qiniuHandler = Handler()