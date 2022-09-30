# port - глобална променлива
port = 1521
# 1. дефиниция
def show():
    global port
    port = 3306
    print(f'port={port}')
    

if __name__ == '__main__':
    
    # 2. извикване
    print(f'before:{port}')
    show()
    print(f'after:{port}')
    
    print('---')