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

![GCP cost calculator](/CloudAppsDev/assets/images/1-costs.png)


2. Set up stringent access rights to all your API calls, cloud functions, etc.
3. Do not publish any access keys, API ID's, passwords, etc. to version control (e.g., GitHub, BitBucket, etc.).  Keep in mind that if you *accidentally* push something identifiable that it can be **easily discovered** by checking commit history.  


## Google Cloud vs. AWS vs. Azure

> Module Video: TBD

There are several players in the game (i.e., the battle for cloud dominance) as of this point, however the big three are Google, Microsoft, and Amazon.  Whichever you end up using is more than likely going to come down to enumerating a list of tradeoffs, business decisions, and personal preferences.  

As of now (December 2020), AWS owns an astonishing 62% of the cloud market, with Microsoft (Azure) coming in at 20% and Google (GCP) with 12%.  

> *Source: [https://medium.com/weekly-webtips/google-cloud-vs-aws-vs-azure-bafb554e036](https://medium.com/weekly-webtips/google-cloud-vs-aws-vs-azure-bafb554e036)*

Really, there isn't one "good" answer for which you should pick.  We'll now list out some considerations for you to ponder.

### Cloud Provider Considerations

![Gartner Report - Cloud Market Share](/CloudAppsDev/assets/images/Cloud-Gartner-report.png)

Considerations consistently change with respect to cloud providers.  Here, I am going to very briefly summarize some of the pros and cons for the big three providers with a massive caveat that these points can and will change.  

> *Source: [https://www.datamation.com/cloud-computing/aws-vs-azure-vs-google-cloud-comparison.html](https://www.datamation.com/cloud-computing/aws-vs-azure-vs-google-cloud-comparison.html)*

**Amazon Web Services**

* Pros:
  - Existing dominance in market
  - Mature and enterprise-ready
  
* Cons:
  - Can have a higher cost than competitors

**Microsoft Azure**

* Pros:
  - Pre-existing familiarity with Microsoft products (e.g., Windows Server, Sharepoint, Active Directory, etc.)
  - Tightly-coupled with Microsoft ecosystem

* Cons:
  - Issues with enterprise-readiness
  - Technical support problems

**Google Cloud**

* Pros:
  - Success with containers/orchestration
  - Prominent in research-oriented areas (e.g., machine learning, big data analysis)
  - Massive scale
  - *Works well with education (cough cough)*
* Cons:
  - Tend to be a 'secondary partner' as they not as prominent in the cloud game


## Google Cloud Account Setup (Lab)

> Module Video: TBD (GCP walkthrough)

Time for your first lab assignment!  This will get you up and running with a Google Cloud account, walk you through the web interface, and have you create a web server.  

**Ensure you download the lab manual from Blackboard!**

Click here for your first lab [CIS680 Lab 1 - Intro. to Google Cloud](https://efredericks.github.io/CloudAppsDev/codelabs/CIS680-Lab1-Setup)
