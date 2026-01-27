l = ["data\human.txt", "data\dog.txt", "data\chimpanzee.txt"]
for i in l:
    with open(i, "r") as f:
        data = f.readlines()
        with open(i[:-4:]+".csv", "a") as k:
            for j in data:
                k.write(",".join(j.split("\t")) + '\n')

# dont ask me why i didnt imported csv 
# dont ask anything about this script
# "write so garbage code that if u somehow get that job noone can replace you cause noone can understand what you wrote"  -not me
#  please hire me i am not like this, I AM JUST HAVING SOME FUN