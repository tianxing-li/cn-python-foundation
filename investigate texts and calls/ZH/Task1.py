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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

count_tele = []
for i in texts:
	if i[0] not in count_tele:
		count_tele.append(i[0])
	if i[1] not in count_tele:
		count_tele.append(i[1])

for i in calls:
	if i[0] not in count_tele:
		count_tele.append(i[0])
	if i[1] not in count_tele:
		count_tele.append(i[1])

print('There are {} different telephone numbers in the records.'.format(len(count_tele)))