> By the end of this module, you will gain experience with server-less technologies, understand how to create and access them, perform authentication, and logging.

> Module videos:
> * Core concepts
> * Cloud Functions Codelab Demo 

## Cloud Functions

A Cloud Function, or more generically, a *server-less* function, effectively is just a function call you make to a remote server.  The nifty thing here is that you don't have to worry about the whole pesky *setting up a machine to run that function* type of concern.  You simply reference an API endpoint of some sort (e.g., an HTTP call, a RESTful call, a pub/sub trigger, etc.) and then receive data.

The following screenshot shows the list of *currently available* triggers for a Cloud Function.  Note that some are in beta, meaning they are not necessarily ready for prime time yet.

![Cloud Function triggers](/CloudAppsDev/assets/images/3-cf-triggers.png)

We will be mainly using HTTP for this section.  


### What are they?

### How can we use them?

## Accessing

Cloud functions

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
