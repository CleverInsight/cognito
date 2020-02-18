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
`remove_records` remove the missing data from the given dataframe.

.. code-block:: python
		
		>> Check.remove_col(data)
        >> dataframe


is_outlier
^^^^^^^^^^
`is_outliers` detect the outliers from the given column and returns a list of the outliers.

.. code-block:: python

Check.is_outlier(data['population'])
           >> [6815.0, 6860.0, 11551.0]