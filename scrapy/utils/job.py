import os

# 获取工作目录，如不存在则自动创建
def job_dir(settings):
    path = settings['JOBDIR']

    if path and not os.path.exists(path):
        os.makedirs(path)
    return path
