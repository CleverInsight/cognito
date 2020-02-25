import os
from cognito.table import Table
from prettytable import PrettyTable


class Report:
    
    def __init__(self, filename):
        self.data = Table(filename)



    def generate(self):

        columns = self.data.columns()
        table = PrettyTable(columns)
        print(table)
        




