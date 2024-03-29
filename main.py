import random
import re
from sql_to_select import *

p1 = re.compile('\d{2}.\d{2}.\d{2,4}')
p2 = re.compile('\d{2}-\d{2}-\d{2,4}')
p3 = re.compile('\d{2}.\d{2}')
p4 = re.compile('\d{2}-\d{2}')

## Generator Class
class QueryGenerator:
    def __init__(self, table, table_name):
        # Declare Required Variable
        self.num_col_index = []
        self.col_index = []
        self.src_table = table
        self.src_table_name = table_name

        # Classification col, num_col
        for index in range(len(self.src_table[0])):
            self.col_index.append(index)
            if self.is_number_column(self.src_table, index):
                self.num_col_index.append(index)

        # Set fixed operation
        self.operation_text = {
            "MAX": ['maximum '],
            "MIN" : ['minimun ', 'least '],
            "Sum": ['sum ', 'total amount ', 'addition '],
            "Avg": ['the average ', 'the mean '],
            "Diff": ['difference ', 'gap '],
            "Verb": ['Tell me ', 'Give me ', 'Check ', 'Find ', 'Show me '],
            "Conj": ['What is ', 'Which is ', 'What was ', 'What\'s '],
            "Count": ['Count ', 'Count the number of '],
            "How": ['How many ', 'How much '],
            "Comp": ['more than ',' less than '],
            "Relation": ['which ', 'that '],
            "Relation2": ['where ', 'that ', 'whose '],
            "num_op": ['==', '!=', '>', '<', '>=', '<='],
            "op": ['==', '!=']
        }

        # Set not-num operation
        self.not_num_op_list = {
            "==": ['same with ', 'equal to ', 'equivalent of ', 'equivalent to '],
            "!=": ['different from ', 'not equal to ', 'not equivalent of ', 'not alike ', 'except',  'not same with '],
        }

        # Set op_text
        self.op_list = {
            "==": ['same with ', 'equal to ', 'equivalent of ', 'equivalent to '],
            "!=": ['different from ', 'not equal to ', 'not equivalent of ', 'not alike ', 'except', 'not same with '],
            ">": ['bigger than ', 'more than ', 'higher than ', 'larger than ', 'exceeding '],
            "<": ['smaller than ', 'less than ', 'lower than ', 'below ', 'lesser ', 'under '],
            ">=": ['no less than ', 'above ', 'equal or bigger than ', 'equal or greater than ', 'at least'],
            "<=": ['no more than ', 'not above ', 'equal or smaller than ', 'not above ', 'equal or less than ']
        }

    #### 1. SUM  2. Avg  3. DIFF 4. Count - In variable, number index(like 0, 1, 2, ... ) is sequence of variable ####
    # Sum operation function
    def input_literal_TO_SUM(self):
        # Set Required Variable
        Conj = random.choice(self.operation_text["Conj"])
        Verb = random.choice(self.operation_text["Verb"])
        Sum = random.choice(self.operation_text["Sum"])
        Relation2 = random.choice(self.operation_text["Relation2"])

        col_1_number = random.choice(self.col_index) # col_1 index
        col_1 = self.src_table[0][col_1_number]  # col_1 name
        col_num_0_number = random.choice(self.num_col_index)
        # while (col_num_0_number == col_1_number):
        #     col_num_0_number = random.choice(self.num_col_index)
        col_num_0 = self.src_table[0][col_num_0_number]

        if col_1_number in self.num_col_index:
            op_1_symbol = random.choice(self.operation_text['num_op'])
            op_1 = random.choice(self.op_list[op_1_symbol])
        else:
            op_1_symbol = random.choice(self.operation_text['op'])
            op_1 = random.choice(self.not_num_op_list[op_1_symbol])

        val_1 = self.src_table[random.randrange(1, len(self.src_table))][col_1_number]

        operations_sum = {
            "Sum_0": [f'{Conj}{Sum}of {col_num_0}?', # what is sum of A?
                      f'{Verb}{Sum}of {col_num_0}.', # Tell sum of A.
                      f'{Conj}{Sum} if you add all of {col_num_0}?',  # what is the total if you add all of the selection numbers together?
                      ],
            "Sum_1": [f'{Conj}{Sum}of {col_num_0} {Relation2}{col_1} is {op_1}{val_1}?', # What is sum of A where B > 2 ?
                      # f'Add all the {col_num_0} {Relation2}{col_1} is {op_1}{val_1}.', # Add all the
                      f'Add up {Sum}number of of {col_num_0}.'],
        }
        sql_sum = {
            "Sum_0": [f'SELECT SUM({col_num_0}) FROM [TABLE]'],
            "Sum_1": [f'SELECT SUM({col_num_0}) FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1}']
        }

        # select random query
        select_rand_operation = f'Sum_{random.randrange(len(operations_sum))}'
        my_literal = operations_sum[select_rand_operation][random.randrange(len(operations_sum[select_rand_operation]))]
        my_SQL = sql_sum[select_rand_operation][0]

        return my_literal, my_SQL

    # Avg operation function
    def input_literal_TO_AVG(self):
        # Set Required Variable
        Conj = random.choice(self.operation_text["Conj"])
        Verb = random.choice(self.operation_text["Verb"])
        Avg = random.choice(self.operation_text["Avg"])
        Sum = random.choice(self.operation_text["Sum"])
        How = random.choice(self.operation_text["How"])
        Relation2 = random.choice(self.operation_text["Relation2"])

        col_num_0_number = random.choice(self.num_col_index)
        col_num_0 = self.src_table[0][col_num_0_number]

        col_1_number = random.choice(self.col_index)
        # while (col_num_0_number == col_1_number):
        #     col_1_number = random.choice(self.col_index)
        col_1 = self.src_table[0][col_1_number]

        if col_1_number in self.num_col_index:
            op_1_symbol = random.choice(self.operation_text["num_op"])
            op_1 = random.choice(self.op_list[op_1_symbol])
        else:
            op_1_symbol = random.choice(self.operation_text["op"])
            op_1 = random.choice(self.not_num_op_list[op_1_symbol])

        val_1 = self.src_table[random.randrange(1, len(self.src_table))][col_1_number]

        if self.src_table_name == None:
            self.src_table_name = "this table"

        operations_avg = {
            "Avg_0": [f'{Conj}{Avg}{col_num_0} {Relation2}{col_1} is {op_1}{val_1}?',
                      f'{Verb}{Avg}{col_num_0} {Relation2}{col_1} is {op_1}{val_1}.'
                      f'On Average, {How}{col_num_0}?',
                      f'{Conj}{Avg}number of {col_num_0} {col_1} is {op_1}{val_1}?'],
            "Avg_1": [f'{Conj}{Avg}{col_num_0} of {self.src_table_name}?',
                      f'{Verb}{Avg}of {col_num_0}.',
                      f'{Conj}{Sum}of {col_num_0} divided by number of {col_num_0}?',
                      f'{Conj}{Avg}{col_num_0}?']
        }
        sql_avg = {
            "Avg_0": [f'SELECT AVG({col_num_0}) FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1}'],
            "Avg_1": [f'SELECT AVG({col_num_0}) FROM [TABLE]']
        }

        # select random query
        select_rand_operation = f'Avg_{random.randrange(len(operations_avg))}'
        my_literal = operations_avg[select_rand_operation][random.randrange(len(operations_avg[select_rand_operation]))]
        my_SQL = sql_avg[select_rand_operation][0]

        return my_literal, my_SQL

    # Diff operation function
    def input_literal_TO_DIFF(self):
        # Set Required Variable
        Conj = random.choice(self.operation_text["Conj"])
        Verb = random.choice(self.operation_text["Verb"])
        max = random.choice(self.operation_text["MAX"])
        min = random.choice(self.operation_text["MIN"])
        Relation = random.choice(self.operation_text["Relation"])
        Comp = random.choice(self.operation_text["Comp"])
        Diff = random.choice(self.operation_text["Diff"])

        col_num_0_number = random.choice(self.num_col_index)
        col_num_0 = self.src_table[0][col_num_0_number]

        col_1_number = random.choice(self.col_index)
        # while (col_num_0_number == col_1_number):
        #     col_1_number = random.choice(self.col_index)
        col_1 = self.src_table[0][col_1_number]
        col_2_number = random.choice(self.col_index)
        col_2 = self.src_table[0][col_2_number]

        if col_1_number in self.num_col_index:
            op_1_symbol = random.choice(self.operation_text["num_op"])
            op_1 = random.choice(self.op_list[op_1_symbol])
        else:
            op_1_symbol = random.choice(self.operation_text["op"])
            op_1 = random.choice(self.not_num_op_list[op_1_symbol])

        val_1 = self.src_table[random.randrange(1, len(self.src_table))][col_1_number]
        val_2 = self.src_table[random.randrange(1, len(self.src_table))][col_1_number]
        # rand_row = self.src_table[random.randrange((1, len(self.src_table)))]

        # if val_1 == val_2 ~ we use max/min gap (for cases that there are many stasified cell)
        # if val_1 != val_2:
        operations_diff = {
            # "Diff_0": [f'{Conj}{max}{Diff}in {col_num_0}?',
            #        f'How much {max}{col_num_0} is {Comp}minimum {col_num_0}?',
            #        f'{Verb}the {Diff}between max of {col_num_0} and min of {col_num_0}.'],
            # "Diff_1": [f'{Conj}{max}{Diff}between {col_num_0} {Relation}{col_1} {op_1}{val_1}?',
            #        f'From {col_1} {op_1}{val_1}, {Verb}the {max}{Diff}between {col_num_0}.',
            #        f'{Verb}{max}{Diff}between {col_num_0} {Relation}{col_1} {op_1}{val_1}.'],
            # "Diff_2": [f'{Conj}the second {min}in {col_num_0}?',
            #        f'{Verb}the second {min}in {col_num_0}.',
            #        f'Return the second {min}in {col_num_0}?',
            #        f'{Conj}the second value of {col_num_0} in ascending order?',
            #        f'{Conj}the second vaule of {col_num_0} from the back of descending order?'],
            "Diff_3": [f'{Conj}the {Diff}in {col_num_0} between {val_1} and {val_2}?',
                       f'Calculate the {Diff}in {col_num_0} between {val_1} and {val_2}.',
                       f'{Conj}the {col_num_0} {Diff}between {val_1} and {val_2}?',
                       f'In {col_num_0}, {Conj}the {Diff}between {val_1} and {val_2}?'],
            "Diff_3_NUM":[f'{Conj}the {Diff}in {col_num_0} {Relation}{col_1} is between {val_1} and {val_2}?',
                       f'Calculate the {Diff}in {col_num_0} {Relation}{col_1} is between {val_1} and {val_2}.',
                       f'{Conj}the {col_num_0} {Diff}{Relation}{col_1} is between {val_1} and {val_2}?',
                       f'In {col_num_0}, {Conj}the {Diff}{Relation}{col_1} is between {val_1} and {val_2}?',
                       ]
        }
        sql_diff = {
            # "Diff_0": [f'SELECT MAX({col_num_0}) - MIN({col_num_0}) FROM [TABLE]'],
            # "Diff_1": [f'SELECT MAX({col_num_0}) - MIN({col_num_0}) FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1}'],
            # "Diff_2": [f'SELECT MIN({col_num_0}) FROM [TABLE] WHERE {col_num_0} > MIN({col_num_0}) ORDER BY {col_num_0} ASC'],
            "Diff_3": [f'SELECT {col_num_0} FROM [TABLE] WHERE {col_1} == {val_1} + SELECT {col_num_0} FROM [TABLE] WHERE {col_1} == {val_2}'],
            "Diff_3_NUM": [f'SELECT {col_num_0} FROM [TABLE] WHERE {col_1} == {val_1} + SELECT {col_num_0} FROM [TABLE] WHERE {col_1} == {val_2}'],

        }
        # else:
        #     operations_diff = {
        #         "Diff_3": [f'{Conj}the {max}{Diff}in {col_num_0} between {val_1} and {val_2}?',
        #                    f'Calculate the {Diff}in {col_num_0} between {val_1} and {val_2}.',
        #                    f'{Conj}the {col_num_0} {Diff} between {val_1} and {val_2}',
        #                    f'In {col_num_0}, {Conj}the {Diff}between {val_1} and {val_2}?']
        #     }
        #
        #     sql_diff = {
        #         "Diff_3": [f'SELECT {col_num_0} FROM [TABLE] WHERE {col_1} == {val_1} + SELECT {col_num_0} FROM [TABLE] WHERE {col_1} == {val_2}']
        #     }

        # select random query
        # select_rand_operation = f'Diff_{random.randrange(len(operations_diff))}'

        try:
            tmp = int(val_1)
            select_rand_operation = f'Diff_3_NUM'
        except:
            select_rand_operation = f'Diff_3'
        my_literal = operations_diff[select_rand_operation][random.randrange(len(operations_diff[select_rand_operation]))]
        my_SQL = sql_diff[select_rand_operation][0]

        return my_literal, my_SQL

    def input_literal_TO_DIFF2(self):
        # Set Required Variable
        Conj = random.choice(self.operation_text["Conj"])
        Verb = random.choice(self.operation_text["Verb"])
        max = random.choice(self.operation_text["MAX"])
        min = random.choice(self.operation_text["MIN"])
        Relation = random.choice(self.operation_text["Relation"])
        Comp = random.choice(self.operation_text["Comp"])
        Diff = random.choice(self.operation_text["Diff"])

        col_num_0_number = random.choice(self.num_col_index)
        col_num_0 = self.src_table[0][col_num_0_number]

        col_1_number = random.choice(self.col_index)
        # while (col_num_0_number == col_1_number):
        #     col_1_number = random.choice(self.col_index)
        col_1 = self.src_table[0][col_1_number]
        col_2_number = random.choice(self.col_index)
        col_2 = self.src_table[0][col_2_number]

        if col_1_number in self.num_col_index:
            op_1_symbol = random.choice(self.operation_text["num_op"])
            op_1 = random.choice(self.op_list[op_1_symbol])
        else:
            op_1_symbol = random.choice(self.operation_text["op"])
            op_1 = random.choice(self.not_num_op_list[op_1_symbol])

        val_1 = self.src_table[random.randrange(1, len(self.src_table))][col_1_number]
        val_2 = self.src_table[random.randrange(1, len(self.src_table))][col_1_number]
        # rand_row = self.src_table[random.randrange((1, len(self.src_table)))]

        operations_diff = {
            "Diff_3_NUM":[f'{Conj}the {Diff}in {col_num_0} {Relation}{col_1} is between {val_1} and {val_2}?',
                       f'Calculate the {Diff}in {col_num_0} {Relation}{col_1} is between {val_1} and {val_2}.',
                       f'{Conj}the {col_num_0} {Diff}{Relation}{col_1} is between {val_1} and {val_2}?',
                       f'In {col_num_0}, {Conj}the {Diff}{Relation}{col_1} is between {val_1} and {val_2}?',
                       ]
        }
        sql_diff = {
            "Diff_3_NUM": [f'SELECT {col_num_0} FROM [TABLE] WHERE {col_1} == {val_1} + SELECT {col_num_0} FROM [TABLE] WHERE {col_1} == {val_2}'],

        }

        select_rand_operation = f'Diff_3_NUM'
        my_literal = operations_diff[select_rand_operation][random.randrange(len(operations_diff[select_rand_operation]))]
        my_SQL = sql_diff[select_rand_operation][0]

        return my_literal, my_SQL

    # Count operation function
    def input_literal_TO_COUNT(self):
        # Set Required Variable
        Conj = random.choice(self.operation_text["Conj"])
        Verb = random.choice(self.operation_text["Verb"])
        Count = random.choice(self.operation_text["Count"])
        Relation = random.choice(self.operation_text["Relation"])
        Relation2 = random.choice(self.operation_text["Relation2"])

        col_0_number = random.choice(self.col_index)
        col_0 = self.src_table[0][col_0_number]

        col_num_1_number = random.choice(self.num_col_index)
        # while(col_num_1_number==col_0_number):
        #     col_num_1_number = random.choice(self.num_col_index)
        col_num_1 = self.src_table[0][col_num_1_number]

        col_1_number = random.choice(self.col_index)
        while (col_num_1_number == col_1_number and col_1_number == col_0_number):
            col_1_number = random.choice(self.col_index)
        col_1 = self.src_table[0][col_1_number]

        if col_0_number in self.num_col_index:
            op_0_symbol = random.choice(self.operation_text["num_op"])
            op_0 = random.choice(self.op_list[op_0_symbol])
        else:
            op_0_symbol = random.choice(self.operation_text["op"])
            op_0 = random.choice(self.not_num_op_list[op_0_symbol])

        if col_1_number in self.num_col_index:
            op_1_symbol = random.choice(self.operation_text["num_op"])
            op_1 = random.choice(self.op_list[op_1_symbol])
        else:
            op_1_symbol = random.choice(self.operation_text["op"])
            op_1 = random.choice(self.not_num_op_list[op_1_symbol])

        val_0 = self.src_table[random.randrange(1, len(self.src_table))][col_0_number]
        val_1 = self.src_table[random.randrange(1, len(self.src_table))][col_1_number]

        # Set Count operation
        operations_count = {
            "Count_0": [f'{Conj}the number of {col_0} is {op_0}{val_0}?',
                        f'How many {col_0} are {op_0}{val_0}?',
                        f'{Count}{col_0}{Relation}is {op_0}{val_0}.',
                        f'{Count}{col_0}is {op_0}{val_0}.',
                        f'For each {col_0}, return how many {col_1} are {op_1}{val_1}.'],
            "Count_1": [f'How many types are in {col_0}?',
                        f'How many numbers are in {col_0}?',
                        f'{Verb}how many total options in {col_0}.',
                        f'Add up the total number of of {col_0}.'],
            "Count_2": [f'How many {col_0} {Relation2}{col_num_1} is {op_1}minimum {col_num_1}?',
                        f'From {col_num_1} is {op_1}minimum {col_num_1}, {Verb}the number of {col_0}.',
                        f'For each {col_0}, how many {col_num_1} are {op_1}minimum {col_num_1}?'],
            "Count_3": [f'{Conj}the number of {col_0} is {op_0}{val_0} or {col_1} is {op_1}{val_1}?',
                        f'How many {col_0} are {op_0}{val_0} or {col_1} are {op_1}{val_1}?',
                        f'{Count} {col_0} {op_0}{val_0} or {col_1} {op_1}{val_1}?',
                        f'{Verb} the number of {col_0} {op_0} {val_0} or {col_1} {op_1} {val_1}?'],
        }
        sql_count = {
            "Count_0": [f'SELECT COUNT(*) FROM [TABLE] WHERE {col_0} {op_0_symbol} {val_0}'],
            "Count_1": [f'SELECT COUNT(DISTINCT {col_0}) FROM [TABLE]'],
            "Count_2": [f'SELECT COUNT(*) FROM [TABLE] WHERE {col_num_1} {op_1_symbol} MIN({col_num_1})'],
            "Count_3": [f'SELECT COUNT(*) FROM [TABLE] WHERE {col_0} {op_0_symbol} {val_0} OR {col_1} {op_1_symbol} {val_1}'],
        }

        # select random query
        select_rand_operation = f'Count_{random.randrange(0, len(operations_count))}'
        my_literal = operations_count[select_rand_operation][random.randrange(0, len(operations_count[select_rand_operation]))]
        my_SQL = sql_count[select_rand_operation][0]

        return my_literal, my_SQL

    def input_literal_TO_SELECT(self):
        # Set Required Variable
        Conj = random.choice(self.operation_text["Conj"])
        Verb = random.choice(self.operation_text["Verb"])
        Relation = random.choice(self.operation_text["Relation"])
        MIN = random.choice(self.operation_text["MIN"])
        MAX = random.choice(self.operation_text["MAX"])

        col_num_0_number = random.choice(self.num_col_index)
        col_num_0 = self.src_table[0][col_num_0_number]

        col_1_number = random.choice(self.col_index)
        col_1 = self.src_table[0][col_1_number]

        col_2_number = random.choice(self.col_index)
        col_2 = self.src_table[0][col_2_number]

        if col_1_number in self.num_col_index:
            op_1_symbol = random.choice(self.operation_text["num_op"])
            op_1 = random.choice(self.op_list[op_1_symbol])
        else:
            op_1_symbol = random.choice(self.operation_text["op"])
            op_1 = random.choice(self.not_num_op_list[op_1_symbol])

        if col_2_number in self.num_col_index:
            op_2_symbol = random.choice(self.operation_text["num_op"])
            op_2 = random.choice(self.op_list[op_2_symbol])
        else:
            op_2_symbol = random.choice(self.operation_text["op"])
            op_2 = random.choice(self.not_num_op_list[op_2_symbol])

        val_1 = self.src_table[random.randrange(1, len(self.src_table))][col_1_number]
        val_2 = self.src_table[random.randrange(1, len(self.src_table))][col_2_number]

        operations_sel = {
            "SELECT_0": [f'{Conj}all the {col_num_0} on the [TABLE]?',
                         f'{Verb}all the {col_num_0} on the [TABLE].'],
            "SELECT_1": [f'{Conj}the {col_num_0} where {col_1} is {op_1}{val_1}?',
                         f'{Verb}the {col_num_0} where {col_1} is {op_1}{val_1}.'],
            "SELECT_2":[f'{Conj}the {col_num_0} where {col_1} is {op_1}{val_1} and {col_2} is {op_2}{val_2}?',
                        f'{Verb}the {col_num_0} where {col_1} is {op_1}{val_1} and {col_2} is {op_2}{val_2}.'],
            "SELECT_3":[f'{Conj}the {MAX}{col_num_0} on the [TABLE]?',
                        f'{Verb}the {MAX}{col_num_0} on the [TABLE].'],
            "SELECT_4": [f'{Conj}the {MAX}{col_num_0} where {col_1} is {op_1}{val_1}?',
                         f'{Verb}the {MAX}{col_num_0} where {col_1} is {op_1}{val_1}.'],
            "SELECT_5":[f'{Conj}the {MAX}{col_num_0} where {col_1} is {op_1}{val_1} and {col_2} is {op_2}{val_2}?',
                        f'{Verb}the {MAX}{col_num_0} where {col_1} is {op_1}{val_1} and {col_2} is {op_2}{val_2}.'],
            "SELECT_6": [f'{Conj}the {MIN}{col_num_0} on the [TABLE]?',
                         f'{Verb}the {MIN}{col_num_0} on the [TABLE].'],
            "SELECT_7": [f'{Conj}the {MIN}{col_num_0} where {col_1} is {op_1}{val_1}?',
                         f'{Verb}the {MIN}{col_num_0} where {col_1} is {op_1}{val_1}.'],
            "SELECT_8": [f'{Conj}the {MIN}{col_num_0} where {col_1} is {op_1}{val_1} and {col_2} is {op_2}{val_2}?',
                         f'{Verb}the {MIN}{col_num_0} where {col_1} is {op_1}{val_1} and {col_2} is {op_2}{val_2}.']
        }
        sql_sel = {
            "SELECT_0": [f'SELECT {col_num_0} FROM [TABLE]'],
            "SELECT_1": [f'SELECT {col_num_0} FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1}'],
            "SELECT_2": [f'SELECT {col_num_0} FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1} and {col_2} {op_2_symbol} {val_2}'],
            "SELECT_3": [f'SELECT MAX({col_num_0}) FROM [TABLE]'],
            "SELECT_4": [f'SELECT MAX({col_num_0}) FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1}'],
            "SELECT_5": [f'SELECT MAX({col_num_0}) FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1} and {col_2} {op_2_symbol} {val_2}'],
            "SELECT_6": [f'SELECT MIN({col_num_0}) FROM [TABLE]'],
            "SELECT_7": [f'SELECT MIN({col_num_0}) FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1}'],
            "SELECT_8": [f'SELECT MIN({col_num_0}) FROM [TABLE] WHERE {col_1} {op_1_symbol} {val_1} and {col_2} {op_2_symbol} {val_2}'],

        }

        # select random query
        select_rand_operation = f'SELECT_{random.randrange(len(operations_sel))}'
        my_literal = operations_sel[select_rand_operation][random.randrange(len(operations_sel[select_rand_operation]))]
        my_SQL = sql_sel[select_rand_operation][0]

        return my_literal, my_SQL

    def check_date(self, seq: str):
        date_list = ['date', 'Date', 'DATE', 'DAY', 'day', 'Day']
        for day in date_list:
            if day in seq:
                return True

    def is_num(self, word: str):  # num인지 파악
        num_str = ''
        for i in range(len(word)):
            if ord('0') <= ord(word[i]) <= ord('9'):
                num_str += word[i]
            elif word[i] == '.':
                num_str += word[i]

        if len(word) == 0:  # 문자열 없으면 None 반환
            return False, None
        if len(num_str) * 2 >= len(word):  # 문자열 절반이상이 숫자면 True랑 num_str 반환
            return True, num_str
        else:
            return False, num_str

    ## This def cannot distinguish numeric data using ','
    def is_number_column(self, table: list, col_idx: int):  # Column 중에 num이 있는지 확인
        is_number = True
        if self.check_date(self.src_table[0][col_idx]):
            is_number = False
            return is_number

        for i in range(1, len(table)):
            isNum, _ = self.is_num(table[i][col_idx])  # T/F 반환만 원함
            if isNum is False:
                is_number = False
        return is_number

