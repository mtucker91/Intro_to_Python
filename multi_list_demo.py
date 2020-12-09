# def set_to_one (my_2d_list):
#     for i in range(len(my_2d_list)):
#         for j in range(len(my_2d_list[i])):
#             my_2d_list[i][j] = 1   
        

def product_row_column(my_2d_list):
    for i in range(len(my_2d_list)):
        for j in range(len(my_2d_list[i])):
            my_2d_list[i][j] = i * j


def checkboard (row_num, col_num):
    a = [ ([0] * col_num) for row in range(row_num) ]
    spot = 0
    for i in range(row_num):
        for j in range(col_num):
            if spot == 0:
                a[i][j] = 1
                spot = 1
            else:
                a[i][j] = 0
                spot = 0
    print(" a =", a)



if __name__ == "__main__":
    # my_2d_list =  [[0,0,0],[0,0,0],[0,0,0]]  
    # print(my_2d_list)
    #set_to_one(my_2d_list)
    #product_row_column(my_2d_list)
    checkboard(3,3)
    print()
    # print(my_2d_list)

    # my_2d_list =  [['my','ass','fat'],['your','dick','small'],['what','the','fuck']]
    # for i in range(len(my_2d_list)):
    #     print('just i:', my_2d_list[i], 'loc:', i)
    #     for j in range(len(my_2d_list[i])):
    #         print(f'both i and j: {my_2d_list[i][j]} loc: {i} and {j} or [{i}][{j}]')
