#
# MIT License
# 
# Copyright (c) 2023-2024 Manuel Bottini
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

#!/usr/bin/python3

import csv
import json
import os


POSSIBLE_BUCKETS = [
    "0 FOOD",
    "1 MAKESPACE",
    "2 DANCING",
    "3 DRINKS",
    "4 TRAVEL",
    "5 MUM PENSION",
    "6 INVESTMENTS",
    "7 RENT",
    "8 DELIVERY FOOD",
    "9 UNKNOWN",
    "10 GOING OUT",
    "11 VIRGIN",
    "12 CLOTHES",
    "13 SALARY",
    "14 PATREON",
    "15 MEDICINES",
    "16 GYM"]

def ask_for_memo_field(fields):
    return input("Write which field is the Memo?\n"+str(fields)+"\n")

def ask_for_amount_field(fields):
    return input("Write which field is the Amount?\n"+str(fields)+"\n")

def ask_for_bucket(buckets, memo):
    print("This type of memo couldn't be found = ")
    print(memo)
    print("What bucket should it belong to?")
    print(POSSIBLE_BUCKETS)
    bucket_index = int(input("Input the index of the bucket you want to use: "))
    yesno = ""
    while yesno != "y" and yesno != "n":
        yesno = input("You choose "+ POSSIBLE_BUCKETS[bucket_index] + " are you sure? (y/n) ")
    text_to_search = input("What text should be associated to this memo? ")

    buckets[text_to_search] = POSSIBLE_BUCKETS[bucket_index]

    with open("buckets.json", "w") as outfile:
        buckets_text = json.dumps(buckets, indent=4)
        outfile.write(buckets_text)

    return [buckets, text_to_search] 

def show_bucket(bucket, bucket_tot):
    name = bucket["name"]
    print(name+": Num Movements = "+str(bucket["num_movements"])+
            "  ("+str(float(bucket["num_movements"])/float(bucket_tot["num_movements"])*100) +"%)")
    print(name+": Money In = "+str(bucket["money_in"])+
            "  ("+str(float(bucket["money_in"])/float(bucket_tot["money_in"])*100) +"%)")
    print(name+": Money Out = "+str(bucket["money_out"])+
            "  ("+str(float(bucket["money_out"])/float(bucket_tot["money_out"])*100) +"%)")
    print(name+": Money Diff = "+str(bucket["money_in"] - bucket["money_out"]))
    print("-------------------------")

def main():
    print("Reading the buckets.json file")
    buckets = {}
    if not os.path.isfile("buckets.json"):
        with open("buckets.json", "w") as outfile:
            outfile.write("{}")
    else:
        with open('buckets.json', 'r') as openfile:
            buckets = json.load(openfile)

    buckets_values = {}

    print("Reading the data.csv file")
    with open("data.csv","r") as data_csv:
        csv_reader = list(csv.DictReader(data_csv))
        memo_field = ask_for_memo_field(csv_reader[0].keys())
        amount_field = ask_for_amount_field(csv_reader[0].keys())
        tot_num_movements = 0
        tot_money_in = 0
        tot_money_out = 0
        #header = next(csv_reader)
        for row in csv_reader:
            #print(row)
            memo = row[memo_field]
            if(row[memo_field] != None ):
                print(row)
                found = False
                bucket = None
                for text_to_search in buckets.keys():
                    if text_to_search in memo:
                        found = True
                        bucket = buckets[text_to_search]
                        break
                if not found:
                    [buckets, text_to_search] = ask_for_bucket(buckets, memo)
                    bucket = buckets[text_to_search]
                if bucket not in buckets_values:
                    buckets_values[bucket] = {
                        "name" : bucket,
                        "num_movements" : 0,
                        "money_in" : 0,
                        "money_out" : 0
                    }

                tot_num_movements = tot_num_movements + 1
                buckets_values[bucket]["num_movements"] = buckets_values[bucket]["num_movements"] + 1
                amount = float(row[amount_field])
                if amount > 0:
                    tot_money_in = tot_money_in + amount
                    buckets_values[bucket]["money_in"] = buckets_values[bucket]["money_in"] + amount
                else:
                    tot_money_out = tot_money_out - amount
                    buckets_values[bucket]["money_out"] = buckets_values[bucket]["money_out"] - amount

        bucket_values_tot = {
            "name" : "TOT",
            "num_movements" : tot_num_movements,
            "money_in" : tot_money_in,
            "money_out" : tot_money_out
        }
        show_bucket(bucket_values_tot, bucket_values_tot)
        for bucket in buckets_values.keys():
            show_bucket(buckets_values[bucket], bucket_values_tot  )
        #print("Header is = "+str(header))


if __name__ == "__main__":
    main()

