> By the end of this module, you will gain experience with serverless technologies, understand how to create and access them, perform authentication, and logging.

> Module videos:
> * Core concepts
> * Cloud Functions Codelab Demo 

>**Note -- interchangeable terms!**
>
>A *serverless* function is the generic activity we're discussing here, and each provider has their own proprietary name for this:  
>
>* Google: Cloud Functions
>* AWS: Lambda functions
>* Microsoft Azure: Azure Functions

## Cloud Functions

A Cloud Function (Google-branded), or more generically, a *serverless* function, effectively is just a function call you make to a remote server.  The nifty thing here is that you don't have to worry about the whole pesky *setting up a machine to run that function* type of concern.  You simply reference an API endpoint of some sort (e.g., an HTTP call, a RESTful call, a pub/sub trigger, etc.) and then receive data.

[A Google Intro to Cloud Functions](https://youtu.be/1r3vMYywNLk)

The following screenshot shows the list of *currently available* triggers for a Cloud Function.  Note that some are in beta, meaning they are not necessarily ready for prime time yet.

![Cloud Function triggers](/CloudAppsDev/assets/images/3-cf-triggers.png "Cloud Function triggers")

We will be mainly using HTTP for this section.  

### What are they?

Serverless functions, or *Functions as a Service* (FaaS), are effectively some sort of executable code that can run without you ever needing to worry about the underlying infrastructure.  Essentially, you set up a **thing** to execute and you don't care about the server hosting it.  You simply trigger the function and see what data comes back.

Here is an example (from Microsoft's Azure Functions):

![Azure Functions](https://docs.microsoft.com/en-us/dotnet/architecture/serverless/media/cqrs-example.png)

The lightning bolt represents the serverless function in this example.  Here are the general steps:

1. Something triggers a serverless function (we'll talk about *how* soon)
2. The cloud provider receives the input from the client (`query` or `command` from the image) and then processes it, sending the output to wherever the function directs it.
   * Keep in mind that what is happening behind the scenes is still occurring on a server - meaning that the cloud provider is most likely spinning up a transient virtual machine (or similar) to care for your request.
3. Function done!  

Let's take a look at the key benefits published by Google and Amazon, respectively:

**Google** (c/o [Google Cloud Functions](https://cloud.google.com/functions/))

* No servers to provision, manage, or upgrade
* Automatically scale based on the load
* Integrated monitoring, logging, and debugging capability
* Built-in security at role and per function level based on the principle of least privilege
* Key networking capabilities for hybrid and multi-cloud scenarios

**AWS** (c/o [AWS Lambda Functions](https://aws.amazon.com/lambda/))

* No servers to manage
* Continuous scaling
* Cost optimized with millisecond metering
* Consistent performance at any scale

Sounds pretty good, right?  Let's pull apart what is being offered.

**(Lack of) Server Management**

To me, this is the **number one** reason that serverless functions exist.  You as the developer (or software engineer, business manager, etc.) have no concern whatsoever for the server infrastructure, meaning that you don't have to setup and configure a new environment to process incoming requests.  You no longer have to worry about maintaining a virtual machine or setting up a physical server, including common concerns like keeping it up to date, managing it, etc.

With serverless functions we still need to configure and monitor them, however this is not nearly as involved as managing a real machine.

> Each cloud provider (naturally) has their own method for configuring and securing serverless functions, so be aware that the demos we're looking at here will need to be tweaked for whichever provider you use.  The concepts are transferrable, however.

**Scaling**

Scaling is one of the other key benefits of using the cloud (and most likely why you're considering the cloud anyway).  In line with not having to worry about the server backend, you also don't need to worry about scalability from a technological perspective.

**You'll pay for scalability, naturally**.  You just won't have to worry about such pesky things like server scalability.

Since the backend is relatively flexible, your cloud provider only needs to spin up as many resources as necessary.  If you are only being hit with 10 requests, then you don't need a massive virtual machine to handle it.  Likewise if you're in the millions of requests per minute range, more than likely a load-balanced infrastructure will be seamlessly created.

You don't see any of that though!  You just see a bill for resources consumed.

**Monitoring/Metering**

I'm going to lump these two together as they both consider "keeping an eye" on the serverless function.  Regardless if it is performance or cost-related, you do need to watch these.  

We'll come back to performance later, however the usual considerations for performance apply here: memory overhead, run time, etc.  We have logging tools available that can help us easily profile what is going wrong with our functions.

In terms of cost monitoring, AWS actually provides a lovely example of a cost calculation ([AWS pricing](https://aws.amazon.com/lambda/pricing/)) (note, I **strongly recommend** you take advantage of cost calculators whenever you intend to deploy anything cloud related!):

> If you allocated 512MB of memory to your function, executed it 3 million times in one month, and it ran for 1 second each time, your charges would be calculated as follows:
>
> **Monthly compute charges**
>
> The monthly compute price is $0.00001667 per GB-s and the free tier provides 400,000 GB-s.
>
> `Total compute (seconds) = 3M * (1s) = 3,000,000 seconds`
>
> `Total compute (GB-s) = 3,000,000 * 512MB/1024 = 1,500,000 GB-s`
>
> `Total compute – Free tier compute = Monthly billable compute GB- s`
>
> `1,500,000 GB-s – 400,000 free tier GB-s = 1,100,000 GB-s`
>
> `Monthly compute charges = 1,100,000 * $0.00001667 = $18.34`
>
> **Monthly request charges**
>
> The monthly request price is $0.20 per 1 million requests and the free tier provides 1M requests per month.
> Total requests – Free tier requests = Monthly billable requests
>
> 3M requests – 1M free tier requests = 2M Monthly billable requests
>
> `Monthly request charges = 2M * $0.2/M = $0.40`
>
> **Total monthly charges**
>
> Total charges = Compute charges + Request charges = $18.34 + $0.40 = **$18.74 per month**

Considerations for creating and using serverless functions:

1. How many you plan to invoke per billing cycle
2. How *long* your function will take to execute
3. How much memory your function will consume
4. How will you access it?
5. What language would you prefer to use?

Consider these points when setting up a function.  Points 1-3 tend to focus more on the billing side of things, however 4 and 5 are more related to the technologies.   The big three (Google, AWS, Microsoft) support multiple languages, so be sure to check that the language you intend to use is supported.

For instance, Python and Node.js are supported by all, but Microsoft also supports C# and F#.

### How can we use them?

The big question.  Why would you even bother to use them?  I've pulled a few examples from [Google Cloud's list](https://cloud.google.com/functions/#section-5), I suggest you take a look at them as well.

**Example 1 - A Simple Website (HTTP Endpoint)**

The default "Hello World" of serverless, and you get it for free when setting up a new Google Cloud Function.  Simply visit the `trigger URL` in any browser and you are rewarded with Hello World.

![Hello world CF](/CloudAppsDev/assets/images/3-cf-hello-world.png "Hello World CF")

(You'll do this as part of your lab at the bottom of this post).

**Example 2 - Execute a Slack Slash Command**

Perhaps you want to up your Slack game and make your chats come to life.  This one uses a customized Slack command to search the Knowledge Graph API (i.e., search for information) via a Cloud Function.

The tutorial is [here if you're interested](https://cloud.google.com/functions/docs/tutorials/slack), but the gist is that a custom Slack command triggers the Cloud Function and sends the search query as its payload.  The Cloud Function then reaches out to the Knowledge Graph with the query and returns the results back to Slack.  The following image demonstrates this activity:

<img src="https://cloud.google.com/functions/img/gcf-slack.svg" alt="Slack to CF to Knowledge Grpah" title="Slack to CF to Knowledge Graph" style="background-color: white" />

**Example 3 - Perform Optical Character Recognition**

## What about those *other* serverless functions?

Serverless is not strictly limited to running small functions anymore (though that was how it got started).  Serverless databases are becoming popular, for one (e.g. Google Cloud Data Store, MongoDB, DynamoDB, etc.).  The concept is similar to functions - you don't have to worry about maintaining a server.

We're not strictly going to cover that in this module, but be aware that it exists!

For more information: [Serverless Databases](https://dashbird.io/blog/what-is-serverless-database/)

## Accessing


## Authentication

## Logging

## Lab - Cloud Functions (Advanced)

This codelab is going to do two things.  First, you will spin up a Cloud Function and get it up and running, learn how to access it, etc.  This part is not strictly a difficult concept and the typical `Hello World` function is beneath you. 

However, let's add on an exceedingly important component to any cloud app developer: *logging*.

Here we're going to work through Stackdriver logging and trace, two components of Google Cloud that will really help you understand what is happening with your cloud functions.  

### Lab Instructions

Download the appropriate lab manual from Blackboard and keep it open while you work through the Codelab.  I'll be asking for screenshots from your progress.  

The following link will take you to a Google-created Codelab.  

[Google CodeLab -- Stackdriver Logging and Stackdriver Trace for Cloud Functions](https://codelabs.developers.google.com/codelabs/cloud-function-logs-traces)

> 

## Additional Resources

* [AWS Lambda Functions](https://aws.amazon.com/lambda/)
* [Google Cloud Functions](https://cloud.google.com/functions/)
* [Microsoft Azure Serverless Functions Overview](https://docs.microsoft.com/en-us/azure/architecture/serverless-quest/serverless-overview)
* [SnipCart - A Serverless Function Example: Why & How to Get Started](https://snipcart.com/blog/why-serverless-example)
* [HubSpot - Serverless Functions](https://developers.hubspot.com/docs/cms/features/serverless-functions)
