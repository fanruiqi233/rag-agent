"""
为整个工程提供统一绝对路径
"""
import os

def get_project_root()->str:
    """
    获取工程的根目录
    :return: 字符串根目录
    """
    #当前文件的绝对路径
    currentFile = os.path.abspath(__file__)

    # 当前文件夹的绝对路径
    currentDir=os.path.dirname(currentFile)

    # 获取工程的根目录
    project_root=os.path.dirname(currentDir)

    return project_root

def get_abs_path(relative_path)->str:
    """
    传递相对路径，返回绝对路径
    :param relative_path: 相对路径
    :return: 绝对路径
    """
    project_path = get_project_root()
    return os.path.join(project_path, relative_path)

if __name__ == '__main__':
    print(get_abs_path("config/config.text"))