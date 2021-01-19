> By the end of this module, you'll gain experience with interacting with the cloud via application programming interfaces (APIs)

> Module videos:

## Let's be RESTful

RESTful services are more than likely a phrase you've heard in the past.  If you already know what they are, wonderful, however we should talk about what they exactly are and how we can use them to interact with our cloud services.

First of all, what is it to be **RESTful**?

A RESTful (Reppresentational State Transfer)-ful service follows a standardized approach for enabling interaction.  

[Wikipedia has a delightful overview of what REST means](https://en.wikipedia.org/wiki/Representational_state_transfer)!

Effectively, a service accepts 

Figure X shows an example of a RESTful interaction between an application and an API (c/o TowardsDataScience): 

![RESTful API](https://miro.medium.com/max/5230/1*ZU1EQ7tYeQNQlhOhyonHFA.png "RESTful API")

> Figure X: RESTful API

Here, you can get a feel for how a RESTful call is constructed.  The URL is built as you normally would expect for accessing a website, however instead the service is accepting the URL as an instruction sequence for how to parse the request.  *Note, a RESTful call can also accomodate data payloads (e.g., via JSON packets), however we'll just focus on simple commands here*.

We will assume the protocol (`http`) and domain (`www.somewebsite.com`) are known to you at this point ... they give you a human-readable method for accessing the server that your service is hosted upon.

## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.