target = "success"

def target_function(**kwargs):
	if 'target' in kwargs and kwargs['target']:
		print(target)
	else:
		print(kwargs)

if __name__ == "__main__":
	print("fail lmao")
