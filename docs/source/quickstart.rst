==========
Quickstart
==========

Example Data Link: `https://zenodo.org/record/7815394 <https://zenodo.org/record/7815394>`_

1. Data preprocessing
----------------------

The data used for SOPiNet have two parts. The first part is the labeled data for modeling and they should be in .csv format and be named after train.csv, valid.csv and test.csv for training, validation and testing data, respectively. The second part is the unlabeled data for retrieval PM2.5 and Ozone of full image, which can be any name in .csv format and usually named by its date The format in each .csv should be as follows. To make the structure of data clearer, we set the continuous variables start with X_* and * should be in the sequence of number. The categorical variables should start with C_* and * should also be in the sequence of number. For the labeled data, it should be contain both PM2.5 and Ozone in-situ measurement for training and we default it with Y_1 and Y_2. In addition, to utilize more training samples, we used mask columns to deal with the absence of observations at those sites. The main structure of data is as follow:

.. image:: ../images/sopinet-tutorial-4.png
   :alt: sopinet-tutorial-4.png
   :align: center

2. Parameter Configuration
--------------------------

After you finished the installation of the model, you will see the following main folder in the project(esidlm, examples, outputs). All of the codes are encapsulated in the esidlm folder and we do not recommend you change the code in this folder. In the examples folder, we uploaded a small part of train/valid/test data and the “SOPiNet.ipynb” file in this folder is showed how to used esidlm module as an instance. You only need to change some simple parameter configurations and run each cells in the jupyter notebook by order to get your own model. To simplify use, we have consolidated all configurations into a dictionary variable ``SOPINET_TRAINING_ CONFIG``. We will briefly explain what you need to modified in your local in API.

3. Training the model
----------------------

Here, we showed a complete training process using example train data. First, open the ESIDLM project and change the system path by sys (first code cell), then set your own data path and optimized parameter. After setting the parameters well, you can create a ``SOPiNetLearner`` object and call ``run_model_training`` function.

.. image:: ../images/sopinet-tutorial-5.png
   :alt: sopinet-tutorial-5.png

In this instance, we set the parameter with "batch_size": 64, "d_embed": 32,"d_model": 128,"n_layers": 1,"n_head": 4,"p_drop": 0.1. As you can see, just after 20 epoch of training (2 minute), we have achieved remarkable accuracy with 0.59 R2 of PM2.5 (Y_1) and 0.61 R2 of ozone (Y_2). Now, a full round of training model is finished, the rest need to constantly adjust the parameter and optimize the model.

.. image:: ../images/sopinet-tutorial-6.jpg
   :alt: sopinet-tutorial-6.jpg

It should be emphasized that both each training of the model and Hyperparameter file are saved in the output folder (default=’ /.. /outputs/sopinet’).

4. Using model Inference
------------------------

After determining the best optimal model, we will use this model for inference. It is also should used the dictionary named `SOPINET_ INFERENCE_CONFIG` to which is mostly similar to the training model. As follow, you should set the input and output folder in which the input data should be unlabeled. Then set the optimal model path and run the inference function.

.. image:: ../images/sopinet-tutorial-7.jpg
   :alt: sopinet-tutorial-7.jpg
