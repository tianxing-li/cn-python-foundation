"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

num4tele = []
num4normal =[]
#get all the called numbers
for i in calls:
	if i[1] not in num4normal:
		num4normal.append(i[1])
#get all the txt numbers
for i in texts:
	if i[0] not in num4normal:
		num4normal.append(i[0])
	if i[1] not in num4normal:
		num4normal.append(i[1])
#get all the potential telemarketers
for i in calls:
	if i[0] not in num4normal and i[0] not in num4tele:
		num4tele.append(i[0])

print("These numbers could be telemarketers:")
for i in sorted(num4tele):
	print(i)
