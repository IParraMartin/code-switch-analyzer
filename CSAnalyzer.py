import pandas as pd
import matplotlib.pyplot as plt
import es
import en

#Input data ======= ADD FILE OPTION? =========
cs_input = input('Insert code switch here: ')
tokens = cs_input.split()

#set dictionaries ======= ADD BIGGER BANK =========
sp_dic = es.words
en_dic = en.words 
print(en_dic)

def code_lookup(text):

    #Algorithm core
    sp_token_count = 0
    en_token_count = 0
    for token in text:
        if token in sp_dic:
            sp_token_count += 1
            print(f'{token}: sp')
        elif token in en_dic:
            en_token_count += 1
            print(f'{token}: en')
        else:
            print('[0]')

    print('–––––––')

    #Percentage section
    sp_perc = sp_token_count*100 / len(text)
    en_perc = 100 - sp_perc
    print(f'sp: {sp_perc}')
    print(f'en: {en_perc}')
    data = [sp_perc, en_perc]

    print('–––––––')

    #DataFrame section
    df = pd.DataFrame(data, columns=['lang %'])
    df.index = ['sp', 'en']
    print(df)

    #Plotting section 
    langs = ['SP', 'EN']
    perc = data
    plt.bar(langs, perc)
    plt.title('SP-EN switching (%)', fontweight='bold')
    plt.ylabel('Language usage %')
    plt.xlabel('Languages')
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.show()

    #======= ANY OTHER PARAMETERS TO ADD TO THE DATAFRAME? =========   
    input('Do you want to save the data in a .csv file?: ')
    if input == 'yes' or 'Yes':
        df.to_csv('cs-data.csv')
    else:
        quit

code_lookup(tokens)
