import argparse
import csv



# def merge_files(file_list, output_file):
#     fout = open(output_file,'a', encoding='UTF-8')
#     for f in file_list:
#         for line in open(f, encoding='UTF-8'):
#             fout.write(line)
#     fout.close()

def merge_files_csv(file_list, output_file):
    for each_file in file_list:
        with open(each_file, 'r', encoding='UTF-8') as csvfile:
            inp_file = csv.reader(csvfile)
            out_file = csv.writer(open(output_file, 'a', encoding='UTF-8', newline=''))
            for row in inp_file:
                out_file.writerow(row)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='Output file', type=str)
    parser.add_argument('-i', '--input', help='List of files', nargs='+', type=str)
    args = parser.parse_args()

    if args.output and args.input:
        merge_files_csv(args.input, args.output)
    # output_file = args.output
    if args.output:
        print("the output file is " + args.output)

if __name__ == '__main__':
    main()
#
# print(args.num)