import pandas as pd
import json as js

class Processor:
    pos_rate = pd.DataFrame()
    recom_matrix = pd.DataFrame()
    data = pd.DataFrame()

    def __init__(self):
        print("Processor initiated")
        self.pos_rate = pd.read_csv(r'./static/positivity_rate.csv')
        self.recom_matrix = pd.read_csv(r'./static/recommender_matrix.csv')
        self.data = pd.read_csv(r'./static/sample30.csv')
        self.recom_matrix.set_index('prod_id', inplace=True)
        self.pos_rate.drop(columns=['Unnamed: 0'], inplace=True)

    def predict(self,name):
        if name in self.recom_matrix.columns.values:

            temp = self.recom_matrix[name].sort_values(ascending=False)
            temp = pd.concat([pd.Series(temp.index), pd.Series(temp.values)], axis=1)
            temp.rename(columns={0: "like_Rank"}, inplace=True)
            op = pd.merge(temp, self.pos_rate, on='prod_id', how='inner')
            res = op[:20].sort_values('pos_rate', ascending=False)['prod_id'][:5].values
            op = {'op': list(res), 'status': 0}
            res = js.dumps(op)

        else:
            op = {'op': [], 'status': 1}
            res = js.dumps(op)
        return res





