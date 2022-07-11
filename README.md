# ECG_Classification
Project on electrocardio signal classification as a part of the Science Training Program 2018 at the School of Mathematics, Sun Yat-sen University. Advised by Dr. Peixin Li.

**load_data.py:** Takes in original heartbeat data. Goes through random sampling. Returns 'samplist.npy' and 'atrslist.npy'.

**data_processing.py:** Takes in 'samplist.npy' and 'atrslist.npy'. Apply median filter. Segment heartbeat signals. Conduct statistical summary on the number of samples in each category, and discard categories with too few samples. Random sampling, and making sure all samples are of the same length

**wavelet.py:** Perform wavelet transform on preprocessed samples to further reduce noise
