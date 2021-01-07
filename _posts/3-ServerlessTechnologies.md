> By the end of this module, you will gain experience with serverless technologies, understand how to create and access them, perform authentication, and logging.

> Module videos:
> * Core concepts
> * Cloud Functions Codelab Demo 

## Cloud Functions

A Cloud Function, or more generically, a *serverless* function, effectively is just a function call you make to a remote server.  The nifty thing here is that you don't have to worry about the whole pesky *setting up a machine to run that function* type of concern.  You simply reference an API endpoint of some sort (e.g., an HTTP call, a RESTful call, a pub/sub trigger, etc.) and then receive data.

The following screenshot shows the list of *currently available* triggers for a Cloud Function.  Note that some are in beta, meaning they are not necessarily ready for prime time yet.

![Cloud Function triggers](/CloudAppsDev/assets/images/3-cf-triggers.png)

We will be mainly using HTTP for this section.  

### What are they?

Serverless functions, or *Functions as a Service* (FaaS), G

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

Sounds prettty good, right?  Let's pull apart what is being offered.

**(Lack of) Server Management**

**Scaling**

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

## What about those *other* serverless functions?

Serverless is not strictly limited to running small functions anymore (though that was how it got started).  Serverless databases are becoming popular, for one (e.g. Google Cloud Data Store).  The concept is similar to functions - you don't have to worry about maintaining a server.

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