if __name__=='__main__':
    src_talbe_name = None
    src_table = list()
    src_table.append(['number', 'name', 'Position', 'Birthday', 'Size', 'Weight', 'Last Team'])
    src_table.append(['5', 'Tom Lipke', 'Guard/ Forward', '12.04.1986', '1,96', '98', 'Bremen Roosters'])
    src_table.append(['6', 'Muamer Taletovic', 'Guard', '02.04.1976', '1,87', '98', 'SSC Karlsruhe'])
    src_table.append(['7', 'David Watson', 'Forward', '16.09.1988', '1,84', '100', 'Hertener Löwen'])
    src_table.append(['8', 'Brandon Gary', 'Center', '26.01.1983', '2,03', '110', 'Aschersleben Tiger'])
    src_table.append(['9', 'Theodis Tarver', 'Guard', '09.07.1984', '2,06', '108', 'Chemosvit Svit'])
    src_table.append(['10', 'Muamer Taletovic', 'Forward', '25.05.1977', '1,80', '68', 'SG Bad Dürkheim/Speyer'])

    Generator = QueryGenerator(src_table, src_talbe_name)

    # print('Sum================')
    # query, sql = Generator.input_literal_TO_SUM()
    # print(f'Query: {query}\nSQL: {sql}\nSELECT CELL: {Change_SQL_CAP(sql)}')
    # print('\nAvg================')
    # query, sql = Generator.input_literal_TO_AVG()
    # print(f'Query: {query}\nSQL: {sql}\nSELECT CELL: {Change_SQL_CAP(sql)}')
    # print('\nDiff================') ## Diff 3이 wikitq 스타일임!!!!!
    # query, sql = Generator.input_literal_TO_DIFF()
    # print(f'Query: {query}\nSQL: {sql}\nSELECT CELL: {Change_SQL_CAP(sql)}')
    # print('\nDiff2================')  ## Diff 3_NUM 은 조건에 사용되는 컬럼 다 나옴!!!!!
    # query, sql = Generator.input_literal_TO_DIFF2()
    # print(f'Query: {query}\nSQL: {sql}\nSELECT CELL: {Change_SQL_CAP(sql)}')
    # print('\nCount================')
    # query, sql = Generator.input_literal_TO_COUNT()
    # print(f'Query: {query}\nSQL: {sql}\nSELECT CELL: {Change_SQL_CAP(sql)}')
    print('\nSELECT================')
    query, sql = Generator.input_literal_TO_SELECT()
    print(f'Query: {query}\nSQL: {sql}\nSELECT CELL: {Change_SQL_CAP(sql)}')



