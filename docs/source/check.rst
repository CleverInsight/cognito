:orphan:


Check class
============


Simple Usage
~~~~~~~~~~~~

.. code-block:: python

    >>> from cognito.modules import Check
    >>> import congito



is_categorical
~~~~~~~~~~~~~~~
is_categorical is a staticmethod which checks if a column is categorical or not.

.. code-block:: python
        
    >> Check.is_categorical(data['Age'])
    >> True



is_missing
~~~~~~~~~~~~~~~
is_missing is a staticmethod which checks if a column has missing values or not.

.. code-block:: python
        
    >> Check.is_missing(data['population'])
    >> True


