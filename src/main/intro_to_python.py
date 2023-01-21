import numpy as np

if __name__ == "__main__":
    m1 = np.array([[1, 0, 0],[0, 1, 0], [0, 0, 1]])

    #formatting to get rid of the brackets in the output
    print(str(m1).replace(' [', '').replace('[', '').replace(']', '') + '\n')

    m2 = np.array([[1, 3, 3],[3, 1, 3], [3, 3, 1]])

    #formatting to get rid of the brackets in the output
    print(str(m2).replace(' [', '').replace('[', '').replace(']', '') + '\n') 

    m3 = np.array([[1, 3],[3, 1], [3, 3]])

    #formatting to get rid of the brackets in the output
    print(str(m3).replace(' [', '').replace('[', '').replace(']', '') + '\n')
