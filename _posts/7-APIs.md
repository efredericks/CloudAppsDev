> By the end of this module, you'll gain experience with interacting with the cloud via application programming interfaces (APIs), learn a bit about managed messaging, and look at the Publish/Subscribe (PubSub) service.

> Module videos:
* [APIs / REST / Cloud Endpoints Overview [12:33]](https://youtu.be/4PXLJ1B4b-w)
* [Python / Flask RESTful calls [11:18]](https://youtu.be/YLTTi9WpVCY)
* [Pub/Sub Overview [11:45]](https://youtu.be/QcILsObM4LM)
* [Pub/Sub Demo [21:08]](https://youtu.be/UKAmZBrR300)

> Module labs:
> * [Build a simple RESTful API (see Blackboard for manual)](https://codelabs.developers.google.com/codelabs/cloud-springboot-cloudshell)
> * [Qwiklab - Cloud Endpoints: Qwik Start (GSP164) [1 credit]](https://www.qwiklabs.com/focuses/767?parent=catalog)

## Let's be RESTful

Here's a video outlining the basics:

> Module Video: [APIs / REST / Cloud Endpoints Overview [12:33]](https://youtu.be/4PXLJ1B4b-w)

[RESTful services](https://restfulapi.net/) are more than likely a phrase you've heard in the past.  If you already know what they are, wonderful, however we should talk about what they exactly are and how we can use them to interact with our cloud services.

First of all, what is it to be **RESTful**?

A RESTful (REpresentational State Transfer)-ful service follows a [standardized approach](https://www.w3.org/2001/sw/wiki/REST) for enabling interaction.  

[Wikipedia has a delightful overview of what REST means](https://en.wikipedia.org/wiki/Representational_state_transfer)!

Effectively, REST is a set of constraints that a service follows to allow other services/applications/users to use it via common HTTP requests.  Specifically, a RESTful API can be queried via `GET`, `POST`, `PUT`, and `DELETE` calls.  Given that the greater web is HTTP-based, a RESTful API provides a very familiar approach to interaction.  Another nice benefit is that REST is stateless -- nothing state-related needs to be stored/referenced to work.  You can also perform authentication/authorization with REST as well, OAuth or other token-based approaches can be used to enable security for RESTful services. 

Figure 1 shows an example of a RESTful interaction between an application and an API (c/o TowardsDataScience): 

![RESTful API](https://miro.medium.com/max/5230/1*ZU1EQ7tYeQNQlhOhyonHFA.png "RESTful API")

> Figure 1: RESTful API

Here, you can get a feel for how a RESTful call is constructed.  The URL is built as you normally would expect for accessing a website, however instead the service is accepting the URL as an instruction sequence for how to parse the request.  *Note, a RESTful call can also accomodate data payloads (e.g., via JSON packets), however we'll just focus on simple commands here*.

We will assume the protocol (`http`) and domain (`www.somewebsite.com`) are known to you at this point ... they give you a human-readable method for accessing the server that your service is hosted upon.  The `Path` noted in the figure demonstrate how the API should be handling the request -- in this example `api/v3/jobs` means *something* to the API.  The last portion of the URI is `datascience` (again, meaning *something* to the API).  It should be of note that defining the HTTP request is completely up to the API itself.  In this example, the service most likely is a website route that renders `datascience` specific information to the user.

A similar example would be querying an embedded system with a temperature sensor to get the current room temperature in your unit of choice.  For instance, I might have a Raspberry Pi outfitted with an appropriate sensor at `192.168.1.1`.  I could run a RESTful API, where I can query the device for information simply by accessing `http://192.168.1.1/getTemperature`.  The HTTP response from the device would simply be the current room temperature.  I could extend this API as well by adding a unit -- `http://192.168.1.1/getTemperature/Fahrenheit` or `http://192.168.1.1/getTemperature/Celsius`.  Again, it is up to the API to understand what this route means and how to accept or return data.  We could access the data via a web browser or via the `curl` command, as you'll see in a forthcoming lab (e.g., `curl http://192.168.1.1/getTemperature`).

Here is a [tutorial on building a RESTful API with Flask (Python) and Postman](https://www.kite.com/blog/python/flask-restful-api-tutorial/).

And here is a [simpler one](https://medium.com/@onejohi/building-a-simple-rest-api-with-python-and-flask-b404371dc699)!

> [Video on Python / Flask RESTful calls [11:18]](https://youtu.be/YLTTi9WpVCY)

Python source / requirements files:
> * [main1.py](/CloudAppsDev/assets/code/REST/main1.py)
> * [main2.py](/CloudAppsDev/assets/code/REST/main2.py)
> * [requirements.txt](/CloudAppsDev/assets/code/REST/requirements.txt)

*Variables to set and how to run*

```
$ export FLASK_ENV=development
$ export FLASK_APP=main1.py
$ python3 -m flask run

... open a browser with http://localhost:5000 to see the results.
```

> Notes: *Change main1 to main2 when going to the second example*, and your method of running Flask may be different (mine is mainly because I have several versions of Python installed on my machine)

### But was is an API?

An application programming interface (API) is a programming construct that hides the back-end details for multiple reasons.  They simplify communication from service to service, enable code reuse, and enhance portability (at minimum)!  An API enables easier interaction with a service -- you (the programmer) have no worries about what is happening behind the scenes.  All you are aware of is that you need to call particular functions to interact with some service.  

Let's take an example.  For instance, let's say that you are developing a phone application to interact with a cloud-based map service.  Your application is going to pull down restaurant addresses, phone numbers, GPS coordinates, etc. and 'prettify' them for your userbase.  However,  you don't want to index this all yourself, the cloud provider already does that.

To get this information, do you need to understand the complex inner-workings of the mapping service?  Do you need to know geographic information service (GIS) algorithms?  Absolutely not, other people/companies have done the hard work.  However, you do need to know how to handshake with those services!  Perhaps you need to follow a procedure for getting information.  It may be as simple as:

1. Authenticate your application with the service (credential flow)
2. Understand the service's API (i.e., what function calls do you need to make to get your data?)
3. Perform the necessary actions to receive data from the service.

We could use a RESTful query as previously described (perhaps your query looks like `https://maps.cloud-provider.com/getRestaurants/ZIP-CODE`) and that returns a JSON packet of all the information you need.  Or, you might need to write a script that authenticates with the service, calls something along the lines of `data = service.getRestaurants(ZIP-CODE)`, and then parse out what is in `data`.  There is not one specific way to interact with a service -- it depends on the service itself!  Let us use that lovely internet acronym of RTFM, and I'll let you look up what that means.  Basically, read the manual!

Figure 2 (c/o Google Cloud) shows a logical API that demonstrates how users interact with some service, with an API sitting in between to abstract away the details of the service itself.

![APIs hide the details and enforce contracts](/CloudAppsDev/assets/images/7-api.png "APIs hide the details and enforce contracts")

> Figure 2: APIs hide the details and enforce contracts

*What is a contract* you may ask?  Depending on the specification being followed, a *contract*  is a specific method exactly how an API functions, how to interact with it, and how to receive data from it.  [Check out this article for some of the different ways of specifying contracts](https://medium.com/theagilemanager/development-what-is-an-api-contract-683ced58e06f).

### Is there more to it than just interaction?

Oh my yes.  Figure 3 (c/o Google) shows you a high-level of the concerns we have with APIs.

![Deploying and Managing APIs can be difficult](/CloudAppsDev/assets/images/7-api-mgmt.png "Deploying and Managing APIs can be difficult")

> Figure 3: Deploying and Managing APIs can be difficult

In the context of this class, an API is simply the interface for your cloud service.  As such, we care about:

* Interface definition

How are the programmers/users going to interact with your API?  Let's say you've created a wonderful cloud service, however if users don't understand how to use it then it is not strictly useful!  Ensure your interface definition **makes logical sense**, **is well documented**, and **is well tested**!

* Authentication and authorization

Who is allowed to use your API.  You don't necessarily want to make your API fully public unless if you have unlimited funds, so you will need to ensure that the correct users are interacting with it.  As such, you must **authenticate** (i.e., ensure users are who they say they are) and **authorize** (i.e., ensure users have the correct rights/privileges to use your service).  Fortunately, cloud providers typically have methods for handling this for you.  

* Management and scalability

Will your API scale to meet user demand, both upwards and downwards?  As you are now cloud-based, consider how many users will be using it at once, as well as over time!

* Logging and monitoring

Keeping an eye on what your API is doing and how it is being used is also a major consideration.  You must have traceable evidence of exactly what your API has been doing so that you can properly manage your service and usage patterns.

Let's do a *very* simple RESTful lab to get you up and running.  Because it is fun to experience new things, let's try out Spring Boot:

> Lab: [Build a simple RESTful API (see Blackboard for manual)](https://codelabs.developers.google.com/codelabs/cloud-springboot-cloudshell)

## Cloud Endpoints

Time to look at what is available to us in the cloud!  Figure 4 (c/o Google) demonstrates Cloud Endpoints, their approach for handling cloud-based APIs.  In this figure you see what is available via Endpoints.

![Cloud Endpoints help you create and maintain APIs](/CloudAppsDev/assets/images/7-endpoints.png "Cloud Endpoints help you create and maintain APIs")

> Figure 4: Cloud Endpoints help you create and maintain APIs

Here, you see the concerns described above, fully managed.  You can generate keys for authentication/authorization, handle scalability concerns, monitor/log your API, and integrate with the various API specifications available.  Now, you can use whatever API framework/implementation that you wish, however using a service such as Endpoints can significantly speed up your development process.

> Note: AWS' version is called '[Service Endpoints](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-endpoints.html)' and Azure calls it '[API Management](https://azure.microsoft.com/en-us/services/api-management/).'

Figure 5 (c/o Google) demonstrates how they (i.e., Cloud Endpoints) fit into the general Google Cloud ecosystem.  Essentially, consider Endpoints (or similar) a cloud service for interacting with your cloud services.

![Where Cloud Endpoints fit](/CloudAppsDev/assets/images/7-endpoints2.png "Where Cloud Endpoints fit")

> Figure 5: Where Cloud Endpoints fit

Let's get some practical experience using QwikLabs.  

> [Qwiklab - Cloud Endpoints: Qwik Start (GSP164) [1 credit]](https://www.qwiklabs.com/focuses/767?parent=catalog)

## Managed Message Services and Pub/Sub

> Module video: [Pub/Sub Overview [11:45]](https://youtu.be/QcILsObM4LM)

Figure 6 (c/o Google) demonstrates how data moves from clients at the Endpoint to internal services and then back to users.  What generally happens, from a service perspective, is that data comes in, something *happens* to that data (i.e., it is transformed in some way), and then data comes out.  In the cloud world, this procedure needs to happen quickly and reliably.

![Data Ingestion](/CloudAppsDev/assets/images/7-data-mgmt.png "Data Ingestion")

> Figure 6: Data Ingestion

Consider a streaming gaming platform (publicity photo as shown in Figure 7).  There must exist a handshake between client and server, with services interspersed between along the way.  In this example (Google Stadia, though others exist), the core processing occurs on cloud servers and the game experience is transmitted to the player, leveraging high speed internet to deliver a high quality of service.

![Google Stadia Publicity (c/o Forbes/Google)](https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fkevinmurnane%2Ffiles%2F2019%2F06%2FMultiple-platforms_Stadia.jpg "Google Stadia Publicity (c/o Forbes/Google)")

> Figure 7: Google Stadia Publicity (c/o Forbes/Google)

Let us assume we can solve the 'speed' issues here (hint: games need to run fast otherwise you have a poor player experience).  However, there is so much more going on here.  You might be interested in 'how' players are interacting with the game.  For instance, you might be interested to see what keypresses they make most often, which areas they are drawn to, how they solve puzzles, etc.  This type of information can be gleaned from user input via analytics.  Using such information, you can tailor the experience to the user, create innovative experiences, gain business insights, etc.

Another example is in music streaming services (or some other complex orchestration task specific to *your* business).  Let's say a user wants to play a song on whichever of the multiple audio-ready devices they own.  The service itself must do a lot in the background!  The record company needs to be paid for royalties, music catalogues require updating, song recommendations need updating, analytics must be performed on user actions, and so on.  What started as a simple task (play a song) has transformed into a massive set of interacting service activities.  Figure 8 (c/o Google) shows such an interaction:

![Complex Business Processes](/CloudAppsDev/assets/images/7-complicated.png "Complex Business Processes")

> Figure 8 : Complex Business Processes

One approach for handling such a complex orchestration is in a **managed messaging system**.  One of the more common ways of implementing such a service is the **publish/subscribe** model (Pub/Sub).  Figure 9 shows off Pub/Sub (c/o Amazon):

![Pub/Sub Messaging](https://d1.awsstatic.com/product-marketing/Messaging/sns_img_topic.e024462ec88e79ed63d690a2eed6e050e33fb36f.png "Pub/Sub Messaging")

> Figure 9: Pub/Sub Messaging

> For another perspective, here is [Amazon's explanation of Pub/Sub](https://aws.amazon.com/pub-sub-messaging/).

Pub/Sub enables messages (data payloads) to be broadcast to whichever recipients are interested in the data/message.  Pub/Sub tends to be very lightweight, making it attractive for embedded applications as well.  This process works by splitting up services into *publishers* and *subscribers*.  Depending on your Pub/Sub implementation, there may be a *broker* in the middle as well that manages subscriptions as well.

> Note that Pub/Sub can also specify how important messages are, if the message must be acknowledged by the receiver, etc.  For this post we won't do a deep dive on the design pattern itself, however. 

The Pub/Sub design pattern is illustrated in Figure 10 (c/o Google).  In this design pattern, publishers and subscribers are both (generally separate) applications.  The *publisher* sends message to a topic, and subscribers *subscribe* to a topic to receive messages.  Note that this activity can happen asynchronously, and that subscribers only receive messages from the initial publisher.  At least with Google Cloud (you can set this up without cloud services -- e.g., via [Python and the MQTT library](http://www.steves-internet-guide.com/publishing-messages-mqtt-client/)), you should specify a *subscription service* rather than a topic for reading data.

![Publish-Subscribe Pattern](/CloudAppsDev/assets/images/7-pubsub-pattern.png "Publish-Subscribe Pattern")

> Figure 10: Publish-Subscribe Pattern

Figure 11 (c/o Google) demonstrates an example of Pub/Sub.  Here, a company is using Pub/Sub to handle employee hiring procedures system-wide.  In this example, the employee information needs to be spread throughout the system to the relevant systems.  A `message` is published to a `topic`, and all services that subscribe to that topic (and that have the proper authorization) receive the `message` that the new employee has been hired.  The services listed in the figure (e.g., badge, email accounts, etc.) can all be turned into cloud-based microservices, rather than separate, isolated systems. 

![Pub/Sub Example](/CloudAppsDev/assets/images/7-pubsub-ex.png "Pub/Sub Example")

> Figure 11: Pub/Sub Example

Figure 12 (c/o Google) demonstrates multiple pub/sub activities in the context of HTTP.  In this figure, there exist two subscriptions: `push` and `pull`.  In the case of `push`, the subscriber is receiving information at the whim of the publisher (i.e., a `push` event, via HTTP `POST`).  In the case of `pull`, the subscriber is receiving data as the result of a request for information (via an HTTP `GET` request).  In either case, Google Pub/Sub is acting as a buffer/shock absorber in terms of ensuring all services/applications receive/transmit the data necessary, as well as scaling as necessary in the case of a sudden influx of users/events.

![Pub/Sub Subscriptions](/CloudAppsDev/assets/images/7-pubsub-buffer.png "Pub/Sub Subscriptions")

> Figure 12: Pub/Sub Subscriptions

To further illustrate this concept, Figure 13 (c/o Google) shows a bit more of a complex Pub/Sub setup.  Everything in the middle green box is part of the Google Pub/Sub managed service, and everything else is outside of the framework.  "Outside of the framework" means that you provide the applications/services to interact with Pub/Sub -- they could be internal to other Google services, use external cloud services (e.g., via AWS/Azure), or use external applications (e.g., a Raspberry Pi local application).

![Pub/Sub Complex Example](/CloudAppsDev/assets/images/7-complicated.png "Pub/Sub Complex Example")

> Figure 13: Pub/Sub Complex Example

To give you an idea as to where Pub/Sub sits in the cloud hierarchy (i.e., where we would use it when processing big data), Figure 14 (c/o Google) shows you its place.  Effectively, you can consider Pub/Sub to be part of the *Ingestion* phase, where data needs to be captured and brought into the system.  If you're not in the mood to deal with big data, Pub/Sub can be used nicely in Internet of Things applications where data needs to be passed from device to device.  However, this figure also presents some interesting implications.  For instance, we can see the tools we can leverage to process data, to store it, and to analyze it within the Google Cloud ecosystem.  As always, there exist parallel services in AWS and Azure that could be used if you are in that environment.

![Pub/Sub Location](/CloudAppsDev/assets/images/7-pubsub-loc.png "Pub/Sub Location")

> Figure 14: Pub/Sub Location

The following video walks you through a [Codelab](https://cloud.google.com/pubsub/docs/building-pubsub-messaging-system) that helps you (1) install gcloud locally and (2) interact with Google Pub/Sub from a local Python script.

> Module video: [Pub/Sub Demo [21:08]](https://youtu.be/UKAmZBrR300)

Time for a Pub/Sub lab!  For this I'd like to have you get experience with Pub/Sub in two different forms - the Cloud Console/Shell and Python.  Note that you can run Python in the Cloud Shell, so nothing needed locally!

> [QwikLabs - Google Cloud Pub/Sub: Qwik Start - Console (GSP096) [Free]](https://www.qwiklabs.com/focuses/3719?catalog_rank=%7B%22rank%22%3A4%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=8673991)

> [QwikLabs - Google Cloud Pub/Sub: Qwik Start - Python (GSP094) [1 Credit]](https://www.qwiklabs.com/focuses/2775?catalog_rank=%7B%22rank%22%3A3%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=8673991)

## Additional Resources

* [Pub/Sub Codelab](https://cloud.google.com/pubsub/docs/building-pubsub-messaging-system) cript.

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.