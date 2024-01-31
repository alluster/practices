#!/usr/bin/env python3


def square(y: int):          				
	return y ** 2
def triple(x: int):
	return x * 3
def main():
	for i in range(1, 11):
		t = triple(i)
		s = square(i)

		if t < s: 
			break
		else:
			print(f"triple({i})=={t} square({i})=={s}")	


if __name__ == "__main__":
    main()
