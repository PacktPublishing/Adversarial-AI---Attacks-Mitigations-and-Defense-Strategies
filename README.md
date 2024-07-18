# Adversarial AI Attacks, Mitigations, and Defense Strategies
<a href="https://www.packtpub.com/en-us/product/adversarial-ai-attacks-mitigations-and-defense-strategies-9781835087985?utm_source=github&utm_medium=repository&utm_campaign=9781801076012"><img src="https://content.packt.com/B21235/cover_image_small.jpg" alt="Adversarial AI Attacks, Mitigations, and Defense Strategies" height="256px" align="right"></a>

This is the code repository for [Adversarial AI Attacks, Mitigations, and Defense Strategies](https://www.packtpub.com/en-us/product/adversarial-ai-attacks-mitigations-and-defense-strategies-9781835087985?utm_source=github&utm_medium=repository&utm_campaign=9781801076012), published by Packt.

**A cybersecurity professional's guide to AI attacks, threat modeling, and securing AI with MLSecOps**

## What is this book about?
* This book covers the following exciting features:
* Understand poisoning, evasion, and privacy attacks and how to mitigate them
* Discover how GANs can be used for attacks and deepfakes
* Explore how LLMs change security, prompt injections, and data exposure
* Master techniques to poison LLMs with RAG, embeddings, and fine-tuning
* Explore supply-chain threats and the challenges of open-access LLMs
* Implement MLSecOps with CIs, MLOps, and SBOMs

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1835087981) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example,

The code will look like the following:
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.2, random_state=42)
```

**Following is what you need for this book:**
This book tackles AI security from both angles - offense and defense. AI builders (developers and engineers) will learn how to create secure systems, while cybersecurity professionals, such as security architects, analysts, engineers, ethical hackers, penetration testers, and incident responders will discover methods to combat threats and mitigate risks posed by attackers. The book also provides a secure-by-design approach for leaders to build AI with security in mind. To get the most out of this book, you'll need a basic understanding of security, ML concepts, and Python.

With the following software and hardware list you can run all code files present in the book (Chapter 1-19).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-19 | Python 3.x, TensorFlow 2.x with Keras | Windows, Mac OS X, and Linux (Any) |
| 1-19 | OpenAI and Hugging Face APIs | Windows, Mac OS X, and Linux (Any) |
| 1-19 | LangChain | Windows, Mac OS X, and Linux (Any) |
| 1-19 | Docker | Windows, Mac OS X, and Linux (Any) |


### Related products
* A CISO Guide to Cyber Resilience [[Packt]](https://www.packtpub.com/en-in/product/a-ciso-guide-to-cyber-resilience-9781835466926?utm_source=github&utm_medium=repository&utm_campaign=9781801073240) [[Amazon]](https://www.amazon.com/dp/1835466923)

* Cybersecurity Architect's Handbook [[Packt]](https://www.packtpub.com/en-in/product/cybersecurity-architects-handbook-9781803235844?utm_source=github&utm_medium=repository&utm_campaign=9781800568754) [[Amazon]](https://www.amazon.com/dp/1803235845)

## Get to Know the Author
**John Sotiropoulos**
is a senior security architect at Kainos where he is responsible for AI security and works to secure national-scale systems in government, regulators, and healthcare. John has gained extensive experience in building and securing systems in roles such as developer, CTO, VP of engineering, and chief architect.
A co-lead of the OWASP Top 10 for Large Language Model (LLM) Applications and a core member of the AI Exchange, John leads standards alignment for both projects with other standards organizations and national cybersecurity agencies. He is the OWASP lead at the US AI Safety Institute Consortium.
An avid geek and marathon runner, he is passionate about enabling builders and defenders to create a safer future.


## Basic Setup Guide
This repository contains the code and material used in the Adversarial AI book. It's organized by chapter. See the book for more details. 

In each chapter directory you youill find the requirements.txt for the dependencies you will need to install using `pip install -r requirements.txt`

We recommend that you use environments  usiing venv as we describe in chapter 2. For GPU environments you may need to use conda if you encounter CUDA and NVIDIA driver misconfigurations. 

We have included trained models as in some cases (especially chapter 2 and 11) it may take too long to train if you don't have a decent NVICAI GPU environment.

In ch2 we have also provided under the subfolder aws scripts to setup cheap SageMaker notebook instances with an EFS volume and scripts to start and stop without loosing your data between sessions. These instances cost $1-$2 hour but please be cafeful; if you leave them running you may accumalate high and unecxpected costs. We recommend that you set billing alerts, if you use AWS, to avoid unpleasant surprises.

In chapter 12 we use many third party repositories. We have cached them in the root folder of this repository to make it easier for you and we have introduced some fixes or helper utilities for some of them, as described in the book. 

Before you start using the repository we recommend you read chapter 2 of the book. We hope you find the code useful in your learning journey and please report any issues.

### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781835087985">https://packt.link/free-ebook/9781835087985 </a> </p>
