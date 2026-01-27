l = ["data\human.txt", "data\dog.txt", "data\chimpanzee.txt"]
for i in l:
    with open(i, "r") as f:
        data = f.readlines()
        with open(i[:-4:]+".csv", "a") as k:
            for j in data:
                k.write(",".join(j.split("\t")) + '\n')
