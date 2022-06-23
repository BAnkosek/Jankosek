## this code inserts two | characters before and after every character of whatever text you put into "copy" variable,
## this makes every character its own individual spoiler on discord, and makes it a pain to read any message
## there are however relatively simple workarounds to this ;p 

copy = list("")
i = 0
while True:
    print('||', copy[i], '||', sep = '', end='')
    i += 1
    if i >= len(copy):
        break
