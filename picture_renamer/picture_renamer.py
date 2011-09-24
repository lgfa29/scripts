import shutil
#import exif
import sys
import os



def main():
	root_path = sys.argv[1]
	output_path = sys.argv[2]

	for root, dirs, files in os.walk(root_path):
		current_path = os.path.join(output_path, os.path.split(root)[1])
		for dir in dirs:
			os.mkdir(os.path.join(current_path, dir))

if __name__ == '__main__':
	main()