#!/usr/bin/python3
import os, argparse

cmd = '''python3 -c "from %s import *; %s"'''

def parse_args():
	p = argparse.ArgumentParser()
	p.add_argument(
		"-f","--file",
		help=("File to run"),
		required=True)
	p.add_argument(
		"-c","--code",
		help=("Code to run"),
		required=True)
	p.add_argument(
		"-i","--interactive",
		help=("Drop into an interactive python shell after"),
		action="store_true")
	return p.parse_args()
def main(args):
	c = cmd % (args.file.split(".")[0].replace("/","."), args.code)
	if args.interactive:
		t = c.split("-c")
		a = t[0] + "-i -c " + t[1]
		c = a
	os.system(c)
if __name__ == "__main__":
	main(parse_args())