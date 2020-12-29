# CIS680 Week 1/Module 1 - Introduction

Welcome to Cloud Application Development!  This module will introduce you to the basics of cloud computing.

> By the end of this module, you should understand the underlying concepts of cloud computing, be able to setup your GCP account and billing, and create and use a remote virtual machine.

> Module Video: TBD

For this course we will be using [Google Cloud Platform](https://cloud.google.com/) as our cloud provider, however others such as [Amazon Web Services (AWS)](https://aws.amazon.com/) and [Microsoft Azure](https://azure.microsoft.com/) are common as well.  While each provides their own particular flavor, understanding the basics should enable you to transition between one and the other as necessary.

Plus, assuming you are registered for the course at GVSU, you will receive free cloud computing credits (contact me on Blackboard).  If you somehow stumbled across this you can get [free credits via Google](https://cloud.google.com/free), however you're on your own with those.

## Cloud Computing Costs

The most important concept to understand about cloud computing is that it is **not** free.  Each moment a virtual machine is on, each API call, each image access in a storage bucket will cost money.  

Repeat after me:

**CLOUD COMPUTING IS NOT FREE.**

Unless if you are running a business with unlimited funds, you don't want to see charges start to accrue on your account that could be avoided.  That means:

1. Shut down your virtual machine when you are done.

Here is a screenshot of an Ubuntu 20 virtual machine with a default configuration.  Note how much it costs to run monthly.  **This is the cost for simply leaving the machine up and running**, i.e., TURN IT OFF WHEN YOU'RE DONE.

![GCP cost calculator](/CloudAppsDev/images/1-costs.png)


2. Set up stringent access rights to all your API calls, cloud functions, etc.
3. Do not publish any access keys, API ID's, passwords, etc. to version control (e.g., GitHub, BitBucket, etc.).  Keep in mind that if you *accidentally* push something identifiable that it can be **easily discovered** by checking commit history.  


## Google Cloud vs. AWS vs. Azure

> Module Video: TBD

TBD

