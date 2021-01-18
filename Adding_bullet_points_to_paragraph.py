# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:19:13 2021

@author: gshambul
"""

text='''Emphasize the beginning of the bullet point, as in this list, when the first few words capture the main idea. That way, readers can skim easily. Use bold type, italics, or underlining for emphasis.
Make bullet points consistent in structure. For example, make all of them sentences or fragments or questions. However, if you have two sets of bullet points in a document, you don't need to make them consistent with each other--just within themselves.
Punctuate bullets consistently. That is, if one bullet ends with a period (full stop), end all with a period, following these rules.
If all bullets are sentences, end each one with a period (full stop).
If all bullets are phrases or fragments, use no end punctuation.
Avoid ending bullet points with semicolons. Semicolons have been used that way, but the style seems old-fashioned in today's crisp documents. Note: A semicolon looks like this: ;
Avoid making bullet points so long that they look like paragraphs. Three lines is a reasonable maximum length.
Number bullet points when you have many--more than five or so. That way your readers can easily track the bullets and refer to them.
Avoid using transition words and phrases such as "secondly" or "another point." Such linking phrases are unnecessary, and they slow down readers. 
Be sure bullet points are related, especially if you have a lot of them. When you have many, you may need two sets instead of one. For example, if your bullets contain a blend of advantages and opportunities, break them into two lists, with one labeled Advantages and another labeled Opportunities.
Avoid bullet points when you want to build rapport or deal with a sensitive issue. Bullets communicate efficiency rather than warmth.
Lay out bullet points cleanly. Avoid a variety of fonts or a mix of margins.'''
    
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* '+lines[i]
    
text = '\n'.join(lines)

print(text)
