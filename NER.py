__tile__ = 'news'
__author__ = 'Supriyo Sarkar'
__license__ = 'JISCE'
__copyright__ = 'Copyright 2022, Supriyo Sarkar'


import nltk
import pandas as pd


def wordBasedNER(text):
    # tokenize to words
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    nltk.help.upenn_tagset('NNP')
    chunks = nltk.ne_chunk(pos_tags, binary=False)
    entities = []
    labels = []
    for chunk in chunks:
        if hasattr(chunk, 'label'):
            entities.append(' '.join(c[0] for c in chunk))
            labels.append(chunk.label())

    entities_labels = list(set(zip(entities, labels)))
    entities_df = pd.DataFrame(entities_labels)
    entities_df.columns = ["Entities", "Labels"]
    return entities_df


def senBasedNER(text):
    # tokenize to sentences
    entities = []
    labels = []
    sentence = nltk.sent_tokenize(text)
    for sent in sentence:
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)), binary=False):
            if hasattr(chunk, 'label'):
                entities.append(' '.join(c[0] for c in chunk))
                labels.append(chunk.label())
    entities_labels = list(set(zip(entities, labels)))
    entities_df = pd.DataFrame(entities_labels)
    entities_df.columns = ['Entities', 'labels']
    return entities_df


textR = """External Affairs Minister S Jaishankar is understood to have discussed various global issues, including the US-Russia stand-off over Ukraine, during a meeting with American Secretary of State Antony Blinken in Melbourne on the margins of the Quad foreign ministers’ meeting.
“A review of our bilateral cooperation with @SecBlinken. The readout on progress in different domains was positive. Our strategic partnership has deepened so visibly,” Jaishankar tweeted later.
He also had a bilateral meeting with his Japanese counterpart Yoshimasa Hayashi and discussed a range of issues. “Good to meet [email protected] in person. Our conversation followed up on two virtual discussions. We prepare for our Annual Summit of Leaders,” he tweeted.
Jaishankar also met Marise Payne who hosted the Quad meeting and visited the MCG Cricket ground in Melbourne. 
“A fitting end to a busy day. Quad FMs visit the @MCG. Presented @MarisePayne with a bat signed by @imVkohli. A message of fair play and rules of the game,” he tweeted."""

print(senBasedNER(textR))

