> By the end of this module, you will learn how to start designing cloud applciations and gain experience with microservices (via Google Cloud App Engine).

> Module videos:
> * Core concepts
> * Microservices
> * Introduction to App Engine

## Cloud Applications

Let's start thinking about how we can take our applications, no matter what type we need, and transition them to the cloud.  Your first question should really be "do we need the cloud?"  If you are designing an application in the cloud just because it is trendy, then there is a good chance you don't actually *need* the cloud.

However, if you do need cloud resources (e.g., scalability, uptime, network-based delivery) then you're exactly where you need to be.

I will link this again at the bottom, but this article is a pretty good read for considerations you'll need to keep in mind when designing an application for the cloud - [Google Cloud - 5 Principles for Cloud-Native Architecture](https://cloud.google.com/blog/products/application-development/5-principles-for-cloud-native-architecture-what-it-is-and-how-to-master-it).  I'll be mainly distilling this article here (plus some of the others I've linked).

> *We'll be getting to concepts such as containers a Cloud Run later on, for now we'll focus on what we need to design for the cloud*.

Depending on which article you read, there are multiple considerations you'll have for transitioning your applications to the cloud.  I'd recommend checking out the linked resources at the bottom to get different perspectives as well.  But, this is a class and you need well-synthesized information so here we go!

### 1. Understand your Needs

This should come as no surprise, but before you start writing code you need to at least have a basis for what you plan to do.  Like any good software project, you can't just jump into it expecting success.  Your strategies need to be well-planned.  Consider the "standard" software engineering processes, from waterfall to agile.  They all have *some* sort of firm basis for designing artifacts, requirements, use cases, user stories, etc.  Do the same thing here!  

Let's take a hypothetical example:

> I need an application and it needs to be scalable to 100,000 concurrent users.

> > Ok great!  Let's toss the processing up as a Lambda/Cloud/Azure Function and just point our user's app towards that.

> Also it needs to talk to Firebase and Firebase only.

> > O...ok great!  We'll do Firebase and Cloud Functions to stay in the same ecosystem.

> Yea sounds good!

> > > 10 months later...

> Also I need the performance logs for the past 10 months as well as now it should be containerized.

> > WHY DIDN'T YOU TELL ME THAT 10 MONTHS AGO.  

Ok, existential crises aside, planning out your cloud strategy early on can help you identify:

1. Which technologies are required (i.e., what APIs do you plan to pay for)

2. Which ecosystem(s) you plan to use (i.e., do you want to pay both Microsoft and Amazon or just one?  Are there discounts available for staying internal to one as well?)

3. Minimize tear-ups for a cloud strategy (i.e., don't redesign the whole thing from scratch because somebody got a new "idea").

The points above should sound *exceedingly* similar to what you'd hear in a Software Engineering / Systems Analysis class.  Your standard concepts of the software engineering and design process apply to the cloud as well.

The takeway here is you should treat your cloud strategy as a software engineering problem.  Design requirements (both functional and non-functional), understand who your stakeholders are (e.g., customers, managers, developers, testers, etc.), have a team development strategy (e.g., Agile, V, Scrum, Waterfall, etc.), *plan things out*!  Furthermore, break your design into releases/sprints/etc. so that you can have a manageable design process!


### 2. Break your application into a *collection of services*

That monolithic `C` application that you're planning to port to the cloud?  You can't just dump it into the cloud and expect it to work as is (well, unless if you're containerizing and deploying, but that's a whole other [ball of wax](https://i.imgur.com/Jrr9zJ8.png "ball of wax")).  No, what we need to do is leverage the various *services* that the cloud offers to build our application.

Example time!  Let's cloudify a simplified ERP application.  Consider the most basic of needs/goals (hint: these should inform your requirements design...):

1. Employees should be able to log hours spent per project
2. Application must be accessible from any device at all times
3. Employee must be able to generate payroll reports 

Obviously this is a small, hamfisted example for what is a massive application.  However, they exemplify how it might look as a cloud application based around services (hint, microservices are coming into play).  We have three considerations here: data entry, data accessibility, and data reporting.  While we could create one large applicatioon fairly trivially for these considerations, we can also break them up into services and leverage the abilities of the cloud.

Let's extend this problem a bit.  Instead of a small company we're a massive company with tens of thousands of employees worldwide.  We can separate each of our considerations out into separate APIs with local instances, rather than one global instance that may present downtime or lag. We also have the nice benefit that our data can be decoupled from the application if it is broken up.  For instance, let's say we're running a virtual machine that presents an hours-logging form.  Since our company is so large it may make sense to use a big data-specific storage format (data warehousing, BigTable, graphs, etc.).  As such, we can have separate services dump data into that format and other services retrieve information.  We'll use an appropriate cloud storage technology (bucket, BigTable, etc.) for our data, a service that generates reports on the fly (BigQuery, Cloud Function running a simple `CRUD` (i.e., Change-Read-Update-Delete) query, etc.).  Each of these are *decoupled* into services, meaning that they are treated separately.  

What does decoupling do for us?  We can isolate each service and the data, enabling finer-grained control over all aspects of the application. This not only simplifies our problem, but enables other concerns such as data governance, reuse across other applications, security implications, etc.

### 3. Design your application to be automated

With decoupling comes automation.  If you have broken your application into pieces, chances are you have made an atomic object that can be automated.  I'm sure by now you've heard of all those lovely (buzzwordy at times) tools in the Continuous Integration / Continuous Development (CI/CD) pipelines.  

![CI/CD Pipeline](https://stackify.com/wp-content/uploads/2019/04/big-Feature-Image-on-What-Is-CI_CD-1280x720.jpg "CI/CD pipeline")

> Figure 1: CI/CD Pipeline (c/o Stackify.com)

CI/CD enables quicker development processes and updates.  It is definitely worth checking into as it can help with deployments, testing, rollouts, etc.  Breaking your applications into services enables them to be more easily automated. Moreover, scaling up and down can be better enabled as well, given that each service can be tweaked to your application and organization's needs at any given point in time.

One other consideration for automation is that you can incorporate both [monitoring and logging](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/) into your services.  Monitoring/logging are points we've discussed already, however consider that you can setup automated triggers to support automated recovery and health checks.  For example, you can trigger disk resizes if one is filling up, or generate automated warnings if you are consuming too many resources.  If you don't log and monitor your systems, how will you know what they are doing otherwise?

### 4. Consider the state

What is "state?"  State is the configured state of your application, the user data that has been entered, which jobs are running with which parameters, the number of instances of a Cloud Function, etc.  The main consideration here is that you should endeavor to design [*state-less* applications/services](https://cloud.google.com/solutions/best-practices-for-operating-containers#immutability).  What is state-less?  It is an object that is immutable and can run regardless of state.  Effectively, it can be automated, copied, scaled, etc., without any consideration for the data.  Figure 2 demonstrates an example of containerizing with Docker.  We'll get to containers later, but look at the figure.  The Deployments (Pods A-D) are state-less, immutable objects.  Their purpose is to accept data and execute ... nothing configurable is directly codified!  It is passed in as a parameter and then acted upon.

![Container example](https://cloud.google.com/solutions/images/bp-operating-containers-configmap.svg "Container Example")

> Figure 2: Container Example

State-less components are:

* Reusable
* Scalable
* Repairable
* Roll-back-able
* Load-balanceable

Strive for state-less!  It is the cloud's best friend.

### 5. Practice Defensive Everything

Defensive programming, defensive architecting, defensive defense.  You should, no, **must**, always consider the fact that you are developing and deploying on a publicly-accessible platform that may become an avenue of attack.  Here is your new mantra as a cloud applications architect:

**DO**

**NOT**

**TRUST**

**PERIMETER**

**SECURITY**

Don't assume Google/Microsoft/Amazon/Digital Ocean will protect your application and *its data* simply because it is inside their walled garden.  You are providing an attack surface simply by using them and putting your data out there.  It would be absolutely naive to assume that you won't be the target of an attack at some point.  Always clean your data, **never** publish API keys or configuration information, lock down unauthenticed services, and only enable services/firewall ports that are absolutely required (to name a few, there is so, so much more to do).

Also, keep in mind that revision control systems (such as git) maintain a history.  If you "accidentally" put configuration information/API keys in and then deleted them later on, the history is still there and easily accessible. 

Let me give you an example from a former class - Systems Adminstration, or the art of creating, configuring, and deploying servers.  We were deploying virtual machines on Google Cloud as part of a homework assignment.  Lo and behold, one of my students started getting nasty emails from Google saying that their account is locked, as some of their virtual machines were being used for Bitcoin mining.  The student was not doing that, however we were using insecure passwords on our virtual machines.  The machines, it turns out, were publicly accessible to anybody and an automated script picked up on that fact.  Coupled with a weak point of entry, one of the machines was coopted into Bitcoin mining.  A properly secured account (and strengthened firewall) resolved this issue.  

Let me reiterate: security becomes a massive concern for you in the cloud.  You become a prime target simply by making things easily accessible.  Make sure you treat it as such.

## Microservices

Now then, let's talk about microservices. This term has been a buzzword in industry for quite some time now, but what it really means is to simply break an application apart into smaller pieces.  Decoupling, one might say.

Sound familiar?

![Spinning Think](https://media.tenor.com/images/3a052ff1c095ffe60d03ec031a0c834f/tenor.gif "Spinning Think")

Figure 3 next shows a Microsoft-based example of a microservice architecture.  Note that, to the `Client`, there is no notion what type of application is under the proverbial hood.  The `Client` only sees the `API gateway`; it is the `gateway` that talks to the microservice architecture.  Even then, there may be another layer of abstraction with respect to the `Management/Orchestration` layer.

![Microsoft Microservice Architecture](https://docs.microsoft.com/en-us/azure/architecture/includes/images/microservices-logical.png "Microsoft Microservice Architecture")

> Figure 3: Microsoft Microservice Architecture

Note here that services can also talk to services!  Let's do a practical example using the Google App Engine.  I *highly* recommend you read through [this article to understand how App Engine works](https://cloud.google.com/appengine/docs/standard/python/microservices-on-app-engine).  What is App Engine?  It is simply a Google Cloud service that effectively breaks an application up into microservices, as shown in Figure 4:

<img src="https://cloud.google.com/appengine/docs/images/modules_hierarchy.svg" alt="Google App Engine" title="Google App Engine" style="background-color: white" />

> Figure 4: Google App Engine

You have multiple instances of services, with different versions if necessary, to support whatever target application you have.  Now, let's do another web server project, this time with App Engine instead of virtual machines.

I have a couple of videos for you walking you through the next-linked Codelab on App Engine.  It is split into two videos as it was starting to get long.  Of note I left in two mistakes that I made when walking through the demo -- to me watching how to fix problems as they arise is far more useful than cutting them out, so you get to see my process for debugging.

> Module Video - <a href="https://youtu.be/p7l_7GlFxas" target="_blank">App Engine Demo (1/2) [10:46]</a>
> Module Video - <a href="https://youtu.be/qQF93W_guXU" target="_blank">App Engine Demo (2/2) [10:58]</a>

[Google Codelab - App Engine](https://codelabs.developers.google.com/codelabs/cloud-app-engine-python3/)

(**You may note that there is ... another lab for you in Blackboard!**)

The purpose of this lab is to demonstrate how we might turn a web server into a microservice *that can be deployed and updated without touching the application itself*.  We are creating the microservice using `Flask`, a Python-based web server.  We'll also be using the cloud shell to deploy/re-deploy our microservice.  Again, the lab manual will have screenshots and extensions you'll need to follow as well!

> One thing you should keep in mind when working through this lab.  At present, [you can't delete an app once it is created in Google Cloud](https://stackoverflow.com/questions/42512/deleting-a-google-app-engine-application).  It can be disabled, however you should read the fine print to understand what is going on.

## Migrating from Monolithic to Microlithic (or at least Microservice-based)

This bullet list is directly from [Google here](https://cloud.google.com/appengine/docs/standard/python/microservice-migration), but it is a good procedure/heuristic to follow when migrating from a massive application to one that is centered around microservices:

> * Leaving the existing code in place and operational in the legacy application to facilitate rollback.
> * Creating a new code repository, or at least a sub-directory in your existing repository.
> * Copying the classes into the new location.
> * Writing a view layer that provides the HTTP API hooks and formats the response documents in the correct manner.
> * Formulating the new code as a separate application (create an app.yaml).
> * Deploying your new microservice as a service or separate project.
> * Testing the code to ensure that it is functioning correctly.
> * Migrating the data from the legacy app to the new microservice. See below for a discussion.
> * Altering your existing legacy application to use the new microservices application.
> * Deploying the altered legacy application
> * Verifying that everything works as expected and that you don't need to roll back to the legacy application.
> * Removing any dead code from the legacy application.

App Engine provides two different environments to choose from when designing your application.  It can be "standard" in that everything is fully-managed and you simply write your application.  There also is a *flexible* environment where Docker container support is available, enabling greater customization possibilities for your applications.

## Additional Resources

* [Google Cloud - 5 Principles for Cloud-Native Architecture](https://cloud.google.com/blog/products/application-development/5-principles-for-cloud-native-architecture-what-it-is-and-how-to-master-it)
* [5 Steps to Building a Cloud-Ready Application Architecture](https://www.cloudtp.com/doppler/5-steps-building-cloud-ready-application-architecture/)
* [The Ultimate 9 Step Strategy For Building Cloud Applications](https://arkenea.com/blog/building-cloud-applications/)
* [Microservices Architecture on Google App Engine](https://cloud.google.com/appengine/docs/standard/python/microservices-on-app-engine)
* [Microservice Performance Optimization](https://cloud.google.com/appengine/docs/standard/python/microservice-performance)
* [Monolithic to Microlithic](https://cloud.google.com/appengine/docs/standard/python/microservice-migration)

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.