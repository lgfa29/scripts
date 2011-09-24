import shutil
import exif
import sys
import os

def main():
	root_path = sys.argv[1]
	output_path = sys.argv[2]

	for root, dirs, files in os.walk(root_path):
		for file in files:
			if file.lower().endswith('.jpg'):
				original_file = os.path.join(root, file)
			
				try:
					data = exif.MinimalExifReader(original_file).dateTimeOriginal()
				
					day, time = data.split()
					new_filename = day.replace(':', '-') + '_' + time.replace(':', '_') + '.jpg'
					
					new_file = os.path.join(root, new_filename)
					
					i = 1
					while os.path.exists(new_file):
						i += 1
						new_file = new_file[:-4] + '-' + str(i) + '.jpg'
						
					os.rename(original_file, new_file)
				except:
					print ">> Couldn't process file", original_file

if __name__ == '__main__':
	main()