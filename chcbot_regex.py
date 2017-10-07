#Example code for a regex based response generator

def chcbot(input_str):
    import re, string, csv
    input_str = input_str.lower()
    punctuation = string.punctuation.replace('@','')
    input_str = input_str.translate(None, punctuation)
    #set up primary and secondary keys for commands
    keyword_dict = {}
    import csv
    with open('input.txt', 'rb') as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
        for row in d:
            tab_row = re.split(r'\\t+', row[0])
            secondary_keys = tab_row[1]
            keyword_dict[tab_row[0]] = {secondary_keys:tab_row[2]}
    primary_keys = keyword_dict.keys()
    input_list = input_str.split()
    if bool(set(input_list) & set(primary_keys)) == False:
        return
    if re.search("@chainbot", input_str) != None:
        chainbot_chk = 1
    else:
        chainbot_chk = 0
    if chainbot_chk == 1:
        overlap_str_primary = list(set(input_list) & set(primary_keys))
        if len(overlap_str_primary) == 0:
            return("Sorry I didn't recognize any commands in your message")
        else:
            overlap_str_primary = list(overlap_str_primary)[0]
            if overlap_str_primary in primary_keys:
                return(keyword_dict[overlap_str_primary].values()[0])
    else:
        overlap_str_primary = set(input_list) & set(primary_keys)
        overlap_str_primary = list(overlap_str_primary)[0]
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
