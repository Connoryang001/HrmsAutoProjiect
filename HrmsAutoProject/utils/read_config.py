
import yaml
import os

def read_test_data(filename):
    '''
    读取yml中的测试数据
    :param filename: 路径文件
    :return: 返回读取的测试数据
    '''

    # 读取路径文件中的yml内容
    with open(filename, encoding='gbk') as f:

        #解析yml文件的内容
        data = yaml.load(f, Loader=yaml.FullLoader)

        #关闭文件
        f.close()

    # 返回数据
    return data

if __name__ == '__main__':
    file = os.getcwd()
    print(file)
    file = file.replace('\\', '/') # 将\替换成/
    file = file.split('/lib')[0]   # 根据/lib进行分割，返回list = ['/pythonProject/HrmsAutoProject', '']，取下标为0的内容
    filename = file + '/data/login_data.yml'
    print(filename)
    data = read_test_data(filename)
    print(data)