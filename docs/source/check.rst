:orphan:


Check 
=====


Simple Usage
~~~~~~~~~~~~

.. code-block:: python

    >>> from cognito.check import Check
    >>> import congito



is_categorical
~~~~~~~~~~~~~~~

is_categorical is a staticmethod which checks if a column is categorical or not.

.. code-block:: python
        
    >> Check.is_categorical(data['Age'])
    >> True


is_discrete
~~~~~~~~~~~~~~~
is_discrete is a staticmethod which takes a column as an input and checks if it is discrete or not.

.. code-block:: python
        
    >> Check.is_discrete(data['Age'])
    >> True

is_continuous
~~~~~~~~~~~~~~~
is_continuous is a staticmethod which takes a column as an input and checks if it is continuous or not.

.. code-block:: python
        
    >> Check.is_continuous(data['Age'])
    >> True




is_missing
~~~~~~~~~~~~~~~
is_missing is a staticmethod which checks if a column has missing values or not.

.. code-block:: python
        
    >> Check.is_missing(data['population'])
    >> True



is_identifier
~~~~~~~~~~~~~~~
is_identifier is a staticmethod which checks if a column is an identifier or not.

.. code-block:: python
        
    >> Check.is_identifier(data['Name'])
    >> True

