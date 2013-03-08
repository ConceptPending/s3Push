import os
import boto
from boto.s3.key import Key

def s3Push(path, s3Bucket):
	conn = boto.connect_s3()
	nonexistent = conn.lookup(s3Bucket)
	if nonexistent is None:
		bucket = conn.create_bucket(s3Bucket)
	else:
		bucket = conn.get_bucket(s3Bucket)
	bucketKey = Key(bucket)
	for root, subdir, file in os.walk(path):
		relDir = root.replace(path, "", 1)
		for name in file:
			fileName = relDir + "/" + name
			bucketKey.key = fileName
			bucketKey.set_contents_from_filename(path + "/" + fileName)
