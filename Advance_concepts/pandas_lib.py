import pandas
# marks=pandas.Series([10,20,30])

data={
    'sn':[1,2,3],
    'name':["Tarushi","Sakshi","Shivi"],
    'city':["Lko","Varanasi","Lko"],
    'course':['cse','cse','cse'],
    'marks':[99,95,54]
}


# print("csv created")

info=pandas.read_csv("code.csv")
for i in range(len(info['marks'])):
    info['marks'][i] +=2
print(info)
df=pandas.DataFrame(data)
df.to_csv("code.csv")
# print(df)
# print(df['city'][2])
# print(df['name'][2])

# def student(data):
#     for i in range(len(data['marks'])):
#         if data['marks'][i] >= 90:
#             print(data['name'][i])
# def area(data):
#     for i in range(len(data['city'])):
#         if data['city'][i]=='Lko':
#             print(data['name'][i])

# student(data)
# area(data)

