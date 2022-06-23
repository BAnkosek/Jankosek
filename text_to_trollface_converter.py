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
    ### if text is shorter than required (185 characters long) program will add in random text as filler
    text = list("Givedevbranch?Whatdoyoumeangivedevbranch?Doyouhaveanyideahowsignificantthedevsvisionisforthegame?Theirbugfixingwhichiscompletelyunknownisparamounttothisgamesfutureandthey’reworkinghardt")
    if len(text) < 185:
        text.append(('abcdefghijklmnopqrstuvxyz' * (1+ (185 - len(text)//24)))
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
    
    
    
