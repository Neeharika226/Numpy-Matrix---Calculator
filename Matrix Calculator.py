import numpy as np

def get_matrix():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    print("Enter matrix elements row-wise:")
    matrix = [list(map(int, input().split())) for i in range(r)]
    return np.array(matrix)

def matrix_operations():
    print("\nMatrix Operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Determinant\n6. Inverse\n7. Exit")
    
    while True:
        choice = int(input("\nEnter your choice (1-7): "))

        if choice == 1 or choice == 2 or choice == 3:
            print("\nEnter first matrix:")
            A = get_matrix()
            print("\nEnter second matrix:")
            B = get_matrix()

            if choice == 1:
                print("\nMatrix Addition Result:\n", A + B)
            elif choice == 2:
                print("\nMatrix Subtraction Result:\n", A - B)
            elif choice == 3:
                print("\nMatrix Multiplication Result:\n", np.dot(A, B))

        elif choice == 4:
            print("\nEnter matrix:")
            A = get_matrix()
            print("\nTranspose of the matrix:\n", A.T)

        elif choice == 5:
            print("\nEnter square matrix:")
            A = get_matrix()
            if A.shape[0] == A.shape[1]:
                print("\nDeterminant:", np.linalg.det(A))
            else:
                print("\nDeterminant can only be found for square matrices.")

        elif choice == 6:
            print("\nEnter square matrix:")
            A = get_matrix()
            if A.shape[0] == A.shape[1]:
                try:
                    print("\nInverse of the matrix:\n", np.linalg.inv(A))
                except np.linalg.LinAlgError:
                    print("\nMatrix is singular, inverse does not exist.")
            else:
                print("\nInverse can only be found for square matrices.")

        elif choice == 7:
            print("\nExiting...")
            break

        else:
            print("\nInvalid choice, try again!")

matrix_operations()
