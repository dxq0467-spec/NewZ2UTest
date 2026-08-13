# utils/logger.py
import logging
import os

from Utils.data_reader import read_yaml


class Logger:
    """日志管理类"""
    
    _logger = None
    
    @classmethod
    def get_logger(cls):
        """获取日志实例（单例模式）"""
        if cls._logger is None:
            cls._logger = cls._setup_logger()
        return cls._logger
    
    @classmethod
    def _setup_logger(cls):
        """设置日志"""
        # 创建日志目录
        config=read_yaml('Config/config.yaml')
        log_dir = os.path.dirname(config['LOG_FILE'])
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        logger = logging.getLogger('TestLogger')
        logger.setLevel(getattr(logging, config['LOG_LEVEL']))
        
        # 避免重复添加handler
        if logger.handlers:
            return logger
        
        # 文件handler
        file_handler = logging.FileHandler(
            config['LOG_FILE'],
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        
        # 控制台handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # 格式化
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    @classmethod
    def info(cls, message):
        """记录info日志"""
        cls.get_logger().info(message)
    
    @classmethod
    def warning(cls, message):
        """记录warning日志"""
        cls.get_logger().warning(message)
    
    @classmethod
    def error(cls, message):
        """记录error日志"""
        cls.get_logger().error(message)
    
    @classmethod
    def debug(cls, message):
        """记录debug日志"""
        cls.get_logger().debug(message)