from tika import parser


def find_info(word, data, first_number, second_number):
    data = data.split()
    if word in data:
        return data[data.index(word) + first_number: data.index(word) + second_number + 1]


text = parser.from_file('Sample-Bill-8.01.2019-Sparky-Joule.pdf')
#print(text['content'])

data = text['content']

with open('data.txt', 'w') as fw:
    fw.write(data)

print("FIND ACCOUNT No:", *find_info("No:", data, 1, 1))
print("FIND PHONE NUMBER:", *find_info("Phone:", data, 1, 1))
print("FIND COMPANY:", *find_info("For:", data, 2, 3))
