from datetime import datetime
import pyperclip as pc
import csv
    

def donation_data_entry(f_loc):
    with open(f_loc) as file:
        data = file.readlines()
    with open(f_loc) as file1:
        dt = datetime.now()
        current_timestamp = dt.timestamp()
        old_timestamp_obj = old_timestamp(file1)
        delta_t = round(current_timestamp - old_timestamp_obj, 3)
    if old_timestamp_obj == 0:
            delta_t = 0
        #Date Update ↓
    data.insert(1,pc.paste().replace("\n", '')+  #Email
                ','+dt.strftime("%d-%m-%Y %I:%M:%S %p")+  #Time
                ','+'Successful'+                #Status
                ','+str(delta_t)+'s'                #TimeDifference
                ','+str(current_timestamp)+'\n') #CurrentTimeStamp
    with open(f_loc, 'w') as data_entry:
        data_entry.writelines(data)        
    print('Data Entry Successful')


def old_timestamp(f_obj):
    csvreader = csv.reader(f_obj)
    try:
        l1 = next(csvreader)
        l2 = next(csvreader)
    except:
        l2 = [0]
    return float(l2[-1])

def performance_check():
    pass

donation_data_entry('D://Data//Tech_Upgrade//Tech_Donation_Report.csv')
