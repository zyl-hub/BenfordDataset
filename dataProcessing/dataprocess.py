import pandas as pd
import glob
import os

def get_file_path(file_path):
    return glob.glob(file_path+"\\*.csv")


def getfilename(filename):
    for root, dirs, files in os.walk(filename):
        array = dirs
        if array:
            return array
        return None


def statistics(file_name):
    first_of_over_two_list = [0] * 11
    first_of_over_three_list = [0] * 11
    second_of_over_three_list = [0] * 11
    df = pd.read_csv(file_name,header=0,names=["index","num"])
    data_col = len(df)
    for i in range(data_col):
        data_str = str(df.loc[i,"num"])
        if data_str.isdigit():
            if len(data_str) <= 1:
                continue
            if len(data_str) > 1:
                first_of_over_two_list[0]+= 1
                first_of_over_two_list[eval(data_str[0])+1] += 1
            if len(data_str) > 2:
                first_of_over_three_list[0] += 1
                second_of_over_three_list[0] += 1
                first_of_over_three_list[eval(data_str[0])+1] += 1
                second_of_over_three_list[eval(data_str[1])+1] += 1
        else:
            continue
    print(file_name)
    alldata_1 = "all_num:{num[0]}\t{num[1]}\t{num[2]}\t{num[3]}\t{num[4]}\t{num[5]}\t{num[6]}\t{num[7]}\t{num[8]}\t{num[9]}\t{num[10]}\t".format(num = first_of_over_two_list)
    alldata_2 = "all_num:{num[0]}\t{num[1]}\t{num[2]}\t{num[3]}\t{num[4]}\t{num[5]}\t{num[6]}\t{num[7]}\t{num[8]}\t{num[9]}\t{num[10]}\t".format(num = first_of_over_three_list)
    alldata_3 = "all_num:{num[0]}\t{num[1]}\t{num[2]}\t{num[3]}\t{num[4]}\t{num[5]}\t{num[6]}\t{num[7]}\t{num[8]}\t{num[9]}\t{num[10]}\t".format(num = second_of_over_three_list)
    info = {"first_of_over_two":alldata_1,"first_of_over_three":alldata_2,"second_of_over_three":alldata_3}
    return info


root_path = "\\课程\\概统\\assignment\\dataset\\dataset"

'''
if __name__ == "__main__":
    print(statistics(r"\课程\概统\assignment\dataset\dataset\dataset1\coin.csv"))
'''


if __name__ == "__main__":
    all_rootfile_list = getfilename(root_path)
    all_rootfile_list.sort()
    data_list = []
    print(all_rootfile_list)
    for root_file in all_rootfile_list:
        file_path = root_path + "\\" + root_file
        target_file = get_file_path(file_path)
        for file_name in target_file:
            info = statistics(file_name)
            with open(root_path+"\\info.txt","a") as info_file:
                info_file.write("*"*40+"\n")
                info_file.write("file name:\t")
                info_file.write(file_name+"\n")
                info_file.write("first_of_over_two:\n")
                info_file.write(info["first_of_over_two"])
                info_file.write("\nfirst_of_over_three:\n")
                info_file.write(info["first_of_over_three"])
                info_file.write("\nsecond_of_over_three:\n")
                info_file.write(info["second_of_over_three"])
                data_list.append(info)

    length = len(data_list)
    print(length)
    num_list = [[0]*11]*4
    for data in data_list:
        for i in range(len(num_list)):
            num_list[0][i] += data["first_of_over_two"][i]

