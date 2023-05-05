============
Installation
============

All of our source codes are tested in python 3.9/3.10 for both Win10 /11 and Ubuntu 20.04. You can used git clone to capture our code or directly download the zip file from our GitHub project page. Here we show the two approaches respectively with vscode.

1. Clone the code
~~~~~~~~~~~~~~~~~~

- **Installation method 1**  
  Open the vscode and create a new folder, then you can clone the GitHub repository by the follow command:

  .. code-block:: bash

      git clone https://github.com/RegiusQuant/ESIDLM.git

  ![image](../images/sopinet-tutorial-1.png)

- **Installation method 2**  
  Download the zip file to your local at our project homepage (`https://github.com/RegiusQuant/ESIDLM <https://github.com/RegiusQuant/ESIDLM>`_) and unzip to the folder where you want.

  ![image](../images/sopinet-tutorial-2.jpg)

2. Build the required environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have listed all of the required packages of our model in *environment.yaml* file. You can try to configure in your existing environment one by one or create a new environment automatically by conda (recommend). Here we showed the second approach in our guide.

- **Setting environment method 1**  
  Enter to the created folder firstly and used the follow code to build the required python packages (It is worth highlighting that you should have the conda software before). You can also set the name of your environment by replace *myenv*.

  .. code-block:: bash

      conda env create -f environment.yaml --name myenv

- **Setting environment method 2**  
  Additionally, Mamba-forge install are also recommend in our tutorials. It will helps to speed up installation and improve installation stability. You should used the follow command to install mamba.

  .. code-block:: bash

      conda install mamba -n base -c conda-forge

  Then, the installation command is the same as conda, just replace conda with mamba, as shown below:

  .. code-block:: bash

      mamba env create -f environment.yaml --name myenv

When the environment is established well, you will see the following figure.

.. figure:: ../images/sopinet-tutorial-3.png
   :alt: sopinet tutorial 3.png
   :align: center

   sopinet tutorial 3.png
