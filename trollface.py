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


# ░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░██░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░





def main():
    
    trol_lista = list('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░██░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░')
    
    ilosc_linijek = int(15)
    ilosc_znakow = len(trol_lista)
    ilosc_znakow_na_linijke = int(ilosc_znakow / ilosc_linijek)
    
    
    ### your text goes into this VVV, make sure to watch out for ' and "
    tekst = list("Give devbranch? What do you mean give devbranch? Do you have any idea how significant the devs vision is for the game? Their  bug fixing which is completely unknown is paramount to this games future and they’re working hard to give this to us. And you just come here to say fucking what? 'Give devbranch?' 2 fucking ignorant words coming from your numbskull brain. You can't comprehend the pure intellect it requires to be a moderator let alone BE a DEV and run Siege Camp. And you disrespect those people that contribute much to this great cause, the crusade that will show us the real means of developing. Your dumbass shouldn't be in this world let alone a fucking devbranch.")
    tekst_bez_spacji = list()
    
    for z in range (len(tekst)):
        if tekst[z] == ' ':
            pass
        else:
            tekst_bez_spacji.append(tekst[z])
    
    
    i = 0
    
    trol_output = list()
    trol_output_napis = str()
    
    for x in trol_lista:
        if x == '░' or x == '▒':
            trol_output.append(' ')
        else:
            trol_output.append(tekst_bez_spacji[i])
            i += 1
        
        
        
    for w in range (ilosc_linijek):
        for n in range(ilosc_znakow_na_linijke):
            trol_output_napis += str(trol_output[n+(ilosc_znakow_na_linijke*w)])
        print(trol_output_napis)
        trol_output_napis = str()
            
main()
    
    
    