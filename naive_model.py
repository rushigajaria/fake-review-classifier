
import numpy as np

class NaiveModel:
    # input review in format:
    # Review Id, Review length, Rating/sentiment agreement, Review date, sentiment variability
    def classify(self,some_processed_review):
        if float(some_processed_review[4])>self.sentiment_threshold:
            return True #means review is real
        return False #means review is fake

    # Input list of data with columns:
    #   Review Id, Review length, Rating/sentiment agreement, Review date, sentiment variability
    def train(self,training_data):
        sentiments = training_data[:,4].astype(float)
        self.sentiment_threshold = np.percentile(sentiments,30)