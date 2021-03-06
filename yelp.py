import json
from data import DefDict
import movie
import classifier
import ngrams
import codecs
class Yelp:
    def __init__(self, loc):
        f = open(loc)
        jsons = [json.loads(i) for i in f.readlines()]
        jsons = [i for i in jsons if i['type'] == 'review']
        self.stars = dict([(i, []) for i in range(1, 6)])
        for j in jsons:
            if j['type'] == 'review':
                self.stars[j['stars']].append(j['text'])
                
    def save(self):
        for i in range(1, 6):
            for j in range(0, len(self.stars[i])):
                f = codecs.open("yelp/" + str(i) + "star/file" + str(j), 'w', encoding="ascii", errors="ignore")
                f.write(self.stars[i][j])
                f.close()

    
if __name__ == "__main__":
    #m = movie.MovieReviews(classifier.BayesPresenceClassifier, 2)
    print "Reading Yelp data"
    y = Yelp("yelp/json_ascii")
    print "Saving"
    y.save()
