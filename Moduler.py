# -*- coding: utf-8 -*-
import subprocess
import sys

if __name__ == '__main__':
    
    while True:
        try:
            exec(f'import {sys.argv[2]} as md')
            exec('md.moduled()')
            break
        except ModuleNotFoundError as e:
            module = str(e).split("'")[1]
            subprocess.run(f'{sys.argv[1]} install {module}',shell=True)