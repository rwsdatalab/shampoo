Installation
################

Create environment
**********************

If desired, install ``shampoo`` from an isolated Python environment using conda:

.. code-block:: python

    conda create -n env_shampoo python=3.8
    conda activate env_shampoo


Pypi
**********************

.. code-block:: console

    # Install from Pypi:
    pip install shampoo

    # Force update to latest version
    pip install -U shampoo


Github source
************************************

.. code-block:: console

    # Install directly from github
    pip install git+https://github.com/rwsdatalab/shampoo


Uninstalling
################

Remove environment
**********************

.. code-block:: console

   # List all the active environments. shampoo should be listed.
   conda env list

   # Remove the shampoo environment
   conda env remove --name shampoo

   # List all the active environments. shampoo should be absent.
   conda env list


Remove installation
**********************

Note that the removal of the environment will also remove the ``shampoo`` installation.

.. code-block:: console

    # Install from Pypi:
    pip uninstall shampoo



