> By the end of this module, you'll gain experience with interacting with the cloud via application programming interfaces (APIs), learn a bit about managed messaging, and look at the Publish/Subscribe (PubSub) service.

> Module videos:

> Module labs:
* Create and use a Cloud Endpoint

## Let's be RESTful

RESTful services are more than likely a phrase you've heard in the past.  If you already know what they are, wonderful, however we should talk about what they exactly are and how we can use them to interact with our cloud services.

First of all, what is it to be **RESTful**?

A RESTful (REpresentational State Transfer)-ful service follows a standardized approach for enabling interaction.  

[Wikipedia has a delightful overview of what REST means](https://en.wikipedia.org/wiki/Representational_state_transfer)!

Effectively, a service accepts 

Figure X shows an example of a RESTful interaction between an application and an API (c/o TowardsDataScience): 

![RESTful API](https://miro.medium.com/max/5230/1*ZU1EQ7tYeQNQlhOhyonHFA.png "RESTful API")

> Figure X: RESTful API

Here, you can get a feel for how a RESTful call is constructed.  The URL is built as you normally would expect for accessing a website, however instead the service is accepting the URL as an instruction sequence for how to parse the request.  *Note, a RESTful call can also accomodate data payloads (e.g., via JSON packets), however we'll just focus on simple commands here*.

We will assume the protocol (`http`) and domain (`www.somewebsite.com`) are known to you at this point ... they give you a human-readable method for accessing the server that your service is hosted upon.

NOT DONE HERE!

### But was is an API?

An application programming interface (API) is a programming construct that hides the back-end details for multiple reasons.  They simplify communication from service to service, enable code reuse, and enhance portability (at minimum)!  An API enables easier interaction with a service -- you (the programmer) have no worries about what is happening behind the scenes.  All you are aware of is that you need to call particular functions to interact with some service.  

Let's take an example.  For instance, let's say that you are developing a phone application to interact with a cloud-based map service.  Your application is going to pull down restaurant addresses, phone numbers, GPS coordinates, etc. and 'prettify' them for your userbase.  However,  you don't want to index this all yourself, the cloud provider already does that.

To get this information, do you need to understand the complex inner-workings of the mapping service?  Do you need to know geographic information service (GIS) algorithms?  Absolutely not, other people/companies have done the hard work.  However, you do need to know how to handshake with those services!  Perhaps you need to follow a procedure for getting information.  It may be as simple as:

1. Authenticate your application with the service (credential flow)
2. Understand the service's API (i.e., what function calls do you need to make to get your data?)
3. Perform the necessary actions to receive data from the service.

We could use a RESTful query as previously described (perhaps your query looks like `https://maps.cloud-provider.com/getRestaurants/ZIP-CODE`) and that returns a JSON packet of all the information you need.  Or, you might need to write a script that authenticates with the service, calls something along the lines of `data = service.getRestaurants(ZIP-CODE)`, and then parse out what is in `data`.  There is not one specific way to interact with a service -- it depends on the service itself!  Let us use that lovely internet acronym of RTFM, and I'll let you look up what that means.  Basically, read the manual!

Figure X (c/o Google Cloud) shows a logical API that demonstrates how users interact with some service, with an API sitting in between to abstract away the details of the service itself.

![APIs hide the details and enforce contracts](/CloudAppsDev/assets/images/7-api.png "APIs hide the details and enforce contracts")

> Figure X: APIs hide the details and enforce contracts

*What is a contract* you may ask?  Depending on the specification being followed, a *contract*  is a specific method exactly how an API functions, how to interact with it, and how to receive data from it.  [Check out this article for some of the different ways of specifying contracts](https://medium.com/theagilemanager/development-what-is-an-api-contract-683ced58e06f).

### Is there more to it than just interaction?

Oh my yes.  Figure X (c/o Google) shows you a high-level of the concerns we have with APIs.

![Deploying and Managing APIs can be difficult](/CloudAppsDev/assets/images/7-api-mgmt.png "Deploying and Managing APIs can be difficult")

> Figure X: Deploying and Managing APIs can be difficult

In the context of this class, an API is simply the interface for your cloud service.  As such, we care about:

* Interface definition

How are the programmers/users going to interact with your API?  Let's say you've created a wonderful cloud service, however if users don't understand how to use it then it is not strictly useful!  Ensure your interface definition **makes logical sense**, **is well documented**, and **is well tested**!

* Authentication and authorization

Who is allowed to use your API.  You don't necessarily want to make your API fully public unless if you have unlimited funds, so you will need to ensure that the correct users are interacting with it.  As such, you must **authenticate** (i.e., ensure users are who they say they are) and **authorize** (i.e., ensure users have the correct rights/privileges to use your service).  Fortunately, cloud providers typically have methods for handling this for you.  

* Management and scalability

Will your API scale to meet user demand, both upwards and downwards?  As you are now cloud-based, consider how many users will be using it at once, as well as over time!

* Logging and monitoring

Keeping an eye on what your API is doing and how it is being used is also a major consideration.  You must have traceable evidence of exactly what your API has been doing so that you can properly manage your service and usage patterns.

## Cloud Endpoints

Time to look at what is available to us in the cloud!  Figure X (c/o Google) demonstrates Cloud Endpoints, their approach for handling cloud-based APIs.  In this figure you see what is available via Endpoints.

![Cloud Endpoints help you create and maintain APIs](/CloudAppsDev/assets/images/7-endpoints.png "Cloud Endpoints help you create and maintain APIs")

> Figure X: Cloud Endpoints help you create and maintain APIs

Here, you see the concerns described above, fully managed.  You can generate keys for authentication/authorization, handle scalability concerns, monitor/log your API, and integrate with the various API specifications available.  Now, you can use whatever API framework/implementation that you wish, however using a service such as Endpoints can significantly speed up your development process.

> Note: AWS' version is called '[Service Endpoints](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-endpoints.html)' and Azure calls it '[API Management](https://azure.microsoft.com/en-us/services/api-management/).'

Figure X (c/o Google) demonstrates how they (i.e., Cloud Endpoints) fit into the general Google Cloud ecosystem.  Essentially, consider Endpoints (or similar) a cloud service for interacting with your cloud services.

![Where Cloud Endpoints fit](/CloudAppsDev/assets/images/7-endpoints2.png "Where Cloud Endpoints fit")

> Figure X: Where Cloud Endpoints fit

Let's get some practical experience.  

> Lab: Create and use a Cloud Endpoint

## Managed Message Services and Pub/Sub

Figure X (c/o Google) demonstrates how data moves from clients at the Endpoint to internal services and then back to users.  What generally happens, from a service perspective, is that data comes in, something *happens* to that data (i.e., it is transformed in some way), and then data comes out.  In the cloud world, this procedure needs to happen quickly and reliably.

![Data Ingestion](/CloudAppsDev/assets/images/7-data-mgmt.pnkill "Data Ingestion")

> Figure X: Data Ingestion

Consider a streaming gaming platform (publicity photo as shown in Figure X).  There must exist a handshake between client and server, with services interspersed between along the way.  In this example (Google Stadia, though others exist), the core processing occurs on cloud servers and the game experience is transmitted to the player, leveraging high speed internet to deliver a high quality of service.

![Google Stadia Publicity (c/o Forbes/Google)](https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fkevinmurnane%2Ffiles%2F2019%2F06%2FMultiple-platforms_Stadia.jpg "Google Stadia Publicity (c/o Forbes/Google))

> Figure X: Google Stadia Publicity (c/o Forbes/Google)



## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.