import argparse
import computor.core as core

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("equation", type=str, nargs='?', help="equation to resolve")
  args = parser.parse_args()
  
  if args.equation:
    core.resolve(args.equation.strip())
  else:
    equation = input()
    core.resolve(equation.strip())