import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sklearn.decomposition import PCA
principal = pd.read_csv('LIWC2015final.csv')
df = principal[['WC' , 'Analytic' , 'Clout' , 'Authentic' , 'Tone' , 'WPS' , 'Sixltr' , 'Dic' , 'function' , 'pronoun' , 'ppron' , 'i' , 'we' , 'you' , 'shehe' , 'they' , 'ipron' , 'article' , 'prep' , 'auxverb' , 'adverb' , 'conj' , 'negate' , 'verb' , 'adj' , 'compare' , 'interrog' , 'number' , 'quant' , 'affect' , 'posemo' , 'negemo' , 'anx' , 'anger' , 'sad' , 'social' , 'family' , 'friend' , 'female' , 'male' , 'cogproc' , 'insight' , 'cause' , 'discrep' , 'tentat' , 'certain' , 'differ' , 'percept' , 'see' , 'hear' , 'feel' , 'bio' , 'body' , 'health' , 'sexual' , 'ingest' , 'drives' , 'affiliation' , 'achieve' , 'power' , 'reward' , 'risk' , 'focuspast' , 'focuspresent' , 'focusfuture' , 'relativ' , 'motion' , 'space' , 'time' , 'work' , 'leisure' , 'home' , 'money' , 'relig' , 'death' , 'informal' , 'swear' , 'netspeak' , 'assent' , 'nonflu' , 'filler' , 'AllPunc' , 'Period' , 'Comma' , 'Colon' , 'SemiC' , 'QMark' , 'Exclam' , 'Dash' , 'Quote' , 'Apostro' , 'Parenth']]
df.describe()
pca = PCA(n_components=2)
pca.fit(df)
T = pca.transform(df)
print(df.shape)
print(T.shape)
print(T)