from __future__ import print_function
import test_moving_average as tma

# test weighted moving average
print('Test weighted moving average')
input_file_name = 'tshirt.csv'
print('Input file: {}'.format(input_file_name))
data_frame = tma.load_data(input_file_name)
tma.execute_wma(data_frame, input_file_name)
