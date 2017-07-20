# -*- coding: utf-8 -*-


import os
import os.path
import random
import string
import oss2

rootdir = "/Users/xingmenglin/Desktop/Dogs/original_data/train"                                # 指明被遍历的文件夹



# 以下代码展示了文件上传的高级用法，如断点续传、分片上传等。
# 基本的文件上传如上传普通文件、追加文件，请参见object_basic.py


# 首先初始化AccessKeyId、AccessKeySecret、Endpoint等信息。
# 通过环境变量获取，或者把诸如“<你的AccessKeyId>”替换成真实的AccessKeyId等。
#
# 以杭州区域为例，Endpoint可以是：
#   http://oss-cn-hangzhou.aliyuncs.com
#   https://oss-cn-hangzhou.aliyuncs.com
# 分别以HTTP、HTTPS协议访问。
access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'Aqi9vgI5jYlpXJkG')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'hyh5r7S5uiz3TMaVltOF9gu8j8T0kQ')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'merlin666/dogs_train/data')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-cn-shanghai.aliyuncs.com')


# 确认上面的参数都填写正确了
for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param


# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)


#文件名
lst = os.listdir(rootdir)
for i in lst:
    path = os.path.join(rootdir,i)
    if os.path.isfile(path):
        bucket.put_object_from_file(i, path) ##上传图片


