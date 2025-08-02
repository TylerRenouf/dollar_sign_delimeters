""""
We want to process $$...$$ and $...$ in notes to convert them to Anki MathJax compatible format with the following rules:

	For single dollar signs:
		1. Each opening delimeter must have a character directly to the right of it - cannot have whitespace
		2. Each closing delimeter must have a character directly to its left and whitespace to its right
	For double dollar signs:
		3. These are treated as delimeters no matter how they are placed 
		4. Double dollar signs with no corresponding closing dollar signs are not converted - possibly treated as erroneous input
	5. Delimeters are in general processed left to right - there is no encapsulation for instance $...$..$...$ consists of 2 math blocks one on the left one on the right
		5.5. If there are multiple unmatched openings before a closing, prefer the rightmost opening for math and treat the rest as literal dollar signs
	6. Look for delimeter pairs $$ before single delimeters. If within a block $$...$..$...$$ the inner delimeters are treated as math and will not be converted
 
"""

import re


def valid_closing(text,i):
	if i==0:
		return False
   
	return bool(re.match(r"\S\$",text[i-1:i+1]))

def valid_opening(text,i):
	if i>=len(text)-1:
		return False

	return bool(re.match(r"(\$\S)",text[i:i+2]))

def get_valid_pairs(text):
	single_openings = []
	double_openings = []

	single_pairs = []
	double_pairs = []
	
	
	i = 0

	while i < len(text):
		
		if text[i] == '$':
			if i+1<len(text) and text[i+1]=='$':
				if double_openings:
					start_idx = double_openings.pop()
					double_pairs.append((start_idx, i))
					i+=2
				elif single_openings and valid_closing(text,i):
					start_idx = single_openings.pop() 
					single_pairs.append((start_idx, i))
					i+=1
				else:  
					double_openings.append(i)
					i+=2
			else:
				# Overlaps with math block - skip it and remove any current inline
				if double_openings:
					if single_openings:
						single_openings.pop()
			
				elif valid_closing(text,i) and single_openings:
					start_idx = single_openings.pop() 
					single_pairs.append((start_idx, i))
					
				elif valid_opening(text, i):
					if single_openings:
						single_openings[0] = i
					else:
						single_openings.append(i)
				i+=1
						
	return single_pairs, double_pairs
	

def convert_obsidian_math(text: str) -> str:

	single_pairs, double_pairs = get_valid_pairs(text)
	
	text = list(text)
	
	for start, end in single_pairs:
		text[start] = r"\("
		text[end] = r"\)"
		
	for start, end in double_pairs:
		
		text[start] = r"\["
		text[start+1] = ""
		text[end] = r"\]"
		text[end+1] = ""
	
	return ''.join(text)