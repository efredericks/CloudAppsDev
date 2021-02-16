> By the end of this module, you'll gain experience with automating cloud-based tasks, as well as understanding and using automation tools for managing and optimizing your applications.

> Module videos:

> Module labs:

## Cloud Automation

Now bear with me...

*What if*...we...turned our infrastructure into code?

Well, we can!  Let's take the requirements that we need for an infrastructure (servers, VMs, etc.) and turn them into code-based templates (that can be both read by humans and machines).  By turning our needs into templates, we can very easily create the environments required to run our core processes up on the cloud.  

A nice bonus is that you can track such templates in revision control systems (e.g., git, subversion, etc.) as your needs adapt.  It should also go without saying, but if you create a template then you can very quickly spin up new resources in the event of a disaster, even automatically.

So, time to talk about [Cloud Deployment Manager](https://cloud.google.com/deployment-manager/).


### Cloud Deployment Manager

Figure 1 gives an overview of the Cloud Deployment Manager.  

![Cloud Deployment Manager](/CloudAppsDev/assets/images/10-deployment-mgr.png "Cloud Deployment Manager")

> Figure 1: Cloud Deployment Manager

Consider all of the tasks you need to orchestrate as a budding cloud applications developer.  You will need to understand how to spin up resources in multiple locations and at multiple levels of abstraction (IaaS, PaaS, SaaS) and more than likely *need to do this more than once*!  Consider if you were to setup a set of VMs for your team.  You will need to manage not only the resources themselves, but access to those resources, ensure they are properly accessible, secure, etc.  Now consider turning all of these activities you would do by hand in a web interface into a template.  It nearly becomes your typical infrastructure-based scripting task (creating bash/PowerShell scripts to deploy resources, etc.).

Deployment Manager uses [YAML](https://yaml.org/), a specification format commonly used for defining configuration files.  

## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.