# greedy_monsters = int(input())
# price = []
# bill = 0
# for i in range(greedy_monsters):
#     cost = float(input())
#     price.append(cost)
#     bill += cost
#
# bill *= 1.05
# indvidual = str(bill / (greedy_monsters - 1))
# print(indvidual[:indvidual.index('.') + 3])

# squares = [input().split(' '),
#            input().split(' '),
#            input().split(' '), ]
#
#
# def check(magic_squares):
#     correct = None
#     for i in range(3):
#         cur_total = 0
#         for num in magic_squares[i]:
#             cur_total += int(num)
#         if correct is None:
#             correct = cur_total
#         elif cur_total == correct:
#             continue
#         else:
#             return 'muggle'
#
#     for i in range(3):
#         col1 = int(magic_squares[0][i])
#         col2 = int(magic_squares[1][i])
#         col3 = int(magic_squares[2][i])
#         cur_total = col1 + col2 + col3
#         if cur_total == correct:
#             continue
#         else:
#             return 'muggle'
#
#     diagonal1 = int(magic_squares[0][0])
#     diagonal2 = int(magic_squares[1][1])
#     diagonal3 = int(magic_squares[2][2])
#     cur_total = diagonal1 + diagonal2 + diagonal3
#     if cur_total == correct:
#         pass
#     else:
#         return 'muggle'
#
#     diagonal1 = int(magic_squares[0][2])
#     diagonal2 = int(magic_squares[1][1])
#     diagonal3 = int(magic_squares[2][0])
#     cur_total = diagonal1 + diagonal2 + diagonal3
#     if cur_total == correct:
#         pass
#     else:
#         return 'muggle'
#
#     return 'magic'
#
#
# print(check(squares))

# start = int(input())
# length = 1
# next_num = start * 3 + 1
#
# if next_num > 100:
#     next_num = int(str(next_num)[-2:])
#
# while next_num != start:
#     length += 1
#     next_num = next_num * 3 + 1
#     if next_num > 100:
#         next_num = int(str(next_num)[-2:])
#
# length += 1
# print(length)

# num1 = int(input())
# num2 = int(input())
# prev = num1
# length = 2
#
# while num2 != int(str(prev)[::-1]) and length <= 25:
#     new_num2 = num1 + num2
#     num1 = num2
#     prev = num2
#     num2 = new_num2
#     # length += 1
#
# if num2 == int(str(prev)[::-1]):
#     print(int(str(prev)[::-1]))
# else:
#     print(-1)


global hi
print(hi)
