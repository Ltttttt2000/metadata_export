import csv
import os

import mne

directory_path = '/GPFS/xzd_lab_permanent/liutong/Rnd_data/data/HE05/'
print(directory_path)

to = '/GPFS/xzd_lab_permanent/liutong/HE05/HE05.csv'
with open(to, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["session", "time", "duration", "frequency", "channel_count"])
    for item in os.listdir(directory_path):
        print(item)
        item_path = directory_path + item
        for d in os.listdir(item_path):
            if d.endswith('.ns6'):
                nsx_path = item_path + '/' + d
                ns = mne.io.read_raw_nsx(nsx_path)
                session = item
                time = ns.info['meas_date']
                duration = ns.n_times / ns.info['sfreq']
                frequency = ns.info['sfreq']
                channel_count = ns.info['nchan']
                writer.writerow([session, time, duration, frequency, channel_count])
