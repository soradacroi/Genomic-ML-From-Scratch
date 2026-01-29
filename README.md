# Genomic-ML-From-Scratch

the DNA classes and their corresponding class labels:
| Receptor/Enzyme Type        | class labels |
|:----------------------------|:--:|
| G protein coupled receptors | 0 |
| Tyrosine kinase             | 1 |
| Tyrosine phosphatase        | 2 |
| Synthetase                  | 3 |
| Synthase                    | 4 |
| Ion channel                 | 5 |
| Transcription factor        | 6 |

---

(each line is writen after i edit the code)

---

### using_nb_classifier.py

it uses the [nb_text_classifier](https://github.com/soradacroi/textmood-classifier) i made, long story short its pretty shit.

it's probably because it only has only a c g t (n removed (tried with n and its still shit)).

using a n-gram range = (7,7) works the best.

i tried to shuffle in the correct place this time to get better data... idk why was i shuffling it after i got the data for traning now
i did it when separating the data and making the dataset. well now its giving an correct percentage more then 50% mostly (not everytime still)

i tried to change the dataset of dogs to chimpanzee, and the results were like correct percentage is not more then 60%.
maybe because humans and chimpanzees share more dna then dogs with humans, maybe thats why its not getting better results with chimps (ik dogs was not that good but its still better then chimps).

anyways this [nb_text_classifier](https://github.com/soradacroi/textmood-classifier) is not that good and advance anyways.

---

### counting.py

this one (counting.py), well when making the models (im saying the d_x_h and d_x_d models) its giving some stable models (meaning some stable values for each kmer (ig thats what its called kmer)) i havent tested yet, its 2:21 am i should sleep gn

well its shit... also i rememeber mid way that i was thinking of counting and compairing the sequences but now i did something diff

ok well i made the test data a litter bigger and well the acuraccy is more then 50+%... 

even if its just 51% its still better then 50 (my copium is running out)... well atleast its not going down then 50... it did but its rare
and well its not really counting its more like **"Euclidean Distance"** then counting. 

...

---

well im not a bio student (that dont make any sense ik)

maybe in future i will use **"Cosine Similarity"** or smt that actually works maybe??
