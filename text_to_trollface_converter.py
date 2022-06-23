# ░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░
# ░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
# ░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
# ░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
# ░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
# █░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
# █░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
# ░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
# ░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
# ░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
# ░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
# ░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
# ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
# ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
# ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░

#this file takes any text inserted into it and rearanges it into the shape of a trollface





def main():
    
    trol_list = list('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░██░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░')
    
    number_of_lines = int(15)
    number_of_characters = len(trol_list)
    number_of_characters_per_line = int(number_of_characters / number_of_lines)
    
    
    ### your text goes into this VVV, make sure to watch out for "characters, cause they can finish the string. 
    text = list("Give devbranch? What do you mean give devbranch? Do you have any idea how significant the devs vision is for the game? Their  bug fixing which is completely unknown is paramount to this games future and they’re working hard to give this to us. And you just come here to say fucking what? 'Give devbranch?' 2 fucking ignorant words coming from your numbskull brain. You can't comprehend the pure intellect it requires to be a moderator let alone BE a DEV and run Siege Camp. And you disrespect those people that contribute much to this great cause, the crusade that will show us the real means of developing. Your dumbass shouldn't be in this world let alone a fucking devbranch.")
    text_without_spaces = list()
    
    for z in range (len(text)):
        if text[z] == ' ':
            pass
        else:
            text_without_spaces.append(text[z])
    
    
    i = 0
    
    trol_output = list()
    trol_output_string = str()
    
    for x in trol_list:
        if x == '░' or x == '▒':
            trol_output.append(' ')
        else:
            trol_output.append(text_without_spaces[i])
            i += 1
        
        
        
    for w in range (number_of_lines):
        for n in range(number_of_characters_per_line):
            trol_output_string += str(trol_output[n+(number_of_characters_per_line*w)])
        print(trol_output_string)
        trol_output_string = str()
            
main()
    
    
    
