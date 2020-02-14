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
is_categorical is a staticmethod which checks if a column is catagorical or not.

.. code-block:: python
        
    >> Check.is_categorical(data['Age'])
    >> True



is_identifier
~~~~~~~~~~~~~~~
is_identifier is a staticmethod which checks if a column is an identifier or not.

.. code-block:: python
        
    >> Check.is_identifier(data['Name'])
    >> True
