# # Bagian atas
# for i in range(5):
#     for j in range(5):
#         if j == 2 or i == 2:
#             print("*", end=" ")
#         else:
#             print("-", end=" ")
#     print()

# print()

# # Bagian bawah
# for i in range(5):
#     for j in range(5):
#         # pinggir kotak
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print("*", end=" ")
#         # titik tengah
#         elif i == 2 and j == 2:
#             print("*", end=" ")
#         else:
#             print("-", end=" ")
#     print()


n = 5
for i in range(n):
    for j in range(n):
        if j == n // 2 or i == n // 2:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()
    
n = 5
for i in range(n):
    for j in range(n):
        # Batas kotak ATAU titik tengah
        if i == 0 or i == n-1 or j == 0 or j == n-1 or (i == n//2 and j == n//2):
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()