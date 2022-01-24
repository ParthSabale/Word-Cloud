def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    file_d=""
    for index char in enumerate(file_contents):
        if(char.isalpha()==True or char.isspace()):
            file_d+=char
    file_d=file_d.split()
    file_a=[]
    
    for word in file_d:
        if word.lower() not in uninteresting_words and word.isalpha()==True:
            file_a.append(word)
    frequency={}
    for word in file_a:
        if word.lower() not in frequency:
            frequency[word.lower()]=1
        else:
             frequency[word.lower()]+=1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency)
    return cloud.to_array()
