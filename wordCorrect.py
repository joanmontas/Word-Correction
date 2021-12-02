file=open("diccleandata.txt",'rt')
list_of_word=file.read().splitlines()
file.close()
trie_head_node_list={'a': None, 'b': None, 'c': None, 'd': None, 'e': None,
                   'f': None, 'g': None, 'h': None, 'i': None, 'j': None,
                   'k': None, 'l': None, 'm': None, 'n': None, 'o': None,
                   'p': None, 'q': None, 'r': None, 's': None, 't': None,
                   'u': None, 'v': None, 'w': None, 'x': None, 'y': None,
                   'z': None}
#creates each node/letter of the trie with the attributes necessary for its manipulation
class trie_letter_aka_node:
    def __init__(self,letter=str(),word_syllable=None):
        self.letter=str(letter)
        self.is_it_a_word=bool(False)
        self.next_letter={'a': None, 'b': None, 'c': None, 'd': None, 'e': None,
                   'f': None, 'g': None, 'h': None, 'i': None, 'j': None,
                   'k': None, 'l': None, 'm': None, 'n': None, 'o': None,
                   'p': None, 'q': None, 'r': None, 's': None, 't': None,
                   'u': None, 'v': None, 'w': None, 'x': None, 'y': None,
                   'z': None} #we modify the next_letter to be a dictionary rather than list...
        self.end=bool(True)
        self.word_syllable=word_syllable
#dynamically add words/letter  into a trie ... using the class
### here we will dynamically words, by stringing letters toguether via their next_letter attribute
for i in list_of_word:
    #print(i[0])
    if trie_head_node_list[i[0]] == None:
        trie_head_node_list[i[0]] = trie_letter_aka_node(i[0])
    current = trie_head_node_list[i[0]]
    for k in range(1,len(i)):
        try:
            if current.next_letter[i[k]] == None:
                current.next_letter[i[k]] = trie_letter_aka_node(i[k],i)
            current=current.next_letter[i[k]]
        except Exception as e :
            print(e)
            continue
#### after this we will delete the letter inside each node's next that are not in use
stack=[]
for i in list(trie_head_node_list):
    if trie_head_node_list[i] == None:
        # print("no word starts with letter",i)
        trie_head_node_list.pop(i)  # delete unuse first letter
    else:
        stack.append(trie_head_node_list[i])
while True:
    for i in list(stack[0].next_letter):
        if stack[0].next_letter[i] == None:
            stack[0].next_letter.pop(i)
        else:
            stack.append(stack[0].next_letter[i])
    stack.pop(0)
    if len(stack) == 0:
        break
#now we have form the trie...we will make function to visualize it and manipulate it
pre_suggestion=[]
screen=[]
suggestion=[]
print(screen)
print(suggestion)
input_letter=input("Enter letter:")
if len(screen) == 0:
    screen.append(input_letter)
for i in (trie_head_node_list[input_letter].next_letter):
    suggestion.append(trie_head_node_list[input_letter].next_letter[i].letter)
    pre_suggestion.append((trie_head_node_list[input_letter].next_letter[i]))
print(suggestion,"suggested")
print(screen)
while True:
    input_letter = input("Enter letter:")
    if input_letter in suggestion:

        index_in_pre_of_inputed_letter = suggestion.index(input_letter)
        suggestion.clear()
        t = list(pre_suggestion)
        pre_suggestion.clear()
        try:
            for i in t[index_in_pre_of_inputed_letter].next_letter:
                suggestion.append( t[index_in_pre_of_inputed_letter].next_letter[i].letter)
                pre_suggestion.append(t[index_in_pre_of_inputed_letter].next_letter[i])
        except:
            continue
        screen.append(input_letter)
    print(suggestion,"suggested")
    print(screen)


###
###
###

trie_head_node_list={'a': None, 'b': None, 'c': None, 'd': None}

list_of_word=["ab","ac",'aca',"bb","bc"]
class trie_letter_aka_node:
    def __init__(self,letter=str(),word_syllable=None):
        self.letter=str(letter)
        self.is_it_a_word=bool(False)
        self.next_letter={'a': None, 'b': None, 'c': None, 'd': None}                    #we modify the next_letter to be a dictionary rather than list...
        self.end=bool(True)
        self.word_syllable=word_syllable
head=trie_letter_aka_node("")
for i in list_of_word:
    if head.next_letter[i[0]] == None:
        head.next_letter[i[0]] = trie_letter_aka_node(i[0])
    current = head.next_letter[i[0]]
    for k in range(1,len(i)):
        if current.next_letter[i[k]] == None:
            current.next_letter[i[k]] = trie_letter_aka_node(i[k],i[0:k+1])
        current = current.next_letter[i[k]]
#### after this we will delete the letter inside each node's next that are not in use
stack=[]
for i in (head.next_letter):
    stack.append(head.next_letter[i])
for i in list(head.next_letter):
    while True:
        if len(stack) == 0:
            break
        if stack[0] != None:
            for i in list(stack[0].next_letter):
                if stack[0].next_letter[i] == None:
                    stack[0].next_letter.pop(i)
                else:
                    stack.append(stack[0].next_letter[i])
        stack.pop(0)
        if len(stack) == 0:
            break
pre_suggestion=[]
screen=[]
suggestion=[]
print(screen)
print(suggestion)
current=head.next_letter
while True:
    input_letter=input("Enter letter:")
    if input_letter in current:
        screen.append(input_letter)
        current=(current[input_letter].next_letter)
    else:
        print("not a word")
    print(screen)
    print(suggestion)

