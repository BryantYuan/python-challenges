# # players = int(input())
# # parcels = input()
# # dictinary = {}
# # for i in range(players):
# #   dictinary[i] = 0
# #
# # index = 0
# # while len(parcels) > 0:
# #   if parcels[0] == '1':
# #     dictinary[index] += 1
# #   parcels = parcels[1:]
# #   index += 1
# #   if index == players:
# #       index = 0
# #
# # print(max(dictinary.values()))
# # word = input().split(' ')
# # for i in range(len(word)):
# #     char = word[i]
# #     p = ""
# #     for c in char:
# #         if c not in p:
# #             p += c
# #     char = char[0].upper() + char[1:]
# #     for c in char:
# #         if c in ['a', 'e', 'i', 'o', 'u']:
# #             char = char.replace(c, '')
# #     word[i] = char
# #
# # print("".join(word))
#
# n = int(input())
# asteriks = ''
# while n != 0:
#   if n % 2 == 0:
#     n //= 2
#   else:
#     n -= 1
#     asteriks += '*'
# print(asteriks)

# # sentence = input()
# # sentence = sentence.lower()
# # word = input()
# # word = word.lower()
# # print(sentence.count(word))
#
# numbers = input().split(' ')
# n1 = numbers[0]
# n2 = numbers[1]
# if n1 == 1 and n2 == 1:
#   print(0)
# else:
#   print(1)