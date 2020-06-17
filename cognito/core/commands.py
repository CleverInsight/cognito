# -*- coding: utf-8 -*-
import logging
from cognito import *
from datetime import datetime, timedelta
from tqdm import tqdm
from prettytable import PrettyTable
from cognito.story import Story
from tornado import template




def generate_audit_report(df_raw, save):
	"""
	Generate audit report based on given dataframe
	
	:param      df_raw:  The df raw
	:type       df_raw:  { type_description }
	:param      save:    The save
	:type       save:    { type_description }
	"""
	start_time = datetime.now()
	description = PrettyTable(['Name', 'Values'])
	description.align['Name'] = "l"
	

	table = PrettyTable([
	    'Features', 
	    'Type', 
	    'Value Type', 
	    'Outliers', 
	    'Missing', 
	    '(%) Missing',
	    'Distinct Count',
	    'Min',
	    'Mean',
	    'Max',
	    'Zeros',
	    '(%) Zeros',
	    'Memory Size'            
	])

	try:
		# Access default dataframe
	    df = df_raw.data
	    features = df.columns
	    table.align["Features"] = "l"
	    table.align["Value Type"] = "l"
	    table.sortby = "Distinct Count"
	    table.reversesort = True

	    # Generate interesting brute force story
	    story = Story(df_raw)
	    stories = story.insight()


	    # Group duplicates
	    dups = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:'count'})

	    description.add_row(['Total variables', df.shape[1]])
	    description.add_row(['Total Observations', df.shape[0]])
	    description.add_row(['Missing Cells', df.isnull().sum().sum()])
	    description.add_row(['(%) Missing Cells', df.isnull().sum().sum() / len(df)])
	    description.add_row(['Duplicate Rows', dups['count'].sum() - dups.shape[0]])
	    description.add_row(['(%) Duplicate Rows', (dups['count'].sum() - dups.shape[0]) / len(dups)])
	    description.add_row(['Total Size of Memory', str(df.memory_usage().sum() / 1000) + 'KiB'])
	    description.add_row(['🍋 Total Categorical', count_categorical(df)])
	    description.add_row(['🔟 Total Continuous', len(df_raw.get_numerical().columns)])
	    description.add_row(['Started at', start_time.strftime("%d-%b-%y %H:%M:%S")])

	    for col in tqdm(features, ascii=True, desc="Auditing.. : "):
	        table.add_row([
	            col.strip(),
	            df[col].dtypes,
	            type_of_variable(df[col]), 
	            check_outlier(df[col]),
	            check_missing(df[col]), 
	            column_missing_percentage(df[col]), 
	            distinct_count(df[col]),
	            count_min(df[col]),
	            count_mean(df[col]),
	            count_max(df[col]),
	            df[col].isin([0]).sum(),
	            round(df[col].isin([0]).sum() / len(df.columns), 2),
	            str(df[col].memory_usage() / 1000) + 'KiB'
	        ])

	    end_time = datetime.now()
	    description.add_row(['Ended at', end_time.strftime("%d-%b-%y %H:%M:%S")])
	    description.add_row(['Time Elapsed', (end_time - start_time).total_seconds()])



	    # Save the report into HTML
	    if save:
	        
	        desc_html = description.get_html_string()
	        description_summary = desc_html.replace('<table>', '<table class="table is-bordered">')


	        report_html = table.get_html_string()
	        report_html = report_html.replace('<table>', '<table class="table is-bordered">')

	        
	        stories_json = [{'question': row['question'], \
	        'answer': row['answer'], 'type': row['type']} for row in stories]
	        loader = template.Loader(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../' 'scripts/templates'))

	        total_categorical = list(df_raw.get_categorical())
	        total_continuous = list(df_raw.get_numerical())

	        open(save + '.html', 'wb').write(loader.load("index.html").generate(**locals()))
	        click.echo('Report generated with name ' + save + '.html')


	    click.echo(description)
	    click.echo(table)

	except FileNotFoundError as e:
	    logging.warning("Given input file doesn't exists")
