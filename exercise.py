import os
import sys

def list(dir):
  filenames= os.listdir(dir)
  print filenames
    
def main():
  List(sys.argv[1])