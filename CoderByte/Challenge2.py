def LetterCapitalize(str):
	words = str.split(' ')
	capitalized_words = []
	for word in words:
		title_case_word = word[0].upper() + word[1:]
		capitalized_words.append(title_case_word)
		output = ' '.join(capitalized_words)
	return output	

k=LetterCapitalize("hello world")
print(k)