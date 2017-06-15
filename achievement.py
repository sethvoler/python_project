#coding:utf8

record = [['名次', '姓名', '语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '总分', '平均分']]
inRecord1 = ['0', '平均']
score = []#记录学生的成绩

#读取 report.txt 文件中的成绩
with open('report.txt') as f:
    lines = f.readlines()

    #统计每名学生总成绩、计算平均并从高到低重新排名；
    for line in lines:
        every = line.replace('\r\n', '').split()
        sum = 0
        avg = 0
        for i in every[1:]:
            sum += float(i)
        avg = sum/9
        sum = ('%.1f' % sum)
        avg = ('%.1f' % avg)
        every.append(sum)
        every.append(avg)
        score.append(every)
    score.sort(key = lambda x:(x[-1]),reverse=True)

#汇总每一科目的平均分和总平均分
inRecord2 = []
scoreAll = 0 #记录总分
for j in range(1,10):
    scores = 0
    for i in range(0, 30):
        scores += float(score[i][j])

    scoreAvg = scores/30
    scoreAvg = ('%.1f' % scoreAvg)
    inRecord2.append(scoreAvg)

for i in inRecord2:
    scoreAll += float(i)
scoreAllAvg = scoreAll/9
inRecord2.append(str(scoreAll))
inRecord2.append(str(scoreAllAvg))
inRecord1 += inRecord2

#替换60分以下的成绩为“不及格”；
for i in range(0, 30):
    for j in range(1, 10):
        if (float(score[i][j]) < 60):
            score[i][j] = '不及格'

#添加名次
i = 0
for line in score:
    i += 1
    line.insert(0, str(i))

#将处理后的成绩另存为一个新文件
output = []
record.append(inRecord1)
record += score
for line in record:
    line[12] += '\n'
    output += line
outputF = []
for i in output:
    i = '{:^12}'.format(i)
    outputF.append(i)


with open('output.txt', 'w') as f:
    f.writelines(outputF)















































