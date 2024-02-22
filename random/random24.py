#write function that take a sentence and return the longest even-length word in the sentence. Or if it has no even-length words, return '00'

para = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis voluptas laborum perferendis iusto voluptate impedit tenetur modi numquam ex officiis esse eum, saepe autem harum, unde dicta totam vero commodi.'
def longest_even(text):
    longest='00'
    for word in text.split():
        if len(word)%2==0 and len(word)>=len(longest):
            longest=word
    return longest

print(longest_even(para))
print('---------------')
for i in para.split():
    print(longest_even(i))