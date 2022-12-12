out = []
# print(type(out))

# out.append({
#     'menines':"claudio",
#     'idade':[1,2,3,4],
# })

# out.append({
#     'menines':"Adriana",
#     'idade':[5,6,7,8],
# })

# for item in out:
#     print(item['menines'])

# q = {'cd_subgrupo': 24,}

# print(**q)

# terapias = [0,1]

# for terapia in terapias:
#     for index, item in enumerate(out):
#         print(index)
#         print(item)
#         print(item['menines'])
        

        # for indexB, itemB in enumerate(out[index][item['menines']]):
        #     print(indexB)
        #     print(itemB)

# for indexB, itemB in enumerate(out[index][item]):
#     print(indexB)
#     print(itemB)


# for i in range(1,10):
#     if i == 5:
#         print(i)
#         continue
#     if i > 7:
#         print(i)


# terapias = [0,1]

# out.append({'terapia':[],
# 'escalonar':[]})
# out.append({'terapia':[],
# 'escalonar':[]})

# for terapia in terapias:
#     for index, item in enumerate(out):
#         tipo = 'terapia'
#         flag = False
#         for indexB, itemB in enumerate(out[index][tipo]):
#             print(flag)
#             flag = True
#         if flag == False:
#             out[index][tipo].append({
#                 'medicamento':[]
#             })

#         print(out[index][tipo])

# print()

tipo_indicacao = "Terapia|Composta|TipoA"

tp_tipo_indicacao = tipo_indicacao.split('|')

print(tp_tipo_indicacao)