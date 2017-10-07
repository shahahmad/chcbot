#Example code for a regex based response generator

def chcbot(input_str):
    import re, string, csv
    input_str = input_str.lower()
    #remove all punctuation from input string besides @
    punctuation = string.punctuation.replace('@','')
    input_str = input_str.translate(None, punctuation)
    #set up primary and secondary keys for commands
    keyword_dict = {}
    import csv
    #open the input file and store the data in a dictionary
    with open('input.txt', 'rb') as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
        for row in d:
            tab_row = re.split(r'\\t+', row[0])
            secondary_keys = tab_row[1]
            keyword_dict[tab_row[0]] = {secondary_keys:tab_row[2]}
    #split input words into a list using a space as a delimiter
    primary_keys = keyword_dict.keys()
    input_list = input_str.split()
    #if input stirng doesn't containg primary keys then return nothing
    if bool(set(input_list) & set(primary_keys)) == False:
        return
    #check if @chainbot in input string
    if re.search("@chainbot", input_str) != None:
        chainbot_chk = 1
    else:
        chainbot_chk = 0
    #if @chainbot is in input string, then generate reponse based on primary keys
    if chainbot_chk == 1:
        overlap_str_primary = list(set(input_list) & set(primary_keys))
        if len(overlap_str_primary) == 0:
            return("Sorry I didn't recognize any commands in your message")
        else:
            overlap_str_primary = list(overlap_str_primary)[0]
            if overlap_str_primary in primary_keys:
                return(keyword_dict[overlap_str_primary].values()[0])
    #if @chainbot not in input string then check primary keys for overlap
    else:
        overlap_str_primary = set(input_list) & set(primary_keys)
        overlap_str_primary = list(overlap_str_primary)[0]
        #if any primary key is in input string check if its associated secondary
        #keys are as well
        if overlap_str_primary in primary_keys:
            secondary_keys = keyword_dict[overlap_str_primary].keys()[0].split(',')
            if len(secondary_keys) == 0:
                return(keyword_dict[overlap_str_primary].values()[0])
            else:
                if bool(set(input_list) & set(secondary_keys)) == False:
                    return
                else:
                    overlap_str_secondary = list(set(input_list) & set(secondary_keys))
                    if len(overlap_str_secondary) >= 1:
                        return_str = keyword_dict[overlap_str_primary].values()[0]
                        return(return_str)
