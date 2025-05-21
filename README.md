# DatasetPreparation
This is the repository to create datasets for fine-tuning models and instructions for model testing. It is a part of the master thesis "Evaluation and Adaptation of Large Language Models for Question-Answering on Legislation" made in University of Latvia.

### Data used
The base data used is available here: http://hdl.handle.net/20.500.12574/130. You need to be able to sign in to download and use this dataset.

### Python and packages
This script was used with Python 3.10 so it is recomended to use this version of python. You also need to install PyQuery and bs4 packages.

### How to get instructions for testing
1) Put the test data in data folder
2) Run GetModelTestInstructions.py script
3) The instructions will be saved in instructions folder

These instructions are used to generate responses for models to test them. The link to response generation repository is here: https://github.com/artiks12/ResponseGeneration 

### How to prepare datasets for fine-tuning
1) Put the training and validation data in data folder. Make sure to create folders "Training" and "Validation" in data folder and store the necessary files there.
2) Run PrepareDatasets.py script
3) The datasets will be stored in datasets folder

These datasets are uused in model fine-tuning process. The link to model fine-tuning repository is here: https://github.com/artiks12/ModelFineTuningPipeline 

### Version 2
There are two problems with the GetmodelTestInstructions.py script
- It does not filter out duplicates
- It might crash if the link is incorrect or the HTML DOM is not made properly.

To prevent these issues use GetModelTestInstructions_v2.py script. The original was used for the thesis.
