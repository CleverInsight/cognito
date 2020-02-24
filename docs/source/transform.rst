:orphan:


Transform
=========


encoding_categorical
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
	
		>> Check.encoding_categorical(data['Age'])
		>> False



remove_records
^^^^^^^^^^^^^^^
remove_records removes the missing data from the given dataframe row wise.

.. code-block:: python
		>> Check.remove_records(data)
    >> dataframe



remove_columns
^^^^^^^^^^^^^^^
remove_columns removes the missing data from the given dataframe column wise.

.. code-block:: python
		
		>> Check.remove_columns(data)
        >> dataframe



percentage_missing
^^^^^^^^^^^^^^^^^^^
percentage_missing returns a dictionary containing percentage of missing data in each column.

.. code-block:: python
		
		>> Check.percentage_missing(data)
        >> dictionary



replace_mean
^^^^^^^^^^^^^
replace_mean replaces the missing value by the mean of the column.

.. code-block:: python
		
		>> Check.replace_mean(data)
        >> series



replace_median
^^^^^^^^^^^^^^^
replace_median replaces the missing value by the median of the column.

.. code-block:: python
		
		>> Check.replace_median(data)
    >> series



ignore_identifier
^^^^^^^^^^^^^^^^^^
`ignore_identifier` remove the column from the given dataframe if the row is an identifer row.

.. code-block:: python
		
		>> Check.ignore_identifier(data)
		>> dataframe
