#You enter the number of blocks
#computer output the number of layers you can do with them
#Every layer contains one block more than the layer above

blocks = int(input("Enter the number of blocks: "))

counter = 1
height = 1

while blocks > 0:
    
    blocks = blocks - counter
    print("*" * counter)
    
    if blocks > counter:
        
        height+=1
        counter+=1
        
    else:
        print("Blocks left " + str(blocks) )
        break
        

print("The height of the pyramid:", height)