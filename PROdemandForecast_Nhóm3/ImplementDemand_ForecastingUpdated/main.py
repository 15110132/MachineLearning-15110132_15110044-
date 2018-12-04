from __future__ import print_function
import test_moving_average as tma


listproduct = ['Akitchen.csv', 'Clothes.csv', 'Fishsauce.csv', 'Instantnoodles.csv', 'learningtools.csv', 
                'Salt.csv', 'shampoo.csv', 'Sugar.csv', 'Toothpaste.csv', 'washingpowder.csv', 'beans.csv','beer.csv', 
                'breads.csv', 'cake.csv', 'cheese.csv', 'coffee.csv', 'cream.csv', 'eggs.csv', 'fabric.csv', 'juice.csv',
                 'makeup.csv', 'mask.csv', 'milk.csv', 'petfood.csv', 'sauce.csv', 'shavingCream.csv',
                 'snack.csv', 'soda.csv', 'tea.csv', 'wine.csv'  ]

# test weighted moving average
for i in range(0, len(listproduct)):

    print(listproduct[i].split('.')[0])
    print('Test weighted moving average for', listproduct[i].split('.')[0])

    input_file_name = listproduct[i]
    print('Input file: {}'.format(input_file_name))
    data_frame = tma.load_data(input_file_name)
    tma.execute_wma(data_frame, input_file_name, 2)

