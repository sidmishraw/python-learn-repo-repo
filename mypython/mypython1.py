import sys

def hello(name):
  name = name + "!!!!!"
  print("Hello", name)

def main():
  hello(sys.argv[1])

if __name__ == "__main__":
  main()
