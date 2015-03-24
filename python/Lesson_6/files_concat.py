import argparse
import csv


encoding = ['UTF-8', 'Windows-1251']
# def merge_files(file_list, output_file):
#     fout = open(output_file,'a', encoding='UTF-8')
#     for f in file_list:
#         for line in open(f, encoding='UTF-8'):
#             fout.write(line)
#     fout.close()

def merge_files_csv(file_list, output_file, encod):
    for each_file in file_list:
        with open(each_file, 'r', encoding=encod) as csvfile:
            inp_file = csv.reader(csvfile)
            out_file = csv.writer(open(output_file, 'a', encoding=encod, newline=''))
            for row in inp_file:
                out_file.writerow(row)

def read_file():
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='Output file', type=str)
    parser.add_argument('-i', '--input', help='List of files', nargs='+', type=str)
    parser.add_argument('-r', '--read', help='Read file wo work', type=str)
    args = parser.parse_args()

    if args.output and args.input:
        for i in range(len(encoding)):
            try:
                merge_files_csv(args.input, args.output, encoding[i])
            except UnicodeDecodeError:
                continue
        #merge_files_csv(args.input, args.output)
    # output_file = args.output
    if args.output:
        print("the output file is " + args.output)
    if args.read:
        pass

if __name__ == '__main__':
    main()
#
# print(args.num)