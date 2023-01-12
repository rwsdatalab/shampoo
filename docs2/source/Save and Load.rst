.. _code_directive:

-------------------------------------

Save and Load
''''''''''''''

Saving and loading models is desired as the learning proces of a model for ``shampoo`` can take up to hours.
In order to accomplish this, we created two functions: function :func:`shampoo.save` and function :func:`shampoo.load`
Below we illustrate how to save and load models.


Saving
----------------

Saving a learned model can be done using the function :func:`shampoo.save`:

.. code:: python

    import shampoo

    # Load example data
    X,y_true = shampoo.load_example()

    # Learn model
    model = shampoo.fit_transform(X, y_true, pos_label='bad')

    Save model
    status = shampoo.save(model, 'learned_model_v1')



Loading
----------------------

Loading a learned model can be done using the function :func:`shampoo.load`:

.. code:: python

    import shampoo

    # Load model
    model = shampoo.load(model, 'learned_model_v1')

