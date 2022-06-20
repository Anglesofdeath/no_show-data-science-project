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
&emsp;&emsp;&emsp; - SVM     
&emsp;&emsp; Can either choose to run 1/2/all 3 algorithms within the pipeline. The selection of algorithm to run in the pipeline is done by setting the ['Run'] parameter under each algorithm name to ['True']. If ['Run] == ['True], the pipeline will run the algorithm. If ['Run'] == ['False'] the pipeline will skip the algorithm.     
&emsp; 2. Choose whether to run Grid Search Cross Validation (Grid CV) when running the algorithm. If the ['GridCV'] parameter under each algorithm is set to ['True'], a Grid Search CV will be run to find the best hyper-parameters for the algorithm. If ['GridCV'] == ['False'], it will skip the Grid Search and run the algorithm using the hyperparameters already listed in the config file. It is by default set to ['False'] as a 2-fold Grid Search CV was already run for the hyper-parameters listed within the config file and the ideal hyper-parameters found from that run are already being used as the input. 

##### Description of logical steps/flow of Pipeline  
