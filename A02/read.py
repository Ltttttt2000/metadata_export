import os

p = '/GPFS/xzd_lab_permanent/liutong/A02data/Rats/'
r = 'R907'
dir1 = p + r

flie_dir = os.listdir(dir1)

import csv
import NexFileReaders


to = dir1 + '.csv'
with open(to, "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["rat", "time", "duration", "frequency", "number_of_neuros"])


    for time in flie_dir:
        if os.path.isdir(dir1 + '/' + time):
            files = os.listdir(dir1 + '/' + time)
            frequency = 0
            duration = 0
            neuros = 0
            for file in files:
                if file.endswith('.nex5'):
                    readerNex5 = NexFileReaders.Nex5FileReader()
                    fileData = readerNex5.ReadNex5File(dir1 + '/' + time + '/' + file)
                    print(dir1+'/'+time+'/'+file)
                    frequency = fileData.TimestampFrequency
                    duration = fileData.MaxTimestamp()
                    neuros = len(fileData.Neurons)

                    # frequency = 1
                    # duration = 1
                    # neuros = 1

            writer.writerow([r, time, duration, frequency, neuros])

