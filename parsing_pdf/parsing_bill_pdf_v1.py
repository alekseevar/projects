from tika import parser


def find_info(data, start_word, finish_word):
    data = data.split()
    index_of_start = data.index(start_word)
    index_of_finish = data[index_of_start:].index(finish_word) + index_of_start
    return data[index_of_start: index_of_finish]


text = parser.from_file('Sample-Bill-8.01.2019-Sparky-Joule.pdf')
#print(text['content'])

data = text['content']

#with open('data.txt', 'w') as fw:
#    fw.write(data)

print("FIND ACCOUNT No:", *find_info(data, "No:", "Statement"))
print("FIND PHONE NUMBER:", find_info(data, "Phone:", "Ways")[1])
print("FIND COMPANY:", *find_info(data, "For:", "Your")[2:4])
print("FIND AMOUNT DUE ON PREVIOUS STATEMENT:", find_info(data, "Previous", "Payment(s)")[-1])
print("FIND TOTAL AMOUNT DUE:", *find_info(data, "Total", "Questions")[3:6])
print("FIND total electric charges:", find_info(data, "PCIA", "Rules")[-1])
print("FIND total silicon Valley Clean Energy Electric Generation Changes:", find_info(data, "SVCE", "Service")[-1])
print("FIND TOTAL GAS CHARGES:", find_info(data, "PPP", "Service")[-1])



data = data.split("Details")[1:]
for each in data:
    print("-" * 10, *find_info(each, "of", "Charges")[1:], "-" * 10)
    date = find_info(each, "Charges", "days)")
    print(f"Date from: {date[1]}, date to: {date[3]}")
    print("ID:", find_info(each, "ID:", "Rate")[1])
    print("Total Usage", find_info(each, "Usage", "Baseline")[1])
