#!/usr/bin/env python3


def main():
	i = 1
	for i in range (1, 11):
		print()
		for j in range (1, 11):
			print(("{:4d}".format(i * j,)), end=' ')
if __name__ == "__main__":
    main()
