#!/usr/bin/env python
#coding=utf-8
__author__ = 'vzer'
import paramiko,datetime,os
hostname='192.168.1.230'
username='root'
password='root@xiniu'
port=22
def upload(local_dir,remote_dir):
    try:
        t=paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        print 'upload file start %s ' % datetime.datetime.now()
        for root,dirs,files in os.walk(local_dir):
            for filespath in files:
                local_file = os.path.join(root,filespath)
                a = local_file.replace(local_dir,'')
                remote_file = os.path.join(remote_dir,a)
                try:
                    sftp.put(local_file,remote_file)
                except Exception,e:
                    print os.path.split(remote_file)[0]
                    mkPath="mkdir -p %s"%os.path.split(remote_file)[0]
                    sshNew=paramiko.SSHClient()
                    sshNew.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    sshNew.connect(hostname,port,username,password)
                    sshNew.exec_command(mkPath)
                    sshNew.close()
                    sftp.put(local_file,remote_file)
                print "upload %s to remote %s" % (local_file,remote_file)
            for name in dirs:
                print "in dirs:"
                local_path = os.path.join(root,name)
                a = local_path.replace(local_dir,'')
                remote_path = os.path.join(remote_dir,a)
                try:
                    mkPath="mkdir -p %s"%remote_path
                    sshNew=paramiko.SSHClient()
                    sshNew.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    sshNew.connect(hostname,port,username,password)
                    sshNew.exec_command(mkPath)
                    sshNew.close()
                    print "mkdir path %s" % remote_path
                except Exception,e:
                    print e
        print 'upload file success %s ' % datetime.datetime.now()

        t.close()
    except Exception,e:
        print e

if __name__=='__main__':
    local_dir='/root/test/'
    remote_dir='/root/aaa/'
    upload(local_dir,remote_dir)