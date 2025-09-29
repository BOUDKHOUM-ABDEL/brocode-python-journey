

#indexing = accessing elements of a sequence
#using [] ([start:end:step])])

credit_card="1234-5678-9876-5432"
print(credit_card[0]) #1
print(credit_card[0:4]) #1234
print(credit_card[5:9]) #5678
print(credit_card[0:16:5]) #1-8-4
print(credit_card[-1]) #2 (last character)
print(credit_card[-4:]) #5432 (last 4 characters)
print(credit_card[::-1]) #2345-6789-8765-4321 (reversed)
print(credit_card.replace("-","")) #1234567898765432 (removes dashes)