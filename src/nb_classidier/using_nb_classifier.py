from nb_text_classifier import TextMood, load_data
import random as r
import csv

files = {'data/human.csv': 'human', 'data/dog.csv': 'dog'}
train_data = []
test_data = []
for f, species in files.items():
    with open(f, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        all_rows = list(reader) 
        r.shuffle(all_rows)
        train_data += [(" ".join(row['sequence']), species) for row in all_rows[:810]]
        test_data += [(" ".join(row['sequence']), species) for row in all_rows[810:820]]

print("total train data :",len(train_data))
print(f"Sample at index 0: {train_data[0][1]}")
print(f"Sample at index 809: {train_data[809][1]}")
print(f"Sample at index 810: {train_data[810][1]}")
print(f"Sample at index 819: {train_data[819][1]}")

print("total test data :",len(test_data))


print()


model = TextMood(ngram_range=(6, 8), stop_words = [])

model.train(train_data, ["human", "dog"])

print()
correct = 0
for i in range(len(test_data)):
    test_seq, actual_label = test_data[i]
    prediction = model.predict(test_seq)
    print(f"Pred: {prediction:10} | Actual: {actual_label}")
    if prediction == actual_label:
        correct += 1

print("correct percentage :", 100*(correct/len(test_data)))