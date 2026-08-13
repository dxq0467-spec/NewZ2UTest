import yaml


def read_yaml(file_path):
    """
    读取YAML文件
    :param file_path: 相对于项目根目录的路径，例如 'config/config.yaml'
    :return: 解析后的字典或列表
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
            return content
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return None
    except yaml.YAMLError as e:
        print(f"错误：解析YAML失败 - {e}")
        return None