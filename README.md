# adversarial-ai-book
This repository contains the code and material used in the Adversarial AI book. It's organized by chapter. See the book for more details. 

In each chapter directory you youill find the requirements.txt for the dependencies you will need to install using `pip install -r requirements.txt`

We recommend that you use environments  usiing venv as we describe in chapter 2. For GPU environments you may need to use conda if you encounter CUDA and NVIDIA driver misconfigurations. 

We have included trained models as in some cases (especially chapter 2 and 11) it may take too long to train if you don't have a decent NVICAI GPU environment.

In ch2 we have also provided under the subfolder aws scripts to setup cheap SageMaker notebook instances with an EFS volume and scripts to start and stop without loosing your data between sessions. These instances cost $1-$2 hour but please be cafeful; if you leave them running you may accumalate high and unecxpected costs. We recommend that you set billing alerts, if you use AWS, to avoid unpleasant surprises.

In chapter 12 we use many third party repositories. We have cached them in the root folder of this repository to make it easier for you and we have introduced some fixes or helper utilities for some of them, as described in the book. 

Before you start using the repository we recommend you read chapter 2 of the book. We hope you find the code useful in your learning journey and please report any issues.








