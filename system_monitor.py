import psutil
import time
import logging
import signal
import sys

# 设置日志配置
logging.basicConfig(filename='system_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_cpu_usage():
    """
    获取CPU使用率。
    
    Returns:
    float: 当前CPU使用率百分比。
    """
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """
    获取内存使用率。
    
    Returns:
    dict: 包含总内存、已用内存、空闲内存和内存使用率的字典。
    """
    memory = psutil.virtual_memory()
    return {
        'total': memory.total,
        'used': memory.used,
        'free': memory.available,
        'percent': memory.percent
    }

def get_disk_usage():
    """
    获取磁盘使用率。
    
    Returns:
    dict: 包含总磁盘空间、已用磁盘空间、空闲磁盘空间和磁盘使用率的字典。
    """
    disk = psutil.disk_usage('/')
    return {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent
    }

def log_system_usage():
    """
    记录系统使用情况到日志文件。
    """
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    logging.info(f'CPU Usage: {cpu}%')
    logging.info(f'Memory Usage: {memory["percent"]}% (Total: {memory["total"]}, Used: {memory["used"]}, Free: {memory["free"]})')
    logging.info(f'Disk Usage: {disk["percent"]}% (Total: {disk["total"]}, Used: {disk["used"]}, Free: {disk["free"]})')

def signal_handler(sig, frame):
    """
    捕获终止信号并停止脚本。
    """
    print("监控脚本已停止")
    logging.info("监控脚本已停止")
    sys.exit(0)

def main():
    # 注册信号处理函数
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    while True:
        log_system_usage()
        time.sleep(60)  # 每隔60秒记录一次

if __name__ == "__main__":
    main()
