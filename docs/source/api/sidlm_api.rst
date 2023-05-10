============
SIDLMNet API
============


SIDLMNetLearner Parameter Configuration
---------------------------------------------

Global
++++++

- **seed:** the random seed in model. (default=42).
- **output_folder:** This parameter control output path of the model after training, we default it to "../outputs/sidlm"

Data
++++

- **train_data:** the file path of your train data. (default=’ ../data/sidlm/train.csv’)
- **valid_data:** the file path of your valid data. (default=’ ../data/sidlm/valid.csv’)
- **test_data:** the file path of your test data. (default=’ ../data/sidlm/test.csv’)
- **wide_cols:** 
- **cont_cols:** the columns name of continuous variable in the dataset. In our study, we default it to “X_1, X_2 ‧‧‧‧‧‧X_n” but it can be flexible.
- **cate_cols:** the columns name of categorical variable in the dataset. In our study, we default it to “C_1, C_2 ‧‧‧‧‧‧C_n” but it can be flexible.
- **target_cols:** the columns name of prediction in dataset.(default=‘Y’,flexible)

Hyperparameter configuration
----------------------------

Dataloader
++++++++++

- **batch_size:** The number of data samples captured in one step training. (default=64)
- **num_workers:**  The number of process created when used dataloader. (default=4)

Model
+++++

- **d_embed:** The number of dimensions used to represent each input feature in the embedding for categorical. (default=32)
- **d_model:** The number of hidden layer nodes. (default=256)
- **n_layers:** The number of hidden layer. (default=1)
- **p_drop:** The percent of neurons are temporarily removed from the network during training. (default=0.3)
- **act_fn:** Activation function. (default=relu)
- **loss:**  The dictionary configuring the loss function for model training.
    **name:** Specifies the loss function. Can be "mse"(recommend) for Mean Squared Error or "rel" for Relative Error. If not specified or any other value,defaults to "mse".
    **a:** Used only with "rel" loss to adjust the scale of error. Multiplied with target values in error calculation. (No default)
    **b:** Used only with "rel" loss to provide a baseline for error. Added to a * targets in error calculation. (No default)
- **lr:** Learning rate. (default=3e-4)
- **weight_decay:** The value for penalizes large weights in the model during training to prevent overfitting. (default=1e-5)

Model_Callback
++++++++++++++

- **save_top_k:** Specifies the number of best models to keep based on a given metric during training on validation accuracy. (default=1, save the best)
- **monitor:** Specifies the metric to monitor during training. (default=valid_loss)
- **mode:** Specifies whether the monitored metric should be minimized (MAE) or maximized (R). (default=min)
- **verbose:** Determines whether to print information about the saving process to the console. (default=True)
- **patience:** Specifies the number of epochs to wait for improvement in the monitored metric before stopping training. (default=10)

Trainer
+++++++

- **max_epochs:** Specifies the maximum number of epochs to train for. (default=5)
- **accelerator:** Specifies the hardware accelerator to use during training. (default="gpu")
- **devices:** Specifies the number of devices to use during training. (default=1)
- **deterministic:** Ensures reproducibility of the training results. (default=True)
