import time


def print_format(data: str) -> str:
    """输出一条内容"""
    try:
        print('\r >>> 调试内容 .... %s' % data, end="")
    except Exception as e:
        print('Error', e)


if __name__ == '__main__':
    # 模拟第一次, 加调试信息
    print_format('msg1')
    time.sleep(30)
    # 模拟第二次, 加调试信息
    print_format('msg2')
