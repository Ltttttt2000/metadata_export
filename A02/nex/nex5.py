import NexFileReaders
readerNex5 = NexFileReaders.Nex5FileReader()
path = 'D:/DATA/Rats/R701/20231106/20231106FOF2000R701_64CH_test.nex5'
fileData = readerNex5.ReadNex5File(path)

print(fileData.TimestampFrequency)
print('神经元的数量: ', len(fileData.Neurons))
print(fileData.Continuous)  # []
print('duration: ', fileData.MaxTimestamp())
print(len(fileData.Markers))