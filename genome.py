inp = open('18s_humano.fasta').read() # Read entire DNA .fasta file
out = open('18s_humano.html', 'w') # Read html file created by Diego Mariano in this Udemy course ('Python & MySQL)

counter = {} # Create empty dictionarie to count nucleotides

# possible ways to group nucleotides
# AA
# AT
# AC
# AG
# then repeat for each letter

for i in ['A', 'T', 'C', 'G']: # As known above, each letter must group with another, So when i is 'A':
    for j in ['A', 'T', 'C', 'G']: # Do i ('A') + each element in ('A', 'T', 'C', 'G'), this will create a key for each group in counter
        counter[i+j] = 0

inp = inp.replace('\n', '') # In fasta file after each line is inserted a break, so replace it with nothing

for k in range(len(inp)-1): # From 0 to fasta size look for groups as element one + element in front of with, must use -1 to check last but one + last element, since after last element theres nothing
    counter[inp[k]+inp[k+1]] += 1


i = 1
for nucleotide in counter:
    opacity = counter[nucleotide]/max(counter.values()) # Nucleotide that most occuried will have 100% opacity, the ones left will have their occurrencies/max ocurrencies
    out.write("<div style='width: 100px; border: 1px solid #111; font-size: 1.5em; font-weight: bold; text-align: center; height: 100px; float:left; color:white; background-color: rgba(155, 0, 255," + str(opacity) + ")'>"+ nucleotide +"</div>")

    if i%4 == 0: # Break line every 4 divs
        out.write("<div style='clear:both'></div>")
    i+=1
out.close()