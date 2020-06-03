import argparse
import csv
import sys

#A
#if downloaded zip folder named "week6" paste in bash: python 02_Exercise_EX1.py my_modules/exercise_two_A.csv
def print_file_content(file):
        with open(file) as file_o:
            reader = csv.reader(file_o)
            for row in reader:
                print(row)

#B
#if downloaded zip folder named "week6" paste in bash: python 02_Exercise_EX1.py -f lst.csv my_modules/Exercise_2_B.csv
#det vil kopierer alt fra filen my_modules/Exercise_2_B.csv til filen lst.csv
def write_list_to_file(output_file,lst):
        with open(output_file, 'w') as file_object:
            file_object.write("".join(lst))

#C
def read_csv(input_file):
    with open(input_file) as file_object:
        lines = file_object.readlines()
        return lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that reads from a file and can write to another file')
    parser.add_argument('path', help='Path to read files from')
    parser.add_argument('-f','--file', help='File to write to')
    args = parser.parse_args()
    print(parser.parse_args())

path_to_file = args.path

if args.file is None:
    print_file_content(path_to_file)
else:
    lines = read_csv(args.path)
    write_list_to_file(args.file,lines)
    print(lines)