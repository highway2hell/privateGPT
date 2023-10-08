import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.set_proxy('http://127.0.0.1:10809')
nltk.download('averaged_perceptron_tagger')