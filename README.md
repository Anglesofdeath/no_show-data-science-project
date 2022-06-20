### AIAP11 Assessment 2 Submission   
Name: Joshua Ashwin Thomas;  Email: joshua_thomas@live.com   

##### Overview of folders      
&emsp; 1. **.github folder** (provided by AIAP)   
&emsp; 2. **src folder**    
&emsp;&emsp; - **Conf folder** (contains config.yaml file)   
&emsp;&emsp;&emsp; - **config.yaml** (contains the configurable settings for the machine learning pipeline)    
&emsp;&emsp; - __init__.py    
&emsp;&emsp; - **cleaning_engineering_functions.py** (this folder contains the various functions that are used during DataCleaning and feature Engineering)   
&emsp;&emsp; - **data_processing.py** (this file contains 2 classes. The first one: DataProcessing is where the db is downloaded from the link provided. The second one: DataCleaning is where the data is cleaned and new features are engineered based on EDA)   
&emsp;&emsp; - **model.py** (this file contains the functions where our 3 Ml models are defined)   
&emsp; 3. **eda.ipynb** (this file contains the EDA done on the dataset)   
&emsp; 4. **main.py** (this file is the main file which executes all the modules above. Is run by the run.sh file)   
&emsp; 5. **README.md** (this file)    
&emsp; 6. **requirements.txt** list of python modules required    
&emsp; 7. **run.sh** executable file   

##### Instructions for executing pipeline: 
The pipeline can be executed by either running the executable **run.sh** file or by just running the **main.py** file directly. I have set up the pipeline such that certain parameters are able to be edited within the **config.yaml** file. We are able to:    
&emsp; 1. Choose which algorithms to run:   
&emsp;&emsp; Choice of 3 algorithms:    
&emsp;&emsp;&emsp; - Random Forest Classifier   
&emsp;&emsp;&emsp; - Logistic Regression   
&emsp;&emsp;&emsp; - KNN classifier     
&emsp;&emsp; Can either choose to run 1/2/all 3 algorithms within the pipeline. The selection of algorithm to run in the pipeline is done by setting the ['Run'] parameter under each algorithm name to ['True']. If ['Run] == ['True], the pipeline will run the algorithm. If ['Run'] == ['False'] the pipeline will skip the algorithm.     
&emsp; 2. Choose whether to run Grid Search Cross Validation (Grid CV) when running the algorithm. If the ['GridCV'] parameter under each algorithm is set to ['True'], a Grid Search CV will be run to find the best hyper-parameters for the algorithm. If ['GridCV'] == ['False'], it will skip the Grid Search and run the algorithm using the hyperparameters already listed in the config file. It is by default set to ['False'] as a 2-fold Grid Search CV was already run for the hyper-parameters listed within the config file and the ideal hyper-parameters found from that run are already being used as the input. 

##### Description of logical steps/flow of Pipeline  
The pipeline works by executing the run.sh file. This will then run the main.py file. This will then start the running of the pipeline.   
&emsp; 1. Download the data from the url provided in the assessment doc provided. If db already exists then delete db and download and extract out all columns from the table.   
&emsp; 2. Clean the data as was described in the EDA and create new feature: booked_months_before   
&emsp; 3. The main.py file will then run all 3 functions that run the different ML algorithms. If the ['Run'] field in the Algorithm's class in the config file is set to False it will skip the running of the algorithm. If the ['Run'] == ['True'] and ['GridCV'] == ['False'] it will run the algorithm with the predefined hyperparameters that were chosen after performing the Grid Search CV shown in **model.py**. If ['GridCV'] == ['True'], It will run a Grid Search Cross Validation and then run the algorithm using the hyper-parameters that resulted in the highest accuracy (evaluation metric chosen). It will then log the results of the accuracy and f1 test so that the results can be seen by the user. f1 is given for user info but evaluation metric used is accuracy. 
##### Evaluation Metrics used
As there is nothing particularly worrying about having a false positive or false negative (as this is a hotel no_show prediction) the evaluation metric chosen was ['accuracy']. This is because, in this situation we would want to choose the model that is the most accurate (able to label the highest percetage of no_show's correctly). The performace of all the models was:    
&emsp; Random Forest: 74.12%   
&emsp; Logistic Regression: 71.65%  
&emsp; KNN: 72.32%

##### Reason for choice of models: 
This is a binary classification so one of the best models to use for that is logistic regression. I did not standardise as I did not think it was necessary for this particular problem as all features used were either ordinal or nominal.    
I chose Random Forest classifier because we have a large dataset and interpretability of the results is not a big deal as we are simply trying to predict if a customer is a no-show or show. Hence, its useful in this scenario.    
I chose KNN because it is useful for classifying in this scenario as there really isn't a lot of correlation between a lot of the categorical data and the target (shown in EDA). Therefore, i thought KNN might be useful in this scenario. 

##### Key findings from EDA: 
The main takeaway is that none of the features on their own is well correlated with the target. We also found out that of the features chosen for the modelling there was minimal correlation between them (mostly used pie charts to see this). In my opinon, branch was one of the best features to use for predicting in this model. 