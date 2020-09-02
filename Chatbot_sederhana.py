import re
from nltk.corpus import wordnet

# Membangun daftar kata kunci
list_words=['hello','timings','nothing']
list_syn={}
for word in list_words:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            
            #menghapus karakter spesial dari sinonim
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]',' ', lem.name())
            synonyms.append(lem_name)
            
    list_syn[word]=set(synonyms)
    
# print(list_syn)

# membangun dictionary of intents dan keyword
keywords={}
keywords_dict={}

# mendefinisikan kunci baru dalam keyword dictionary
keywords['greet']=[]

# mengisi nilai dalam keywords dictionary dengan sinonim kata kunci yang diformat dengan metakarakter Regex
for synonym in list(list_syn['hello']):
    keywords['greet'].append('.*\\b'+synonym+'\\b.*')

# mendefinisikan kunci baru dalam keyword dictionary
keywords['timings']=[]

# mengisi nilai dalam keywords dictionary dengan sinonim kata kunci yang diformat dengan metakarakter Regex
for synonym in list(list_syn['timings']):
    keywords['timings'].append('.*\\b'+synonym+'\\b.*')

# mendefinisikan kunci baru dalam keyword dictionary
keywords['nothing']=[]

# mengisi nilai dalam keywords dictionary dengan sinonim kata kunci yang diformat dengan metakarakter Regex
for synonym in list(list_syn['nothing']):
    keywords['nothing'].append('.*\\b'+synonym+'\\b.*')
    
for intent, keys in keywords.items():
    
    # menggabungkan nilai dalam keywords dictionary dengan operator OR(|) memperbaruinya dalam kamus keywords_dict
    keywords_dict[intent]=re.compile('|'.join(keys))
# print(keywords_dict)

# membangun kamus tanggapan
responses={
    'greet':'Hello! How can I help you?',
    'timings':'We are open from 9AM to 5PM, Monday to Friday. We are closed on weekends and public holidays.',
    'nothing':'What i should to be help?',
    'fallback':'I don\'t quite understand. Could you repeat that?'
}

exit_list = ['exit', 'See you later', 'bye', 'quit', 'break']

print("Bot\t: Welcome to MEBank. How may I help you?")

# while untuk mengulang percakapan tanpa batas waktu
while(True):
    
    # mengambil input pengguna dan mengubah semua karakter menjadi huruf kecil
    user_input = input('User\t: ').lower()
    
    # mendefinisikan ketika chatbot berhenti
    if user_input in exit_list:
        print("Bot\t: Thank you for visiting.")
        break
        
    matched_intent = None
    
    for intent, pattern in keywords_dict.items():
        
        # menggunakan fungsi pencarian pada regex untuk melihat kata kunci yang pengguna berikan
        if re.search(pattern, user_input):
            
            # jika kata kunci cocok, pilih intent yang sesuai dari keywords_dictionary
            matched_intent=intent
            
        # mengatur fallback intent pada default
    key='fallback'
    if matched_intent in responses:
            
        #jika kata kunci cocok, fallback intent akan diubah ke match intent yang sesuai dengan tanggapan yang dimasukan pengguna
        key = matched_intent
            
    # chatbot mencetak tanggapan yang berdasar dari masukan pengguna
    print("Bot\t: "+responses[key])