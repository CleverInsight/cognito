# -*- coding: utf-8 -*-
import os
import cognito
import pandas as pd
import numpy as np
from cognito.table import Table





class Story:

    def __init__(self, dataframe):
        self.table = dataframe


    @staticmethod
    def prepare(df, x1, x2, y1, y2, aggfunc, val_type):

        if aggfunc == 'count':

            return dict(
                    question= "{} {} was {}, {} {}.".format(val_type, x1, x2, y1, y2),
                    question_html= "{} <span class='tag is-primary is-light'>{}</span>\
                         was {} of  <span class='tag is-success is-light'>{}</span> {}.".format(val_type, x1, x2, y1, y2),
                    answer= x2,
                    misc= df,
                    type=val_type
            )

        if aggfunc == 'sum':

            return dict(
                        question = "{} {} was {}, {} {}.".format(val_type, x1, x2, y1, y2),
                        question_html = "{} <span class='tag is-primary is-light'>{}</span>\
                             was {} of  <span class='tag is-success is-light'>{}</span> {}.".format(val_type, x1, x2, y1, y2),
                        answer = x2,
                        misc = df,
                        type=val_type
            )



    def insight(self):
        """
        Get intutive descriptive stories from given dataset
        
        :param      df:   { parameter_description }
        :type       df:   { type_description }
        """
        categories = self.table.get_categorical().columns
        continuous = self.table.get_numerical().columns

        stories = []
        cat_copy = list(categories)
        for col in categories:
            # Remove the current col
            if col in cat_copy:
                cat_copy.remove(col)
            try:
                # Get comparison variable
                x = cat_copy.pop()
                d = pd.pivot_table(self.table.data, index=(col), values=[x],\
                 aggfunc='count').reset_index().sort_values(by=x, ascending=False)

                # Highest 
                stories.append(
                    self.prepare(d, x, d[x].head(1).values[0],
                    col, d[col].head(1).values[0], val_type='Highest', aggfunc='count')
                )   

                # Lowest
                stories.append(
                    self.prepare(d, x, d[x].tail(1).values[0], 
                    col, d[col].tail(1).values[0], val_type='Lowest', aggfunc='count')
                )


            except IndexError as e:
                pass
            
            for num in continuous:
                d = pd.pivot_table(self.table.data, index=[col], values=[num],\
                 aggfunc=np.sum).reset_index().sort_values(by=num, ascending=False)

                # Highest 
                stories.append(
                    self.prepare(d, num, d[num].head(1).values[0], 
                        col, d[col].head(1).values[0], aggfunc='sum', val_type='Highest')
                )

                # Lowest
                stories.append(
                    self.prepare(d, num, d[num].tail(1).values[0], 
                        col, d[col].tail(1).values[0], aggfunc='sum', val_type='Lowest')
                )

        return stories





