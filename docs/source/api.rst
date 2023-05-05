=============
API reference
=============

Parameter Configuration
-----------------------

After you finished the installation of the model, you will see the following main folder in the project(esidlm, examples, outputs). All of the codes are encapsulated in the esidlm folder and we do not recommend you change the code in this folder. 

In the examples folder, we uploaded a small part of train/valid/test data and the “SOPiNet.ipynb” file in this folder is showed how to used esidlm module as an instance. You only need to change some simple parameter configurations and run each cells in the jupyter notebook by order to get your own model. To simplify use, we have consolidated all configurations into a dictionary variable `SOPINET_TRAINING_CONFIG`. Then we will briefly explain what you need to modified in your local.

Basic Parameter Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Global
++++++

- **seed:** the random seed in model. (default=42).
- **output_folder:** This parameter control output path of the model after training, we default it to "../outputs/sopinet"

Data
+++++

- **train_data:** the file path of your train data. (default=’ ../data/sopinet/train.csv’)
- **valid_data:** the file path of your valid data. (default=’ ../data/sopinet/valid.csv’)
- **test_data:** the file path of your test data. (default=’ ../data/sopinet/test.csv’)
- **cont_cols:** the columns name of continuous variable in the train data. In our study, we default it to “X_1, X_2 ‧‧‧‧‧‧X_n” but it can be flexible. 
- **cate_cols:** the columns name of categorical variable in the train data. In our study, we default it to “C_1, C_2 ‧‧‧‧‧‧C_n” but it can be flexible. 
- **time_cols:** the columns of time series variable in the train data. Compare to cont_cols, we processed them into transformer frame. Noticed that each different time period in the time series needs to be in the list independently. For example, If you have three days of time series data of meteorological data (RH,WS,PS). The time_cols should be the format as follow:

```python
time_cols = {
   [RH_1, WS_1, PS_1],
   [RH_2, WS_2, PS_2],
   [RH_3, WS_3, PS_3],
} 
```

- **target_cols:** the columns name of prediction in train data. Due to the ability of simultaneous inversion, it should be set two predictions name. In our study, we default it to “Y_1, Y_2” but it also can be flexible.
- **mask_cols:** the columns name of you want to masked in targets value. The masked value will not participate in the calculation of the loss function. In our study, we masked the in-situ measurement which are missing. Note that code used 0 or 1 to determine whether the value mask or not.(1 = keep, 0 = mask) and the order should be same with target_cols.


Hyperparameter configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dataloader
++++++++++

- `batch_size`: The number of data samples captured in one step training. (default=64)
- `num_workers`: The number of process created when used dataloader. (default=4)

Model
++++++

- **d_embed**: The number of dimensions used to represent each input feature in the embedding for categorical. (default=32)
- **d_model**: The number of hidden layer nodes. (default=256)
- **n_layers**: The number of hidden layer. (default=1)
- **n_head**: The number of attention heads used in the multi-head attention mechanism. (default=4)
- **p_drop**: The percent of neurons are temporarily removed from the network during training. (default=0.3)
- **act_fn**: Activation function. (default=relu)
- **lr**: Learning rate. (default=3e-4)
- **weight_decay**: The value for penalizes large weights in the model during training to prevent overfitting. (default=1e-5)

Model_Callback
++++++++++++++

- **save_top_k**: Specifies the number of best models to keep based on a given metric during training on validation accuracy. (default=1, save the best)
- **monitor**: Specifies the metric to monitor during training. (default=valid_loss)
- **mode**: Specifies whether the monitored metric should be minimized (MAE) or maximized (R). (default=min)
- **verbose**: Determines whether to print information about the saving process to the console. (default=True)
- **patience**: Specifies the number of epochs to wait for improvement in the monitored metric before stopping training. (default=10)

Trainer
+++++++

- **max_epochs**: Specifies the maximum number of epochs to train for. (default=5)
- **accelerator**: Specifies the hardware accelerator to use during training. (default="gpu")
- **devices**: Specifies the number of devices to use during training. (default=1)
- **deterministic**: Ensures reproducibility of the training results. (default=True)
