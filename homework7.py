#Egor Eliseev
#Program that analyzes the job listings for gender biasness
#11/19/2016
def byFreq(pair):
    return pair[1]
def wordFreq(text, n): #Creating a function that will output n most frequent words
    counts = {}
    for w in text:
        counts[w] = counts.get(w,0) + 1
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))
#Reading the job listing from a file, file name entered by a user
fname = input("Enter the name of a file to analyze: ")
text = open(fname,'r').read()
#Cleaning the text from special characters
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
    text = text.replace(ch, ' ')
#Splitting the text into the list
text = text.lower().split()
#Creating a list with the stop words
stopWords = ['a', 'an', 'and', 'as', 'at', 'be', 'but', 'etc', 'for', 'in', 'it', 'its', 'is', 'of', 'or', 'so', 'such', 'the', 'this', 'to', 'with']
#Cleaning the text from a stop words
for ch in text:
    match = set(text) & set(stopWords)
    for x in match:
        text.remove(x)
#Printing most frequent words
print('--------------Most frequent words--------------')
#If listing is more than 25 words than program prints top25 frequent words
if len(text) >= 25:
    wordFreq(text, 25)
else: #If listing is less than 25 than prints all the words with their frequency
    wordFreq(text, len(text))
#Creatin lists for gender biased words
male_bias = ['ninja', 'rockstar', 'nerf', 'proven', 'pressure', 'competitive', 'leader', 'best', 'ambitious', 'analytical', 'assertive', 'strong', 'risk']
female_bias = ['learn', 'creative', 'validated', 'thoughtful', 'collaborate', 'curious', 'imaginative', 'intuitive', 'resilient', 'responsible', 'adaptable', 'flexible', 'competent']
#Counting how many gender biased words are there in the text
m_count = []
f_count = []
bias = 0 #Creating a variable for Bias score
for ch in text :
    for m,f in zip(male_bias,female_bias):
        if ch == m:
            bias += 1
            m_count.append(m)
        elif ch == f:
            bias -= 1
            f_count.append(f)
#Printing the frequency of gender biased words
print ('--------------How many gender biased words--------------')
print ('---Male biased:')
wordFreq(m_count, len(m_count))
print ('---Female biased:')
wordFreq(f_count, len(f_count))
#Printing the verdict based on the value of Bias score
print ('--------------Verdict--------------')
if bias > 0:
    print ('Job listing is male biased')
elif bias < 0:
    print ('Job listing is femake biased')
else:
    print ('Job listing is neutral')
