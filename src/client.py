#!/usr/bin/env python3

import subprocess

def main():
    subprocess.run("echo \"Hello World\"", shell=True, check=True)

if __name__ == '__main__':
    main()
