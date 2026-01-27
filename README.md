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

### using_nb_classifier.py

(each line is writen after i edit the code and run it again and see if it fixes)

it uses the [nb_text_classifier](https://github.com/soradacroi/textmood-classifier) i made, long story short its pretty shit.

it's probably because it only has only a c g t (n removed (tried with n and its still shit)).

using a n-gram range = (7,7) works the best.

i tried to shuffle in the correct place this time to get better data... idk why was i shuffling it after i got the data for traning now
i did it when separating the data and making the dataset. well now its giving an correct percentage more then 50% mostly (not everytime still)

i tried to change the dataset of dogs to chimpanzee, and the results were like correct percentage is not more then 60%.
maybe because humans and chimpanzees share more dna then dogs with humans, maybe thats why its not getting better results with chimps (ik dogs was not that good but its still better then chimps).

anyways this [nb_text_classifier](https://github.com/soradacroi/textmood-classifier) is not that good and advance anyways.
