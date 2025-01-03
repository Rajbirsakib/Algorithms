# 1. sort the activities as per finishing time
# 2. select the first activity
# 3. selection of new activity (new activity starting time >= previous selected activity finished time)
# 4. repeat step 3 until all activities are checked

activity=['a3','a1','a2','a7','a8','a4','a6','a5']
start=[1,1,0,3,4,4,5,2]
finish=[2,3,4,5,5,6,8,9]
start_update=[]
activity_update=[]
activity_selection=[]

li=[]

for i in range(len(finish)):
    li.append([finish[i],i])

# print(li)
li.sort()
# print(li)
sort_index=[]
finish_update=[]

for x in li:
    sort_index.append(x[1])
    finish_update.append(x[0])

for i in sort_index:
    start_update.append(start[i])
    activity_update.append(activity[i])

# print(sort_index)
# print(start_update)
# print(activity_update)
# print(finish_update)

activity_selection.append(activity_update[0])
k=1
for i  in range(1, len(activity_update)):
    if start_update[i]==finish_update[k]:
        activity_selection.append(activity_update[i])
        k=i

print("Final Selected Activity")
print(activity_selection)

