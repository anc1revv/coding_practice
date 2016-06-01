import csv
from random import randint

def create_delta4_table():
    user_dict = {}
    for i in range(10000):
        if(randint(1,4) == 4):
            user_dict[i+1] = [randint(5000,7000),randint(0,50),randint(0,1000),randint(6001,8000)]

    create_csv(user_dict,'delta4.csv')

def create_delta3_table():
    user_dict = {}
    for i in range(10000):
        if(randint(1,4) == 3):
            user_dict[i+1] = [randint(4000,5000),randint(0,50),randint(0,1000),randint(4501,6000)]

    create_csv(user_dict,'delta3.csv')

def create_delta2_table():
    user_dict = {}
    for i in range(10000):
        if(randint(1,4) == 2):
            user_dict[i+1] = [randint(3000,4000),randint(0,50),randint(0,1000),randint(3001,4500)]

    create_csv(user_dict,'delta2.csv')

def create_delta1_table():
    user_dict = {}
    for i in range(10000):
        if(randint(1,4) == 1):
            user_dict[i+1] = [randint(2000,3000),randint(0,50),randint(0,1000),randint(2001,3000)]

    create_csv(user_dict,'delta1.csv')

def create_delta0_table():
    user_dict = {}
    for i in range(10000):
        user_dict[i+1] = [randint(0,2000),randint(0,50),randint(0,1000),randint(0,2000)]

    create_csv(user_dict,'base_table.csv')

def dedupe_table(*file_names):
    files = locals().values()
    deduped_table = {}

    for f in file_names:
        pick_latest_batch(deduped_table,f)

    create_csv(deduped_table,'deduped_table.csv') 

def pick_latest_batch(dedupe_dict, new_file):
    with open(new_file, mode='r') as infile:
        infile.readline() #skip header row
        reader = csv.reader(infile)
        for rows in reader:
            if dedupe_dict.has_key(rows[0]):
                # if the batch_id is greater in the new file, overwrite for that user's row
                if int(rows[4]) > int(dedupe_dict.get(rows[0])[3]):
                    dedupe_dict[rows[0]] = rows[1:]
            else:
                dedupe_dict[rows[0]] = rows[1:]

    return dedupe_dict

def file_to_dict(file_name):
    mydict = {}
    with open(file_name, mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1:] for rows in reader}
    return mydict


def create_csv(user_dict, file_name):
    with open(file_name,'wb') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['user_id','total_spend','count_saved_items','loyalty_credits','batch_id'])
        for k,v in user_dict.items():
            csv_writer.writerow([k] + v)

def users_spent_over_twothousand(file_name):
    usercount = 0
    with open(file_name, mode='r') as infile:
        infile.readline() #skip header row
        reader = csv.reader(infile)    
        for rows in reader:
            if int(rows[1]) > 2000:
                usercount += 1

    return usercount

def main():
    #print users_spent_over_twothousand('customer_correct_table.csv')
    #print users_spent_over_twothousand('AIQ_Broken_table.csv')

    #AIQ_Broken_table
    dedupe_table('delta0.csv','delta1.csv','delta2.csv','delta4.csv')
    '''create_base_table()
    create_delta1_table()
    create_delta2_table()
    create_delta3_table()
    create_delta4_table()'''

if __name__ == "__main__": main()