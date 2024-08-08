import os

p = 'D:/DATA/Rats/'
r = 'R701'
dir1 = p + r

flie_dir = os.listdir(dir1)


import csv
import NexFileReaders


# python2可以用file替代open
to = dir1 + '.csv'
with open(to, "w",encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    #先写入columns_name
    writer.writerow(["rat", "time", "duration", "frequency", "number_of_neuros"])


    # 开始读每只大鼠的info
    for time in flie_dir:

        if os.path.isdir(dir1 + '/' + time):
            files = os.listdir(dir1 + '/' + time)
            frequency = 0
            duration = 0
            neuros = 0
            for file in files:
                if file.endswith('.nex5'):
                    path = dir1 + '/' + time + '/' + file
                    readerNex5 = NexFileReaders.Nex5FileReader()
                    fileData = readerNex5.ReadNex5File(path)
                    print(dir1+'/'+time+'/'+file)
                    frequency = fileData.TimestampFrequency
                    duration = fileData.MaxTimestamp()
                    neuros = len(fileData.Neurons)

                    # 因为不能使用NexFileReaders
                    # frequency = 1
                    # duration = 1
                    # neuros = 1

            # 写入多行用writerows
            writer.writerow([r, time, duration, frequency, neuros])

