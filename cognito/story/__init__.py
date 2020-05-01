# -*- coding: utf-8 -*-
import os
import cognito
import pandas as pd
import numpy as np
from cognito.table import Table




def get_stories(df):
    """
    Get intutive stories from given dataset
    
    :param      df:   { parameter_description }
    :type       df:   { type_description }
    """
    categories = df.get_categorical().columns
    continuous = df.get_numerical().columns

    stories = []
    cat_copy = list(categories)
    for col in categories:
        # Remove the current col
        if col in cat_copy:
            cat_copy.remove(col)
        try:
            # Get comparison variable
            x = cat_copy.pop()
            d = pd.pivot_table(df.data, index=(col), values=[x],\
             aggfunc='count').reset_index().sort_values(by=x, ascending=False)
            stories.append({
                'question': "%s with high count of %s" %(col, x),
                'question_html': "<span class='tag is-primary is-light'>%s</span>\
                 with high count of  <span class='tag is-success is-light'>%s</span>" % (col, x),
                'answer': d[col].head(1).values[0],
                'misc': d
            })
        except IndexError as e:
            pass
        
        for num in continuous:
            d = pd.pivot_table(df.data, index=[col], values=[num],\
             aggfunc=np.sum).reset_index().sort_values(by=num, ascending=False)
            stories.append({
                'question': "%s with sum of %s" % (col, num),
                'question_html': "<span class='tag is-primary is-light'>%s</span>\
                with sum of <span class='tag is-success is-light'>%s</span>" % (col, num),
                'answer': round(d[num].head(1).values[0]),
                'misc': d
            })

    return stories


def get_interesting_stories(df):
    """
    Get intutive stories from given dataset
    
    :param      df:   { parameter_description }
    :type       df:   { type_description }
    """
    categories = df.get_categorical().columns
    continuous = df.get_numerical().columns

    stories = []
    cat_copy = list(categories)
    for col in categories:
        # Remove the current col
        if col in cat_copy:
            cat_copy.remove(col)
        try:
            # Get comparison variable
            x = cat_copy.pop()
            d = pd.pivot_table(df.data, index=(col), values=[x],\
             aggfunc='count').reset_index().sort_values(by=x, ascending=False)


            # Highest %s was %s on the %s %s
            stories.append({
                'question': "Highest %s was %s, %s %s." %(x, d[x].head(1).values[0], col, d[col].head(1).values[0]),
                'question_html': "Highest <span class='tag is-primary is-light'>%s</span>\
                 was %s of  <span class='tag is-success is-light'>%s</span> %s." % (x, d[x].head(1).values[0], col, d[col].head(1).values[0]),
                'answer': d[col].head(1).values[0],
                'misc': d
            })

            # Lowest %s was %s on the %s %s
            stories.append({
                'question': "Lowest %s was %s, %s %s." %(x, d[x].tail(1).values[0], col, d[col].tail(1).values[0]),
                'question_html': "Lowest <span class='tag is-primary is-light'>%s</span>\
                 was %s of  <span class='tag is-success is-light'>%s</span> %s." % (x, d[x].tail(1).values[0], col, d[col].tail(1).values[0]),
                'answer': d[col].tail(1).values[0],
                'misc': d
            })


        except IndexError as e:
            pass
        
        for num in continuous:
            d = pd.pivot_table(df.data, index=[col], values=[num],\
             aggfunc=np.sum).reset_index().sort_values(by=num, ascending=False)


            stories.append({
                'question': "Highest %s is %s, for %s %s." % (num, d[num].head(1).values[0], col, d[col].head(1).values[0]),
                'question_html': "Highest <span class='tag is-primary is-light'>%s</span>\
                is %s for <span class='tag is-success is-light'>%s</span> %s." % (num, d[num].head(1).values[0], col, d[col].head(1).values[0]),
                'answer': round(d[num].head(1).values[0]),
                'misc': d
            })


            stories.append({
                'question': "Lowest %s is %s, for %s %s." % (num, d[num].tail(1).values[0], col, d[col].tail(1).values[0]),
                'question_html': "Lowest <span class='tag is-primary is-light'>%s</span>\
                is %s for <span class='tag is-success is-light'>%s</span> %s." % (num, d[num].tail(1).values[0], col, d[col].tail(1).values[0]),
                'answer': round(d[num].tail(1).values[0]),
                'misc': d
            })

    return stories



